#!/usr/bin/env python3
"""
Chapter 11: Areas Related to Circles - Hinglish notes PDF.
Red-page core basics (PART A) + main chapter content (PART B), green EXAM tags,
solved examples + step-by-step solutions.
numbers_notes.py ka pure-Python PDF engine reuse karta hai.

Output: Areas_Related_to_Circles_Notes.pdf
"""

from numbers_notes import (
    PDFBuilder, write_pdf,
    LEFT, RIGHT, PAGE_W, NAVY, GREY,
)


def build_document():
    d = PDFBuilder()

    d.title("Areas Related to Circles")
    d.subtitle("Chapter 11 - Hinglish Notes, Area, Sector, Segment + Solutions")
    d.hline(LEFT, PAGE_W - RIGHT, d.y + 4, NAVY, 1.2)
    d.space(10)
    d.body("Ye Chapter 11 (Areas Related to Circles) ka complete guide hai. Pehle "
           "red-page ke core basics (circle parts, pi, area vs perimeter, sector, "
           "angle, fraction of circle), fir chapter ka main content - circumference, "
           "area, sector aur segment ke formulas. End me solved examples aur 20 "
           "practice questions ke step-by-step solutions hain.", color=GREY)
    d.space(4)
    d.legend_exam()
    d.space(4)

    # ================= PART A : CORE BASICS =========================
    d.h2("PART A - Core Basics (Miss Mat Karna)")
    d.space(2)

    d.h2("1. Circle - Radius, Diameter")
    d.exam_tag()
    d.bullet("Radius (r) = centre se circle tak ki doori.")
    d.bullet("Diameter = 2r (circle ke aar-paar, centre se hokar).")
    d.space(6)

    d.h2("2. pi (PI) Kya Hai?")
    d.exam_tag()
    d.bullet("pi = circumference / diameter = 3.14 (ya 22/7).")
    d.bullet("Radius 7 ka multiple ho to 22/7 use karo, warna 3.14.")
    d.space(6)

    d.h2("3. Area vs Perimeter")
    d.exam_tag()
    d.bullet("Area = andar ki jagah (unit: cm^2).")
    d.bullet("Perimeter / circumference = boundary ki length (unit: cm).")
    d.space(6)

    d.h2("4. Circle ke 2 Formula")
    d.exam_tag()
    d.bullet("Circumference = 2 pi r.")
    d.bullet("Area = pi r^2.")
    d.space(6)

    d.h2("5. Angle (degree)")
    d.exam_tag()
    d.bullet("Pura circle = 360 degree.")
    d.bullet("Sector ek hissa hai jiska apna angle theta hota hai.")
    d.space(6)

    d.h2("6. Fraction of Circle")
    d.exam_tag()
    d.bullet("Sector = circle ka theta/360 hissa.")
    d.bullet("Isi se sector ka area aur arc length nikalte hain.")
    d.space(6)

    d.h2("7. Square / Units")
    d.bullet("r^2 = r x r.")
    d.bullet("Area ka unit hamesha square hota hai (cm^2).")
    d.space(6)

    # ================= PART B : MAIN CONTENT ========================
    d.h2("PART B - Chapter 11 ka Main Content")
    d.space(2)

    d.h2("8. Circumference aur Area of Circle")
    d.exam_tag()
    d.box_note([
        "Circumference = 2 pi r",
        "Area = pi r^2",
        "",
        "pi = 22/7 (ya 3.14).",
    ])
    d.bullet("Example: r=7 -> Circumference = 2 x 22/7 x 7 = 44 cm.")
    d.space(6)

    d.h2("9. Length of an Arc")
    d.exam_tag()
    d.box_note([
        "Arc length = (theta / 360) x 2 pi r",
        "",
        "theta = sector ka angle (degree me).",
    ])
    d.bullet("Yani poori circumference ka theta/360 hissa.")
    d.space(6)

    d.h2("10. Area of a Sector")
    d.exam_tag()
    d.box_note([
        "Area of sector = (theta / 360) x pi r^2",
        "",
        "= poore circle ke area ka theta/360 hissa.",
    ])
    d.bullet("Minor sector = chhota hissa; Major sector = bada hissa.")
    d.space(6)

    d.h2("11. Area of a Segment")
    d.exam_tag()
    d.box_note([
        "Area of segment = Area of sector - Area of triangle",
        "",
        "(triangle = do radii aur chord se banta hai).",
    ])
    d.bullet("Minor segment chord ke ek taraf, major segment doosri taraf hota hai.")
    d.space(6)

    d.h2("12. Combination / Shaded Area")
    d.bullet("Shaded area = badi shape ka area - chhoti shape ka area.")
    d.bullet("Jaise square me circle, ya do circles ka antar (ring).")
    d.bullet("Ring (annulus) area = pi(R^2 - r^2).")
    d.space(6)

    d.h2("Quick Revision")
    d.box_note([
        "Circumference = 2 pi r;  Area = pi r^2.",
        "Arc length = (theta/360) x 2 pi r.",
        "Sector area = (theta/360) x pi r^2.",
        "Segment = sector - triangle.",
        "pi = 22/7 (r me 7 ho) warna 3.14.",
    ])
    d.space(6)

    # ---- Solved Examples --------------------------------------------
    d.h2("Solved Examples - Samjho Kaise Solve Karte Hain")
    d.body("Neeche 10 examples step-by-step solve karke dikhaye gaye hain.", color=GREY)
    d.space(3)

    examples = [
        ("Example 1:  r = 7 cm. Area of circle? (pi = 22/7)",
         ["Area = pi r^2 = (22/7) x 7 x 7.",
          "= 22 x 7."],
         "Area = 154 cm^2"),
        ("Example 2:  r = 7 cm. Circumference? (pi = 22/7)",
         ["Circumference = 2 pi r = 2 x (22/7) x 7.",
          "= 2 x 22."],
         "44 cm"),
        ("Example 3:  r = 14 cm. Area? (pi = 22/7)",
         ["Area = (22/7) x 14 x 14 = 22 x 2 x 14.",
          "= 22 x 28."],
         "616 cm^2"),
        ("Example 4:  Sector theta=90, r=14. Area? (pi=22/7)",
         ["Sector area = (90/360) x pi r^2 = (1/4) x (22/7) x 196.",
          "= (1/4) x 616."],
         "154 cm^2"),
        ("Example 5:  Arc length, theta=60, r=21. (pi=22/7)",
         ["Arc = (60/360) x 2 pi r = (1/6) x 2 x (22/7) x 21.",
          "= (1/6) x 132."],
         "22 cm"),
        ("Example 6:  Diameter = 28 cm. Radius aur area? (pi=22/7)",
         ["r = 28/2 = 14.  Area = (22/7) x 14 x 14.",
          "= 616."],
         "r=14, Area=616 cm^2"),
        ("Example 7:  Sector theta=180 (half), r=7. Area? (pi=22/7)",
         ["(180/360) x pi r^2 = (1/2) x (22/7) x 49.",
          "= (1/2) x 154."],
         "77 cm^2"),
        ("Example 8:  Ring: R=7, r=conf... r=  inner 0? Outer 7 area.",
         ["Area of circle = pi R^2 = (22/7) x 49.",
          "= 154."],
         "154 cm^2"),
        ("Example 9:  theta=90, r=10. Arc length? (pi=3.14)",
         ["Arc = (90/360) x 2 x 3.14 x 10 = (1/4) x 62.8.",
          "= 15.7."],
         "15.7 cm"),
        ("Example 10:  Quarter circle area, r=4. (pi=3.14)",
         ["Quarter = (1/4) pi r^2 = (1/4) x 3.14 x 16.",
          "= (1/4) x 50.24."],
         "12.56 cm^2"),
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
        "Circle ke area ka formula kya hai?",
        "Circle ke circumference ka formula kya hai?",
        "pi ka value kya hota hai (2 forms)?",
        "Pura circle kitne degree ka hota hai?",
        "Sector ka area formula kya hai?",
        "Arc length ka formula kya hai?",
        "Segment ka area kaise nikalte hain?",
        "r=7, pi=22/7 -> area?",
        "r=7, pi=22/7 -> circumference?",
        "Diameter=14 ho to radius?",
        "Sector theta=90, r=14 -> area? (pi=22/7)",
        "Area ka unit kya hota hai?",
        "Perimeter/circumference ka unit kya hota hai?",
        "theta=180 ka sector circle ka kitna hissa hai?",
        "Ring (annulus) ka area formula?",
        "r=14, pi=22/7 -> area?",
        "Half circle (r=7) ka area? (pi=22/7)",
        "Sector circle ka kitna fraction hota hai?",
        "Quarter circle ka angle kitna hota hai?",
        "Shaded area kaise nikalte hain (general rule)?",
    ]
    for i, q in enumerate(questions, start=1):
        d.label_body(f"Q{i}.", q)
        d.space(2)

    # ---- Step-by-Step Solutions -------------------------------------
    d.h2("Step-by-Step Solutions")
    solutions = [
        ("Circle area formula?",
         ["Standard formula."], "pi r^2"),
        ("Circumference formula?",
         ["Standard formula."], "2 pi r"),
        ("pi ka value?",
         ["Do common forms."], "22/7 ya 3.14"),
        ("Pura circle kitne degree?",
         ["Full angle."], "360 degree"),
        ("Sector area formula?",
         ["theta/360 hissa of pi r^2."], "(theta/360) x pi r^2"),
        ("Arc length formula?",
         ["theta/360 hissa of 2 pi r."], "(theta/360) x 2 pi r"),
        ("Segment area?",
         ["Sector me se triangle ghatao."], "Sector area - triangle area"),
        ("r=7, pi=22/7 -> area?",
         ["(22/7) x 49 = 22 x 7."], "154 cm^2"),
        ("r=7 -> circumference?",
         ["2 x (22/7) x 7 = 44."], "44 cm"),
        ("Diameter=14 -> radius?",
         ["r = d/2."], "7"),
        ("Sector theta=90, r=14 -> area?",
         ["(1/4) x (22/7) x 196 = (1/4) x 616."], "154 cm^2"),
        ("Area ka unit?",
         ["2-D jagah."], "cm^2 (square)"),
        ("Circumference ka unit?",
         ["Length."], "cm"),
        ("theta=180 sector hissa?",
         ["180/360 = 1/2."], "Aadha (half)"),
        ("Ring area formula?",
         ["Bahar - andar."], "pi(R^2 - r^2)"),
        ("r=14, pi=22/7 -> area?",
         ["(22/7) x 196 = 22 x 28."], "616 cm^2"),
        ("Half circle r=7 area?",
         ["(1/2) x (22/7) x 49 = (1/2) x 154."], "77 cm^2"),
        ("Sector fraction?",
         ["Angle ratio."], "theta/360"),
        ("Quarter circle angle?",
         ["360/4."], "90 degree"),
        ("Shaded area rule?",
         ["Bade me se chhota ghatao."], "Badi shape - chhoti shape"),
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
    out_file = "Areas_Related_to_Circles_Notes.pdf"
    pages = write_pdf(doc, out_file)
    print(f"Generated '{out_file}' with {pages} page(s).")
