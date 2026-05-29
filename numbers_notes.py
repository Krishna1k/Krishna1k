#!/usr/bin/env python3
"""
Pure-Python PDF generator (no external libraries).
Creates a study-notes PDF: "Numbers ke Prakar" (Types of Numbers) - Hinglish.
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
# Assemble the actual document content (Hinglish)
# ----------------------------------------------------------------------
def build_document():
    d = PDFBuilder()

    d.title("Numbers ke Prakar")
    d.subtitle("Types of Numbers - Aasan Hinglish Notes, Examples aur Practice Q's")
    d.hline(LEFT, PAGE_W - RIGHT, d.y + 4, NAVY, 1.2)
    d.space(10)
    d.body("Maths me numbers ko alag-alag families me baanta jata hai, aur har family "
           "pichli wali ke upar bani hoti hai. Is guide me har type ko simple Hinglish "
           "me examples ke saath samjhaya gaya hai, aur end me 22 practice questions "
           "(answer key ke saath) diye gaye hain.", color=GREY)
    d.space(6)

    def section(title, definition, symbol, examples, notes):
        d.h2(title)
        d.label_body("Definition:", definition)
        if symbol:
            d.label_body("Symbol:", symbol)
        d.label_body("Example:", examples)
        d.label_body("Yaad rakho:", "")
        for n in notes:
            d.bullet(n)
        d.space(6)

    section(
        "1. Natural Numbers (N)",
        "Ginti (counting) wale numbers jo 1 se shuru hote hain aur aage badhte rehte "
        "hain: 1, 2, 3, 4, ...",
        "N",
        "1, 2, 3, 4, 5, ...  (jaise class me students ki sankhya)",
        [
            "Sabse chhota natural number 1 hai.",
            "Zero (0) ek natural number NAHI hai.",
            "Ye hamesha positive whole numbers hote hain.",
        ],
    )

    section(
        "2. Whole Numbers (W)",
        "Saare natural numbers + 0 milakar: 0, 1, 2, 3, 4, ...",
        "W",
        "0, 1, 2, 3, 4, ...",
        [
            "Whole numbers = Natural numbers + 0.",
            "Sabse chhota whole number 0 hai.",
            "Har natural number ek whole number hai (par 0 whole hai, natural nahi).",
        ],
    )

    section(
        "3. Integers (Z)",
        "Saare whole numbers + unke negatives: ..., -3, -2, -1, 0, 1, 2, 3, ...",
        "Z",
        "-100, -5, -1, 0, 3, 47",
        [
            "Isme positive, negative aur zero teeno aate hain.",
            "Integers me koi fraction ya decimal nahi hota.",
            "Zero ek integer hai jo na positive hai na negative.",
        ],
    )

    section(
        "4. Rational Numbers (Q)",
        "Wo numbers jinhe p/q fraction ke roop me likha ja sake, jahan p aur q integers "
        "hon aur q zero ke barabar na ho.",
        "Q",
        "1/2, -3/4, 5 (= 5/1), 0.75, 0.333... (= 1/3)",
        [
            "Jo decimals khatam ho jayein (terminating) ya repeat hon, wo rational hain.",
            "Har integer bhi ek rational number hai.",
            "Denominator q kabhi 0 nahi ho sakta.",
        ],
    )

    section(
        "5. Irrational Numbers",
        "Wo numbers jinhe simple fraction p/q me NAHI likha ja sakta. Inka decimal part "
        "kabhi khatam nahi hota aur repeat bhi nahi karta.",
        "",
        "pi = 3.14159..., sqrt(2) = 1.41421..., e = 2.71828...",
        [
            "Ye non-terminating aur non-repeating decimals hote hain.",
            "Non-perfect squares ke square root irrational hote hain (sqrt2, sqrt3, sqrt5).",
            "pi aur e sabse famous irrational numbers hain.",
        ],
    )

    section(
        "6. Real Numbers (R)",
        "Saare rational aur irrational numbers milakar. Jo bhi number number-line par "
        "rakha ja sake, wo real number hai.",
        "R",
        "-2, 0, 1/2, 7.5, sqrt(2), pi",
        [
            "Real numbers = Rational numbers + Irrational numbers.",
            "Roz-marra ke lagbhag saare numbers real numbers hote hain.",
            "sqrt(-1) jaise numbers real NAHI hote - unhe imaginary numbers kehte hain.",
        ],
    )

    section(
        "7. Even aur Odd Numbers",
        "Even numbers 2 se poori tarah divide ho jate hain; odd numbers 2 se divide "
        "nahi hote.",
        "",
        "Even: 2, 4, 6, 8, 10  |  Odd: 1, 3, 5, 7, 9",
        [
            "Even numbers ke end me 0, 2, 4, 6 ya 8 aata hai.",
            "Odd numbers ke end me 1, 3, 5, 7 ya 9 aata hai.",
            "Zero (0) ek even number hai.",
        ],
    )

    section(
        "8. Prime aur Composite Numbers",
        "Prime number ke exactly do factors hote hain (1 aur khud wo number). Composite "
        "number ke do se zyada factors hote hain.",
        "",
        "Prime: 2, 3, 5, 7, 11  |  Composite: 4, 6, 8, 9, 10",
        [
            "2 hi ekmatra even prime number hai.",
            "1 na prime hai na composite.",
            "Sabse chhota prime 2 hai; sabse chhota composite 4 hai.",
        ],
    )

    d.h2("Quick Revision Summary")
    d.body("Number families ek dusre ke andar aise fit hoti hain:", color=GREY)
    d.space(2)
    d.box_note([
        "Natural  <  Whole  <  Integers  <  Rational  <  Real",
        "",
        "Irrational numbers bhi Real hain, par Rational se alag.",
        "Real Numbers = Rational + Irrational  (number line ke saare numbers).",
    ])
    d.space(6)

    # ---- Practice Questions -----------------------------------------
    d.h2("Practice Questions (Khud Try Karo!)")
    d.body("In 22 questions ko khud solve karne ki koshish karo. Answers neeche answer "
           "key me diye gaye hain.", color=GREY)
    d.space(3)

    questions = [
        "Sabse chhota natural number kaunsa hai?",
        "Sabse chhota whole number kaunsa hai?",
        "Kya 0 ek natural number hai? (Haan/Nahi)",
        "Kya 0 ek whole number hai? (Haan/Nahi)",
        "-5 kis type ka number hai (natural / whole / integer)?",
        "Kya har natural number ek whole number hota hai?",
        "3/4 kis type ka number hai?",
        "sqrt(2) rational hai ya irrational?",
        "pi (3.14159...) rational hai ya irrational?",
        "7 ko p/q form me likho.",
        "Kya 0.75 rational hai? (Haan/Nahi)",
        "Sabse chhota prime number kaunsa hai?",
        "Kya 1 prime hai ya composite?",
        "2 ke alawa koi aur even prime number hai? (Haan/Nahi)",
        "4, 6 aur 8 - ye prime hain ya composite?",
        "Kya 0 even hai ya odd?",
        "17 prime hai ya composite?",
        "Real numbers kis-kis se milkar bante hain?",
        "Kya sqrt(-1) ek real number hai?",
        "-3, 0 aur 5 - ye sab kis ek hi category me aate hain?",
        "9 ke saare factors likho. Kya 9 composite hai?",
        "0.333... (repeating) rational hai ya irrational?",
    ]
    for i, q in enumerate(questions, start=1):
        d.label_body(f"Q{i}.", q)
        d.space(2)

    # ---- Answer Key --------------------------------------------------
    d.h2("Answer Key")
    answers = [
        "1   (sabse chhota natural number)",
        "0   (sabse chhota whole number)",
        "Nahi   (0 natural number nahi hai)",
        "Haan   (0 whole number hai)",
        "Integer   (negative hone ke kaaran natural/whole nahi)",
        "Haan   (par 0 whole hai, natural nahi)",
        "Rational number   (p/q form me likha ja sakta hai)",
        "Irrational   (p/q form me nahi likh sakte)",
        "Irrational   (non-terminating, non-repeating)",
        "7/1",
        "Haan   (0.75 terminating decimal hai)",
        "2",
        "Dono nahi - 1 na prime hai na composite",
        "Nahi - 2 hi ekmatra even prime hai",
        "Composite   (sabke 2 se zyada factors hain)",
        "Even   (0 even number hai)",
        "Prime   (factors sirf 1 aur 17)",
        "Rational + Irrational numbers",
        "Nahi   (ye imaginary number hai)",
        "Integers",
        "Factors: 1, 3, 9 - Haan, 9 composite hai (2 se zyada factors)",
        "Rational   (repeating decimal = 1/3)",
    ]
    for i, a in enumerate(answers, start=1):
        d.bullet(f"Q{i}: {a}")

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
