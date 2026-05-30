#!/usr/bin/env python3
"""
Chapter 4: Quadratic Equations - Hinglish notes PDF.
Red-page core basics + main chapter content, green EXAM tags,
solved examples + step-by-step solutions.
numbers_notes.py ka pure-Python PDF engine reuse karta hai.

Output: Quadratic_Equations_Notes.pdf
"""

from numbers_notes import (
    PDFBuilder, write_pdf,
    LEFT, RIGHT, PAGE_W, NAVY, GREY,
)


def build_document():
    d = PDFBuilder()

    # ---- Title -------------------------------------------------------
    d.title("Quadratic Equations")
    d.subtitle("Chapter 4 - Hinglish Notes, Methods, Examples + Solutions")
    d.hline(LEFT, PAGE_W - RIGHT, d.y + 4, NAVY, 1.2)
    d.space(10)
    d.body("Ye Chapter 4 (Quadratic Equations) ka complete guide hai. Pehle red-page ke "
           "core basics (power, coefficient, zero product rule, +/- etc.), fir chapter "
           "ka main content - factorisation, quadratic formula, discriminant aur "
           "sum/product of roots. End me solved examples aur 20 practice questions ke "
           "step-by-step solutions hain.", color=GREY)
    d.space(4)
    d.legend_exam()
    d.space(4)

    # ================= PART A : CORE BASICS =========================
    d.h2("PART A - Core Basics (Miss Mat Karna)")
    d.space(2)

    d.h2("1. Power / Square")
    d.bullet("x^2 = x times x. Ise 'x square' bolte hain.")
    d.bullet("x^2 me x base hai aur 2 power hai.")
    d.space(6)

    d.h2("2. Equation vs Expression")
    d.exam_tag()
    d.label_body("Expression:", "Sirf likha hua, '=' nahi. Jaise 2x^2 + 3x - 5.")
    d.label_body("Equation:", "'=' sign ke saath. Jaise 2x^2 + 3x - 5 = 0.")
    d.space(6)

    d.h2("3. Degree")
    d.bullet("Degree = sabse bada power. Quadratic me degree hamesha 2 hota hai.")
    d.space(6)

    d.h2("4. Coefficient (a, b, c)")
    d.exam_tag()
    d.label_body("Rule:", "ax^2 + bx + c me a = x^2 ka, b = x ka, c = constant.")
    d.bullet("Example: 3x^2 - 5x + 2  ->  a = 3, b = -5, c = 2.")
    d.space(6)

    d.h2("5. Root / Zero / Solution")
    d.exam_tag()
    d.label_body("Definition:", "Root = wo x jiske liye equation 0 ho jaye.")
    d.bullet("Quadratic equation ke MAXIMUM 2 roots hote hain.")
    d.space(6)

    d.h2("6. Factorisation (Splitting Middle Term)")
    d.exam_tag()
    d.label_body("Idea:", "ax^2 + bx + c ko (..)(..) me todo.")
    d.bullet("Middle term b ko aise 2 numbers p, q me todo jahan:")
    d.bullet("p + q = b   AND   p x q = a x c.")
    d.space(6)

    d.h2("7. Square Root (sqrt)")
    d.bullet("sqrt(25) = 5, kyunki 5 x 5 = 25. Ye power (square) ka ulta hai.")
    d.bullet("sqrt(D) ka matlab D ka square root.")
    d.space(6)

    d.h2("8. Zero Product Rule")
    d.exam_tag()
    d.label_body("Rule:", "Agar A x B = 0, to ya A = 0 ya B = 0 (ya dono).")
    d.bullet("Yahi factorisation method ka base hai. (x+2)(x+3)=0 -> x=-2 ya x=-3.")
    d.space(6)

    d.h2("9. Plus-Minus (+/-)")
    d.exam_tag()
    d.bullet("Quadratic formula me +/- ka matlab DO answers milte hain:")
    d.bullet("ek '+' wala root, aur ek '-' wala root.")
    d.space(6)

    # ================= PART B : MAIN CONTENT ========================
    d.h2("PART B - Chapter 4 ka Main Content")
    d.space(2)

    d.h2("10. Quadratic Equation Kya Hai?")
    d.exam_tag()
    d.label_body("Standard Form:", "ax^2 + bx + c = 0, jahan a != 0.")
    d.bullet("a != 0 zaroori hai (warna x^2 hi nahi bachega, linear ban jayega).")
    d.bullet("Example: 2x^2 - 3x + 1 = 0.")
    d.space(6)

    d.h2("11. Solve Karne ke Methods")
    d.exam_tag()
    d.label_body("(a) Factorisation:", "Middle term todo, fir Zero Product Rule lagao.")
    d.label_body("(b) Quadratic Formula:", "Hamesha kaam karta hai:")
    d.box_note([
        "x = [ -b +/- sqrt(b^2 - 4ac) ] / (2a)",
        "",
        "Yahan b^2 - 4ac ko Discriminant (D) kehte hain.",
    ])
    d.label_body("(c) Completing the Square:", "Equation ko (x + k)^2 = number form me "
                 "badal kar solve karna.")
    d.space(6)

    d.h2("12. Discriminant (D) aur Nature of Roots")
    d.exam_tag()
    d.label_body("Formula:", "D = b^2 - 4ac.")
    d.box_note([
        "D > 0  ->  2 alag-alag (distinct) real roots",
        "D = 0  ->  2 barabar (equal) real roots",
        "D < 0  ->  koi real root nahi (imaginary)",
    ])
    d.space(6)

    d.h2("13. Sum aur Product of Roots")
    d.exam_tag()
    d.label_body("Agar roots A aur B hon:", "")
    d.bullet("Roots ka SUM (A + B) = -b/a")
    d.bullet("Roots ka PRODUCT (A x B) = c/a")
    d.bullet("Example: 2x^2 - 7x + 3 = 0 -> sum = 7/2, product = 3/2.")
    d.space(6)

    d.h2("14. Word Problems")
    d.bullet("Sentence ko x me likho, equation banao, fir solve karo.")
    d.bullet("Common: consecutive numbers, area/length, age, speed-time problems.")
    d.bullet("Answer me practical value lo (jaise length negative nahi hoti).")
    d.space(6)

    # ---- Quick Revision ---------------------------------------------
    d.h2("Quick Revision")
    d.box_note([
        "Standard form: ax^2 + bx + c = 0 (a != 0).",
        "Formula: x = [-b +/- sqrt(b^2-4ac)] / 2a.",
        "D = b^2 - 4ac:  >0 distinct,  =0 equal,  <0 no real root.",
        "Sum of roots = -b/a,  Product = c/a.",
        "Factorise: p+q=b, p x q = a x c, fir zero product rule.",
    ])
    d.space(6)

    # ---- Solved Examples --------------------------------------------
    d.h2("Solved Examples - Samjho Kaise Solve Karte Hain")
    d.body("Neeche 10 examples step-by-step solve karke dikhaye gaye hain.", color=GREY)
    d.space(3)

    examples = [
        ("Example 1 (Factorisation):  x^2 + 5x + 6 = 0",
         ["a=1, b=5, c=6. a x c = 6.",
          "p+q=5 aur pxq=6 -> 2, 3.",
          "x^2 + 2x + 3x + 6 = 0 -> (x+2)(x+3) = 0.",
          "x + 2 = 0 ya x + 3 = 0."],
         "x = -2 ya x = -3"),
        ("Example 2 (Factorisation):  x^2 - 7x + 12 = 0",
         ["p+q = -7 aur pxq = 12 -> -3, -4.",
          "(x - 3)(x - 4) = 0."],
         "x = 3 ya x = 4"),
        ("Example 3 (Quadratic Formula):  x^2 - 4x + 1 = 0",
         ["a=1, b=-4, c=1. D = b^2-4ac = 16 - 4 = 12.",
          "x = [4 +/- sqrt(12)] / 2 = [4 +/- 2 sqrt(3)] / 2."],
         "x = 2 +/- sqrt(3)"),
        ("Example 4 (Discriminant):  x^2 + 2x + 5 = 0 ke roots ka nature?",
         ["D = b^2 - 4ac = 4 - 20 = -16.",
          "D < 0."],
         "Koi real root nahi"),
        ("Example 5 (Discriminant):  x^2 - 6x + 9 = 0 ka nature?",
         ["D = 36 - 36 = 0.",
          "D = 0 -> 2 barabar roots."],
         "2 equal real roots (x = 3)"),
        ("Example 6 (Zero Product):  (x - 2)(x + 5) = 0",
         ["Zero product rule: koi ek bracket 0 hoga.",
          "x - 2 = 0 ya x + 5 = 0."],
         "x = 2 ya x = -5"),
        ("Example 7 (Sum & Product):  2x^2 - 7x + 3 = 0",
         ["a=2, b=-7, c=3.",
          "Sum = -b/a = 7/2;  Product = c/a = 3/2."],
         "Sum = 7/2, Product = 3/2"),
        ("Example 8 (Square root):  x^2 = 49",
         ["Dono taraf square root lo.",
          "x = +/- sqrt(49)."],
         "x = 7 ya x = -7"),
        ("Example 9 (a, b, c pehchaano):  3x^2 - 5x + 2 = 0",
         ["x^2 ka coefficient a, x ka b, constant c."],
         "a = 3, b = -5, c = 2"),
        ("Example 10 (Word problem):  Do consecutive positive integers ka product 20.",
         ["Maano x aur x+1: x(x+1) = 20 -> x^2 + x - 20 = 0.",
          "(x + 5)(x - 4) = 0 -> x = 4 (positive lete hain)."],
         "Numbers = 4 aur 5"),
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
        "Quadratic equation ka standard form kya hai?",
        "Quadratic equation me maximum kitne roots hote hain?",
        "2x^2 + 3x - 5 expression hai ya equation?",
        "ax^2 + bx + c = 0 me agar a = 0 ho to kya hoga?",
        "Discriminant ka formula kya hai?",
        "D > 0 ho to roots kaise hote hain?",
        "D = 0 ho to roots kaise hote hain?",
        "D < 0 ho to roots kaise hote hain?",
        "Quadratic formula likho.",
        "Solve karo: x^2 - 9 = 0.",
        "Solve karo: x^2 + 7x + 10 = 0.",
        "3x^2 - 5x + 2 = 0 me a, b, c batao.",
        "Zero product rule kya kehta hai?",
        "Roots ka sum (A + B) kis ke barabar hota hai?",
        "Roots ka product (A x B) kis ke barabar hota hai?",
        "Solve karo: (x - 3)(x + 4) = 0.",
        "x^2 = 36 ho to x = ?",
        "x^2 - 4x + 4 = 0 ka D aur nature?",
        "Splitting middle term me kaunsi 2 conditions chahiye?",
        "x^2 - 5x + 6 = 0 ke roots kya hain?",
    ]
    for i, q in enumerate(questions, start=1):
        d.label_body(f"Q{i}.", q)
        d.space(2)

    # ---- Step-by-Step Solutions -------------------------------------
    d.h2("Step-by-Step Solutions")
    solutions = [
        ("Standard form?",
         ["x^2 wala term, a != 0."], "ax^2 + bx + c = 0"),
        ("Max kitne roots?",
         ["Degree 2 -> maximum 2 roots."], "2"),
        ("2x^2 + 3x - 5 expression ya equation?",
         ["'=' sign nahi hai."], "Expression"),
        ("a = 0 ho to?",
         ["x^2 term hat jata hai -> bachta hai bx + c."], "Linear ban jata hai"),
        ("Discriminant formula?",
         ["b^2 me se 4ac ghatao."], "D = b^2 - 4ac"),
        ("D > 0?",
         ["2 alag real roots."], "Distinct real roots"),
        ("D = 0?",
         ["2 barabar real roots."], "Equal real roots"),
        ("D < 0?",
         ["Real roots possible nahi."], "No real roots"),
        ("Quadratic formula?",
         ["Standard formula yaad karo."], "x = [-b +/- sqrt(b^2-4ac)] / 2a"),
        ("x^2 - 9 = 0?",
         ["x^2 = 9 -> x = +/- sqrt(9)."], "x = 3 ya -3"),
        ("x^2 + 7x + 10 = 0?",
         ["p+q=7, pxq=10 -> 2,5.", "(x+2)(x+5)=0."], "x = -2 ya -5"),
        ("3x^2 - 5x + 2 = 0 me a,b,c?",
         ["x^2, x aur constant ke coefficients."], "a=3, b=-5, c=2"),
        ("Zero product rule?",
         ["A x B = 0 ho to."], "A = 0 ya B = 0"),
        ("Roots ka sum?",
         ["Formula yaad karo."], "-b/a"),
        ("Roots ka product?",
         ["Formula yaad karo."], "c/a"),
        ("(x - 3)(x + 4) = 0?",
         ["x-3=0 ya x+4=0."], "x = 3 ya -4"),
        ("x^2 = 36?",
         ["Dono taraf sqrt: x = +/- 6."], "x = 6 ya -6"),
        ("x^2 - 4x + 4 = 0 ka D aur nature?",
         ["D = 16 - 16 = 0."], "D=0, equal real roots (x=2)"),
        ("Splitting middle term ki 2 conditions?",
         ["Do numbers p, q chahiye."], "p+q=b AND p x q = a x c"),
        ("x^2 - 5x + 6 = 0 ke roots?",
         ["(x-2)(x-3)=0."], "x = 2 ya 3"),
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
    out_file = "Quadratic_Equations_Notes.pdf"
    pages = write_pdf(doc, out_file)
    print(f"Generated '{out_file}' with {pages} page(s).")
