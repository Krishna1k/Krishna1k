#!/usr/bin/env python3
"""
Chapter 10: Circles - Hinglish notes PDF.
Red-page core basics (PART A) + main chapter content (PART B), green EXAM tags,
solved examples + step-by-step solutions.
numbers_notes.py ka pure-Python PDF engine reuse karta hai.

Output: Circles_Notes.pdf
"""

from numbers_notes import (
    PDFBuilder, write_pdf,
    LEFT, RIGHT, PAGE_W, NAVY, GREY,
)


def build_document():
    d = PDFBuilder()

    d.title("Circles")
    d.subtitle("Chapter 10 - Hinglish Notes, Tangents, Theorems + Solutions")
    d.hline(LEFT, PAGE_W - RIGHT, d.y + 4, NAVY, 1.2)
    d.space(10)
    d.body("Ye Chapter 10 (Circles) ka complete guide hai. Pehle red-page ke core basics "
           "(circle ke parts, perpendicular, Pythagoras, tangent vs secant), fir chapter "
           "ka main content - tangent ke theorems aur tangent ki length. End me solved "
           "examples aur 20 practice questions ke step-by-step solutions hain.",
           color=GREY)
    d.space(4)
    d.legend_exam()
    d.space(4)

    # ================= PART A : CORE BASICS =========================
    d.h2("PART A - Core Basics (Miss Mat Karna)")
    d.space(2)

    d.h2("1. Circle ke Parts")
    d.exam_tag()
    d.bullet("Centre = beech ka point.")
    d.bullet("Radius (r) = centre se circle tak ki doori.")
    d.bullet("Diameter = 2r (circle ke aar-paar, centre se hokar).")
    d.bullet("Chord = circle pe do points ko jodne wali line.")
    d.space(6)

    d.h2("2. Perpendicular (90 degree)")
    d.exam_tag()
    d.bullet("Do lines jo 90 degree par milti hain.")
    d.bullet("Symbol: corner par chhota square banate hain.")
    d.space(6)

    d.h2("3. Right Triangle + Pythagoras")
    d.exam_tag()
    d.bullet("90 degree wale triangle me: hyp^2 = side1^2 + side2^2.")
    d.bullet("Tangent ki length nikaalne me use hota hai.")
    d.space(6)

    d.h2("4. Square / Square Root")
    d.bullet("a^2 = a x a.  sqrt(100) = 10.")
    d.bullet("Tangent ki length nikaalne me sqrt use hota hai.")
    d.space(6)

    d.h2("5. Tangent vs Secant (Is Chapter ka Dil)")
    d.exam_tag()
    d.bullet("SECANT = line jo circle ko 2 points par CUT kare.")
    d.bullet("TANGENT = line jo circle ko sirf 1 point par TOUCH kare.")
    d.bullet("Touch point = 'point of contact'.")
    d.space(6)

    d.h2("6. Number of Tangents")
    d.exam_tag()
    d.bullet("Circle ke ANDAR ke point se: 0 tangent.")
    d.bullet("Circle PE point se: 1 tangent.")
    d.bullet("Circle ke BAHAR ke point se: 2 tangent.")
    d.space(6)

    d.h2("7. Angle Bisector")
    d.bullet("Ek line jo kisi angle ko 2 barabar hisson me baant-ti hai.")
    d.bullet("Centre aur external point ko jodne wali line tangents ke angle ko bisect karti hai.")
    d.space(6)

    # ================= PART B : MAIN CONTENT ========================
    d.h2("PART B - Chapter 10 ka Main Content")
    d.space(2)

    d.h2("8. Tangent to a Circle")
    d.exam_tag()
    d.label_body("Definition:", "Wo line jo circle ko sirf ek hi point par touch kare. "
                 "Us point ko point of contact kehte hain.")
    d.space(6)

    d.h2("9. Theorem 1 - Radius Tangent par Perpendicular")
    d.exam_tag()
    d.box_note([
        "Point of contact par radius, tangent ke PERPENDICULAR (90 degree) hoti hai.",
        "",
        "Yani: OP (radius) _|_ tangent at P.",
    ])
    d.bullet("Isliye OP, tangent ke saath right-angle triangle banata hai.")
    d.space(6)

    d.h2("10. Theorem 2 - Do Tangents Barabar")
    d.exam_tag()
    d.box_note([
        "Bahar ke ek point se khinchi gayi do tangents ki length BARABAR hoti hai.",
        "",
        "Yani: PA = PB  (P bahar ka point, A aur B contact points).",
    ])
    d.bullet("Aur wo tangents centre wali line ke saath barabar angle banati hain.")
    d.space(6)

    d.h2("11. Length of Tangent")
    d.exam_tag()
    d.box_note([
        "Tangent length = sqrt( OP^2 - r^2 )",
        "",
        "OP = centre se external point ki doori,  r = radius.",
    ])
    d.bullet("Ye Pythagoras se aata hai (kyunki radius _|_ tangent).")
    d.space(6)

    d.h2("12. Extra Important Facts")
    d.bullet("Do parallel tangents ke beech ki doori = diameter (2r).")
    d.bullet("Diameter ke dono sire par tangents aapas me parallel hoti hain.")
    d.bullet("Chord ke perpendicular bisector hamesha centre se hokar jaata hai.")
    d.space(6)

    d.h2("Quick Revision")
    d.box_note([
        "Tangent = 1 point touch; Secant = 2 points cut.",
        "Tangents: andar 0, pe 1, bahar 2.",
        "Radius _|_ tangent at point of contact (90 degree).",
        "Bahar ke point se 2 tangents barabar (PA = PB).",
        "Tangent length = sqrt(OP^2 - r^2).",
    ])
    d.space(6)

    # ---- Solved Examples --------------------------------------------
    d.h2("Solved Examples - Samjho Kaise Solve Karte Hain")
    d.body("Neeche 10 examples step-by-step solve karke dikhaye gaye hain.", color=GREY)
    d.space(3)

    examples = [
        ("Example 1:  r=6, OP=10. Tangent ki length?",
         ["Tangent = sqrt(OP^2 - r^2).",
          "= sqrt(10^2 - 6^2) = sqrt(100 - 36).",
          "= sqrt(64)."],
         "Tangent = 8"),
        ("Example 2:  r=5, tangent length=12. OP (centre se doori)?",
         ["OP^2 = r^2 + tangent^2 = 25 + 144.",
          "OP = sqrt(169)."],
         "OP = 13"),
        ("Example 3:  Bahar ke point se kitni tangents?",
         ["Rule: bahar ke point se 2 tangents."],
         "2"),
        ("Example 4:  PA = 7 (ek tangent). Doosri tangent PB?",
         ["Bahar ke point se do tangents barabar.",
          "PB = PA."],
         "PB = 7"),
        ("Example 5:  Radius aur tangent ke beech ka angle?",
         ["Point of contact par radius _|_ tangent."],
         "90 degree"),
        ("Example 6:  r=8, OP=17. Tangent length?",
         ["sqrt(17^2 - 8^2) = sqrt(289 - 64) = sqrt(225)."],
         "15"),
        ("Example 7:  Circle pe point se kitni tangent?",
         ["Circle PE point se exactly 1 tangent."],
         "1"),
        ("Example 8:  Andar ke point se kitni tangent?",
         ["Andar ke point se 0 tangent (line cut karegi)."],
         "0"),
        ("Example 9:  Diameter = 14. Do parallel tangents ke beech doori?",
         ["Parallel tangents ke beech doori = diameter."],
         "14"),
        ("Example 10:  r=9, OP=15. Tangent length?",
         ["sqrt(15^2 - 9^2) = sqrt(225 - 81) = sqrt(144)."],
         "12"),
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
        "Radius aur diameter me kya relation hai?",
        "Chord kya hota hai?",
        "Tangent kya hota hai?",
        "Secant kya hota hai?",
        "Bahar ke point se kitni tangents khinch sakte hain?",
        "Circle pe point se kitni tangents?",
        "Andar ke point se kitni tangents?",
        "Point of contact par radius aur tangent ke beech angle?",
        "Tangent ki length ka formula kya hai?",
        "r=3, OP=5 -> tangent length?",
        "r=8, tangent=6 -> OP?",
        "Bahar ke point se do tangents ke beech kya relation?",
        "Point of contact kise kehte hain?",
        "Do parallel tangents ke beech doori kiske barabar hoti hai?",
        "r=12, OP=13 -> tangent length?",
        "Tangent length formula kis theorem se aata hai?",
        "PA=9 ek tangent ho to doosri PB?",
        "Diameter 10 ho to radius?",
        "Secant circle ko kitne points par cut karti hai?",
        "Centre se chord par dali gayi perpendicular chord ko kya karti hai?",
    ]
    for i, q in enumerate(questions, start=1):
        d.label_body(f"Q{i}.", q)
        d.space(2)

    # ---- Step-by-Step Solutions -------------------------------------
    d.h2("Step-by-Step Solutions")
    solutions = [
        ("Radius aur diameter relation?",
         ["Diameter centre se hokar dono taraf radius."], "Diameter = 2r"),
        ("Chord kya hota hai?",
         ["Circle pe 2 points jodne wali line."], "Do points jodne wali line"),
        ("Tangent kya hota hai?",
         ["Circle ko 1 point par touch."], "1 point touch karne wali line"),
        ("Secant kya hota hai?",
         ["Circle ko 2 points par cut."], "2 points par cut karne wali line"),
        ("Bahar ke point se tangents?",
         ["Rule."], "2"),
        ("Circle pe point se tangents?",
         ["Rule."], "1"),
        ("Andar ke point se tangents?",
         ["Line cut karegi."], "0"),
        ("Radius-tangent angle?",
         ["Theorem 1."], "90 degree"),
        ("Tangent length formula?",
         ["Pythagoras se."], "sqrt(OP^2 - r^2)"),
        ("r=3, OP=5 -> tangent?",
         ["sqrt(25 - 9) = sqrt(16)."], "4"),
        ("r=8, tangent=6 -> OP?",
         ["OP = sqrt(64 + 36) = sqrt(100)."], "10"),
        ("Do tangents (bahar se) relation?",
         ["Theorem 2."], "Barabar (PA = PB)"),
        ("Point of contact?",
         ["Jahan tangent circle ko touch kare."], "Touch karne wala point"),
        ("Parallel tangents ke beech doori?",
         ["Diameter ke barabar."], "Diameter (2r)"),
        ("r=12, OP=13 -> tangent?",
         ["sqrt(169 - 144) = sqrt(25)."], "5"),
        ("Tangent formula kis theorem se?",
         ["Radius _|_ tangent -> Pythagoras."], "Pythagoras theorem"),
        ("PA=9 -> PB?",
         ["Do tangents barabar."], "9"),
        ("Diameter 10 -> radius?",
         ["r = diameter/2."], "5"),
        ("Secant kitne points cut?",
         ["Do points par."], "2"),
        ("Centre se chord par perpendicular?",
         ["Chord ko do barabar hisson me baant-ti hai."], "Chord ko bisect karti hai"),
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
    out_file = "Circles_Notes.pdf"
    pages = write_pdf(doc, out_file)
    print(f"Generated '{out_file}' with {pages} page(s).")
