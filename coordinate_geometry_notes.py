#!/usr/bin/env python3
"""
Chapter 7: Coordinate Geometry - Hinglish notes PDF.
Red-page core basics (PART A) + main chapter content (PART B), green EXAM tags,
solved examples + step-by-step solutions.
numbers_notes.py ka pure-Python PDF engine reuse karta hai.

Output: Coordinate_Geometry_Notes.pdf
"""

from numbers_notes import (
    PDFBuilder, write_pdf,
    LEFT, RIGHT, PAGE_W, NAVY, GREY,
)


def build_document():
    d = PDFBuilder()

    d.title("Coordinate Geometry")
    d.subtitle("Chapter 7 - Hinglish Notes, Formulas, Examples + Solutions")
    d.hline(LEFT, PAGE_W - RIGHT, d.y + 4, NAVY, 1.2)
    d.space(10)
    d.body("Ye Chapter 7 (Coordinate Geometry) ka complete guide hai. Pehle red-page ke "
           "core basics (axis, coordinates, quadrants, square/sqrt, average, ratio), fir "
           "chapter ka main content - distance formula, section formula aur midpoint. "
           "End me solved examples aur 20 practice questions ke step-by-step solutions "
           "hain.", color=GREY)
    d.space(4)
    d.legend_exam()
    d.space(4)

    # ================= PART A : CORE BASICS =========================
    d.h2("PART A - Core Basics (Miss Mat Karna)")
    d.space(2)

    d.h2("1. X-axis, Y-axis, Origin")
    d.exam_tag()
    d.bullet("X-axis = leti (horizontal) line; Y-axis = khadi (vertical) line.")
    d.bullet("Dono milte hain ORIGIN (0, 0) pe.")
    d.space(6)

    d.h2("2. Coordinates (x, y)")
    d.exam_tag()
    d.bullet("Point ko (x, y) likhte hain.")
    d.bullet("x = abscissa (X par doori), y = ordinate (Y par doori).")
    d.bullet("Order important hai: (3, 5) != (5, 3).")
    d.space(6)

    d.h2("3. Signs / Quadrants")
    d.exam_tag()
    d.bullet("Q1 (+,+),  Q2 (-,+),  Q3 (-,-),  Q4 (+,-).")
    d.bullet("X-axis pe y = 0; Y-axis pe x = 0.")
    d.space(6)

    d.h2("4. Square aur Square Root")
    d.bullet("a^2 = a x a.  sqrt(25) = 5.")
    d.bullet("Distance formula me squares aur sqrt use hote hain.")
    d.space(6)

    d.h2("5. Negative ka Square")
    d.bullet("(-4)^2 = 16  (negative ka square POSITIVE hota hai).")
    d.bullet("Isliye distance hamesha positive aati hai.")
    d.space(6)

    d.h2("6. Average (Mean)")
    d.bullet("Do numbers ka average = (a + b)/2.")
    d.bullet("Midpoint formula me bas average lena hota hai.")
    d.space(6)

    d.h2("7. Ratio (m1 : m2)")
    d.bullet("Ratio = do hisson ki tulna.")
    d.bullet("Section formula me point segment ko m1 : m2 me baant-ta hai.")
    d.space(6)

    # ================= PART B : MAIN CONTENT ========================
    d.h2("PART B - Chapter 7 ka Main Content")
    d.space(2)

    d.h2("8. Distance Formula")
    d.exam_tag()
    d.label_body("Do points ke beech ki doori:", "")
    d.box_note([
        "Distance = sqrt[ (x2 - x1)^2 + (y2 - y1)^2 ]",
        "",
        "Points: A(x1, y1) aur B(x2, y2).",
    ])
    d.bullet("Example: (0,0) aur (3,4) ki doori = sqrt(9+16) = sqrt(25) = 5.")
    d.space(6)

    d.h2("9. Distance from Origin")
    d.exam_tag()
    d.label_body("Origin (0,0) se point (x, y) ki doori:", "")
    d.bullet("Distance = sqrt(x^2 + y^2).")
    d.bullet("Example: (6, 8) ki origin se doori = sqrt(36+64) = sqrt(100) = 10.")
    d.space(6)

    d.h2("10. Section Formula")
    d.exam_tag()
    d.label_body("Point P jo A(x1,y1) aur B(x2,y2) ko m1:m2 me baant-ta hai:", "")
    d.box_note([
        "P = ( (m1.x2 + m2.x1)/(m1+m2) ,  (m1.y2 + m2.y1)/(m1+m2) )",
    ])
    d.bullet("Yaad: ratio m1:m2 me 'door wale' point ka coordinate pehle aata hai.")
    d.space(6)

    d.h2("11. Midpoint Formula")
    d.exam_tag()
    d.label_body("Beech (mid) ka point (ratio 1:1):", "")
    d.box_note([
        "Midpoint = ( (x1 + x2)/2 ,  (y1 + y2)/2 )",
    ])
    d.bullet("Bas dono x ka average aur dono y ka average le lo.")
    d.bullet("Example: (2,3) aur (4,7) ka midpoint = (3, 5).")
    d.space(6)

    d.h2("12. Collinear Points")
    d.bullet("Agar teen points ek hi seedhi line par hon to wo COLLINEAR kehlate hain.")
    d.bullet("Check: AB + BC = AC ho (distances jod kar) to points collinear hain.")
    d.space(6)

    d.h2("13. Word Problems / Uses")
    d.bullet("Diagonal ya side ki length nikalna -> distance formula.")
    d.bullet("Beech ka point -> midpoint; ratio me baant -> section formula.")
    d.bullet("Type of figure (square/rhombus) check karna -> sides/diagonals compare.")
    d.space(6)

    d.h2("Quick Revision")
    d.box_note([
        "Distance = sqrt[(x2-x1)^2 + (y2-y1)^2].",
        "From origin = sqrt(x^2 + y^2).",
        "Section: ((m1x2+m2x1)/(m1+m2), (m1y2+m2y1)/(m1+m2)).",
        "Midpoint = ((x1+x2)/2, (y1+y2)/2).",
        "Quadrants: Q1(+,+) Q2(-,+) Q3(-,-) Q4(+,-).",
    ])
    d.space(6)

    # ---- Solved Examples --------------------------------------------
    d.h2("Solved Examples - Samjho Kaise Solve Karte Hain")
    d.body("Neeche 10 examples step-by-step solve karke dikhaye gaye hain.", color=GREY)
    d.space(3)

    examples = [
        ("Example 1 (Distance):  A(1,2) aur B(4,6) ki doori?",
         ["Distance = sqrt[(x2-x1)^2 + (y2-y1)^2].",
          "= sqrt[(4-1)^2 + (6-2)^2] = sqrt[9 + 16].",
          "= sqrt(25)."],
         "Distance = 5"),
        ("Example 2 (From origin):  Point (6, 8) ki origin se doori?",
         ["Distance = sqrt(x^2 + y^2) = sqrt(36 + 64).",
          "= sqrt(100)."],
         "10"),
        ("Example 3 (Midpoint):  (2,3) aur (4,7) ka midpoint?",
         ["Midpoint = ((x1+x2)/2, (y1+y2)/2).",
          "= ((2+4)/2, (3+7)/2) = (6/2, 10/2)."],
         "(3, 5)"),
        ("Example 4 (Midpoint):  (-2, 4) aur (6, -2) ka midpoint?",
         ["x = (-2+6)/2 = 2;  y = (4 + (-2))/2 = 1."],
         "(2, 1)"),
        ("Example 5 (Section):  A(1,2), B(4,5) ko 1:2 me baant ne wala point?",
         ["m1=1, m2=2.  x = (1x4 + 2x1)/(1+2) = (4+2)/3 = 2.",
          "y = (1x5 + 2x2)/3 = (5+4)/3 = 3."],
         "(2, 3)"),
        ("Example 6 (Quadrant):  Point (-3, 5) kis quadrant me hai?",
         ["x negative, y positive -> (-,+)."],
         "Quadrant 2 (Q2)"),
        ("Example 7 (Distance check):  Kya (0,0),(3,4) ki doori 5 hai?",
         ["sqrt(3^2 + 4^2) = sqrt(9+16) = sqrt(25)."],
         "Haan, 5"),
        ("Example 8 (Equal distance):  (0,0) se (5,0) aur (0,5) - doori barabar?",
         ["(5,0): sqrt(25) = 5.  (0,5): sqrt(25) = 5."],
         "Haan, dono 5"),
        ("Example 9 (Midpoint reverse):  Midpoint (3,4), ek end (1,2). Doosra end?",
         ["(1+x)/2 = 3 -> x = 5;  (2+y)/2 = 4 -> y = 6."],
         "(5, 6)"),
        ("Example 10 (Collinear idea):  (1,1),(2,2),(3,3) ek line par?",
         ["Teeno me y = x pattern hai, ek hi seedhi line."],
         "Haan, collinear"),
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
        "Origin ke coordinates kya hote hain?",
        "Point (x, y) me x aur y ko kya kehte hain?",
        "Distance formula kya hai?",
        "Midpoint formula kya hai?",
        "(0,0) aur (3,4) ki doori kya hai?",
        "(6,8) ki origin se doori kya hai?",
        "(2,4) aur (6,8) ka midpoint?",
        "Point (-5, -2) kis quadrant me hai?",
        "X-axis par kisi point ki y-coordinate kya hoti hai?",
        "Y-axis par kisi point ki x-coordinate kya hoti hai?",
        "(1,1) aur (5,5) ki doori?",
        "Section formula kis kaam aata hai?",
        "(-2,3) aur (4,3) ka midpoint?",
        "Quadrant 3 me signs kaise hote hain?",
        "(0,0) aur (0,7) ki doori?",
        "Midpoint (4,5), ek end (2,3) -> doosra end?",
        "(3,0) aur (0,4) ki doori?",
        "A(2,3), B(8,3) ko 1:1 me baant ne wala point?",
        "(7, -2) kis quadrant me hai?",
        "Collinear points ka matlab kya hai?",
    ]
    for i, q in enumerate(questions, start=1):
        d.label_body(f"Q{i}.", q)
        d.space(2)

    # ---- Step-by-Step Solutions -------------------------------------
    d.h2("Step-by-Step Solutions")
    solutions = [
        ("Origin ke coordinates?",
         ["Jahan dono axis milte hain."], "(0, 0)"),
        ("x aur y ko kya kehte?",
         ["X par doori = abscissa, Y par = ordinate."], "abscissa aur ordinate"),
        ("Distance formula?",
         ["Do points ke beech."], "sqrt[(x2-x1)^2 + (y2-y1)^2]"),
        ("Midpoint formula?",
         ["Dono coordinates ka average."], "((x1+x2)/2, (y1+y2)/2)"),
        ("(0,0),(3,4) doori?",
         ["sqrt(9+16) = sqrt(25)."], "5"),
        ("(6,8) origin se doori?",
         ["sqrt(36+64) = sqrt(100)."], "10"),
        ("(2,4),(6,8) midpoint?",
         ["((2+6)/2, (4+8)/2) = (4, 6)."], "(4, 6)"),
        ("(-5,-2) quadrant?",
         ["x-, y- -> (-,-)."], "Q3"),
        ("X-axis par y?",
         ["X-axis par height 0 hoti hai."], "0"),
        ("Y-axis par x?",
         ["Y-axis par doori 0 hoti hai."], "0"),
        ("(1,1),(5,5) doori?",
         ["sqrt(16+16) = sqrt(32) = 4 sqrt(2)."], "4 sqrt(2) (~5.66)"),
        ("Section formula kis kaam?",
         ["Segment ko ratio me baant ne ke liye."], "Point dividing in m1:m2"),
        ("(-2,3),(4,3) midpoint?",
         ["((-2+4)/2, (3+3)/2) = (1, 3)."], "(1, 3)"),
        ("Q3 me signs?",
         ["Teesra quadrant."], "(-, -)"),
        ("(0,0),(0,7) doori?",
         ["sqrt(0 + 49) = 7."], "7"),
        ("Midpoint(4,5), end(2,3) -> doosra?",
         ["(2+x)/2=4 -> x=6; (3+y)/2=5 -> y=7."], "(6, 7)"),
        ("(3,0),(0,4) doori?",
         ["sqrt(9+16) = sqrt(25)."], "5"),
        ("A(2,3),B(8,3) ko 1:1?",
         ["1:1 matlab midpoint = ((2+8)/2, 3)."], "(5, 3)"),
        ("(7,-2) quadrant?",
         ["x+, y- -> (+,-)."], "Q4"),
        ("Collinear points?",
         ["Ek hi seedhi line par hone wale points."], "Same line par points"),
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
    out_file = "Coordinate_Geometry_Notes.pdf"
    pages = write_pdf(doc, out_file)
    print(f"Generated '{out_file}' with {pages} page(s).")
