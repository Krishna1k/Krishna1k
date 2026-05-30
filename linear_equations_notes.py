#!/usr/bin/env python3
"""
Chapter 3: Pair of Linear Equations in Two Variables - Hinglish notes PDF.
Red-page core basics + main chapter content, green EXAM tags,
solved examples + step-by-step solutions.
numbers_notes.py ka pure-Python PDF engine reuse karta hai.

Output: Linear_Equations_Notes.pdf
"""

from numbers_notes import (
    PDFBuilder, write_pdf,
    LEFT, RIGHT, PAGE_W, NAVY, GREY,
)


def build_document():
    d = PDFBuilder()

    # ---- Title -------------------------------------------------------
    d.title("Linear Equations in Two Variables")
    d.subtitle("Chapter 3 - Hinglish Notes, Methods, Examples + Solutions")
    d.hline(LEFT, PAGE_W - RIGHT, d.y + 4, NAVY, 1.2)
    d.space(10)
    d.body("Ye Chapter 3 (Pair of Linear Equations in Two Variables) ka complete guide "
           "hai. Pehle red-page ke core basics (jo Class 7-8-9 me padhe), fir chapter ka "
           "main content - graphical, substitution aur elimination methods + a1/a2 "
           "conditions. End me solved examples aur 20 practice questions ke step-by-step "
           "solutions hain.", color=GREY)
    d.space(4)
    d.legend_exam()
    d.space(4)

    # ================= PART A : CORE BASICS =========================
    d.h2("PART A - Core Basics (Miss Mat Karna)")
    d.space(2)

    # 1. Variable & Equation
    d.h2("1. Variable aur Equation")
    d.exam_tag()
    d.label_body("Variable:", "Unknown number, jaise x ya y.")
    d.label_body("Equation:", "Aisa statement jisme '=' (barabar) ka chinh ho.")
    d.bullet("Example: 2x + 3 = 7 ek equation hai.")
    d.space(6)

    # 2. Linear Equation in One Variable
    d.h2("2. Linear Equation in ONE Variable")
    d.exam_tag()
    d.label_body("Form:", "ax + b = 0  (sirf ek variable, power 1).")
    d.bullet("Example: 3x - 6 = 0  ->  x = 2.")
    d.bullet("Ise sirf EK hi solution milta hai.")
    d.space(6)

    # 3. Linear Equation in Two Variables
    d.h2("3. Linear Equation in TWO Variables")
    d.exam_tag()
    d.label_body("Form:", "ax + by + c = 0  (do variables, dono ki power 1).")
    d.bullet("Example: 2x + 3y = 12.")
    d.bullet("Iske INFINITE (anant) solutions hote hain - har x ke liye ek y.")
    d.space(6)

    # 4. Solution
    d.h2("4. Solution Kya Hai?")
    d.exam_tag()
    d.label_body("Definition:", "Wo (x, y) jodi jo equation ko sahi (satisfy) kare.")
    d.bullet("Example: x + y = 5 ke liye (2, 3) solution hai, kyunki 2 + 3 = 5.")
    d.space(6)

    # 5. Graph Basics
    d.h2("5. Graph Basics")
    d.exam_tag()
    d.bullet("X-axis = horizontal (leti), Y-axis = vertical (khadi).")
    d.bullet("Dono ORIGIN (0, 0) par milte hain. Point ko (x, y) likhte hain.")
    d.bullet("Linear equation ka graph hamesha ek SEEDHI LINE hoti hai.")
    d.space(6)

    # 6. Ratio
    d.h2("6. Ratio (a1/a2 type)")
    d.label_body("Ratio:", "Do numbers ki tulna, jaise 2/4 = 1/2.")
    d.bullet("Is chapter me coefficients ke ratio compare karenge: a1/a2, b1/b2, c1/c2.")
    d.space(6)

    # 7. Simple equation solve
    d.h2("7. Simple Equation Solve Karna")
    d.exam_tag()
    d.label_body("Transposition:", "Ek side ki cheez doosri side le jao to uska sign "
                 "badal jata hai.")
    d.bullet("Example: 2x = 18  ->  x = 18/2 = 9.")
    d.bullet("Jo jod raha tha wo ghatne lagta hai; jo guna kar raha tha wo bhaag.")
    d.space(6)

    # ================= PART B : MAIN CONTENT ========================
    d.h2("PART B - Chapter 3 ka Main Content")
    d.space(2)

    # 8. Pair of linear equations
    d.h2("8. Pair of Linear Equations")
    d.label_body("Matlab:", "Do linear equations jo ek saath (simultaneously) di gayi "
                 "hon, jaise:")
    d.bullet("a1 x + b1 y + c1 = 0")
    d.bullet("a2 x + b2 y + c2 = 0")
    d.bullet("Inhe ek saath solve karke wo (x, y) dhoondte hain jo DONO ko satisfy kare.")
    d.space(6)

    # 9. Graphical method
    d.h2("9. Graphical Method (3 Cases)")
    d.exam_tag()
    d.bullet("Dono equations ki seedhi lines banao aur dekho wo kaise milti hain:")
    d.bullet("Case 1: Lines ek point par CUT karein -> 1 unique solution.")
    d.bullet("Case 2: Lines PARALLEL hon -> koi solution nahi (no solution).")
    d.bullet("Case 3: Lines bilkul UPAR-UPAR (coincident) -> infinite solutions.")
    d.space(6)

    # 10. Conditions
    d.h2("10. Conditions for Solutions (a1/a2 Rule)")
    d.exam_tag()
    d.body("Ye sabse important exam point hai. Coefficients ke ratio se solution ka "
           "type pata chalta hai:", color=GREY)
    d.space(2)
    d.box_note([
        "a1/a2 != b1/b2          -> Unique solution (lines intersect)  [Consistent]",
        "a1/a2 = b1/b2 != c1/c2  -> No solution (parallel lines)       [Inconsistent]",
        "a1/a2 = b1/b2 = c1/c2   -> Infinite solutions (coincident)    [Consistent]",
    ])
    d.bullet("Consistent = solution hai; Inconsistent = koi solution nahi.")
    d.space(6)

    # 11. Substitution method
    d.h2("11. Substitution Method")
    d.exam_tag()
    d.bullet("Step 1: Ek equation se ek variable ko doosre ke roop me likho (jaise x = ...).")
    d.bullet("Step 2: Use doosri equation me substitute (daal) karo -> ek variable bachega.")
    d.bullet("Step 3: Use solve karo, fir value wapas daal kar doosra variable nikalo.")
    d.space(6)

    # 12. Elimination method
    d.h2("12. Elimination Method")
    d.exam_tag()
    d.bullet("Step 1: Coefficients barabar karne ke liye equations ko number se multiply karo.")
    d.bullet("Step 2: Dono equations ko jodo ya ghatao taaki ek variable HAT (eliminate) jaye.")
    d.bullet("Step 3: Bache hue variable ko solve karo, fir doosra nikalo.")
    d.space(6)

    # 13. Word problems
    d.h2("13. Word Problems")
    d.bullet("Sentences ko x aur y me likho (do unknowns -> do equations banao).")
    d.bullet("Fir substitution ya elimination se solve karo.")
    d.bullet("Common types: numbers ka sum/difference, age problems, cost of items.")
    d.space(6)

    # ---- Quick Revision ---------------------------------------------
    d.h2("Quick Revision")
    d.box_note([
        "One variable -> 1 solution;  Two variables -> infinite (akeli eq).",
        "Solution = (x, y) jo equation satisfy kare.",
        "a1/a2 != b1/b2 -> unique;  =b1/b2 !=c1/c2 -> none;  all equal -> infinite.",
        "Methods: Graphical, Substitution, Elimination.",
        "Linear graph hamesha seedhi line.",
    ])
    d.space(6)

    # ---- Solved Examples --------------------------------------------
    d.h2("Solved Examples - Samjho Kaise Solve Karte Hain")
    d.body("Neeche 10 examples step-by-step solve karke dikhaye gaye hain.", color=GREY)
    d.space(3)

    examples = [
        ("Example 1 (Substitution):  x + y = 5,  x - y = 1",
         ["Eq1 se: x = 5 - y.",
          "Eq2 me daalo: (5 - y) - y = 1 -> 5 - 2y = 1.",
          "2y = 4 -> y = 2.  Fir x = 5 - 2 = 3."],
         "x = 3, y = 2"),
        ("Example 2 (Elimination):  2x + 3y = 12,  2x - y = 4",
         ["Dono me 2x same hai, to ghatao (Eq1 - Eq2):",
          "(2x + 3y) - (2x - y) = 12 - 4 -> 4y = 8 -> y = 2.",
          "2x - 2 = 4 -> 2x = 6 -> x = 3."],
         "x = 3, y = 2"),
        ("Example 3 (Condition):  2x + 3y - 5 = 0,  4x + 6y - 10 = 0",
         ["a1/a2 = 2/4 = 1/2.",
          "b1/b2 = 3/6 = 1/2.",
          "c1/c2 = -5/-10 = 1/2.  Teeno barabar."],
         "Infinite solutions (coincident lines)"),
        ("Example 4 (Condition):  x + 2y - 4 = 0,  2x + 4y - 12 = 0",
         ["a1/a2 = 1/2,  b1/b2 = 2/4 = 1/2.",
          "c1/c2 = -4/-12 = 1/3.",
          "a1/a2 = b1/b2 but != c1/c2."],
         "No solution (parallel lines)"),
        ("Example 5 (Condition):  x + y - 5 = 0,  x - y - 1 = 0",
         ["a1/a2 = 1/1 = 1.",
          "b1/b2 = 1/(-1) = -1.",
          "1 != -1, to a1/a2 != b1/b2."],
         "Unique solution (intersecting)"),
        ("Example 6 (One variable):  3x - 6 = 0",
         ["3x = 6.",
          "x = 6/3."],
         "x = 2"),
        ("Example 7 (Transposition):  2x = 18",
         ["x = 18 / 2."],
         "x = 9"),
        ("Example 8 (Check solution):  Kya (2, 3) x + y = 5 ka solution hai?",
         ["x=2, y=3 daalo: 2 + 3 = 5.",
          "Equation satisfy ho gayi."],
         "Haan, solution hai"),
        ("Example 9 (Word problem):  Do numbers ka sum 10, difference 4.",
         ["Maano numbers x aur y: x + y = 10,  x - y = 4.",
          "Jodo: 2x = 14 -> x = 7.",
          "y = 10 - 7 = 3."],
         "Numbers = 7 aur 3"),
        ("Example 10 (Substitution):  y = 2x,  x + y = 9",
         ["y = 2x ko doosri me daalo: x + 2x = 9.",
          "3x = 9 -> x = 3.  Fir y = 2(3) = 6."],
         "x = 3, y = 6"),
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
        "Linear equation in two variables ka general form kya hai?",
        "ax + b = 0 ke kitne solutions hote hain?",
        "2x + 3y = 12 ke kitne solutions hote hain?",
        "Kya (1, 4) equation x + y = 5 ka solution hai?",
        "Solve karo: x + y = 7,  x - y = 3.",
        "Substitution se solve: y = 2x,  x + y = 9.",
        "a1/a2 != b1/b2 ho to kitne solutions?",
        "a1/a2 = b1/b2 != c1/c2 ho to kya hota hai?",
        "a1/a2 = b1/b2 = c1/c2 ho to kitne solutions?",
        "Linear equation ka graph kaisa hota hai?",
        "Origin ke coordinates kya hote hain?",
        "Solve karo: 2x = 16.",
        "Parallel lines wale system ko consistent kehte hain ya inconsistent?",
        "Coincident lines ke kitne solutions hote hain?",
        "Elimination se solve: x + y = 10,  x - y = 2.",
        "3x - 9 = 0 ka solution kya hai?",
        "Intersecting lines ke kitne solutions hote hain?",
        "X-axis aur Y-axis kahan milte hain?",
        "Do numbers ka sum 12 aur difference 2 hai. Numbers batao.",
        "Solve karo: 5x = 35.",
    ]
    for i, q in enumerate(questions, start=1):
        d.label_body(f"Q{i}.", q)
        d.space(2)

    # ---- Step-by-Step Solutions -------------------------------------
    d.h2("Step-by-Step Solutions")
    solutions = [
        ("General form?",
         ["Do variables, power 1, '=' ke saath."], "ax + by + c = 0"),
        ("ax + b = 0 ke solutions?",
         ["Ek variable, power 1 -> ek hi value milti hai."], "1 (unique)"),
        ("2x + 3y = 12 ke solutions?",
         ["Two variables -> har x ke liye ek y."], "Infinite"),
        ("Kya (1, 4) x + y = 5 ka solution?",
         ["x=1, y=4: 1 + 4 = 5. Satisfy."], "Haan"),
        ("x + y = 7, x - y = 3?",
         ["Jodo: 2x = 10 -> x = 5.", "y = 7 - 5 = 2."], "x=5, y=2"),
        ("y = 2x, x + y = 9?",
         ["x + 2x = 9 -> 3x = 9 -> x = 3.", "y = 2(3) = 6."], "x=3, y=6"),
        ("a1/a2 != b1/b2?",
         ["Lines intersect karti hain."], "Unique solution"),
        ("a1/a2 = b1/b2 != c1/c2?",
         ["Lines parallel hoti hain."], "No solution (inconsistent)"),
        ("a1/a2 = b1/b2 = c1/c2?",
         ["Lines coincident (upar-upar) hoti hain."], "Infinite solutions"),
        ("Linear equation ka graph?",
         ["Degree 1 -> seedhi line."], "Straight line"),
        ("Origin ke coordinates?",
         ["X aur Y axis jahan milte hain."], "(0, 0)"),
        ("2x = 16?",
         ["x = 16/2."], "x = 8"),
        ("Parallel lines -> consistent ya inconsistent?",
         ["Koi solution nahi hota."], "Inconsistent"),
        ("Coincident lines ke solutions?",
         ["Lines bilkul same hain."], "Infinite"),
        ("x + y = 10, x - y = 2?",
         ["Jodo: 2x = 12 -> x = 6.", "y = 10 - 6 = 4."], "x=6, y=4"),
        ("3x - 9 = 0?",
         ["3x = 9 -> x = 9/3."], "x = 3"),
        ("Intersecting lines ke solutions?",
         ["Ek hi point par milti hain."], "1 (unique)"),
        ("X-axis aur Y-axis kahan milte?",
         ["Dono ka milan bindu = origin."], "Origin (0,0)"),
        ("Sum 12, difference 2?",
         ["x + y = 12, x - y = 2.", "Jodo: 2x = 14 -> x = 7, y = 5."], "7 aur 5"),
        ("5x = 35?",
         ["x = 35/5."], "x = 7"),
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
    out_file = "Linear_Equations_Notes.pdf"
    pages = write_pdf(doc, out_file)
    print(f"Generated '{out_file}' with {pages} page(s).")
