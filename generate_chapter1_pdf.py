"""
Pure-Python PDF generator for Class 10 Maths Chapter 1: Real Numbers.
No external libraries required.

Generates: Class10_Maths_Ch1_Real_Numbers.pdf
"""

import re
import zlib
from pathlib import Path


# ---------- Content ----------
CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 1: REAL NUMBERS
==========================================

A simplified, detailed guide in Hinglish
For students who missed Class 7-8-9
Based on the official NCERT English Medium textbook
==========================================


==========================================
PART 1: FOUNDATION (Class 7-8-9 ka revision)
==========================================


1. NUMBERS KE TYPES - EK FAMILY TREE
------------------------------------

   Sochh sabhi numbers ek bada family hai.

                    Real Numbers (R)
                    /              \
            Rational (Q)        Irrational (P)
            /        \              |
      Integers (Z)  Fractions   sqrt(2), pi, e
        /    \      (1/2, 3/4)
   Whole(W)  Negative
    /    \   (-1, -2, -3)
  Zero  Natural (N)
        (1, 2, 3, 4...)


   DEFINITIONS EASY BHASHA MEIN:

   - Natural Numbers (N):  Counting numbers - 1, 2, 3, 4, 5...
   - Whole Numbers (W):    Natural + 0      - 0, 1, 2, 3...
   - Integers (Z):         Whole + negative - ..., -2, -1, 0, 1, 2...
   - Rational Numbers (Q): p/q form (q != 0)- 1/2, -3/4, 5, 0.25
   - Irrational Numbers:   NOT p/q form     - sqrt(2), sqrt(3), pi
   - Real Numbers (R):     Rational + Irrational (sab kuch)


2. RATIONAL VS IRRATIONAL - KAISE PEHCHANEN
-------------------------------------------

   RATIONAL number ki decimal expansion 2 type ki hoti hai:
     - Terminating (khatam ho jaye): 0.5, 0.25, 0.125
     - Non-terminating but Repeating: 0.333..., 0.142857142857...

   IRRATIONAL number ki decimal expansion:
     - Non-terminating AND Non-repeating
     - Example: sqrt(2) = 1.41421356237...


3. PRIME NUMBERS VS COMPOSITE NUMBERS
-------------------------------------

   PRIME NUMBER:
     Wo number jo SIRF 1 aur apne aap se divide hota hai.
     Examples: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29...

     IMPORTANT:
       - 1 prime NAHI hai!
       - 2 ekloti EVEN prime hai (baaki sab prime odd hain)

   COMPOSITE NUMBER:
     Jo prime nahi hai (1 ke alawa). Iske 2 se zyada factors hote hain.
     Examples: 4, 6, 8, 9, 10, 12, 14, 15...

   EXAMPLES:
     7 ke factors:  1, 7              -> 2 factors    -> Prime
     12 ke factors: 1, 2, 3, 4, 6, 12 -> 6 factors    -> Composite


4. HCF AUR LCM - BACHPAN SE YAAD RAKH
-------------------------------------

   HCF (Highest Common Factor) = GCD
     Sabse bada number jo dono ko divide kare.

   LCM (Least Common Multiple)
     Sabse chhota number jo dono se divide ho.

   EXAMPLE: 12 aur 18 ka HCF aur LCM
     12 ke factors: 1, 2, 3, 4, 6, 12
     18 ke factors: 1, 2, 3, 6, 9, 18
     Common factors: 1, 2, 3, 6
     HCF = 6 (sabse bada common)

     Multiples of 12: 12, 24, 36, 48...
     Multiples of 18: 18, 36, 54...
     LCM = 36 (sabse chhota common)

   MAGIC FORMULA:
     HCF x LCM = Product of two numbers

     Check: 6 x 36 = 216
            12 x 18 = 216
            Match!


==========================================
PART 2: ASLI CHAPTER 1 CONTENT (NCERT)
==========================================


TOPIC 1: THE FUNDAMENTAL THEOREM OF ARITHMETIC
----------------------------------------------

   STATEMENT:
     "Every composite number can be expressed (factorised) as
      a product of primes, and this factorisation is UNIQUE,
      apart from the order in which the prime factors occur."

   AASAAN BHASHA MEIN:
     Koi bhi composite number ko prime numbers ke multiplication
     se likh sakte hain, aur ye tareeka UNIQUE hota hai.


   EXAMPLE 1: 156 ka prime factorisation kar

     156 / 2 = 78
      78 / 2 = 39
      39 / 3 = 13
      13 / 13 = 1

     So, 156 = 2 x 2 x 3 x 13 = 2^2 x 3 x 13


   EXAMPLE 2: 3825 ka prime factorisation

     3825 / 3 = 1275
     1275 / 3 = 425
      425 / 5 = 85
       85 / 5 = 17
       17 / 17 = 1

     So, 3825 = 3^2 x 5^2 x 17


   EXAMPLE 3: 7 x 11 x 13 + 13 - kya ye composite hai?

     = 13 x (7 x 11 + 1)
     = 13 x (77 + 1)
     = 13 x 78

     Haan, ye composite hai kyunki iske factors
     1, 13, 78 ke alawa aur bhi hain.


TOPIC 2: HCF AND LCM USING PRIME FACTORISATION
----------------------------------------------

   METHOD:
     HCF = Common prime factors ka product (LOWEST power)
     LCM = Sab prime factors ka product (HIGHEST power)


   EXAMPLE 4: 96 aur 404 ka HCF aur LCM nikaal

     Step 1: Prime factorisation
       96  = 2^5 x 3
       404 = 2^2 x 101

     Step 2: HCF (common primes, lowest power)
       Common prime: 2 (lowest power = 2^2)
       HCF = 2^2 = 4

     Step 3: LCM (all primes, highest power)
       LCM = 2^5 x 3 x 101 = 32 x 3 x 101 = 9696

     Verify: HCF x LCM = 4 x 9696 = 38784
             96 x 404  = 38784
             Match!


   EXAMPLE 5: 6, 72, 120 - teen numbers ka HCF aur LCM

     Prime factorisation:
       6   = 2 x 3
       72  = 2^3 x 3^2
       120 = 2^3 x 3 x 5

     HCF (common, lowest power):
       2^1 x 3^1 = 6

     LCM (all, highest power):
       2^3 x 3^2 x 5 = 8 x 9 x 5 = 360


TOPIC 3: REVISITING IRRATIONAL NUMBERS
--------------------------------------

   THEOREM:
     Let p be a prime number. If p divides a-square (a^2),
     then p divides a (where a is a positive integer).


   FAMOUS PROOF: sqrt(2) IS IRRATIONAL
   (Ye exam mein aata hai!)

   Proof by CONTRADICTION:

   Step 1: Maan le sqrt(2) rational hai.
     Toh sqrt(2) = p/q
     where p, q are integers, q != 0,
     and HCF(p, q) = 1 (simplest form).

   Step 2: Dono sides square karo
     2 = p^2 / q^2
     2 q^2 = p^2     ...(i)

   Step 3: Iska matlab 2 divides p^2.
     Toh theorem se, 2 divides p.

   Step 4: Toh p = 2c (kisi integer c ke liye).

   Step 5: Equation (i) mein daal
     2 q^2 = (2c)^2 = 4 c^2
     q^2 = 2 c^2

   Step 6: Iska matlab 2 divides q^2,
     toh 2 divides q.

   Step 7: Ab problem!
     Humne kaha tha HCF(p, q) = 1,
     par dono ko 2 divide kar raha hai.
     Ye CONTRADICTION hai.

   CONCLUSION:
     Hamari assumption galat thi.
     Toh sqrt(2) IRRATIONAL hai. (Proved)


   EXAMPLE 6: Prove that sqrt(3) is irrational

     1. Maan le sqrt(3) = p/q (HCF = 1)
     2. 3 q^2 = p^2 -> 3 divides p^2 -> 3 divides p
     3. p = 3c -> 3 q^2 = 9 c^2 -> q^2 = 3 c^2
        -> 3 divides q
     4. Contradiction (HCF = 1 ko hum break kar diye)
     5. So sqrt(3) is irrational.


   EXAMPLE 7: Prove that 5 - sqrt(3) is irrational

     1. Maan le 5 - sqrt(3) rational hai, kaho r.
     2. Toh sqrt(3) = 5 - r.
     3. 5 - r rational hai (rational - rational = rational).
     4. Par sqrt(3) irrational hai.
     5. Contradiction! So 5 - sqrt(3) is irrational.


   EXAMPLE 8: Prove that 3 x sqrt(2) is irrational

     1. Maan le 3 x sqrt(2) rational hai, kaho r = p/q.
     2. Toh sqrt(2) = p / (3q), jo rational hai.
     3. Par sqrt(2) irrational hai.
     4. Contradiction! So 3 x sqrt(2) is irrational.


   USEFUL RULES TO REMEMBER:
     - Rational + Irrational = Irrational
     - Non-zero Rational x Irrational = Irrational
     - Irrational + Irrational = could be either
       (e.g., sqrt(2) + (-sqrt(2)) = 0 which is rational)


==========================================
PART 3: PRACTICE PROBLEMS (Tu solve kar)
==========================================

   Q1. Express 140 as a product of its prime factors.

   Q2. Find the HCF and LCM of 26 and 91 by prime
       factorisation.

   Q3. Prove that sqrt(5) is irrational.

   Q4. Show that 3 + 2 x sqrt(5) is irrational.

   Q5. Find LCM and HCF of 17, 23, 29.


==========================================
SUMMARY (YAAD RAKH)
==========================================

   1. Fundamental Theorem of Arithmetic:
      Har composite number = UNIQUE product of primes.

   2. HCF x LCM = Product of two numbers
      (sirf 2 numbers ke liye, 3 ke liye nahi).

   3. HCF = common primes x LOWEST powers

   4. LCM = all primes x HIGHEST powers

   5. sqrt(p) is IRRATIONAL when p is prime.

   6. Rational + Irrational = Irrational

   7. Non-zero Rational x Irrational = Irrational


==========================================
TIPS FOR EXAM
==========================================

   1. Prime factorisation hamesha tree method se kar -
      mistake nahi hogi.

   2. HCF aur LCM ke questions mein dono nikalna hota
      hai. Verify karne ke liye HCF x LCM = product
      formula use kar.

   3. Irrationality proofs mein "Proof by Contradiction"
      ka exact format yaad rakh:
        - Assume opposite
        - Derive equation
        - Apply theorem
        - Find contradiction
        - Conclude

   4. Common irrationality questions:
        sqrt(2), sqrt(3), sqrt(5), sqrt(7) - prove karne aate hain
        a + b x sqrt(p) form ke numbers - prove karne aate hain

   5. Numericals practice kar - NCERT exercise 1.1 aur
      example questions saari solve kar.


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 1: Real Numbers
==========================================
"""


# ---------- PDF builder ----------

PAGE_W, PAGE_H = 595, 842         # A4 in points
MARGIN_L, MARGIN_R = 50, 50
MARGIN_T, MARGIN_B = 60, 50
LINE_HEIGHT = 13
FONT_SIZE = 10
HEADER_FONT_SIZE = 14
TITLE_FONT_SIZE = 20


def escape_pdf_text(s: str) -> str:
    """Escape special characters for PDF text strings."""
    s = s.replace("\\", "\\\\")
    s = s.replace("(", "\\(").replace(")", "\\)")
    # Strip non-ASCII (built-in fonts only support WinAnsi roughly).
    s = re.sub(r"[^\x20-\x7E]", "", s)
    return s


def wrap_line(line: str, max_chars: int = 95) -> list[str]:
    """Simple wrap by characters; preserves leading indentation."""
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
    """Split content into pages of (font, size, text) line tuples."""
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


def make_content_stream(page_lines, is_first=False) -> bytes:
    """Build a single page's content stream."""
    parts = []
    if is_first:
        title = "Class 10 NCERT Maths"
        subtitle = "Chapter 1: Real Numbers - Detailed Guide"
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


def build_pdf(out_path: Path):
    pages = build_pages(CONTENT)

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
        stream = make_content_stream(page_lines, is_first=(i == 0))
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


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch1_Real_Numbers.pdf"
    build_pdf(out)
