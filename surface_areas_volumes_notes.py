#!/usr/bin/env python3
"""
Chapter 12: Surface Areas and Volumes - Hinglish notes PDF.
Red-page core basics (PART A) + main chapter content (PART B), green EXAM tags,
solved examples + step-by-step solutions.
"""

from numbers_notes import (
    PDFBuilder, write_pdf,
    LEFT, RIGHT, PAGE_W, NAVY, GREY,
)


def build_document():
    d = PDFBuilder()

    d.title("Surface Areas and Volumes")
    d.subtitle("Chapter 12 - Hinglish Notes, Formulas, Examples + Solutions")
    d.hline(LEFT, PAGE_W - RIGHT, d.y + 4, NAVY, 1.2)
    d.space(10)
    d.body("Ye Chapter 12 (Surface Areas and Volumes) ka complete guide hai. Pehle "
           "red-page ke core basics (SA vs Volume, CSA vs TSA, pi, slant height, shapes "
           "ke naam, units), fir chapter ka main content - har solid ke CSA/TSA/Volume "
           "formulas, combination of solids aur frustum. End me solved examples aur 20 "
           "practice questions ke step-by-step solutions hain.", color=GREY)
    d.space(4)
    d.legend_exam()
    d.space(4)

    d.h2("PART A - Core Basics (Miss Mat Karna)")
    d.space(2)

    d.h2("1. Surface Area vs Volume")
    d.exam_tag()
    d.bullet("Surface Area = bahar ki area (paint karne wali jagah), unit cm^2.")
    d.bullet("Volume = andar ki jagah (paani aa sake jitni), unit cm^3.")
    d.space(6)

    d.h2("2. CSA vs TSA")
    d.exam_tag()
    d.bullet("CSA = Curved / Side Surface (top-bottom chhod ke).")
    d.bullet("TSA = Total Surface Area (saari surfaces milake).")
    d.space(6)

    d.h2("3. pi (PI)")
    d.bullet("pi = 22/7 (radius 7 ka multiple ho to) ya 3.14.")
    d.space(6)

    d.h2("4. Square aur Cube")
    d.exam_tag()
    d.bullet("a^2 = a x a (area me).")
    d.bullet("a^3 = a x a x a (volume me).")
    d.space(6)

    d.h2("5. Square Root (slant height ke liye)")
    d.exam_tag()
    d.bullet("Cone me slant height: l = sqrt(r^2 + h^2).")
    d.bullet("Ye Pythagoras se aata hai.")
    d.space(6)

    d.h2("6. Basic Shapes ke Naam")
    d.bullet("Cube, Cuboid, Cylinder (belan), Cone (shanku),")
    d.bullet("Sphere (gol), Hemisphere (aadha sphere).")
    d.space(6)

    d.h2("7. Units")
    d.bullet("Area -> cm^2,  Volume -> cm^3.  Mat bhoolna!")
    d.space(6)

    d.h2("PART B - Chapter 12 ka Main Content")
    d.space(2)

    d.h2("8. Cuboid aur Cube")
    d.exam_tag()
    d.box_note([
        "CUBOID (l, b, h):",
        "  TSA = 2(lb + bh + hl),   Volume = l x b x h",
        "CUBE (side a):",
        "  TSA = 6 a^2,   Volume = a^3",
    ])
    d.space(6)

    d.h2("9. Cylinder")
    d.exam_tag()
    d.box_note([
        "CSA = 2 pi r h",
        "TSA = 2 pi r (r + h)",
        "Volume = pi r^2 h",
    ])
    d.space(6)

    d.h2("10. Cone")
    d.exam_tag()
    d.box_note([
        "Slant height l = sqrt(r^2 + h^2)",
        "CSA = pi r l",
        "TSA = pi r (l + r)",
        "Volume = (1/3) pi r^2 h",
    ])
    d.space(6)

    d.h2("11. Sphere aur Hemisphere")
    d.exam_tag()
    d.box_note([
        "SPHERE:  Surface = 4 pi r^2,   Volume = (4/3) pi r^3",
        "HEMISPHERE:  CSA = 2 pi r^2,   TSA = 3 pi r^2",
        "             Volume = (2/3) pi r^3",
    ])
    d.space(6)

    d.h2("12. Combination of Solids")
    d.exam_tag()
    d.bullet("Combined shape ka surface = bahar dikhne wali surfaces ka jod.")
    d.bullet("Combined volume = alag-alag solids ke volumes ka jod.")
    d.bullet("Example: ice-cream cone = cone + hemisphere.")
    d.space(6)

    d.h2("13. Frustum of a Cone")
    d.exam_tag()
    d.label_body("Cone ka upar ka hissa kaat do to frustum banta hai (R, r, h):", "")
    d.box_note([
        "Volume = (1/3) pi h (R^2 + r^2 + R r)",
        "CSA = pi (R + r) l,   l = sqrt(h^2 + (R-r)^2)",
        "TSA = CSA + pi R^2 + pi r^2",
    ])
    d.space(6)

    d.h2("Quick Revision")
    d.box_note([
        "Cube: TSA=6a^2, V=a^3.  Cuboid: V=lbh.",
        "Cylinder: CSA=2 pi r h, V=pi r^2 h.",
        "Cone: CSA=pi r l, V=(1/3)pi r^2 h, l=sqrt(r^2+h^2).",
        "Sphere: 4 pi r^2, V=(4/3)pi r^3.  Hemisphere V=(2/3)pi r^3.",
        "Combination: surfaces/volumes jodo. Area cm^2, Volume cm^3.",
    ])
    d.space(6)

    d.h2("Solved Examples - Samjho Kaise Solve Karte Hain")
    d.body("Neeche 10 examples step-by-step solve karke dikhaye gaye hain.", color=GREY)
    d.space(3)

    examples = [
        ("Example 1:  Cube ka side 5 cm. Volume aur TSA?",
         ["Volume = a^3 = 5 x 5 x 5 = 125.",
          "TSA = 6 a^2 = 6 x 25 = 150."],
         "Volume = 125 cm^3, TSA = 150 cm^2"),
        ("Example 2:  Cuboid l=4, b=3, h=2. Volume?",
         ["Volume = l x b x h = 4 x 3 x 2."],
         "24 cm^3"),
        ("Example 3:  Cylinder r=7, h=10. Volume? (pi=22/7)",
         ["Volume = pi r^2 h = (22/7) x 49 x 10.",
          "= 22 x 7 x 10."],
         "1540 cm^3"),
        ("Example 4:  Cylinder r=7, h=10. CSA? (pi=22/7)",
         ["CSA = 2 pi r h = 2 x (22/7) x 7 x 10.",
          "= 2 x 22 x 10."],
         "440 cm^2"),
        ("Example 5:  Cone r=3, h=4. Slant height l?",
         ["l = sqrt(r^2 + h^2) = sqrt(9 + 16).",
          "= sqrt(25)."],
         "l = 5 cm"),
        ("Example 6:  Cone r=3, h=4. Volume? (pi=3.14)",
         ["V = (1/3) pi r^2 h = (1/3) x 3.14 x 9 x 4.",
          "= (1/3) x 113.04."],
         "37.68 cm^3"),
        ("Example 7:  Sphere r=7. Surface area? (pi=22/7)",
         ["SA = 4 pi r^2 = 4 x (22/7) x 49.",
          "= 4 x 22 x 7."],
         "616 cm^2"),
        ("Example 8:  Sphere r=3. Volume? (pi=3.14)",
         ["V = (4/3) pi r^3 = (4/3) x 3.14 x 27.",
          "= (4/3) x 84.78."],
         "113.04 cm^3"),
        ("Example 9:  Hemisphere r=7. TSA? (pi=22/7)",
         ["TSA = 3 pi r^2 = 3 x (22/7) x 49.",
          "= 3 x 22 x 7."],
         "462 cm^2"),
        ("Example 10:  Cone (r=3,h=4) ke upar hemisphere (r=3). Exposed surface?",
         ["Cone CSA = pi r l = pi x 3 x 5 = 15 pi.",
          "Hemisphere CSA = 2 pi r^2 = 2 pi x 9 = 18 pi.",
          "Jodo: 15 pi + 18 pi."],
         "33 pi cm^2"),
    ]
    for q, steps, ans in examples:
        d.label_body(q, "")
        for s in steps:
            d.bullet("Step: " + s)
        d.label_body("   Answer:", ans)
        d.space(5)

    d.h2("Practice Questions")
    d.body("Pehle khud solve karne ki koshish karo. Neeche har question ka step-by-step "
           "solution diya gaya hai.", color=GREY)
    d.space(3)

    questions = [
        "Cube ka volume formula kya hai?",
        "Cube ka TSA formula kya hai?",
        "Cuboid ka volume formula kya hai?",
        "Cylinder ka volume formula kya hai?",
        "Cylinder ka CSA formula kya hai?",
        "Cone ka volume formula kya hai?",
        "Cone ki slant height ka formula kya hai?",
        "Cone ka CSA formula kya hai?",
        "Sphere ka volume formula kya hai?",
        "Sphere ka surface area formula kya hai?",
        "Hemisphere ka volume formula kya hai?",
        "Hemisphere ka TSA formula kya hai?",
        "CSA aur TSA me kya antar hai?",
        "Area aur volume ke units kya hote hain?",
        "Cube side=4 -> volume?",
        "Cylinder r=7,h=5 -> volume? (pi=22/7)",
        "Cone r=6,h=8 -> slant height?",
        "Sphere r=7 -> surface area? (pi=22/7)",
        "Frustum ka volume formula kya hai?",
        "Combination of solids me total volume kaise nikalte hain?",
    ]
    for i, q in enumerate(questions, start=1):
        d.label_body("Q" + str(i) + ".", q)
        d.space(2)

    d.h2("Step-by-Step Solutions")
    solutions = [
        ("Cube ka volume?", ["side ka cube."], "a^3"),
        ("Cube ka TSA?", ["6 faces, har ek a^2."], "6 a^2"),
        ("Cuboid ka volume?", ["l x b x h."], "l b h"),
        ("Cylinder ka volume?", ["base area x height."], "pi r^2 h"),
        ("Cylinder ka CSA?", ["curved surface."], "2 pi r h"),
        ("Cone ka volume?", ["cylinder ka 1/3."], "(1/3) pi r^2 h"),
        ("Cone slant height?", ["Pythagoras."], "l = sqrt(r^2 + h^2)"),
        ("Cone ka CSA?", ["curved surface."], "pi r l"),
        ("Sphere ka volume?", ["standard."], "(4/3) pi r^3"),
        ("Sphere ka SA?", ["standard."], "4 pi r^2"),
        ("Hemisphere ka volume?", ["sphere ka aadha."], "(2/3) pi r^3"),
        ("Hemisphere ka TSA?", ["curved + flat circle."], "3 pi r^2"),
        ("CSA vs TSA?", ["curved only vs sab milake."], "CSA = side only; TSA = total"),
        ("Area aur volume units?", ["2D vs 3D."], "cm^2 aur cm^3"),
        ("Cube side=4 -> volume?", ["4^3 = 64."], "64 cm^3"),
        ("Cylinder r=7,h=5 -> volume?", ["(22/7) x 49 x 5 = 22 x 7 x 5."], "770 cm^3"),
        ("Cone r=6,h=8 -> slant?", ["sqrt(36+64) = sqrt(100)."], "10"),
        ("Sphere r=7 -> SA?", ["4 x (22/7) x 49 = 4 x 22 x 7."], "616 cm^2"),
        ("Frustum ka volume?", ["standard formula."], "(1/3) pi h (R^2 + r^2 + R r)"),
        ("Combination total volume?", ["alag solids ke volume jodo."], "Volumes ka jod"),
    ]
    for i, (q, steps, ans) in enumerate(solutions, start=1):
        d.label_body("Q" + str(i) + ".", q)
        for s in steps:
            d.bullet("Step: " + s)
        d.label_body("   Answer:", ans)
        d.space(4)

    return d


if __name__ == "__main__":
    doc = build_document()
    out_file = "Surface_Areas_and_Volumes_Notes.pdf"
    pages = write_pdf(doc, out_file)
    print("Generated '" + out_file + "' with " + str(pages) + " page(s).")
