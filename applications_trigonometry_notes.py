#!/usr/bin/env python3
"""
Chapter 9: Some Applications of Trigonometry (Heights & Distances) - Hinglish PDF.
Red-page core basics (PART A) + main chapter content (PART B), green EXAM tags,
solved examples + step-by-step solutions.
numbers_notes.py ka pure-Python PDF engine reuse karta hai.

Output: Applications_of_Trigonometry_Notes.pdf
"""

from numbers_notes import (
    PDFBuilder, write_pdf,
    LEFT, RIGHT, PAGE_W, NAVY, GREY,
)


def build_document():
    d = PDFBuilder()

    d.title("Applications of Trigonometry")
    d.subtitle("Chapter 9 - Heights & Distances, Hinglish Notes + Solutions")
    d.hline(LEFT, PAGE_W - RIGHT, d.y + 4, NAVY, 1.2)
    d.space(10)
    d.body("Ye Chapter 9 (Some Applications of Trigonometry) ka complete guide hai. Isme "
           "trigonometry ka use height aur distance nikalne me hota hai. Pehle red-page "
           "ke core basics, fir main content - line of sight, angle of elevation/"
           "depression aur problems solve karna. End me solved examples aur 20 practice "
           "questions ke step-by-step solutions hain.", color=GREY)
    d.space(4)
    d.legend_exam()
    d.space(4)

    # ================= PART A : CORE BASICS =========================
    d.h2("PART A - Core Basics (Miss Mat Karna)")
    d.space(2)

    d.h2("1. Trig Ratios (Chapter 8 Recap)")
    d.exam_tag()
    d.bullet("sin = Perpendicular / Hypotenuse")
    d.bullet("cos = Base / Hypotenuse")
    d.bullet("tan = Perpendicular / Base")
    d.space(6)

    d.h2("2. Special Angle Values (Zaroori)")
    d.exam_tag()
    d.bullet("tan 30 = 1/sqrt3,  tan 45 = 1,  tan 60 = sqrt3.")
    d.bullet("sin 30 = 1/2,  sin 45 = 1/sqrt2,  sin 60 = sqrt3/2.")
    d.bullet("cos 30 = sqrt3/2,  cos 45 = 1/sqrt2,  cos 60 = 1/2.")
    d.space(6)

    d.h2("3. Square Root Values")
    d.bullet("sqrt3 = 1.732,  sqrt2 = 1.414  (decimal answer ke liye).")
    d.space(6)

    d.h2("4. Horizontal aur Vertical")
    d.exam_tag()
    d.bullet("Horizontal = leti line (zameen ke parallel).")
    d.bullet("Vertical = khadi line (tower/building ki height).")
    d.space(6)

    d.h2("5. Right Triangle Banta Hai")
    d.exam_tag()
    d.bullet("Tower (vertical) + zameen (horizontal) + line of sight milke ek "
             "right-angled triangle banate hain.")
    d.space(6)

    d.h2("6. Alternate Angles (Parallel Lines)")
    d.exam_tag()
    d.bullet("Jab do horizontal lines parallel ho, to angle of elevation = angle of "
             "depression (alternate angles).")
    d.space(6)

    d.h2("7. Solve for Unknown")
    d.exam_tag()
    d.bullet("tan(angle) = opposite / adjacent.")
    d.bullet("Ek side pata ho to doosri multiply/divide karke nikaal lo.")
    d.space(6)

    # ================= PART B : MAIN CONTENT ========================
    d.h2("PART B - Chapter 9 ka Main Content")
    d.space(2)

    d.h2("8. Line of Sight")
    d.exam_tag()
    d.label_body("Definition:", "Observer ki aankh se object tak ki seedhi (straight) "
                 "line ko line of sight kehte hain.")
    d.space(6)

    d.h2("9. Angle of Elevation")
    d.exam_tag()
    d.label_body("Definition:", "Jab object UPAR ho, to horizontal line se line of sight "
                 "tak UPAR ki taraf bana angle = angle of elevation.")
    d.bullet("Example: zameen par khade ho kar tower ki choti dekhna.")
    d.space(6)

    d.h2("10. Angle of Depression")
    d.exam_tag()
    d.label_body("Definition:", "Jab object NEECHE ho, to horizontal line se line of "
                 "sight tak NEECHE ki taraf bana angle = angle of depression.")
    d.bullet("Example: building ki chhat se neeche khadi car dekhna.")
    d.bullet("Yaad: elevation = upar dekho, depression = neeche dekho.")
    d.space(6)

    d.h2("11. Problem Solve Karne ke Steps")
    d.exam_tag()
    d.bullet("Step 1: Diagram banao - vertical (height), horizontal (distance), angle mark karo.")
    d.bullet("Step 2: Right triangle pehchaano; kaunsi side pata hai aur kya nikaalna hai.")
    d.bullet("Step 3: Sahi ratio chuno (tan, sin ya cos) angle aur sides ke hisaab se.")
    d.bullet("Step 4: Equation banao aur unknown solve karo.")
    d.space(6)

    d.h2("12. Kaunsa Ratio Kab")
    d.box_note([
        "Height aur Base (horizontal distance) involved -> tan use karo.",
        "Height aur Hypotenuse (line of sight) involved -> sin use karo.",
        "Base aur Hypotenuse involved -> cos use karo.",
    ])
    d.space(6)

    d.h2("Quick Revision")
    d.box_note([
        "Elevation = upar dekhne wala angle; Depression = neeche dekhne wala.",
        "tan(angle) = height / base (sabse zyada use hota hai).",
        "Special: tan30=1/sqrt3, tan45=1, tan60=sqrt3.",
        "Elevation = depression (alternate angles, parallel ground).",
        "Hamesha pehle diagram banao!",
    ])
    d.space(6)

    # ---- Solved Examples --------------------------------------------
    d.h2("Solved Examples - Samjho Kaise Solve Karte Hain")
    d.body("Neeche 10 examples step-by-step solve karke dikhaye gaye hain.", color=GREY)
    d.space(3)

    examples = [
        ("Example 1:  Tower se 30m door se choti ka elevation 45 hai. Tower ki height?",
         ["tan 45 = height / base.",
          "1 = h / 30.",
          "h = 30 x 1."],
         "Height = 30 m"),
        ("Example 2:  20m door se elevation 60. Tower ki height?",
         ["tan 60 = h / 20 -> sqrt3 = h / 20.",
          "h = 20 sqrt3.",
          "= 20 x 1.732."],
         "Height = 20 sqrt3 ~ 34.64 m"),
        ("Example 3:  Tower height 30m, base se distance 30 sqrt3 m. Elevation angle?",
         ["tan(angle) = 30 / (30 sqrt3) = 1/sqrt3.",
          "tan 30 = 1/sqrt3."],
         "Angle = 30 degree"),
        ("Example 4:  Pole height 10m. Elevation 30 ho to distance?",
         ["tan 30 = 10 / d -> 1/sqrt3 = 10/d.",
          "d = 10 sqrt3."],
         "Distance = 10 sqrt3 ~ 17.32 m"),
        ("Example 5:  100m building ki chhat se car ka depression 45. Car ki doori?",
         ["Depression 45 = elevation 45 (alternate).",
          "tan 45 = 100 / d -> 1 = 100/d."],
         "Distance = 100 m"),
        ("Example 6:  Ladder 10m, wall se elevation 60. Wall par height?",
         ["sin 60 = height / 10 (ladder = hypotenuse).",
          "sqrt3/2 = h/10 -> h = 5 sqrt3."],
         "Height = 5 sqrt3 ~ 8.66 m"),
        ("Example 7:  Kite ki dori 50m, elevation 30. Kite ki height?",
         ["sin 30 = h / 50 (dori = hypotenuse).",
          "1/2 = h/50 -> h = 25."],
         "Height = 25 m"),
        ("Example 8:  Elevation 45 par height = distance hota hai. Sahi ya galat?",
         ["tan 45 = 1 -> height/base = 1.",
          "Isliye height = base."],
         "Sahi"),
        ("Example 9:  Ladder 10m, base se 5m door. Wall se angle (cos use)?",
         ["cos(angle) = base / hyp = 5/10 = 1/2.",
          "cos 60 = 1/2."],
         "Angle = 60 degree"),
        ("Example 10:  Tower height 15m, elevation 30. Observer ki doori?",
         ["tan 30 = 15 / d -> 1/sqrt3 = 15/d.",
          "d = 15 sqrt3."],
         "Distance = 15 sqrt3 ~ 25.98 m"),
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
        "Line of sight kya hota hai?",
        "Angle of elevation kya hota hai?",
        "Angle of depression kya hota hai?",
        "Height aur base diya ho to kaunsa ratio use karte hain?",
        "tan 45 ka value kya hai?",
        "tan 60 ka value kya hai?",
        "tan 30 ka value kya hai?",
        "Elevation aur depression me kya relation hota hai (parallel ground)?",
        "30m door se elevation 45 -> tower height?",
        "Tower height 10m, elevation 45 -> distance?",
        "Height aur hypotenuse diya ho to kaunsa ratio?",
        "Base aur hypotenuse diya ho to kaunsa ratio?",
        "sqrt3 ka approx value kya hai?",
        "Problem solve karne ka pehla step kya hona chahiye?",
        "Elevation 60, base 10m -> height?",
        "Ladder 10m hypotenuse, sin 30 -> wall par height?",
        "Tower height = distance kab hota hai?",
        "Depression angle kahan se naapte hain (upar ya neeche)?",
        "tan(angle) kis ke barabar hota hai (opposite/adjacent)?",
        "Vertical aur horizontal ka matlab batao.",
    ]
    for i, q in enumerate(questions, start=1):
        d.label_body(f"Q{i}.", q)
        d.space(2)

    # ---- Step-by-Step Solutions -------------------------------------
    d.h2("Step-by-Step Solutions")
    solutions = [
        ("Line of sight?",
         ["Aankh se object tak seedhi line."], "Observer se object tak straight line"),
        ("Angle of elevation?",
         ["Object upar; horizontal se upar ka angle."], "Upar dekhne wala angle"),
        ("Angle of depression?",
         ["Object neeche; horizontal se neeche ka angle."], "Neeche dekhne wala angle"),
        ("Height + base -> kaunsa ratio?",
         ["tan = opp/adj."], "tan"),
        ("tan 45?",
         ["Table se."], "1"),
        ("tan 60?",
         ["Table se."], "sqrt3"),
        ("tan 30?",
         ["Table se."], "1/sqrt3"),
        ("Elevation vs depression?",
         ["Alternate angles (parallel ground)."], "Dono barabar hote hain"),
        ("30m door, elevation 45 -> height?",
         ["tan45 = h/30 -> 1 = h/30."], "30 m"),
        ("Height 10m, elevation 45 -> distance?",
         ["tan45 = 10/d -> 1 = 10/d."], "10 m"),
        ("Height + hypotenuse -> ratio?",
         ["sin = opp/hyp."], "sin"),
        ("Base + hypotenuse -> ratio?",
         ["cos = adj/hyp."], "cos"),
        ("sqrt3 approx?",
         ["Yaad value."], "1.732"),
        ("Pehla step?",
         ["Situation samajhne ke liye."], "Diagram banao"),
        ("Elevation 60, base 10 -> height?",
         ["tan60 = h/10 -> sqrt3 = h/10."], "10 sqrt3 (~17.32 m)"),
        ("Ladder 10m, sin30 -> height?",
         ["sin30 = h/10 -> 1/2 = h/10."], "5 m"),
        ("Height = distance kab?",
         ["tan45 = 1 -> h = base."], "Jab angle 45 ho"),
        ("Depression kahan se?",
         ["Upar ki horizontal se neeche."], "Upar se (neeche ki taraf)"),
        ("tan(angle) = ?",
         ["Right triangle ratio."], "opposite / adjacent"),
        ("Vertical aur horizontal?",
         ["Khadi aur leti line."], "Vertical = khadi, Horizontal = leti"),
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
    out_file = "Applications_of_Trigonometry_Notes.pdf"
    pages = write_pdf(doc, out_file)
    print(f"Generated '{out_file}' with {pages} page(s).")
