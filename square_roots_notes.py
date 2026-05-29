#!/usr/bin/env python3
"""
Square Roots (Vargmool) study-notes ki PDF - Hinglish.
numbers_notes.py ka pure-Python PDF engine reuse karta hai
(koi external library nahi chahiye).
"""

from numbers_notes import (
    PDFBuilder, write_pdf,
    LEFT, RIGHT, PAGE_W, NAVY, GREY,
)


def build_document():
    d = PDFBuilder()

    # ---- Title -------------------------------------------------------
    d.title("Square Roots (Vargmool)")
    d.subtitle("Aasan Hinglish Notes, Methods, Examples aur Practice Questions")
    d.hline(LEFT, PAGE_W - RIGHT, d.y + 4, NAVY, 1.2)
    d.space(10)
    d.body("Square root, square (varg) ka ulta hota hai. Is guide me concept ko simple "
           "Hinglish me examples ke saath samjhaya gaya hai, square root nikalne ke "
           "methods diye gaye hain, aur end me 22 practice questions (answer key ke "
           "saath) hain.", color=GREY)
    d.space(6)

    # ---- What is a square root --------------------------------------
    d.h2("1. Square Root kya hota hai?")
    d.label_body("Definition:", "Kisi number ka square root wo value hai jise khud se "
                 "multiply karne par wahi number mil jaye. Ye squaring ka ulta (inverse) "
                 "hai.")
    d.label_body("Symbol:", "Radical sign  sqrt( )  use hota hai. Jaise sqrt(25).")
    d.label_body("Examples:", "")
    d.bullet("sqrt(25) = 5   kyunki 5 x 5 = 25")
    d.bullet("sqrt(81) = 9   kyunki 9 x 9 = 81")
    d.bullet("Square:  6 x 6 = 36   ->   Square root:  sqrt(36) = 6")
    d.space(6)

    # ---- Perfect squares --------------------------------------------
    d.h2("2. Perfect Squares")
    d.label_body("Definition:", "Perfect square wo number hota hai jiska square root ek "
                 "pura (whole) number ho.")
    d.label_body("Examples:", "1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144 ...")
    d.label_body("Yaad rakho:", "")
    d.bullet("Perfect squares ke square root exact whole numbers hote hain.")
    d.bullet("2, 3, 5, 7 jaise numbers perfect square nahi hain; inke root non-ending "
             "decimals (irrational) hote hain, jaise sqrt(2) = 1.414...")
    d.bullet("Perfect square kabhi 2, 3, 7 ya 8 par khatam nahi hota.")
    d.space(6)

    # ---- Methods -----------------------------------------------------
    d.h2("3. Square Root Nikalne ke Methods")
    d.label_body("(a) Prime Factorisation:", "Number ko prime factors me todo, pairs "
                 "banao, aur har pair me se ek factor lo.")
    d.bullet("Example: 144 = 2x2 x 2x2 x 3x3  ->  2 x 2 x 3 = 12, to sqrt(144) = 12")
    d.label_body("(b) Long Division:", "Bade numbers aur non-perfect squares ke liye "
                 "step-by-step answer (decimals me bhi) nikalne ke liye.")
    d.label_body("(c) Estimation:", "Do nazdeeki perfect squares dekh kar approximate "
                 "value guess karo.")
    d.bullet("Example: sqrt(150), sqrt(144)=12 aur sqrt(169)=13 ke beech hai, to lagbhag "
             "12.2")
    d.space(6)

    # ---- Properties --------------------------------------------------
    d.h2("4. Kaam ki Properties")
    d.bullet("sqrt(a x b) = sqrt(a) x sqrt(b)")
    d.bullet("sqrt(a / b) = sqrt(a) / sqrt(b)")
    d.bullet("sqrt(0) = 0  aur  sqrt(1) = 1")
    d.bullet("Negative number ka koi real square root nahi hota.")
    d.space(6)

    # ---- Perfect squares between 100 and 200 ------------------------
    d.h2("5. 100 se 200 ke Beech Perfect Squares")
    d.body("Is range me sirf paanch perfect squares hain:", color=GREY)
    d.space(2)
    d.box_note([
        "sqrt(100) = 10        (10 x 10 = 100)",
        "sqrt(121) = 11        (11 x 11 = 121)",
        "sqrt(144) = 12        (12 x 12 = 144)",
        "sqrt(169) = 13        (13 x 13 = 169)",
        "sqrt(196) = 14        (14 x 14 = 196)",
    ])
    d.space(6)

    # ---- Practice Questions -----------------------------------------
    d.h2("6. Practice Questions (Khud Try Karo!)")
    d.body("In 22 questions ko khud solve karne ki koshish karo. Answers neeche answer "
           "key me diye gaye hain.", color=GREY)
    d.space(3)

    questions = [
        "sqrt(49) = ?",
        "sqrt(64) = ?",
        "sqrt(81) = ?",
        "sqrt(100) = ?",
        "sqrt(121) = ?",
        "sqrt(144) = ?",
        "sqrt(169) = ?",
        "sqrt(196) = ?",
        "sqrt(225) = ?",
        "sqrt(256) = ?",
        "Kya 150 ek perfect square hai?",
        "sqrt(180) kin do whole numbers ke beech aata hai?",
        "sqrt(36) + sqrt(64) = ?",
        "Ek square park ka area 196 sq m hai. Uski side kitni hogi?",
        "100 se 200 ke beech kaunse perfect squares hain?",
        "sqrt(2) rational hai ya irrational?",
        "sqrt(400) = ?",
        "sqrt(1) = ? aur sqrt(0) = ?",
        "Kya negative number ka real square root hota hai?",
        "sqrt(9 x 16) = ?   (property use karo)",
        "sqrt(625) = ?",
        "12 x 12 = 144, to sqrt(144) = ?",
    ]
    for i, q in enumerate(questions, start=1):
        d.label_body(f"Q{i}.", q)
        d.space(2)

    # ---- Answer Key --------------------------------------------------
    d.h2("7. Answer Key")
    answers = [
        "7   (7 x 7 = 49)",
        "8   (8 x 8 = 64)",
        "9   (9 x 9 = 81)",
        "10  (10 x 10 = 100)",
        "11  (11 x 11 = 121)",
        "12  (12 x 12 = 144)",
        "13  (13 x 13 = 169)",
        "14  (14 x 14 = 196)",
        "15  (15 x 15 = 225)",
        "16  (16 x 16 = 256)",
        "Nahi   (sqrt(150) ~ 12.25, whole number nahi)",
        "13 aur 14 ke beech   (13^2 = 169, 14^2 = 196)",
        "14   (6 + 8 = 14)",
        "14 metre   (sqrt(196) = 14)",
        "100, 121, 144, 169 aur 196",
        "Irrational",
        "20  (20 x 20 = 400)",
        "sqrt(1) = 1 aur sqrt(0) = 0",
        "Nahi   (negative ka real square root nahi hota)",
        "12   (sqrt(9) x sqrt(16) = 3 x 4 = 12)",
        "25  (25 x 25 = 625)",
        "12",
    ]
    for i, a in enumerate(answers, start=1):
        d.bullet(f"Q{i}: {a}")

    return d


if __name__ == "__main__":
    doc = build_document()
    out_file = "Square_Roots_Notes.pdf"
    pages = write_pdf(doc, out_file)
    print(f"Generated '{out_file}' with {pages} page(s).")
