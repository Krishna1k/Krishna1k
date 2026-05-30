"""
pdf_utils.py
============
Pure-Python PDF generator (no external libraries, no font embedding).

Reusable across study-note chapters. Uses the built-in PDF Type1 fonts
(Helvetica family) so nothing needs to be installed.

Line-level markup (put the marker at the very start of a line):
    @@   -> render that line in RED   (used for "Core Basics" prerequisite page)
    $$   -> render that line in GREEN (used for "frequently asked in board exam")
    ##   -> render that line as a BOLD HEADER (dark)
    ==== -> a horizontal rule (any line that is only '=' characters)
    <<<PAGEBREAK>>>  -> force a new page

Everything else is normal black body text. Leading spaces are preserved
for indentation. Emojis / non-ASCII are stripped (built-in fonts can't draw
them), so use plain ASCII art markers like [*], ->, (1), etc.

Public API:
    build_pdf(content: str, out_path, title=None, subtitle=None)
"""

import re
import zlib
from pathlib import Path


# ---------- Layout constants ----------
PAGE_W, PAGE_H = 595, 842          # A4 in points
MARGIN_L, MARGIN_R = 50, 50
MARGIN_T, MARGIN_B = 60, 50
LINE_HEIGHT = 14
FONT_SIZE = 10
HEADER_FONT_SIZE = 13
TITLE_FONT_SIZE = 20

# Colors as (r, g, b) in 0..1
COL_BLACK = (0, 0, 0)
COL_RED = (0.80, 0.00, 0.00)
COL_GREEN = (0.00, 0.50, 0.00)
COL_HEADER = (0.10, 0.10, 0.45)   # dark navy for headers


# ---------- Text helpers ----------
def escape_pdf_text(s: str) -> str:
    """Escape special chars for a PDF text string and strip non-ASCII."""
    s = s.replace("\\", "\\\\")
    s = s.replace("(", "\\(").replace(")", "\\)")
    s = re.sub(r"[^\x20-\x7E]", "", s)   # built-in fonts: ASCII only
    return s


def wrap_line(line: str, max_chars: int = 92) -> list:
    """Wrap a long line by characters, preserving leading indentation."""
    if len(line) <= max_chars:
        return [line]
    indent = re.match(r"^(\s*)", line).group(1)
    words = line.split(" ")
    out, cur = [], indent
    for w in words:
        if len(cur) + len(w) + 1 > max_chars and cur.strip():
            out.append(cur.rstrip())
            cur = indent + w
        else:
            cur = (cur + " " + w) if cur.strip() else (indent + w)
    if cur.strip():
        out.append(cur.rstrip())
    return out


# ---------- Parse content into styled lines ----------
def _classify(line: str):
    """
    Return (kind, color, text) for a raw line.
    kind in {body, header, red, green, rule, pagebreak}
    """
    stripped = line.strip()

    if stripped == "<<<PAGEBREAK>>>":
        return ("pagebreak", None, "")
    if stripped and set(stripped) <= set("="):
        return ("rule", None, "")

    if line.startswith("@@"):
        return ("red", COL_RED, line[2:])
    if line.startswith("$$"):
        return ("green", COL_GREEN, line[2:])
    if line.startswith("##"):
        return ("header", COL_HEADER, line[2:].strip())
    return ("body", COL_BLACK, line)


def build_pages(content: str):
    """Split content into pages; each page is a list of draw-instructions."""
    styled = []
    for raw in content.splitlines():
        kind, color, text = _classify(raw)
        if kind in ("rule", "pagebreak"):
            styled.append((kind, color, text))
        elif kind == "header":
            styled.append((kind, color, text))
        else:
            for w in wrap_line(text):
                styled.append((kind, color, w))

    pages, cur = [], []
    y = PAGE_H - MARGIN_T
    for kind, color, text in styled:
        if kind == "pagebreak":
            if cur:
                pages.append(cur)
            cur = []
            y = PAGE_H - MARGIN_T
            continue

        size = HEADER_FONT_SIZE if kind == "header" else FONT_SIZE
        lh = LINE_HEIGHT + (5 if kind == "header" else 0)

        if y - lh < MARGIN_B:
            pages.append(cur)
            cur = []
            y = PAGE_H - MARGIN_T

        cur.append((kind, color, text, y, size))
        y -= lh
    if cur:
        pages.append(cur)
    return pages


# ---------- Content stream per page ----------
def _make_stream(page_lines, is_first, title, subtitle) -> bytes:
    parts = []
    if is_first and title:
        parts.append(
            f"BT /F2 {TITLE_FONT_SIZE} Tf {MARGIN_L} {PAGE_H - MARGIN_T} Td "
            f"({escape_pdf_text(title)}) Tj ET"
        )
        if subtitle:
            parts.append(
                f"BT /F1 12 Tf {MARGIN_L} {PAGE_H - MARGIN_T - 22} Td "
                f"({escape_pdf_text(subtitle)}) Tj ET"
            )
        parts.append(
            f"0.1 0.1 0.45 RG {MARGIN_L} {PAGE_H - MARGIN_T - 32} m "
            f"{PAGE_W - MARGIN_R} {PAGE_H - MARGIN_T - 32} l S 0 0 0 RG"
        )

    for kind, color, text, y, size in page_lines:
        if kind == "rule":
            parts.append(
                f"0.5 0.5 0.5 RG {MARGIN_L} {y + 5} m "
                f"{PAGE_W - MARGIN_R} {y + 5} l S 0 0 0 RG"
            )
            continue
        if not text.strip():
            continue
        font = "/F2" if kind in ("header", "red") else "/F1"
        r, g, b = color if color else COL_BLACK
        safe = escape_pdf_text(text)
        parts.append(
            f"BT {font} {size} Tf {r:.2f} {g:.2f} {b:.2f} rg "
            f"{MARGIN_L} {y} Td ({safe}) Tj ET 0 0 0 rg"
        )

    return ("\n".join(parts)).encode("latin-1")


# ---------- Assemble the PDF ----------
def build_pdf(content: str, out_path, title=None, subtitle=None):
    out_path = Path(out_path)
    pages = build_pages(content)

    catalog_num, pages_num, font1_num, font2_num = 1, 2, 3, 4
    page_nums, content_nums = [], []
    n = 5
    for _ in pages:
        page_nums.append(n); n += 1
        content_nums.append(n); n += 1

    objects = [None] * (n - 1)
    objects[catalog_num - 1] = f"<< /Type /Catalog /Pages {pages_num} 0 R >>".encode()
    kids = " ".join(f"{p} 0 R" for p in page_nums)
    objects[pages_num - 1] = (
        f"<< /Type /Pages /Count {len(pages)} /Kids [ {kids} ] >>".encode()
    )
    objects[font1_num - 1] = (
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica "
        b"/Encoding /WinAnsiEncoding >>"
    )
    objects[font2_num - 1] = (
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold "
        b"/Encoding /WinAnsiEncoding >>"
    )

    for i, page_lines in enumerate(pages):
        pno, cno = page_nums[i], content_nums[i]
        stream = _make_stream(page_lines, i == 0, title, subtitle)
        comp = zlib.compress(stream)
        objects[cno - 1] = (
            f"<< /Length {len(comp)} /Filter /FlateDecode >>\nstream\n".encode()
            + comp + b"\nendstream"
        )
        objects[pno - 1] = (
            f"<< /Type /Page /Parent {pages_num} 0 R "
            f"/MediaBox [0 0 {PAGE_W} {PAGE_H}] "
            f"/Resources << /Font << /F1 {font1_num} 0 R /F2 {font2_num} 0 R >> >> "
            f"/Contents {cno} 0 R >>"
        ).encode()

    out = bytearray()
    out += b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"
    offsets = [0]
    for i, body in enumerate(objects, start=1):
        offsets.append(len(out))
        out += f"{i} 0 obj\n".encode() + body + b"\nendobj\n"

    xref_pos = len(out)
    out += f"xref\n0 {len(objects) + 1}\n".encode()
    out += b"0000000000 65535 f \n"
    for off in offsets[1:]:
        out += f"{off:010d} 00000 n \n".encode()
    out += (
        f"trailer\n<< /Size {len(objects) + 1} /Root {catalog_num} 0 R >>\n"
        f"startxref\n{xref_pos}\n%%EOF\n"
    ).encode()

    out_path.write_bytes(out)
    print(f"Wrote {out_path} ({len(out):,} bytes, {len(pages)} pages)")
    return out_path
