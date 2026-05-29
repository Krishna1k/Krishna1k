#!/usr/bin/env python3
"""
Fractions (Bhinn) study-notes ki PDF - Hinglish, with step-by-step solutions.
numbers_notes.py ka pure-Python PDF engine reuse karta hai
(koi external library nahi chahiye), style baaki notes jaisa.

Output: Fractions_Notes.pdf
"""

from numbers_notes import (
    PDFBuilder, write_pdf,
    LEFT, RIGHT, PAGE_W, NAVY, GREY,
)


def build_document():
    d = PDFBuilder()

    # ---- Title -------------------------------------------------------
    d.title("Fractions (Bhinn)")
    d.subtitle("Hinglish Notes, Types, Operations aur Step-by-Step Solutions")
    d.hline(LEFT, PAGE_W - RIGHT, d.y + 4, NAVY, 1.2)
    d.space(10)
    d.body("Fraction kisi poori cheez ke hisse (part) ko represent karta hai. Is guide "
           "me fraction kya hai, uske types, simplest form, comparison aur sabhi "
           "operations (jod-ghata-guna-bhaag) simple Hinglish me samjhaye gaye hain, "
           "aur end me 22 practice questions ke STEP-BY-STEP solutions diye gaye hain.",
           color=GREY)
    d.space(6)

    # ---- 1. What is a fraction --------------------------------------
    d.h2("1. Fraction kya hota hai?")
    d.label_body("Definition:", "Fraction kisi cheez ke barabar hisson me se kuch hisson "
                 "ko batata hai. Ise p/q form me likha jata hai.")
    d.label_body("Example:", "3/4 ka matlab - poori cheez ko 4 barabar hisson me baanta, "
                 "aur usme se 3 hisse liye.")
    d.label_body("Parts:", "")
    d.bullet("Numerator (ansh) = upar wala number (kitne hisse liye). Jaise 3/4 me 3.")
    d.bullet("Denominator (har) = neeche wala number (total kitne hisse). Jaise 3/4 me 4.")
    d.bullet("Denominator kabhi 0 nahi ho sakta.")
    d.space(6)

    # ---- 2. Types ----------------------------------------------------
    d.h2("2. Fractions ke Types")
    d.bullet("Proper Fraction: numerator < denominator. Jaise 3/4, 2/5.")
    d.bullet("Improper Fraction: numerator >= denominator. Jaise 7/4, 5/5.")
    d.bullet("Mixed Fraction: whole number + proper fraction. Jaise 1 3/4.")
    d.bullet("Like Fractions: same denominator. Jaise 2/5 aur 3/5.")
    d.bullet("Unlike Fractions: alag denominator. Jaise 1/2 aur 1/3.")
    d.bullet("Equivalent Fractions: value barabar. Jaise 1/2 = 2/4 = 3/6.")
    d.bullet("Unit Fraction: numerator 1 ho. Jaise 1/5, 1/8.")
    d.space(6)

    # ---- 3. Equivalent & simplest form ------------------------------
    d.h2("3. Equivalent Fractions aur Simplest Form")
    d.label_body("Equivalent banane:", "Numerator aur denominator dono ko same number "
                 "se multiply ya divide karo. Jaise 1/2 = (1x2)/(2x2) = 2/4.")
    d.label_body("Simplest Form:", "Numerator aur denominator ko unke HCF se divide karo "
                 "jab tak aur simplify na ho sake.")
    d.bullet("Example: 6/9 -> HCF 3 -> (6/3)/(9/3) = 2/3 (simplest form).")
    d.space(6)

    # ---- 4. Comparing ------------------------------------------------
    d.h2("4. Fractions ki Comparison")
    d.bullet("Same denominator ho to bada numerator wala fraction bada hota hai. "
             "Jaise 3/5 > 2/5.")
    d.bullet("Alag denominator ho to LCM lekar same denominator banao, fir compare karo.")
    d.bullet("Same numerator ho to chhota denominator wala bada hota hai. "
             "Jaise 1/2 > 1/3.")
    d.space(6)

    # ---- 5. Operations ----------------------------------------------
    d.h2("5. Fractions par Operations")
    d.label_body("(a) Addition / Subtraction:", "Same denominator ho to numerators jodo/"
                 "ghatao, denominator wahi rakho. Alag ho to pehle LCM se same banao.")
    d.bullet("Example: 1/2 + 1/3 -> LCM 6 -> 3/6 + 2/6 = 5/6")
    d.label_body("(b) Multiplication:", "Numerator x numerator, denominator x denominator. "
                 "Fir simplify karo.")
    d.bullet("Example: 2/3 x 3/4 = 6/12 = 1/2")
    d.label_body("(c) Division:", "Doosre fraction ko ulta (reciprocal) karke multiply karo.")
    d.bullet("Example: 1/2 div 1/4 = 1/2 x 4/1 = 4/2 = 2")
    d.space(6)

    # ---- 6. Conversions ---------------------------------------------
    d.h2("6. Conversions")
    d.label_body("Improper -> Mixed:", "Numerator ko denominator se divide karo. Quotient "
                 "= whole part, remainder/denominator = fraction part.")
    d.bullet("Example: 7/2 -> 7 div 2 = 3 remainder 1 -> 3 1/2")
    d.label_body("Mixed -> Improper:", "(whole x denominator) + numerator, denominator wahi.")
    d.bullet("Example: 2 1/3 -> (2x3)+1 = 7 -> 7/3")
    d.label_body("Fraction -> Decimal:", "Numerator ko denominator se divide karo. "
                 "Jaise 1/4 = 0.25.")
    d.space(6)

    # ---- Quick summary ----------------------------------------------
    d.h2("Quick Revision")
    d.box_note([
        "Proper: upar < neeche (3/4)    |    Improper: upar >= neeche (7/4)",
        "Add/Subtract: denominator same karo (LCM).",
        "Multiply: seedha upar-upar, neeche-neeche.",
        "Divide: doosre ko ulta karke multiply.",
        "Simplest form: HCF se divide.",
    ])
    d.space(6)

    # ---- Practice Questions -----------------------------------------
    d.h2("Practice Questions")
    d.body("Pehle khud solve karne ki koshish karo. Neeche har question ka step-by-step "
           "solution diya gaya hai.", color=GREY)
    d.space(3)

    questions = [
        "3/4 me numerator kaunsa number hai?",
        "7/4 kis type ka fraction hai (proper / improper)?",
        "Kya 2/3 aur 4/6 equivalent fractions hain?",
        "5/10 ko simplest form me likho.",
        "1/2 + 1/2 = ?",
        "3/5 + 1/5 = ?",
        "1/2 + 1/3 = ?",
        "3/4 - 1/4 = ?",
        "2/3 x 3/4 = ?",
        "1/2 div 1/4 = ?",
        "7/2 ko mixed fraction me likho.",
        "2 1/3 ko improper fraction me likho.",
        "1/4 ko decimal me likho.",
        "Proper fraction ki definition kya hai?",
        "Unit fraction kya hota hai? Ek example do.",
        "Kya 4/8, 1/2 aur 3/6 sab equivalent hain?",
        "2/5 aur 3/5 me se bada kaunsa hai?",
        "1/2 aur 1/3 me se bada kaunsa hai?",
        "6/9 ka simplest form kya hai?",
        "3/4 x 4 = ?",
        "Mixed fraction kya hota hai? Ek example do.",
        "0.5 ko fraction me likho.",
    ]
    for i, q in enumerate(questions, start=1):
        d.label_body(f"Q{i}.", q)
        d.space(2)

    # ---- Step-by-Step Solutions -------------------------------------
    d.h2("Step-by-Step Solutions")

    # Each item: (short question, [step lines...], final answer)
    solutions = [
        ("3/4 me numerator?",
         ["Fraction me upar wala number numerator hota hai.",
          "3/4 me upar 3 hai."],
         "Numerator = 3"),
        ("7/4 ka type?",
         ["Numerator = 7, Denominator = 4.",
          "Yahan numerator (7) > denominator (4)."],
         "Improper Fraction"),
        ("2/3 aur 4/6 equivalent?",
         ["2/3 ke upar-neeche ko 2 se multiply karo.",
          "(2x2)/(3x2) = 4/6.",
          "Dono ki value barabar nikli."],
         "Haan, equivalent hain"),
        ("5/10 simplest form?",
         ["HCF(5, 10) = 5 nikalo.",
          "Upar-neeche ko 5 se divide: (5/5)/(10/5)."],
         "1/2"),
        ("1/2 + 1/2 = ?",
         ["Denominator same (2) hai, to numerators jodo.",
          "(1+1)/2 = 2/2.",
          "2/2 simplify -> 1."],
         "1"),
        ("3/5 + 1/5 = ?",
         ["Denominator same (5) hai.",
          "Numerators jodo: (3+1)/5."],
         "4/5"),
        ("1/2 + 1/3 = ?",
         ["Denominator alag hain -> LCM(2,3) = 6.",
          "1/2 = 3/6 aur 1/3 = 2/6.",
          "Ab jodo: 3/6 + 2/6."],
         "5/6"),
        ("3/4 - 1/4 = ?",
         ["Denominator same (4) hai.",
          "Numerators ghatao: (3-1)/4 = 2/4.",
          "Simplify: HCF 2 se -> 1/2."],
         "2/4 = 1/2"),
        ("2/3 x 3/4 = ?",
         ["Multiplication: upar x upar, neeche x neeche.",
          "(2x3)/(3x4) = 6/12.",
          "Simplify: HCF 6 se -> 1/2."],
         "6/12 = 1/2"),
        ("1/2 div 1/4 = ?",
         ["Division me doosre ka reciprocal lo: 1/4 -> 4/1.",
          "Ab multiply: 1/2 x 4/1 = 4/2.",
          "4/2 simplify -> 2."],
         "2"),
        ("7/2 -> mixed fraction?",
         ["Numerator ko denominator se divide: 7 div 2.",
          "Quotient = 3, Remainder = 1.",
          "Mixed = quotient + (remainder/denominator)."],
         "3 1/2"),
        ("2 1/3 -> improper fraction?",
         ["Formula: (whole x denominator) + numerator.",
          "(2 x 3) + 1 = 7.",
          "Denominator wahi (3) rakho."],
         "7/3"),
        ("1/4 -> decimal?",
         ["Numerator ko denominator se divide: 1 div 4."],
         "0.25"),
        ("Proper fraction definition?",
         ["Jis fraction me numerator chhota ho denominator se."],
         "Numerator < Denominator (jaise 3/4)"),
        ("Unit fraction kya hai?",
         ["Wo fraction jiska numerator 1 ho."],
         "Jaise 1/5, 1/7"),
        ("4/8, 1/2, 3/6 equivalent?",
         ["4/8 ko HCF 4 se simplify -> 1/2.",
          "3/6 ko HCF 3 se simplify -> 1/2.",
          "Teeno ki value 1/2 nikli."],
         "Haan, sab equivalent"),
        ("2/5 aur 3/5 me bada?",
         ["Denominator same (5) hai.",
          "Bada numerator wala bada: 3 > 2."],
         "3/5 bada hai"),
        ("1/2 aur 1/3 me bada?",
         ["Numerator same (1) hai.",
          "Chhota denominator wala bada: 2 < 3."],
         "1/2 bada hai"),
        ("6/9 simplest form?",
         ["HCF(6, 9) = 3 nikalo.",
          "Upar-neeche ko 3 se divide: (6/3)/(9/3)."],
         "2/3"),
        ("3/4 x 4 = ?",
         ["4 ko fraction maano: 4/1.",
          "3/4 x 4/1 = 12/4.",
          "Simplify: 12/4 = 3."],
         "3"),
        ("Mixed fraction kya hai?",
         ["Whole number + proper fraction milkar banta hai."],
         "Jaise 2 1/3"),
        ("0.5 -> fraction?",
         ["0.5 = 5/10 likho.",
          "HCF 5 se simplify: (5/5)/(10/5)."],
         "1/2"),
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
    out_file = "Fractions_Notes.pdf"
    pages = write_pdf(doc, out_file)
    print(f"Generated '{out_file}' with {pages} page(s).")
