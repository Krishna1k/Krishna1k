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
           "Hinglish me samjhaya gaya hai, methods diye gaye hain, fir 10 SOLVED "
           "EXAMPLES (sabse HARD se sabse EASY tak, har level cover karte hue), aur end "
           "me 22 practice questions ke STEP-BY-STEP solutions diye gaye hain.",
           color=GREY)
    d.space(4)
    d.legend_exam()
    d.space(4)

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
    d.exam_tag()
    d.label_body("Definition:", "Perfect square wo number hota hai jiska square root ek "
                 "pura (whole) number ho.")
    d.label_body("Examples:", "1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144 ...")
    d.label_body("Yaad rakho:", "")
    d.bullet("Perfect squares ke square root exact whole numbers hote hain.")
    d.bullet("2, 3, 5, 7 jaise numbers perfect square nahi hain; inke root non-ending "
             "decimals (irrational) hote hain, jaise sqrt(2) = 1.414...")
    d.bullet("Pehchaan: perfect square ke end me sirf 0, 1, 4, 5, 6 ya 9 aata hai.")
    d.bullet("Perfect square kabhi 2, 3, 7 ya 8 par khatam NAHI hota.")
    d.space(4)
    d.label_body("Squares Table (1 se 20) - yaad karo:", "")
    d.box_note([
        "1^2=1      2^2=4      3^2=9      4^2=16     5^2=25",
        "6^2=36     7^2=49     8^2=64     9^2=81     10^2=100",
        "11^2=121   12^2=144   13^2=169   14^2=196   15^2=225",
        "16^2=256   17^2=289   18^2=324   19^2=361   20^2=400",
    ])
    d.space(6)

    # ---- Methods -----------------------------------------------------
    d.h2("3. Square Root Nikalne ke Methods")
    d.exam_tag()
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
    d.bullet("(sqrt(a))^2 = a  aur  sqrt(a^2) = a")
    d.bullet("Negative number ka koi real square root nahi hota.")
    d.space(6)

    # ---- Pythagorean triplets ---------------------------------------
    d.h2("4B. Pythagorean Triplets")
    d.exam_tag()
    d.label_body("Kya hai:", "Teen numbers (a, b, c) jinme a^2 + b^2 = c^2 ho. Right-"
                 "angle triangle me kaam aate hain.")
    d.bullet("Famous triplets: (3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25).")
    d.bullet("Check: 3^2 + 4^2 = 9 + 16 = 25 = 5^2. Sahi!")
    d.bullet("Kisi triplet ko same number se multiply karne par naya triplet milta hai: "
             "(3, 4, 5) x 2 = (6, 8, 10).")
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

    # ---- Solved Examples (hardest -> easiest) -----------------------
    d.h2("6. Solved Examples - Hard se Easy (Sab Levels)")
    d.body("Neeche 10 examples step-by-step solve karke dikhaye gaye hain - sabse "
           "MUSHKIL se shuru karke sabse AASAN tak, taaki har type ka method clear ho "
           "jaye.", color=GREY)
    d.space(3)

    examples = [
        ("Example 1 (Hardest):  Long Division se sqrt(5476)",
         ["Right se do-do digit ke pair banao: 54 | 76.",
          "Pehla pair 54: sabse bada n jiska n^2 <= 54 -> 7 (49). Remainder = 5.",
          "Next pair niche lao: 5 76 -> 576.",
          "Quotient (7) ko double karo = 14. '14_' x _ <= 576 dhoondo.",
          "144 x 4 = 576 (exact!). Dusra digit = 4.",
          "Quotient = 74."],
         "sqrt(5476) = 74"),
        ("Example 2 (Hard):  Decimal ka root - sqrt(0.0144)",
         ["0.0144 ko fraction banao: 144 / 10000.",
          "sqrt(144) = 12,  sqrt(10000) = 100.",
          "= 12 / 100."],
         "sqrt(0.0144) = 0.12"),
        ("Example 3 (Hard):  Surd simplify - sqrt(72)",
         ["72 ko perfect square x baaki me todo: 72 = 36 x 2.",
          "sqrt(72) = sqrt(36) x sqrt(2) = 6 x sqrt(2)."],
         "6 sqrt(2)  (lagbhag 8.49)"),
        ("Example 4 (Medium-hard):  Prime factorisation - sqrt(1296)",
         ["1296 = 2 x 2 x 2 x 2 x 3 x 3 x 3 x 3 = 2^4 x 3^4.",
          "Pairs banao: (2x2)(2x2) aur (3x3)(3x3).",
          "Har pair me se ek lo: 2^2 x 3^2 = 4 x 9."],
         "sqrt(1296) = 36"),
        ("Example 5 (Medium-hard):  Property - sqrt(144 x 25)",
         ["Rule: sqrt(a x b) = sqrt(a) x sqrt(b).",
          "= sqrt(144) x sqrt(25) = 12 x 5."],
         "sqrt(144 x 25) = 60"),
        ("Example 6 (Medium):  Prime factorisation - sqrt(324)",
         ["324 = 4 x 81 = 2^2 x 3^4.",
          "Har pair me se ek lo: 2 x 3^2 = 2 x 9."],
         "sqrt(324) = 18"),
        ("Example 7 (Medium):  Estimation - sqrt(50) kin ke beech?",
         ["Nazdeeki perfect squares: 7^2 = 49 aur 8^2 = 64.",
          "50, 49 aur 64 ke beech hai -> answer 7 aur 8 ke beech."],
         "Lagbhag 7.07 (7 aur 8 ke beech)"),
        ("Example 8 (Easy-medium):  Fraction - sqrt(49/64)",
         ["Rule: sqrt(a/b) = sqrt(a) / sqrt(b).",
          "= sqrt(49) / sqrt(64) = 7 / 8."],
         "sqrt(49/64) = 7/8"),
        ("Example 9 (Easy):  Perfect square - sqrt(169)",
         ["Koi number dhoondo jiska square 169 ho.",
          "13 x 13 = 169."],
         "sqrt(169) = 13"),
        ("Example 10 (Easiest):  sqrt(0) aur sqrt(1)",
         ["0 x 0 = 0  ->  sqrt(0) = 0.",
          "1 x 1 = 1  ->  sqrt(1) = 1."],
         "sqrt(0) = 0,  sqrt(1) = 1"),
    ]

    for q, steps, ans in examples:
        d.label_body(q, "")
        for s in steps:
            d.bullet(f"Step: {s}")
        d.label_body("   Answer:", ans)
        d.space(5)

    # ---- Practice Questions -----------------------------------------
    d.h2("7. Practice Questions")
    d.body("Pehle khud solve karne ki koshish karo. Neeche har question ka step-by-step "
           "solution diya gaya hai.", color=GREY)
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

    # ---- Step-by-Step Solutions -------------------------------------
    d.h2("8. Step-by-Step Solutions")
    solutions = [
        ("sqrt(49)", ["Koi number dhoondo jiska square 49 ho.", "7 x 7 = 49."], "7"),
        ("sqrt(64)", ["8 x 8 = 64."], "8"),
        ("sqrt(81)", ["9 x 9 = 81."], "9"),
        ("sqrt(100)", ["10 x 10 = 100."], "10"),
        ("sqrt(121)", ["11 x 11 = 121."], "11"),
        ("sqrt(144)", ["12 x 12 = 144."], "12"),
        ("sqrt(169)", ["13 x 13 = 169."], "13"),
        ("sqrt(196)", ["14 x 14 = 196."], "14"),
        ("sqrt(225)", ["15 x 15 = 225."], "15"),
        ("sqrt(256)", ["16 x 16 = 256."], "16"),
        ("Kya 150 perfect square hai?",
         ["12^2 = 144 aur 13^2 = 169.", "150 in dono ke beech hai, koi whole root nahi.",
          "sqrt(150) ~ 12.25."],
         "Nahi"),
        ("sqrt(180) kin do whole numbers ke beech?",
         ["13^2 = 169 aur 14^2 = 196.", "180 in dono ke beech aata hai."],
         "13 aur 14 ke beech"),
        ("sqrt(36) + sqrt(64)",
         ["sqrt(36) = 6,  sqrt(64) = 8.", "6 + 8."],
         "14"),
        ("Square park ka area 196 sq m, side?",
         ["Square ka area = side x side, to side = sqrt(area).", "side = sqrt(196)."],
         "14 metre"),
        ("100 se 200 ke beech perfect squares?",
         ["10^2=100, 11^2=121, 12^2=144, 13^2=169, 14^2=196."],
         "100, 121, 144, 169, 196"),
        ("sqrt(2) rational ya irrational?",
         ["sqrt(2) = 1.41421... non-terminating aur non-repeating hai."],
         "Irrational"),
        ("sqrt(400)", ["20 x 20 = 400."], "20"),
        ("sqrt(1) aur sqrt(0)",
         ["1 x 1 = 1  aur  0 x 0 = 0."],
         "sqrt(1) = 1,  sqrt(0) = 0"),
        ("Negative number ka real square root?",
         ["Kisi bhi real number ka square negative nahi hota.",
          "Isliye negative ka real square root possible nahi."],
         "Nahi hota"),
        ("sqrt(9 x 16)  (property)",
         ["Rule: sqrt(a x b) = sqrt(a) x sqrt(b).", "= sqrt(9) x sqrt(16) = 3 x 4."],
         "12"),
        ("sqrt(625)", ["25 x 25 = 625."], "25"),
        ("12 x 12 = 144, to sqrt(144)?",
         ["sqrt square ka ulta hai; 12 ka square 144 hai."],
         "12"),
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
    out_file = "Square_Roots_Notes.pdf"
    pages = write_pdf(doc, out_file)
    print(f"Generated '{out_file}' with {pages} page(s).")
