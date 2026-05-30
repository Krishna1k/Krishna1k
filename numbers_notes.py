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
GREEN = (0.0, 0.50, 0.18)
LIGHT_GREEN = (0.88, 0.96, 0.88)
RED = (0.85, 0.11, 0.11)


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

    def exam_tag(self, note="Exam me CONSTANTLY aata hai"):
        """Green 'EXAM' badge marking an exam-frequent topic."""
        label = "EXAM"
        size = 8
        pad = 4
        self.ensure(15)
        bw = text_width(label, size) + pad * 2
        x = LEFT + 16
        y = self.y
        # green filled badge with white text
        self.rect(x, y - 2, bw, 12, GREEN)
        self._draw_line_text(x + pad, y, label, "F2", size, (1, 1, 1))
        # note text in green next to badge
        self._draw_line_text(x + bw + 6, y, "* " + note, "F2", 8.5, GREEN)
        self.y -= 15

    def legend_exam(self):
        """Small explanation of the green EXAM tag."""
        self.exam_tag("aise green tag wale topics exams me baar-baar aate hain")
        self.space(2)

    def red_heading(self, s):
        """Bold RED numbered heading for the Core Basics 'red page' style."""
        size, lead = 15, 22
        self.ensure(lead + 10)
        self.y -= 6
        self._draw_line_text(LEFT, self.y, s, "F2", size, RED)
        self.y -= lead

    def red_body(self, s):
        """Red wrapped body text (indented), red-page style."""
        size, lead = 11.5, 16
        indent = 16
        text_x = LEFT + indent
        max_w = CONTENT_W - indent
        lines = wrap_text(s, size, max_w)
        if not lines:
            lines = ['']
        for ln in lines:
            self.ensure(lead)
            self._draw_line_text(text_x, self.y, ln, "F1", size, RED)
            self.y -= lead

    def red_title_bar(self, s):
        """Top banner heading for the red page (with rules above/below)."""
        self.hline(LEFT, PAGE_W - RIGHT, self.y + 6, BLACK, 1.0)
        self.space(6)
        self._draw_line_text(LEFT, self.y, s, "F2", 17, RED)
        self.y -= 22
        self.hline(LEFT, PAGE_W - RIGHT, self.y + 6, BLACK, 1.0)
        self.y -= 8


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
           "me examples ke saath samjhaya gaya hai, fir solved examples aur end me 22 "
           "practice questions ke step-by-step solutions diye gaye hain.", color=GREY)
    d.space(4)
    d.legend_exam()
    d.space(4)

    def section(title, definition, symbol, examples, notes, exam=False):
        d.h2(title)
        if exam:
            d.exam_tag()
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
        exam=True,
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
        exam=True,
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
        exam=True,
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
        exam=True,
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
        exam=True,
    )

    # ---- 9. More important types ------------------------------------
    d.h2("9. Aur Zaroori Types (Exam Favourite)")
    d.exam_tag()
    d.label_body("Co-prime Numbers:", "Do numbers jinka HCF sirf 1 ho. Jaroori nahi ki "
                 "wo khud prime hon. Jaise (8, 9), (15, 16).")
    d.label_body("Consecutive Numbers:", "Lagatar aane wale numbers jaise 5, 6, 7. Do "
                 "consecutive numbers ka antar hamesha 1 hota hai.")
    d.label_body("Twin Primes:", "Aise do prime numbers jinke beech sirf 2 ka antar ho. "
                 "Jaise (3, 5), (11, 13), (17, 19).")
    d.label_body("Perfect Numbers:", "Wo number jiske apne factors ka jod (khud ko "
                 "chhodkar) usi number ke barabar ho. Jaise 6 = 1 + 2 + 3.")
    d.label_body("Number Line:", "Ek seedhi line jisme left me negative, beech me 0, "
                 "aur right me positive numbers hote hain. Har real number is par ek "
                 "point hota hai.")
    d.space(6)

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

    # ---- Solved Examples --------------------------------------------
    d.h2("Solved Examples - Samjho Kaise Pehchante Hain")
    d.body("Neeche 10 examples step-by-step solve karke dikhaye gaye hain, taaki number "
           "classify karna aur reasoning clear ho jaye.", color=GREY)
    d.space(3)

    examples = [
        ("Example 1:  -7 kis type ka number hai?",
         ["Negative hai, isliye natural ya whole nahi.",
          "Bina fraction ke poora number hai -> Integer.",
          "-7 = -7/1 likh sakte hain -> Rational bhi hai."],
         "Integer (aur Rational)"),
        ("Example 2:  sqrt(16) rational hai ya irrational?",
         ["Pehle value nikalo: sqrt(16) = 4.",
          "4 ek whole number hai -> 4/1 (p/q form).",
          "(Trick: 16 perfect square hai, isliye root rational nikla!)"],
         "Rational"),
        ("Example 3:  0.1010010001... rational ya irrational?",
         ["Decimal kabhi khatam nahi hota aur koi pattern repeat nahi karta."],
         "Irrational"),
        ("Example 4:  0.6 ko p/q form me likho.",
         ["0.6 = 6/10.",
          "HCF 2 se simplify: 6/10 = 3/5."],
         "3/5"),
        ("Example 5:  Kya 14 aur 15 co-prime hain?",
         ["14 = 2 x 7,  15 = 3 x 5.",
          "Koi common factor nahi -> HCF = 1."],
         "Haan, co-prime hain"),
        ("Example 6:  1 prime hai, composite hai, ya dono nahi?",
         ["Prime ke 2 factors hote hain; composite ke 2 se zyada.",
          "1 ka sirf ek factor hai (khud)."],
         "Dono nahi (neither)"),
        ("Example 7:  1/3 aur 1/2 ke beech ek rational number batao.",
         ["Dono ka average lo: (1/3 + 1/2) / 2.",
          "= (5/6) / 2 = 5/12 (ye 1/3 aur 1/2 ke beech hai)."],
         "5/12"),
        ("Example 8:  Sabse chhota 2-digit prime number?",
         ["10 composite hai (2 x 5).",
          "11 ke factors sirf 1 aur 11."],
         "11"),
        ("Example 9:  Kya 2 ke alawa koi even prime hai?",
         ["Har dusra even number 2 se divide hota hai.",
          "Isliye uske 2 se zyada factors -> composite."],
         "Nahi, sirf 2"),
        ("Example 10:  pi ko classify karo.",
         ["pi = 3.14159... non-terminating, non-repeating.",
          "Isliye Irrational; aur number line par hai to Real bhi."],
         "Irrational (aur Real)"),
    ]
    for q, steps, ans in examples:
        d.label_body(q, "")
        for s in steps:
            d.bullet(f"Step: {s}")
        d.label_body("   Answer:", ans)
        d.space(5)

    # ---- Practice Questions -----------------------------------------
    d.h2("Practice Questions")
    d.body("Pehle khud solve karne ki koshish karo. Neeche har question ka step-by-step "
           "solution diya gaya hai.", color=GREY)
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

    # ---- Step-by-Step Solutions -------------------------------------
    d.h2("Step-by-Step Solutions")
    solutions = [
        ("Sabse chhota natural number?",
         ["Natural numbers 1 se shuru hote hain."], "1"),
        ("Sabse chhota whole number?",
         ["Whole numbers 0 se shuru hote hain."], "0"),
        ("Kya 0 ek natural number hai?",
         ["Natural 1 se shuru; 0 unme nahi aata."], "Nahi"),
        ("Kya 0 ek whole number hai?",
         ["Whole = Natural + 0, isliye 0 whole hai."], "Haan"),
        ("-5 kis type ka number hai?",
         ["Negative hai -> natural/whole nahi.", "Bina fraction ke poora -> Integer."],
         "Integer (aur Rational)"),
        ("Kya har natural number whole hota hai?",
         ["Whole = Natural + 0, to har natural whole hai."], "Haan"),
        ("3/4 kis type ka number hai?",
         ["p/q form me hai (q != 0)."], "Rational"),
        ("sqrt(2) rational ya irrational?",
         ["sqrt(2) = 1.414... non-terminating, non-repeating."], "Irrational"),
        ("pi rational ya irrational?",
         ["pi = 3.14159... kabhi khatam/repeat nahi hota."], "Irrational"),
        ("7 ko p/q form me likho.",
         ["Kisi whole number ko /1 likh sakte hain."], "7/1"),
        ("Kya 0.75 rational hai?",
         ["0.75 = 75/100 = 3/4 (terminating decimal)."], "Haan"),
        ("Sabse chhota prime number?",
         ["1 prime nahi; 2 ke sirf 2 factors (1, 2)."], "2"),
        ("1 prime hai ya composite?",
         ["1 ka sirf ek factor hai (khud)."], "Dono nahi (neither)"),
        ("2 ke alawa koi even prime?",
         ["Baaki even numbers 2 se divisible -> 2 se zyada factors."], "Nahi"),
        ("4, 6, 8 prime ya composite?",
         ["Sabke 2 se zyada factors hain."], "Composite"),
        ("0 even hai ya odd?",
         ["0 ko 2 poora divide karta hai (0/2 = 0)."], "Even"),
        ("17 prime ya composite?",
         ["17 ke factors sirf 1 aur 17."], "Prime"),
        ("Real numbers kis-kis se bante hain?",
         ["Real = Rational + Irrational."], "Rational + Irrational"),
        ("Kya sqrt(-1) real number hai?",
         ["Kisi real number ka square negative nahi hota."], "Nahi (imaginary)"),
        ("-3, 0, 5 kis category me aate hain?",
         ["Teeno bina fraction ke poore numbers hain."], "Integers"),
        ("9 ke factors; kya 9 composite hai?",
         ["Factors: 1, 3, 9 -> 2 se zyada factors."], "1,3,9; Haan composite"),
        ("0.333... rational ya irrational?",
         ["Repeating decimal = 1/3, p/q form me likha ja sakta hai."], "Rational"),
    ]
    for i, (q, steps, ans) in enumerate(solutions, start=1):
        d.label_body(f"Q{i}.", q)
        for s in steps:
            d.bullet(f"Step: {s}")
        d.label_body("   Answer:", ans)
        d.space(4)

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
