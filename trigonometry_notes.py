#!/usr/bin/env python3
"""
Chapter 8: Introduction to Trigonometry - Hinglish notes PDF.
Red-page core basics (PART A) + main chapter content (PART B), green EXAM tags,
solved examples + step-by-step solutions.
numbers_notes.py ka pure-Python PDF engine reuse karta hai.

Output: Trigonometry_Notes.pdf
"""

from numbers_notes import (
    PDFBuilder, write_pdf,
    LEFT, RIGHT, PAGE_W, NAVY, GREY,
)


def build_document():
    d = PDFBuilder()

    d.title("Introduction to Trigonometry")
    d.subtitle("Chapter 8 - Hinglish Notes, Ratios, Table, Identities + Solutions")
    d.hline(LEFT, PAGE_W - RIGHT, d.y + 4, NAVY, 1.2)
    d.space(10)
    d.body("Ye Chapter 8 (Introduction to Trigonometry) ka complete guide hai. Pehle "
           "red-page ke core basics (right triangle, teen sides, ratio, reciprocal, "
           "square notation, trick), fir chapter ka main content - 6 trig ratios, "
           "standard table, identities aur complementary angles. End me solved examples "
           "aur 20 practice questions ke step-by-step solutions hain.", color=GREY)
    d.space(4)
    d.legend_exam()
    d.space(4)

    # ================= PART A : CORE BASICS =========================
    d.h2("PART A - Core Basics (Miss Mat Karna)")
    d.space(2)

    d.h2("1. Right-Angled Triangle")
    d.exam_tag()
    d.bullet("Ek angle 90 degree wala triangle.")
    d.bullet("Poori trigonometry isi par based hai.")
    d.space(6)

    d.h2("2. Teen Sides (angle theta ke reference se)")
    d.exam_tag()
    d.bullet("HYPOTENUSE = 90 degree ke saamne wali (sabse lambi side).")
    d.bullet("PERPENDICULAR (Opposite) = theta ke saamne wali side.")
    d.bullet("BASE (Adjacent) = theta ke saath wali side (hypotenuse nahi).")
    d.space(6)

    d.h2("3. Ratio / Fraction")
    d.exam_tag()
    d.bullet("Ratio = upar / neeche (jaise 3/5).")
    d.bullet("Trig ratios bhi bas sides ke fractions hi hote hain.")
    d.space(6)

    d.h2("4. Reciprocal (ulta)")
    d.exam_tag()
    d.bullet("1/x ko x ka reciprocal kehte hain.")
    d.bullet("sin ka reciprocal cosec, cos ka sec, tan ka cot.")
    d.space(6)

    d.h2("5. Square Notation")
    d.exam_tag()
    d.bullet("sin^2(A) ka matlab (sin A)^2 = (sin A) x (sin A).")
    d.bullet("Ye sin(A^2) NAHI hai! Dhyaan rakho.")
    d.space(6)

    d.h2("6. Square Root Values")
    d.bullet("sqrt(2) = 1.414,  sqrt(3) = 1.732  (yaad rakho).")
    d.space(6)

    d.h2("7. Ratio Yaad Karne ka Trick")
    d.exam_tag()
    d.bullet("\"Pandit Badri Prasad / Har Har Bole / Sona Chandi Tole\"")
    d.bullet("Perpendicular / Hypotenuse = sin")
    d.bullet("Base / Hypotenuse = cos")
    d.bullet("Perpendicular / Base = tan")
    d.space(6)

    # ================= PART B : MAIN CONTENT ========================
    d.h2("PART B - Chapter 8 ka Main Content")
    d.space(2)

    d.h2("8. 6 Trigonometric Ratios")
    d.exam_tag()
    d.label_body("P = Perpendicular, B = Base, H = Hypotenuse:", "")
    d.bullet("sin = P/H,   cos = B/H,   tan = P/B")
    d.bullet("cosec = H/P,  sec = H/B,  cot = B/P")
    d.space(6)

    d.h2("9. Reciprocal Relations")
    d.exam_tag()
    d.bullet("sin x cosec = 1   (cosec = 1/sin)")
    d.bullet("cos x sec = 1    (sec = 1/cos)")
    d.bullet("tan x cot = 1    (cot = 1/tan)")
    d.bullet("Aur: tan = sin/cos,  cot = cos/sin.")
    d.space(6)

    d.h2("10. Standard Values Table")
    d.exam_tag()
    d.box_note([
        "angle :   0      30      45      60      90",
        "sin   :   0     1/2    1/sqrt2  sqrt3/2  1",
        "cos   :   1   sqrt3/2  1/sqrt2   1/2     0",
        "tan   :   0   1/sqrt3    1      sqrt3   undefined",
    ])
    d.bullet("Trick: sin ke liye 0,1,2,3,4 ko 4 se divide karke sqrt lo (0, 1/2, "
             "1/sqrt2, sqrt3/2, 1).")
    d.bullet("cos = sin ka ulta order; tan = sin/cos.")
    d.space(6)

    d.h2("11. Trigonometric Identities")
    d.exam_tag()
    d.box_note([
        "sin^2(A) + cos^2(A) = 1",
        "1 + tan^2(A) = sec^2(A)",
        "1 + cot^2(A) = cosec^2(A)",
    ])
    d.bullet("In identities se values aur proofs nikalte hain.")
    d.space(6)

    d.h2("12. Complementary Angles (90 - theta)")
    d.exam_tag()
    d.bullet("sin(90 - A) = cos A,   cos(90 - A) = sin A")
    d.bullet("tan(90 - A) = cot A,   cot(90 - A) = tan A")
    d.bullet("sec(90 - A) = cosec A, cosec(90 - A) = sec A")
    d.space(6)

    d.h2("13. Word Problems / Uses")
    d.bullet("Height aur distance ke problems me trig ratios use hote hain.")
    d.bullet("Diye gaye angle aur ek side se baaki sides nikalte hain.")
    d.space(6)

    d.h2("Quick Revision")
    d.box_note([
        "sin=P/H, cos=B/H, tan=P/B (Pandit Badri Prasad...).",
        "cosec/sec/cot = sin/cos/tan ke reciprocal.",
        "sin^2+cos^2=1; 1+tan^2=sec^2; 1+cot^2=cosec^2.",
        "Table yaad: 0,30,45,60,90.",
        "sin(90-A)=cosA (complementary).",
    ])
    d.space(6)

    # ---- Solved Examples --------------------------------------------
    d.h2("Solved Examples - Samjho Kaise Solve Karte Hain")
    d.body("Neeche 10 examples step-by-step solve karke dikhaye gaye hain.", color=GREY)
    d.space(3)

    examples = [
        ("Example 1:  Right triangle me P=3, B=4. H aur sin nikalo.",
         ["H = sqrt(P^2 + B^2) = sqrt(9+16) = sqrt(25) = 5.",
          "sin = P/H = 3/5."],
         "H = 5, sin = 3/5"),
        ("Example 2:  sin A = 3/5 ho to cos A?",
         ["sin^2 + cos^2 = 1 -> cos^2 = 1 - 9/25 = 16/25.",
          "cos = sqrt(16/25) = 4/5."],
         "cos A = 4/5"),
        ("Example 3:  sin 30 + cos 60 = ?",
         ["sin 30 = 1/2, cos 60 = 1/2.",
          "1/2 + 1/2."],
         "1"),
        ("Example 4:  tan 45 ka value?",
         ["Table se tan 45."],
         "1"),
        ("Example 5:  cosec 30 ka value?",
         ["cosec = 1/sin. sin 30 = 1/2.",
          "cosec 30 = 1/(1/2) = 2."],
         "2"),
        ("Example 6:  sin 60 . cos 30 + cos 60 . sin 30 = ?",
         ["= (sqrt3/2)(sqrt3/2) + (1/2)(1/2).",
          "= 3/4 + 1/4 = 4/4."],
         "1"),
        ("Example 7:  Simplify sin^2(30) + cos^2(30).",
         ["Identity: sin^2 + cos^2 = 1 (kisi bhi angle ke liye)."],
         "1"),
        ("Example 8:  sin(90 - A) ko simplify karo.",
         ["Complementary angle rule lagao."],
         "cos A"),
        ("Example 9:  tan 60 / tan 30 = ?",
         ["tan 60 = sqrt3, tan 30 = 1/sqrt3.",
          "= sqrt3 / (1/sqrt3) = sqrt3 x sqrt3 = 3."],
         "3"),
        ("Example 10:  Agar sec A = 2, to cos A?",
         ["cos = 1/sec = 1/2."],
         "cos A = 1/2"),
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
        "sin theta kis ratio ke barabar hota hai (P/B/H me)?",
        "cos theta kis ratio ke barabar hota hai?",
        "tan theta kis ratio ke barabar hota hai?",
        "sin ka reciprocal kya hota hai?",
        "cos ka reciprocal kya hota hai?",
        "tan ka reciprocal kya hota hai?",
        "sin 30 ka value kya hai?",
        "cos 60 ka value kya hai?",
        "tan 45 ka value kya hai?",
        "sin 90 ka value kya hai?",
        "cos 0 ka value kya hai?",
        "Main identity sin^2 + cos^2 = ? batao.",
        "1 + tan^2(A) kis ke barabar hai?",
        "sin(90 - A) kis ke barabar hai?",
        "cosec 30 ka value?",
        "sec 60 ka value?",
        "sin^2(A) ka matlab kya hai?",
        "sqrt(2) aur sqrt(3) ke approx values?",
        "tan 60 ka value?",
        "Hypotenuse triangle me kaunsi side hoti hai?",
    ]
    for i, q in enumerate(questions, start=1):
        d.label_body(f"Q{i}.", q)
        d.space(2)

    # ---- Step-by-Step Solutions -------------------------------------
    d.h2("Step-by-Step Solutions")
    solutions = [
        ("sin theta = ?",
         ["Perpendicular upar, Hypotenuse neeche."], "P / H"),
        ("cos theta = ?",
         ["Base upar, Hypotenuse neeche."], "B / H"),
        ("tan theta = ?",
         ["Perpendicular upar, Base neeche."], "P / B"),
        ("sin ka reciprocal?",
         ["1/sin."], "cosec"),
        ("cos ka reciprocal?",
         ["1/cos."], "sec"),
        ("tan ka reciprocal?",
         ["1/tan."], "cot"),
        ("sin 30?",
         ["Table se."], "1/2"),
        ("cos 60?",
         ["Table se."], "1/2"),
        ("tan 45?",
         ["Table se."], "1"),
        ("sin 90?",
         ["Table se."], "1"),
        ("cos 0?",
         ["Table se."], "1"),
        ("sin^2 + cos^2 = ?",
         ["Pythagorean identity."], "1"),
        ("1 + tan^2(A) = ?",
         ["Identity."], "sec^2(A)"),
        ("sin(90 - A) = ?",
         ["Complementary."], "cos A"),
        ("cosec 30?",
         ["1/sin30 = 1/(1/2)."], "2"),
        ("sec 60?",
         ["1/cos60 = 1/(1/2)."], "2"),
        ("sin^2(A) ka matlab?",
         ["(sin A) ka square."], "(sin A)^2"),
        ("sqrt2, sqrt3 approx?",
         ["Yaad rakhne wale values."], "1.414 aur 1.732"),
        ("tan 60?",
         ["Table se."], "sqrt(3)"),
        ("Hypotenuse kaunsi side?",
         ["90 degree ke saamne, sabse lambi."], "Sabse lambi (opposite to 90)"),
    ]
    for i, (q, steps, ans) in enumerate(solutions, start=1):
        d.label_body(f"Q{i}.", q)
        for s in steps:
            d.bullet(f"Step: {s}")
        d.label_body("   Answer:", ans)
        d.space(4)

    return d


if __name__ == "__main__":
    doc = build_document()
    out_file = "Trigonometry_Notes.pdf"
    pages = write_pdf(doc, out_file)
    print(f"Generated '{out_file}' with {pages} page(s).")
