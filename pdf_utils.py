"""
Shared utilities for generating Class 10 NCERT Maths chapter PDFs.

Pure Python, no external dependencies. Uses built-in Helvetica/Helvetica-Bold
Type1 fonts, so no font file embedding is needed.

Usage:
    from pdf_utils import build_pdf
    build_pdf("Chapter Title", "Subtitle line", CONTENT_STRING, "out.pdf")
"""

import re
import zlib
from pathlib import Path


PAGE_W, PAGE_H = 595, 842         # A4 in points
MARGIN_L, MARGIN_R = 50, 50
MARGIN_T, MARGIN_B = 60, 50
LINE_HEIGHT = 13
FONT_SIZE = 10
HEADER_FONT_SIZE = 14
TITLE_FONT_SIZE = 20


def escape_pdf_text(s: str) -> str:
    s = s.replace("\\", "\\\\")
    s = s.replace("(", "\\(").replace(")", "\\)")
    s = re.sub(r"[^\x20-\x7E]", "", s)
    return s


def wrap_line(line: str, max_chars: int = 95):
    if len(line) <= max_chars:
        return [line]
    indent_match = re.match(r"^(\s*)", line)
    indent = indent_match.group(1) if indent_match else ""
    words = line.split(" ")
    out, cur = [], indent
    for w in words:
        if len(cur) + len(w) + 1 > max_chars:
            out.append(cur.rstrip())
            cur = indent + w
        else:
            cur = (cur + " " + w) if cur.strip() else (indent + w)
    if cur.strip():
        out.append(cur.rstrip())
    return out


def build_pages(content: str):
    raw_lines = content.splitlines()
    lines = []
    for ln in raw_lines:
        stripped = ln.strip()
        if stripped.startswith("=========="):
            lines.append(("rule", ""))
        elif (stripped and stripped == stripped.upper() and len(stripped) > 5
                and not stripped.startswith("-") and not stripped.startswith("*")
                and re.match(r"^[A-Z0-9 &/().,'\-:]+$", stripped)):
            lines.append(("header", stripped))
        else:
            for w in wrap_line(ln):
                lines.append(("body", w))

    pages = []
    cur_page = []
    y = PAGE_H - MARGIN_T
    for kind, text in lines:
        size = HEADER_FONT_SIZE if kind == "header" else FONT_SIZE
        lh = LINE_HEIGHT + (4 if kind == "header" else 0)
        if y - lh < MARGIN_B:
            pages.append(cur_page)
            cur_page = []
            y = PAGE_H - MARGIN_T
        cur_page.append((kind, text, y, size))
        y -= lh
    if cur_page:
        pages.append(cur_page)
    return pages


def make_content_stream(page_lines, title, subtitle, is_first=False) -> bytes:
    parts = []
    if is_first:
        parts.append(
            f"BT /F2 {TITLE_FONT_SIZE} Tf {MARGIN_L} {PAGE_H - MARGIN_T} Td "
            f"({escape_pdf_text(title)}) Tj ET"
        )
        parts.append(
            f"BT /F1 12 Tf {MARGIN_L} {PAGE_H - MARGIN_T - 22} Td "
            f"({escape_pdf_text(subtitle)}) Tj ET"
        )
        parts.append(
            f"{MARGIN_L} {PAGE_H - MARGIN_T - 32} m "
            f"{PAGE_W - MARGIN_R} {PAGE_H - MARGIN_T - 32} l S"
        )

    for kind, text, y, size in page_lines:
        if kind == "rule":
            parts.append(f"{MARGIN_L} {y + 5} m {PAGE_W - MARGIN_R} {y + 5} l S")
            continue
        if not text.strip():
            continue
        font = "/F2" if kind == "header" else "/F1"
        safe = escape_pdf_text(text)
        parts.append(f"BT {font} {size} Tf {MARGIN_L} {y} Td ({safe}) Tj ET")

    return ("\n".join(parts)).encode("latin-1")


def build_pdf(title: str, subtitle: str, content: str, out_path):
    out_path = Path(out_path)
    pages = build_pages(content)

    catalog_num = 1
    pages_num = 2
    font1_num = 3
    font2_num = 4

    page_object_nums = []
    content_object_nums = []
    next_num = 5
    for _ in pages:
        page_object_nums.append(next_num)
        next_num += 1
        content_object_nums.append(next_num)
        next_num += 1

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
        pno = page_object_nums[i]
        cno = content_object_nums[i]
        stream = make_content_stream(page_lines, title, subtitle, is_first=(i == 0))
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
