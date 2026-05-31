"""
Pure-Python colored PDF generator (no external libraries).

Reusable engine for study/notes PDFs. Uses built-in Type1 fonts
(Helvetica family) so no font embedding is needed.

Line markup (per line):
  - "# text"          -> big bold header (section title)
  - "## text"         -> smaller bold sub-header
  - "==========" line -> horizontal rule
  - "@@text"          -> RED line   (exam-important / must-do)
  - "$$text"          -> GREEN line (common in both boards / safe overlap)
  - "<<<PAGEBREAK>>>"  -> force a new page
  - anything else      -> normal black body text

Indentation before a "@@" / "$$" marker is preserved, e.g. "   @@foo".
Emojis / non-ASCII are stripped (built-in fonts only support WinAnsi).
"""

import re
import zlib
from pathlib import Path

PAGE_W, PAGE_H = 595, 842          # A4 in points
MARGIN_L, MARGIN_R = 50, 50
MARGIN_T, MARGIN_B = 58, 50
LINE_HEIGHT = 13
FONT_SIZE = 10
H1_SIZE = 15
H2_SIZE = 12
TITLE_FONT_SIZE = 20
SUBTITLE_FONT_SIZE = 12

# colors (r, g, b) in 0..1
BLACK = (0, 0, 0)
RED = (0.80, 0.00, 0.00)
GREEN = (0.00, 0.50, 0.00)
BLUE = (0.10, 0.20, 0.55)


def _esc(s: str) -> str:
    s = s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    return re.sub(r"[^\x20-\x7E]", "", s)


def _wrap(text: str, max_chars: int) -> list[str]:
    if len(text) <= max_chars:
        return [text]
    indent = re.match(r"^(\s*)", text).group(1)
    words = text.split(" ")
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


def _classify(raw: str):
    """Return (kind, color, text) for a logical line."""
    # page break
    if raw.strip() == "<<<PAGEBREAK>>>":
        return ("pagebreak", BLACK, "")
    # rule
    if raw.strip().startswith("==========") or raw.strip().startswith("----------"):
        return ("rule", BLACK, "")
    # headers
    if raw.startswith("## "):
        return ("h2", BLUE, raw[3:].strip())
    if raw.startswith("# "):
        return ("h1", BLACK, raw[2:].strip())
    # colored body (allow leading indentation before marker)
    lead = re.match(r"^(\s*)(@@|\$\$)(.*)$", raw)
    if lead:
        indent, marker, rest = lead.group(1), lead.group(2), lead.group(3)
        color = RED if marker == "@@" else GREEN
        return ("body", color, indent + rest)
    return ("body", BLACK, raw)


def _max_chars(kind: str) -> int:
    if kind == "h1":
        return 60
    if kind == "h2":
        return 76
    return 92


def _build_pages(content: str, first_offset: int = 0):
    logical = []
    for raw in content.splitlines():
        kind, color, text = _classify(raw)
        if kind in ("pagebreak", "rule"):
            logical.append((kind, color, ""))
        elif kind in ("h1", "h2"):
            for w in _wrap(text, _max_chars(kind)):
                logical.append((kind, color, w))
        else:
            for w in _wrap(text, _max_chars("body")):
                logical.append((kind, color, w))

    # On the first page, reserve room for the title/subtitle block.
    pages, cur, y = [], [], PAGE_H - MARGIN_T - first_offset
    for kind, color, text in logical:
        if kind == "pagebreak":
            if cur:
                pages.append(cur)
            cur, y = [], PAGE_H - MARGIN_T
            continue
        size = {"h1": H1_SIZE, "h2": H2_SIZE}.get(kind, FONT_SIZE)
        lh = LINE_HEIGHT + (6 if kind == "h1" else 3 if kind == "h2" else 0)
        if y - lh < MARGIN_B:
            pages.append(cur)
            cur, y = [], PAGE_H - MARGIN_T
        cur.append((kind, color, text, y, size))
        y -= lh
    if cur:
        pages.append(cur)
    return pages


def _content_stream(page_lines, title=None, subtitle=None) -> bytes:
    parts = []
    top = PAGE_H - MARGIN_T
    if title is not None:
        parts.append("0 0 0 rg")
        parts.append(
            f"BT /F2 {TITLE_FONT_SIZE} Tf {MARGIN_L} {top} Td ({_esc(title)}) Tj ET"
        )
        if subtitle:
            parts.append(
                f"BT /F1 {SUBTITLE_FONT_SIZE} Tf {MARGIN_L} {top - 22} Td "
                f"({_esc(subtitle)}) Tj ET"
            )
        parts.append(f"{MARGIN_L} {top - 32} m {PAGE_W - MARGIN_R} {top - 32} l S")

    for kind, color, text, y, size in page_lines:
        if kind == "rule":
            parts.append("0 0 0 rg")
            parts.append(f"{MARGIN_L} {y + 5} m {PAGE_W - MARGIN_R} {y + 5} l S")
            continue
        if not text.strip():
            continue
        font = "/F2" if kind in ("h1", "h2") else "/F1"
        r, g, b = color
        parts.append(f"{r:.3f} {g:.3f} {b:.3f} rg")
        parts.append(f"BT {font} {size} Tf {MARGIN_L} {y} Td ({_esc(text)}) Tj ET")
    parts.append("0 0 0 rg")
    return ("\n".join(parts)).encode("latin-1")


def build_pdf(content: str, out_path, title: str = None, subtitle: str = None):
    """Generate a colored PDF from marked-up `content` text."""
    out_path = Path(out_path)
    first_offset = 52 if title else 0
    pages = _build_pages(content, first_offset=first_offset)
    if not pages:
        pages = [[]]

    catalog_num, pages_num, font1_num, font2_num = 1, 2, 3, 4
    page_nums, content_nums, n = [], [], 5
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
        stream = _content_stream(
            page_lines,
            title=title if i == 0 else None,
            subtitle=subtitle if i == 0 else None,
        )
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

    out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
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
