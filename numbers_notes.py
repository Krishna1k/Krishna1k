#!/usr/bin/env python3
"""
Pure-Python PDF generator (no external libraries).
Creates a study-notes PDF: "Types of Numbers".
"""

# ----------------------------------------------------------------------
# Helvetica character widths (per 1000 em) for ASCII 32..126
# ----------------------------------------------------------------------
HELV_W = {
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


def text_width(s, size):
    total = 0
    for ch in s:
        total += HELV_W.get(ch, 556)
    return total * size / 1000.0


def wrap_text(s, size, max_width):
    """Greedy word wrap. Returns a list of lines."""
    words = s.split(' ')
    lines = []
    current = ''
    for w in words:
        trial = w if current == '' else current + ' ' + w
        if text_width(trial, size) <= max_width or current == '':
            current = trial
        else:
            lines.append(current)
            current = w
    if current != '':
        lines.append(current)
    return lines


def esc(s):
    return s.replace('\\', r'\\').replace('(', r'\(').replace(')', r'\)')


# ----------------------------------------------------------------------
# Page / layout configuration
# ----------------------------------------------------------------------
PAGE_W, PAGE_H = 595.28, 841.89
LEFT, RIGHT = 60, 60
TOP_Y = 790
BOTTOM_Y = 60
CONTENT_W = PAGE_W - LEFT - RIGHT

# Colors
NAVY = (0.13, 0.20, 0.45)
ACCENT = (0.74, 0.20, 0.20)
GREY = (0.30, 0.30, 0.30)
BLACK = (0, 0, 0)


class PDFBuilder:
    def __init__(self):
        self.pages = []          # each page: list of op strings
        self.cur = None
        self.y = TOP_Y
        self.new_page()

    def new_page(self):
        self.cur = []
        self.pages.append(self.cur)
        self.y = TOP_Y

    def ensure(self, needed):
        if self.y - needed < BOTTOM_Y:
            self.new_page()

    def _draw_line_text(self, x, y, s, font, size, color):
        r, g, b = color
        self.cur.append(
            f"BT\n/{font} {size:.2f} Tf\n{r:.3f} {g:.3f} {b:.3f} rg\n"
            f"{x:.2f} {y:.2f} Td\n({esc(s)}) Tj\nET"
        )

    def rect(self, x, y, w, h, color, fill=True):
        r, g, b = color
        if fill:
            self.cur.append(f"{r:.3f} {g:.3f} {b:.3f} rg\n{x:.2f} {y:.2f} {w:.2f} {h:.2f} re\nf")
        else:
            self.cur.append(f"{r:.3f} {g:.3f} {b:.3f} RG\n{x:.2f} {y:.2f} {w:.2f} {h:.2f} re\nS")

    def hline(self, x1, x2, y, color, width=1):
        r, g, b = color
        self.cur.append(f"{width:.2f} w\n{r:.3f} {g:.3f} {b:.3f} RG\n{x1:.2f} {y:.2f} m {x2:.2f} {y:.2f} l S")

    # ---- high level blocks -------------------------------------------
    def title(self, s):
        size, lead = 26, 32
        self.ensure(lead)
        self._draw_line_text(LEFT, self.y, s, "F2", size, NAVY)
        self.y -= lead

    def subtitle(self, s):
        size, lead = 13, 20
        self.ensure(lead)
        self._draw_line_text(LEFT, self.y, s, "F1", size, GREY)
        self.y -= lead

    def h2(self, s):
        size, lead = 15, 22
        self.ensure(lead + 10)
        self.y -= 6
        # accent bar
        self.rect(LEFT, self.y - 3, 4, 16, ACCENT)
        self._draw_line_text(LEFT + 12, self.y, s, "F2", size, NAVY)
        self.y -= lead
        self.hline(LEFT, PAGE_W - RIGHT, self.y + 6, (0.8, 0.8, 0.8), 0.6)
        self.y -= 4

    def label_body(self, label, body):
        """Bold inline label followed by wrapped body text."""
        size, lead = 11, 16
        label_str = label + ' '
        lw = text_width(label_str, size)
        # first line wrap accounting for label width
        first_max = CONTENT_W - lw
        # We wrap the whole body using the narrower first-line then full width.
        words = body.split(' ')
        lines = []
        current = ''
        max_w = first_max
        for w in words:
            trial = w if current == '' else current + ' ' + w
            if text_width(trial, size) <= max_w or current == '':
                current = trial
            else:
                lines.append(current)
                current = w
                max_w = CONTENT_W
        if current != '':
            lines.append(current)
        if not lines:
            lines = ['']
        # draw
        self.ensure(lead)
        self._draw_line_text(LEFT, self.y, label, "F2", size, BLACK)
        self._draw_line_text(LEFT + lw, self.y, lines[0], "F1", size, BLACK)
        self.y -= lead
        for ln in lines[1:]:
            self.ensure(lead)
            self._draw_line_text(LEFT, self.y, ln, "F1", size, BLACK)
            self.y -= lead

    def bullet(self, s):
        size, lead = 11, 15
        indent = 16
        text_x = LEFT + indent
        max_w = CONTENT_W - indent
        lines = wrap_text(s, size, max_w)
        if not lines:
            lines = ['']
        self.ensure(lead)
        self._draw_line_text(LEFT + 4, self.y, "-", "F1", size, ACCENT)
        self._draw_line_text(text_x, self.y, lines[0], "F1", size, BLACK)
        self.y -= lead
        for ln in lines[1:]:
            self.ensure(lead)
            self._draw_line_text(text_x, self.y, ln, "F1", size, BLACK)
            self.y -= lead

    def body(self, s, color=BLACK, size=11):
        lead = size + 5
        lines = wrap_text(s, size, CONTENT_W)
        for ln in lines:
            self.ensure(lead)
            self._draw_line_text(LEFT, self.y, ln, "F1", size, color)
            self.y -= lead

    def space(self, h):
        self.ensure(h)
        self.y -= h

    def box_note(self, lines):
        """A light highlighted summary box containing given lines of text."""
        size, lead = 11, 16
        pad = 8
        height = lead * len(lines) + pad * 2
        self.ensure(height + 6)
        top = self.y
        self.rect(LEFT, top - height + 6, CONTENT_W, height, (0.93, 0.95, 1.0))
        self.rect(LEFT, top - height + 6, 4, height, NAVY)
        yy = top - pad - 4
        for ln in lines:
            self._draw_line_text(LEFT + 14, yy, ln, "F1", size, NAVY)
            yy -= lead
        self.y = top - height


# ----------------------------------------------------------------------
# Assemble the actual document content
# ----------------------------------------------------------------------
def build_document():
    d = PDFBuilder()

    d.title("Types of Numbers")
    d.subtitle("Simplified Definitions with Examples & Notes")
    d.hline(LEFT, PAGE_W - RIGHT, d.y + 4, NAVY, 1.2)
    d.space(10)
    d.body("In maths, numbers are grouped into different families. Each family is built "
           "on top of the previous one. This guide explains each type in simple words "
           "with examples and quick revision notes.", color=GREY)
    d.space(6)

    def section(title, definition, symbol, examples, notes):
        d.h2(title)
        d.label_body("Definition:", definition)
        if symbol:
            d.label_body("Symbol:", symbol)
        d.label_body("Examples:", examples)
        d.label_body("Notes:", "")
        for n in notes:
            d.bullet(n)
        d.space(6)

    section(
        "1. Natural Numbers (N)",
        "Counting numbers that start from 1 and go on forever: 1, 2, 3, 4, ...",
        "N",
        "1, 2, 3, 4, 5, ...  (e.g. number of students in a class)",
        [
            "The smallest natural number is 1.",
            "Zero (0) is NOT a natural number.",
            "They are always positive whole numbers.",
        ],
    )

    section(
        "2. Whole Numbers (W)",
        "All natural numbers together with 0: 0, 1, 2, 3, 4, ...",
        "W",
        "0, 1, 2, 3, 4, ...",
        [
            "Whole numbers = Natural numbers + 0.",
            "The smallest whole number is 0.",
            "Every natural number is a whole number (but 0 is whole, not natural).",
        ],
    )

    section(
        "3. Integers (Z)",
        "All whole numbers plus their negatives: ..., -3, -2, -1, 0, 1, 2, 3, ...",
        "Z",
        "-100, -5, -1, 0, 3, 47",
        [
            "Includes positive numbers, negative numbers and zero.",
            "There are no fractions or decimals in integers.",
            "Zero is an integer that is neither positive nor negative.",
        ],
    )

    section(
        "4. Rational Numbers (Q)",
        "Any number that can be written as a fraction p/q, where p and q are integers "
        "and q is not equal to 0.",
        "Q",
        "1/2, -3/4, 5 (= 5/1), 0.75, 0.333... (= 1/3)",
        [
            "Decimals that terminate (end) or repeat are rational.",
            "Every integer is also a rational number.",
            "The denominator q can never be 0.",
        ],
    )

    section(
        "5. Irrational Numbers",
        "Numbers that CANNOT be written as a simple fraction p/q. Their decimal part "
        "goes on forever without repeating.",
        "",
        "pi = 3.14159..., sqrt(2) = 1.41421..., e = 2.71828...",
        [
            "They are non-terminating and non-repeating decimals.",
            "Square roots of non-perfect squares are irrational (sqrt2, sqrt3, sqrt5).",
            "pi and e are the most famous irrational numbers.",
        ],
    )

    section(
        "6. Real Numbers (R)",
        "All rational and irrational numbers together. Any number that can be placed "
        "on the number line is a real number.",
        "R",
        "-2, 0, 1/2, 7.5, sqrt(2), pi",
        [
            "Real numbers = Rational numbers + Irrational numbers.",
            "Almost every number you use day to day is a real number.",
            "Numbers like sqrt(-1) are NOT real - they are called imaginary numbers.",
        ],
    )

    section(
        "7. Even and Odd Numbers",
        "Even numbers are exactly divisible by 2; odd numbers are not divisible by 2.",
        "",
        "Even: 2, 4, 6, 8, 10  |  Odd: 1, 3, 5, 7, 9",
        [
            "Even numbers end in 0, 2, 4, 6 or 8.",
            "Odd numbers end in 1, 3, 5, 7 or 9.",
            "Zero (0) is an even number.",
        ],
    )

    section(
        "8. Prime and Composite Numbers",
        "A prime number has exactly two factors (1 and itself). A composite number "
        "has more than two factors.",
        "",
        "Prime: 2, 3, 5, 7, 11  |  Composite: 4, 6, 8, 9, 10",
        [
            "2 is the only even prime number.",
            "1 is neither prime nor composite.",
            "Smallest prime is 2; smallest composite is 4.",
        ],
    )

    d.h2("Quick Revision Summary")
    d.body("The number families fit inside one another like this:", color=GREY)
    d.space(2)
    d.box_note([
        "Natural  <  Whole  <  Integers  <  Rational  <  Real",
        "",
        "Irrational numbers are also Real, but separate from Rational.",
        "Real Numbers = Rational + Irrational  (everything on the number line).",
    ])

    return d


# ----------------------------------------------------------------------
# Low level PDF writer
# ----------------------------------------------------------------------
def write_pdf(d, filename):
    objects = []  # list of (id, bytes)

    def add(obj_bytes):
        objects.append(obj_bytes)
        return len(objects)  # 1-based id

    # Reserve fixed ids
    # 1 Catalog, 2 Pages, then per page a Page + Content, then fonts.
    catalog_id = 1
    pages_id = 2
    objects.append(b"")  # placeholder for catalog
    objects.append(b"")  # placeholder for pages

    font_reg_id = None
    font_bold_id = None

    page_obj_ids = []
    content_ids = []

    for ops in d.pages:
        stream = ("\n".join(ops)).encode("latin-1", "replace")
        content_obj = (b"<< /Length %d >>\nstream\n" % len(stream)) + stream + b"\nendstream"
        cid = add(content_obj)
        content_ids.append(cid)
        page_obj_ids.append(None)  # fill later

    # font objects
    font_reg_id = add(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>")
    font_bold_id = add(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>")

    # page objects
    for i, cid in enumerate(content_ids):
        page_def = (
            b"<< /Type /Page /Parent %d 0 R /MediaBox [0 0 %.2f %.2f] "
            b"/Resources << /Font << /F1 %d 0 R /F2 %d 0 R >> >> "
            b"/Contents %d 0 R >>"
            % (pages_id, PAGE_W, PAGE_H, font_reg_id, font_bold_id, cid)
        )
        pid = add(page_def)
        page_obj_ids[i] = pid

    kids = " ".join("%d 0 R" % pid for pid in page_obj_ids)
    objects[pages_id - 1] = (
        b"<< /Type /Pages /Kids [%s] /Count %d >>" % (kids.encode(), len(page_obj_ids))
    )
    objects[catalog_id - 1] = b"<< /Type /Catalog /Pages %d 0 R >>" % pages_id

    # Serialize
    out = bytearray()
    out += b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"
    offsets = [0] * (len(objects) + 1)
    for idx, body in enumerate(objects, start=1):
        offsets[idx] = len(out)
        out += b"%d 0 obj\n" % idx
        out += body
        out += b"\nendobj\n"

    xref_pos = len(out)
    n = len(objects) + 1
    out += b"xref\n"
    out += b"0 %d\n" % n
    out += b"0000000000 65535 f \n"
    for idx in range(1, n):
        out += b"%010d 00000 n \n" % offsets[idx]
    out += b"trailer\n"
    out += b"<< /Size %d /Root %d 0 R >>\n" % (n, catalog_id)
    out += b"startxref\n%d\n%%%%EOF\n" % xref_pos

    with open(filename, "wb") as f:
        f.write(out)
    return len(d.pages)


if __name__ == "__main__":
    doc = build_document()
    out_file = "Types_of_Numbers_Notes.pdf"
    pages = write_pdf(doc, out_file)
    print(f"Generated '{out_file}' with {pages} page(s).")
