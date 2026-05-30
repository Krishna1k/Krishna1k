#!/usr/bin/env python3
"""
Chapter 6: Triangles - Hinglish notes PDF.
Red-page core basics + main chapter content, green EXAM tags,
solved examples + step-by-step solutions.
numbers_notes.py ka pure-Python PDF engine reuse karta hai.

Output: Triangles_Notes.pdf
"""

from numbers_notes import (
    PDFBuilder, write_pdf,
    LEFT, RIGHT, PAGE_W, NAVY, GREY,
)


def build_document():
    d = PDFBuilder()

    d.title("Triangles")
    d.subtitle("Chapter 6 - Hinglish Notes, Theorems, Examples + Solutions")
    d.hline(LEFT, PAGE_W - RIGHT, d.y + 4, NAVY, 1.2)
    d.space(10)
    d.body("Ye Chapter 6 (Triangles) ka complete guide hai. Pehle red-page ke core "
           "basics, fir chapter ka main content - similar triangles, criteria "
           "(AA/SSS/SAS), BPT/Thales aur Pythagoras. End me solved examples aur 20 "
           "practice questions ke step-by-step solutions hain.", color=GREY)
    d.space(4)
    d.legend_exam()
    d.space(4)

    # ================= PART A : CORE BASICS =========================
    d.h2("PART A - Core Basics (Miss Mat Karna)")
    d.space(2)

    d.h2("1. Triangle")
    d.bullet("3 side aur 3 angle hote hain.")
    d.bullet("Teeno angle ka sum hamesha = 180 degree.")
    d.space(6)

    d.h2("2. Ratio aur Proportion")
    d.exam_tag()
    d.label_body("Ratio:", "Do cheezon ki tulna, jaise 4/6 = 2/3.")
    d.label_body("Proportion:", "Do ratio barabar hon, jaise a/b = c/d.")
    d.space(6)

    d.h2("3. Congruent vs Similar (Bahut Important Fark)")
    d.exam_tag()
    d.label_body("Congruent:", "Bilkul same - shape AUR size dono same.")
    d.label_body("Similar:", "Same shape, par size alag (sides PROPORTIONAL).")
    d.bullet("Yaad: photo aur uski zoom copy = similar (shape same, size alag).")
    d.space(6)

    d.h2("4. Corresponding (Aamne-saamne wale)")
    d.exam_tag()
    d.bullet("Similar triangles me corresponding angles equal hote hain.")
    d.bullet("Aur corresponding sides proportional hote hain.")
    d.bullet("Order important hai: ABC ~ PQR  ->  A=P, B=Q, C=R.")
    d.space(6)

    d.h2("5. Parallel Lines (||)")
    d.bullet("Do lines jo kabhi nahi milti. Symbol: ||.")
    d.bullet("BPT (Thales) theorem inhi par based hai.")
    d.space(6)

    d.h2("6. Square / Square Root")
    d.bullet("a^2 = a x a. sqrt(25) = 5.")
    d.bullet("Pythagoras theorem me squares use hote hain.")
    d.space(6)

    d.h2("7. Proportion Solve Karna (Cross Multiply)")
    d.exam_tag()
    d.label_body("Rule:", "a/b = c/d  ->  a x d = b x c.")
    d.bullet("Isi cross-multiply se unknown side nikalti hai.")
    d.space(6)

    # ================= PART B : MAIN CONTENT ========================
    d.h2("PART B - Chapter 6 ka Main Content")
    d.space(2)

    d.h2("8. Similar Triangles")
    d.exam_tag()
    d.label_body("Definition:", "Do triangles similar hote hain jab unke corresponding "
                 "angles equal hon AUR corresponding sides ek hi ratio (proportional) me hon.")
    d.bullet("Symbol: ~ (jaise ABC ~ PQR).")
    d.bullet("Sides: AB/PQ = BC/QR = CA/RP.")
    d.space(6)

    d.h2("9. Similarity ke Criteria")
    d.exam_tag()
    d.label_body("AA (ya AAA):", "Do angles equal ho to triangles similar hain.")
    d.label_body("SSS:", "Teeno corresponding sides ka ratio same ho.")
    d.label_body("SAS:", "Do sides proportional + unke beech ka angle equal ho.")
    d.space(6)

    d.h2("10. Basic Proportionality Theorem (BPT / Thales)")
    d.exam_tag()
    d.label_body("Statement:", "Agar ek line triangle ki ek side ke parallel ho aur "
                 "baaki do sides ko cut kare, to wo unhe SAME ratio me divide karti hai.")
    d.box_note([
        "Agar DE || BC ho, to:",
        "AD / DB = AE / EC",
    ])
    d.bullet("Converse: agar AD/DB = AE/EC ho, to DE || BC.")
    d.space(6)

    d.h2("11. Pythagoras Theorem")
    d.exam_tag()
    d.label_body("Right-angle triangle me:", "")
    d.box_note([
        "(Hypotenuse)^2 = (Base)^2 + (Perpendicular)^2",
        "",
        "Hypotenuse = right angle ke saamne wali sabse lambi side.",
    ])
    d.bullet("Converse: agar c^2 = a^2 + b^2 ho, to triangle right-angled hai.")
    d.bullet("Famous triplets: (3,4,5), (5,12,13), (8,15,17).")
    d.space(6)

    d.h2("12. Areas of Similar Triangles")
    d.exam_tag()
    d.label_body("Rule:", "Do similar triangles ke areas ka ratio = unki corresponding "
                 "sides ke ratio ka SQUARE.")
    d.bullet("Area1 / Area2 = (side1 / side2)^2.")
    d.bullet("Example: sides ratio 2:3 -> areas ratio 4:9.")
    d.space(6)

    d.h2("Quick Revision")
    d.box_note([
        "Similar: angles equal + sides proportional (~).",
        "Criteria: AA, SSS, SAS.",
        "BPT: DE || BC -> AD/DB = AE/EC.",
        "Pythagoras: hyp^2 = base^2 + perp^2.",
        "Areas ratio = (sides ratio)^2.",
    ])
    d.space(6)

    # ---- Solved Examples --------------------------------------------
    d.h2("Solved Examples - Samjho Kaise Solve Karte Hain")
    d.body("Neeche 10 examples step-by-step solve karke dikhaye gaye hain.", color=GREY)
    d.space(3)

    examples = [
        ("Example 1 (Pythagoras):  base=3, perpendicular=4, hypotenuse?",
         ["hyp^2 = base^2 + perp^2 = 3^2 + 4^2.",
          "= 9 + 16 = 25.  hyp = sqrt(25)."],
         "Hypotenuse = 5"),
        ("Example 2 (Pythagoras):  hypotenuse=13, base=5, perpendicular?",
         ["13^2 = 5^2 + p^2 -> 169 = 25 + p^2.",
          "p^2 = 144 -> p = sqrt(144)."],
         "Perpendicular = 12"),
        ("Example 3 (Converse):  Kya 6, 8, 10 right triangle banata hai?",
         ["Sabse badi side = 10. Check: 6^2 + 8^2.",
          "= 36 + 64 = 100 = 10^2. Sahi!"],
         "Haan, right-angled"),
        ("Example 4 (Similarity):  2 triangles me 2-2 angles equal hain.",
         ["Do angles equal -> AA criterion lagta hai."],
         "Triangles similar hain (AA)"),
        ("Example 5 (BPT):  DE || BC, AD=2, DB=3, AE=4 -> EC?",
         ["BPT: AD/DB = AE/EC.",
          "2/3 = 4/EC -> EC = (4 x 3)/2."],
         "EC = 6"),
        ("Example 6 (Similar sides):  Similar triangles, sides 4 & 6 correspond. "
         "5 ke corresponding?",
         ["Ratio = 4/6 = 2/3.",
          "5 ko ratio se: 5 x (3/2) = 7.5."],
         "7.5"),
        ("Example 7 (Area ratio):  Similar triangles, sides ratio 2:3. Areas ratio?",
         ["Areas ratio = (sides ratio)^2.",
          "= 2^2 : 3^2 = 4 : 9."],
         "4 : 9"),
        ("Example 8 (Cross multiply):  a/4 = 6/8, a?",
         ["Cross multiply: a x 8 = 4 x 6.",
          "8a = 24 -> a = 24/8."],
         "a = 3"),
        ("Example 9 (Similar sides):  ABC ~ PQR, sides 3,4,5 aur 6,8,?",
         ["Ratio = 3/6 = 1/2 (har side).",
          "5 ke corresponding: 5 x 2 = 10."],
         "10"),
        ("Example 10 (Area):  Areas ratio 9:16 ho to sides ratio?",
         ["Sides ratio = sqrt(areas ratio).",
          "= sqrt(9) : sqrt(16) = 3 : 4."],
         "3 : 4"),
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
        "Triangle ke teeno angles ka sum kitna hota hai?",
        "Similar triangles ki 2 conditions kya hain?",
        "Congruent aur Similar me kya antar hai?",
        "Similarity ke 3 criteria ke naam batao.",
        "BPT (Thales) theorem kya kehta hai?",
        "Pythagoras theorem likho.",
        "Right triangle: base=6, perpendicular=8, hypotenuse?",
        "Kya 5, 12, 13 ek right triangle hai?",
        "Similar triangles ki sides ratio 3:4 -> areas ratio?",
        "AA criterion me kitne angles equal chahiye?",
        "DE || BC, AD/DB = AE/EC - ye kaunsa theorem hai?",
        "Hypotenuse=10, base=6, perpendicular?",
        "Do similar triangles ki corresponding sides 4 aur 8 -> ratio?",
        "Areas ratio 9:16 ho to sides ratio kya hai?",
        "Pythagoras theorem kis type ke triangle me lagta hai?",
        "SSS similarity criterion kya kehta hai?",
        "SAS similarity me kya-kya chahiye?",
        "Triangle me sabse lambi side kis angle ke saamne hoti hai?",
        "Similar triangles ka symbol kya hota hai?",
        "Kya 9, 12, 15 right triangle hai?",
    ]
    for i, q in enumerate(questions, start=1):
        d.label_body(f"Q{i}.", q)
        d.space(2)

    # ---- Step-by-Step Solutions -------------------------------------
    d.h2("Step-by-Step Solutions")
    solutions = [
        ("Teeno angles ka sum?",
         ["Angle sum property."], "180 degree"),
        ("Similar triangles ki 2 conditions?",
         ["Angles + sides dekho."], "Angles equal + sides proportional"),
        ("Congruent vs Similar?",
         ["Size ka farak dekho."], "Congruent = same size; Similar = size alag"),
        ("Similarity ke 3 criteria?",
         ["Standard criteria."], "AA, SSS, SAS"),
        ("BPT kya kehta hai?",
         ["Parallel line baaki sides ko same ratio me baantti hai."],
         "DE || BC -> AD/DB = AE/EC"),
        ("Pythagoras theorem?",
         ["Right triangle me."], "hyp^2 = base^2 + perp^2"),
        ("base=6, perp=8, hyp?",
         ["hyp^2 = 36 + 64 = 100.", "hyp = sqrt(100)."], "10"),
        ("Kya 5,12,13 right triangle?",
         ["5^2 + 12^2 = 25 + 144 = 169 = 13^2."], "Haan"),
        ("Sides ratio 3:4 -> areas ratio?",
         ["(sides ratio)^2 = 3^2 : 4^2."], "9 : 16"),
        ("AA me kitne angles equal?",
         ["Do angles kaafi hain."], "2 angles"),
        ("DE||BC, AD/DB=AE/EC kaunsa theorem?",
         ["Basic Proportionality."], "BPT (Thales)"),
        ("hyp=10, base=6, perp?",
         ["100 = 36 + p^2 -> p^2 = 64."], "8"),
        ("Sides 4 aur 8 -> ratio?",
         ["4/8 simplify."], "1 : 2"),
        ("Areas ratio 9:16 -> sides ratio?",
         ["sqrt(9):sqrt(16)."], "3 : 4"),
        ("Pythagoras kis triangle me?",
         ["Right angle wala."], "Right-angled triangle"),
        ("SSS similarity?",
         ["Teeno sides ka ratio same."], "Teeno corresponding sides proportional"),
        ("SAS similarity me?",
         ["2 sides + beech ka angle."], "2 sides proportional + included angle equal"),
        ("Sabse lambi side kis angle ke saamne?",
         ["Bade angle ke saamne badi side."], "Sabse bade angle ke saamne"),
        ("Similar triangles ka symbol?",
         ["Tilde symbol."], "~"),
        ("Kya 9,12,15 right triangle?",
         ["9^2 + 12^2 = 81 + 144 = 225 = 15^2."], "Haan"),
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
    out_file = "Triangles_Notes.pdf"
    pages = write_pdf(doc, out_file)
    print(f"Generated '{out_file}' with {pages} page(s).")
