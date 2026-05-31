"""
pdf_utils.py — Pure-Python PDF generator (zero external dependencies).

Features
--------
- Word-wrapped text using the built-in Helvetica font family.
- Per-line colour markers:
    '@@'  prefix  -> RED   line   (e.g. core basics / warnings)
    '$$'  prefix  -> GREEN line   (e.g. most-important tips)
    '##'  prefix  -> BOLD heading (dark blue, slightly larger)
    '<<<PAGEBREAK>>>' on its own line -> start a new page
- Blank lines create vertical spacing.

Usage
-----
    from pdf_utils import render_text_to_pdf
    render_text_to_pdf(content_str, "output.pdf", title="My Title")
"""

from typing import List, Tuple

# ----------------------------------------------------------------------------
# Helvetica character widths (in 1/1000 em units) for accurate word-wrapping.
# Only the printable ASCII range is needed for our content.
# ----------------------------------------------------------------------------
_HELV_WIDTHS = {
    ' ': 278, '!': 278, '"': 355, '#': 556, '$': 556, '%': 889, '&': 667,
    "'": 191, '(': 333, ')': 333, '*': 389, '+': 584, ',': 278, '-': 333,
    '.': 278, '/': 278, '0': 556, '1': 556, '2': 556, '3': 556, '4': 556,
    '5': 556, '6': 556, '7': 556, '8': 556, '9': 556, ':': 278, ';': 278,
    '<': 584, '=': 584, '>': 584, '?': 556, '@': 1015, 'A': 667, 'B': 667,
    'C': 722, 'D': 722, 'E': 667, 'F': 611, 'G': 778, 'H': 722, 'I': 278,
    'J': 500, 'K': 667, 'L': 556, 'M': 833, 'N': 722, 'O': 778, 'P': 667,
    'Q': 778, 'R': 722, 'S': 667, 'T': 611, 'U': 722, 'V': 667, 'W': 944,
    'X': 667, 'Y': 667, 'Z': 611, '[': 278, '\\': 278, ']': 278, '^': 469,
    '_': 556, '`': 333, 'a': 556, 'b': 556, 'c': 500, 'd': 556, 'e': 556,
    'f': 278, 'g': 556, 'h': 556, 'i': 222, 'j': 222, 'k': 500, 'l': 222,
    'm': 833, 'n': 556, 'o': 556, 'p': 556, 'q': 556, 'r': 333, 's': 500,
    't': 278, 'u': 556, 'v': 500, 'w': 722, 'x': 500, 'y': 500, 'z': 500,
    '{': 334, '|': 260, '}': 334, '~': 584,
}
_DEFAULT_WIDTH = 556


def _text_width(text: str, font_size: float) -> float:
    """Return rendered width of text at a given font size (points)."""
    total = sum(_HELV_WIDTHS.get(ch, _DEFAULT_WIDTH) for ch in text)
    return total * font_size / 1000.0


def _wrap(text: str, font_size: float, max_width: float) -> List[str]:
    """Greedy word-wrap a single logical line to fit max_width points."""
    if not text:
        return ['']
    words = text.split(' ')
    lines: List[str] = []
    current = ''
    for word in words:
        candidate = word if not current else current + ' ' + word
        if _text_width(candidate, font_size) <= max_width or not current:
            # If a single word is too long, hard-split it.
            if not current and _text_width(word, font_size) > max_width:
                chunk = ''
                for ch in word:
                    if _text_width(chunk + ch, font_size) <= max_width:
                        chunk += ch
                    else:
                        lines.append(chunk)
                        chunk = ch
                current = chunk
            else:
                current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def _esc(text: str) -> str:
    """Escape characters that are special inside a PDF literal string."""
    return text.replace('\\', r'\\').replace('(', r'\(').replace(')', r'\)')


def _sanitize(text: str) -> str:
    """Replace common non-ASCII chars so Helvetica (WinAnsi) renders cleanly."""
    repl = {
        '\u2018': "'", '\u2019': "'", '\u201c': '"', '\u201d': '"',
        '\u2013': '-', '\u2014': '-', '\u2026': '...', '\u2192': '->',
        '\u2022': '-', '\u00a0': ' ', '\u20b9': 'Rs.', '\u2713': '[v]',
        '\u221a': 'sqrt', '\u2260': '!=', '\u2705': '[OK]', '\ud83d': '',
    }
    out = []
    for ch in text:
        if ch in repl:
            out.append(repl[ch])
        elif ord(ch) < 128:
            out.append(ch)
        elif 128 <= ord(ch) <= 255:
            out.append(ch)
        else:
            out.append('')  # drop emoji / unsupported glyphs
    return ''.join(out)


# Layout constants (US Letter portrait).
_PAGE_W, _PAGE_H = 612.0, 792.0
_MARGIN_X = 54.0
_MARGIN_TOP = 60.0
_MARGIN_BOTTOM = 54.0
_BODY_SIZE = 11.5
_HEAD_SIZE = 15.0
_LINE_GAP = 1.40   # multiple of font size
_PARA_GAP = 6.0    # extra points for blank lines


def _color_for(style: str) -> Tuple[float, float, float]:
    if style == 'red':
        return (0.80, 0.00, 0.00)
    if style == 'green':
        return (0.00, 0.55, 0.16)
    if style == 'head':
        return (0.09, 0.20, 0.45)
    return (0.10, 0.10, 0.10)


def _parse(content: str):
    """Yield (style, raw_text) tuples and 'PAGEBREAK' sentinels."""
    for raw in content.split('\n'):
        line = raw.rstrip('\r')
        if line.strip() == '<<<PAGEBREAK>>>':
            yield ('pagebreak', '')
            continue
        if line.startswith('@@'):
            yield ('red', line[2:])
        elif line.startswith('$$'):
            yield ('green', line[2:])
        elif line.startswith('##'):
            yield ('head', line[2:].strip())
        else:
            yield ('body', line)


def render_text_to_pdf(content: str, out_path: str, title: str = '') -> str:
    """Render marker-annotated text to a colored, word-wrapped PDF file."""
    max_width = _PAGE_W - 2 * _MARGIN_X

    # Build a flat list of drawable lines grouped per page.
    pages: List[List[dict]] = [[]]
    y = _PAGE_H - _MARGIN_TOP

    def new_page():
        nonlocal y
        pages.append([])
        y = _PAGE_H - _MARGIN_TOP

    # Optional title at the very top of page 1.
    if title:
        size = 20.0
        pages[0].append({'x': _MARGIN_X, 'y': y, 'size': size,
                         'color': (0.0, 0.0, 0.0), 'text': _sanitize(title),
                          'bold': True})
        y -= size * 1.6

    for style, raw in _parse(content):
        if style == 'pagebreak':
            new_page()
            continue
        if raw.strip() == '':
            y -= _PARA_GAP + _BODY_SIZE * 0.4
            continue

        is_head = style == 'head'
        size = _HEAD_SIZE if is_head else _BODY_SIZE
        color = _color_for(style)
        text = _sanitize(raw)
        wrapped = _wrap(text, size, max_width)

        for seg in wrapped:
            if y - size < _MARGIN_BOTTOM:
                new_page()
            pages[-1].append({'x': _MARGIN_X, 'y': y, 'size': size,
                              'color': color, 'text': seg,
                              'bold': is_head})
            y -= size * _LINE_GAP
        if is_head:
            y -= 3.0  # little breathing room after a heading

    # ---- Assemble PDF objects ----
    objects: List[bytes] = []

    def add_obj(body: bytes) -> int:
        objects.append(body)
        return len(objects)  # 1-based object number

    # Reserve: 1=Catalog, 2=Pages. Fonts next.
    font_reg = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>"
    font_bold = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>"

    # Placeholders for catalog & pages (filled later).
    objects.append(b'')  # obj 1 catalog
    objects.append(b'')  # obj 2 pages
    font_reg_no = add_obj(font_reg)
    font_bold_no = add_obj(font_bold)

    page_obj_nums: List[int] = []
    for page_lines in pages:
        # Build content stream.
        parts = [b'']
        cur_color = None
        for ln in page_lines:
            r, g, b = ln['color']
            font_name = b'/F2' if ln['bold'] else b'/F1'
            chunk = (
                f"BT {font_name.decode()} {ln['size']:.2f} Tf "
                f"{r:.3f} {g:.3f} {b:.3f} rg "
                f"1 0 0 1 {ln['x']:.2f} {ln['y']:.2f} Tm "
                f"({_esc(ln['text'])}) Tj ET\n"
            )
            parts.append(chunk.encode('latin-1', 'replace'))
        stream = b''.join(parts)
        stream_obj = (
            b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n"
            + stream + b"\nendstream"
        )
        content_no = add_obj(stream_obj)
        page_dict = (
            b"<< /Type /Page /Parent 2 0 R "
            b"/MediaBox [0 0 " + f"{_PAGE_W:.0f} {_PAGE_H:.0f}".encode() + b"] "
            b"/Resources << /Font << /F1 " + str(font_reg_no).encode()
            + b" 0 R /F2 " + str(font_bold_no).encode() + b" 0 R >> >> "
            b"/Contents " + str(content_no).encode() + b" 0 R >>"
        )
        page_obj_nums.append(add_obj(page_dict))

    kids = b" ".join(f"{n} 0 R".encode() for n in page_obj_nums)
    objects[1] = (b"<< /Type /Pages /Count " + str(len(page_obj_nums)).encode()
                  + b" /Kids [" + kids + b"] >>")
    objects[0] = b"<< /Type /Catalog /Pages 2 0 R >>"

    # ---- Serialize with xref table ----
    out = bytearray()
    out += b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"
    offsets = [0] * (len(objects) + 1)
    for i, body in enumerate(objects, start=1):
        offsets[i] = len(out)
        out += f"{i} 0 obj\n".encode() + body + b"\nendobj\n"

    xref_pos = len(out)
    out += b"xref\n"
    out += f"0 {len(objects) + 1}\n".encode()
    out += b"0000000000 65535 f \n"
    for i in range(1, len(objects) + 1):
        out += f"{offsets[i]:010d} 00000 n \n".encode()
    out += b"trailer\n"
    out += (b"<< /Size " + str(len(objects) + 1).encode()
            + b" /Root 1 0 R >>\n")
    out += b"startxref\n" + str(xref_pos).encode() + b"\n%%EOF\n"

    with open(out_path, 'wb') as fh:
        fh.write(out)
    return out_path


if __name__ == '__main__':
    demo = (
        "## Demo Heading\n"
        "This is normal body text that should wrap nicely across the page "
        "when it gets long enough to exceed the available width.\n"
        "\n"
        "@@Yeh red line hai - core basic / warning.\n"
        "$$Yeh green line hai - most important tip.\n"
        "<<<PAGEBREAK>>>\n"
        "## Page Two\n"
        "Second page content.\n"
    )
    render_text_to_pdf(demo, 'demo.pdf', title='PDF Utils Demo')
    print('wrote demo.pdf')
