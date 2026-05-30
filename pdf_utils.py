"""
pdf_utils.py
------------
Pure-Python PDF generator (NO external libraries / no pip installs).

Built on top of the built-in PDF Type1 fonts (Helvetica family), so there is
no font embedding. It supports a few lightweight markup conventions that make
it easy to build colourful study notes:

  Line markup (checked AFTER leading whitespace):
    @@   -> render that line in RED      (used for "extra" / core-basics notes)
    $$   -> render that line in GREEN     (used for exam-frequent topics)
    <<<PAGEBREAK>>>  -> force the start of a new page

  Automatic styling:
    A line of "======" becomes a horizontal rule.
    A fully UPPER-CASE line becomes a bold section header.

Public API:
    text_to_pdf(content: str, out_path, title: str, subtitle: str = "")

This module is intentionally dependency-free so it runs in any sandbox.
"""

import re
import zlib
from pathlib import Path


# ---------- Page geometry ----------
PAGE_W, PAGE_H = 595, 842          # A4 in points
MARGIN_L, MARGIN_R = 50, 50
MARGIN_T, MARGIN_B = 60, 50
LINE_HEIGHT = 14
FONT_SIZE = 10
HEADER_FONT_SIZE = 14
TITLE_FONT_SIZE = 20
MAX_CHARS = 95

# Colours as PDF fill operators "r g b rg"
COLORS = {
    "black": "0 0 0 rg",
    "red": "0.85 0.12 0.12 rg",
    "green": "0.05 0.55 0.15 rg",
}

PAGEBREAK_TOKEN = "<<<PAGEBREAK>>>"


def escape_pdf_text(s: str) -> str:
    """Escape special characters for PDF text strings and drop non-ASCII."""
    s = s.replace("\\", "\\\\")
    s = s.replace("(", "\\(").replace(")", "\\)")
    s = re.sub(r"[^\x20-\x7E]", "", s)   # built-in fonts ~ WinAnsi only
    return s


def _split_color(line: str):
    """Return (color, clean_line) after stripping a leading @@ / $$ marker.

    The marker is detected after any leading whitespace, and the indentation
    is preserved so layout stays intact.
    """
    m = re.match(r"^(\s*)(@@|\$\$)(.*)$", line)
    if not m:
        return "black", line
    indent, marker, rest = m.group(1), m.group(2), m.group(3)
    color = "red" if marker == "@@" else "green"
    # keep a single space after indent if the author wrote "@@ text"
    return color, indent + rest


def wrap_line(line: str, max_chars: int = MAX_CHARS):
    """Simple word wrap that preserves leading indentation."""
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


def _is_header(text: str) -> bool:
    stripped = text.strip()
    if len(stripped) <= 4:
        return False
    if stripped.startswith("-") or stripped.startswith("*"):
        return False
    if stripped != stripped.upper():
        return False
    return bool(re.match(r"^[A-Z0-9 &/().,'\-:?!+]+$", stripped))


def build_pages(content: str):
    """Convert raw content into a list of pages.

    Each page is a list of tuples: (kind, text, y, size, color)
    kind is one of: body | header | rule
    """
    # 1) classify every raw line into (kind, text, color)
    classified = []
    for raw in content.splitlines():
        if raw.strip() == PAGEBREAK_TOKEN:
            classified.append(("pagebreak", "", "black"))
            continue
        color, line = _split_color(raw)
        stripped = line.strip()
        if stripped.startswith("=====") or stripped.startswith("-----") \
                or stripped.startswith("~~~~~"):
            classified.append(("rule", "", color))
        elif _is_header(stripped):
            classified.append(("header", stripped, color))
        else:
            for w in wrap_line(line):
                classified.append(("body", w, color))

    # 2) flow lines into pages, respecting forced page breaks
    pages, cur_page = [], []
    y = PAGE_H - MARGIN_T
    for kind, text, color in classified:
        if kind == "pagebreak":
            if cur_page:
                pages.append(cur_page)
            cur_page = []
            y = PAGE_H - MARGIN_T
            continue
        size = HEADER_FONT_SIZE if kind == "header" else FONT_SIZE
        lh = LINE_HEIGHT + (5 if kind == "header" else 0)
        if y - lh < MARGIN_B:
            pages.append(cur_page)
            cur_page = []
            y = PAGE_H - MARGIN_T
        cur_page.append((kind, text, y, size, color))
        y -= lh
    if cur_page:
        pages.append(cur_page)
    return pages


def make_content_stream(page_lines, title="", subtitle="", is_first=False) -> bytes:
    parts = []
    if is_first:
        parts.append(COLORS["black"])
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
            f"0 0 0 RG {MARGIN_L} {PAGE_H - MARGIN_T - 32} m "
            f"{PAGE_W - MARGIN_R} {PAGE_H - MARGIN_T - 32} l S"
        )

    for kind, text, y, size, color in page_lines:
        if kind == "rule":
            parts.append(
                f"0 0 0 RG {MARGIN_L} {y + 5} m "
                f"{PAGE_W - MARGIN_R} {y + 5} l S"
            )
            continue
        if not text.strip():
            continue
        font = "/F2" if kind == "header" else "/F1"
        parts.append(COLORS.get(color, COLORS["black"]))
        parts.append(
            f"BT {font} {size} Tf {MARGIN_L} {y} Td "
            f"({escape_pdf_text(text)}) Tj ET"
        )

    return ("\n".join(parts)).encode("latin-1")


def text_to_pdf(content: str, out_path, title: str, subtitle: str = ""):
    """Render `content` to a PDF at `out_path`."""
    out_path = Path(out_path)
    pages = build_pages(content)
    if not pages:
        pages = [[]]

    catalog_num, pages_num, font1_num, font2_num = 1, 2, 3, 4
    page_object_nums, content_object_nums = [], []
    next_num = 5
    for _ in pages:
        page_object_nums.append(next_num); next_num += 1
        content_object_nums.append(next_num); next_num += 1

    objects = [None] * (next_num - 1)
    objects[catalog_num - 1] = f"<< /Type /Catalog /Pages {pages_num} 0 R >>".encode()
    kids = " ".join(f"{n} 0 R" for n in page_object_nums)
    objects[pages_num - 1] = (
        f"<< /Type /Pages /Count {len(pages)} /Kids [ {kids} ] >>"
    ).encode()
    objects[font1_num - 1] = (
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica "
        b"/Encoding /WinAnsiEncoding >>"
    )
    objects[font2_num - 1] = (
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold "
        b"/Encoding /WinAnsiEncoding >>"
    )

    for i, page_lines in enumerate(pages):
        pno, cno = page_object_nums[i], content_object_nums[i]
        stream = make_content_stream(
            page_lines, title=title, subtitle=subtitle, is_first=(i == 0)
        )
        compressed = zlib.compress(stream)
        objects[cno - 1] = (
            f"<< /Length {len(compressed)} /Filter /FlateDecode >>\nstream\n"
        ).encode() + compressed + b"\nendstream"
        objects[pno - 1] = (
            f"<< /Type /Page /Parent {pages_num} 0 R "
            f"/MediaBox [0 0 {PAGE_W} {PAGE_H}] "
            f"/Resources << /Font << /F1 {font1_num} 0 R "
            f"/F2 {font2_num} 0 R >> >> "
            f"/Contents {cno} 0 R >>"
        ).encode()

    out = bytearray()
    out += b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"
    offsets = [0]
    for i, body in enumerate(objects, start=1):
        offsets.append(len(out))
        out += f"{i} 0 obj\n".encode()
        out += body
        out += b"\nendobj\n"
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
