#!/usr/bin/env python3
"""
Polynomials study-notes ki PDF - Hinglish, green EXAM tags,
solved examples + step-by-step solutions.
numbers_notes.py ka pure-Python PDF engine reuse karta hai.

Output: Polynomials_Notes.pdf
"""

from numbers_notes import (
    PDFBuilder, write_pdf,
    LEFT, RIGHT, PAGE_W, NAVY, GREY,
)


def build_document():
    d = PDFBuilder()

    # ---- Title -------------------------------------------------------
    d.title("Polynomials")
    d.subtitle("Aasan Hinglish Notes, Examples aur Step-by-Step Solutions")
    d.hline(LEFT, PAGE_W - RIGHT, d.y + 4, NAVY, 1.2)
    d.space(10)
    d.body("Polynomial ek algebraic expression hai jisme variables aur constants hote "
           "hain. Is guide me variable/constant se lekar degree, coefficient, zeros, "
           "factorisation aur graph tak sab kuch simple Hinglish me samjhaya gaya hai - "
           "solved examples aur 20 practice questions ke step-by-step solutions ke saath.",
           color=GREY)
    d.space(4)
    d.legend_exam()
    d.space(4)

    # ---- 1. Variable & Constant -------------------------------------
    d.h2("1. Variable aur Constant")
    d.exam_tag()
    d.label_body("Variable:", "Badalne wala (unknown) number, jaise x, y, z.")
    d.label_body("Constant:", "Fixed number jiski value nahi badalti, jaise 5, -3, 1/2.")
    d.bullet("Example: 4x + 7 me 'x' variable hai aur '7' constant hai.")
    d.space(6)

    # ---- 2. Power / Exponent ----------------------------------------
    d.h2("2. Power / Exponent")
    d.exam_tag()
    d.label_body("Matlab:", "Power batata hai ki number ko kitni baar khud se multiply "
                 "karna hai.")
    d.bullet("x^2 = x times x  (ise 'x square' bolte hain).")
    d.bullet("x^3 = x times x times x  (ise 'x cube' bolte hain).")
    d.bullet("Koi bhi number ki power 0 ho to value 1 hoti hai (x^0 = 1).")
    d.space(6)

    # ---- 3. Polynomial kya hai --------------------------------------
    d.h2("3. Polynomial Kya Hai?")
    d.exam_tag()
    d.label_body("Definition:", "Aisa expression jisme variable ke power SIRF whole "
                 "numbers (0, 1, 2, 3...) hon - negative ya fraction power nahi.")
    d.label_body("Polynomial Hai:", "2x + 3,   x^2 - 5x + 6,   7")
    d.label_body("Polynomial Nahi:", "x^(-1) + 2,   sqrt(x) + 1   (in me galat power hai)")
    d.space(6)

    # ---- 4. Degree --------------------------------------------------
    d.h2("4. Degree")
    d.exam_tag()
    d.label_body("Definition:", "Polynomial ka sabse bada power hi uska degree hota hai.")
    d.bullet("2x + 5  ->  degree 1")
    d.bullet("x^2 - 3x + 1  ->  degree 2")
    d.bullet("5x^3 - 2x  ->  degree 3")
    d.space(6)

    # ---- 5. Types (by degree) ---------------------------------------
    d.h2("5. Types (Degree ke Hisaab se)")
    d.bullet("Degree 0 = CONSTANT polynomial  (jaise 7)")
    d.bullet("Degree 1 = LINEAR     :  ax + b")
    d.bullet("Degree 2 = QUADRATIC  :  ax^2 + bx + c")
    d.bullet("Degree 3 = CUBIC      :  ax^3 + bx^2 + cx + d")
    d.bullet("(In sab me 'a' hamesha != 0 hona chahiye.)")
    d.label_body("Terms ke hisaab se:", "")
    d.bullet("Monomial = 1 term (3x),  Binomial = 2 terms (x + 2),  "
             "Trinomial = 3 terms (x^2 + 2x + 1).")
    d.space(6)

    # ---- 6. Coefficient ---------------------------------------------
    d.h2("6. Coefficient")
    d.exam_tag()
    d.label_body("Definition:", "Variable ke aage wala number hi coefficient hota hai.")
    d.label_body("Example:", "3x^2 - 5x + 7 me:")
    d.bullet("x^2 ka coefficient (a) = 3")
    d.bullet("x ka coefficient (b) = -5")
    d.bullet("constant (c) = 7")
    d.space(6)

    # ---- 7. p(x) Notation & Substitution ----------------------------
    d.h2("7. p(x) Notation aur Substitution")
    d.label_body("p(x):", "Polynomial ka naam (jaise function).")
    d.label_body("p(2):", "x ki jagah 2 daal kar value nikalna.")
    d.bullet("Example: p(x) = x^2 - 4  ->  p(2) = 2^2 - 4 = 0.")
    d.space(6)

    # ---- 8. Zero / Root ---------------------------------------------
    d.h2("8. Zero / Root of Polynomial")
    d.exam_tag()
    d.label_body("Definition:", "Wo value of x jiske liye p(x) = 0 ho jaye, usi ko "
                 "polynomial ka ZERO (ya root) kehte hain.")
    d.bullet("Example: p(x) = 2x - 6  ->  2x - 6 = 0  ->  x = 3. So zero = 3.")
    d.bullet("Graph jahan x-axis ko cut kare, wahi zero hota hai.")
    d.bullet("Linear ka 1 zero, Quadratic ke 2 zeros, Cubic ke 3 zeros (maximum).")
    d.space(6)

    # ---- 9. Factorisation -------------------------------------------
    d.h2("9. Factorisation (Splitting the Middle Term)")
    d.exam_tag()
    d.label_body("Idea:", "ax^2 + bx + c ko (..)(..) ke product me todna.")
    d.bullet("Middle term 'b' ko aise 2 numbers p, q me todo jahan:")
    d.bullet("p + q = b   AND   p x q = a x c.")
    d.bullet("Example: x^2 + 5x + 6 -> p+q=5, pxq=6 -> 2,3 -> (x+2)(x+3).")
    d.space(6)

    # ---- 10. Graph Basics -------------------------------------------
    d.h2("10. Graph Basics")
    d.exam_tag()
    d.bullet("X-axis = leti (horizontal) line,  Y-axis = khadi (vertical) line.")
    d.bullet("Linear polynomial ka graph = seedhi line.")
    d.bullet("Quadratic ka graph = 'U' ya ulta 'U' (ise PARABOLA kehte hain).")
    d.bullet("Graph jahan x-axis ko touch/cut kare = wahi zero hota hai.")
    d.space(6)

    # ---- Quick Revision ---------------------------------------------
    d.h2("Quick Revision")
    d.box_note([
        "Degree = sabse bada power.",
        "Coefficient = variable ke aage ka number.",
        "Zero = jahan p(x) = 0  (graph x-axis ko cut kare).",
        "Split middle term: p + q = b  AND  p x q = a x c.",
        "Linear -> line,  Quadratic -> parabola.",
    ])
    d.space(6)

    # ---- Solved Examples --------------------------------------------
    d.h2("Solved Examples - Samjho Kaise Solve Karte Hain")
    d.body("Neeche 10 examples step-by-step solve karke dikhaye gaye hain.", color=GREY)
    d.space(3)

    examples = [
        ("Example 1:  3x^4 - 2x^2 + 7 ka degree?",
         ["Saare terms ke power dekho: 4, 2, 0.",
          "Sabse bada power = 4."],
         "Degree = 4"),
        ("Example 2:  Kya sqrt(x) + 2 polynomial hai?",
         ["sqrt(x) = x^(1/2), yani power 1/2 (fraction).",
          "Polynomial me fraction power allowed nahi."],
         "Nahi"),
        ("Example 3:  5x^2 - 3x + 8 me x ka coefficient?",
         ["x (yani x^1) ke aage wala number dekho.",
          "Wo -3 hai (minus ke saath)."],
         "-3"),
        ("Example 4:  p(x) = x^2 - 4, to p(3) = ?",
         ["x ki jagah 3 daal do: 3^2 - 4.",
          "= 9 - 4."],
         "5"),
        ("Example 5:  p(x) = 2x - 6 ka zero?",
         ["Zero ke liye p(x) = 0 rakho: 2x - 6 = 0.",
          "2x = 6  ->  x = 3."],
         "Zero = 3"),
        ("Example 6:  4x^3 + 2x - 1 ko classify karo.",
         ["Sabse bada power = 3.",
          "Degree 3 wale polynomial ko CUBIC kehte hain."],
         "Cubic"),
        ("Example 7:  x^2 + 5x + 6 ko factorise karo.",
         ["Yahan a=1, b=5, c=6. a x c = 6.",
          "p+q = 5 aur p x q = 6 -> p=2, q=3.",
          "x^2 + 2x + 3x + 6 = x(x+2) + 3(x+2)."],
         "(x + 2)(x + 3)"),
        ("Example 8:  x^2 - 5x + 6 ke zeros?",
         ["Factorise: (x-2)(x-3) = 0.",
          "x - 2 = 0 -> x = 2;  x - 3 = 0 -> x = 3."],
         "Zeros = 2 aur 3"),
        ("Example 9:  Kya 7 polynomial hai? Iska degree?",
         ["7 ko 7x^0 likh sakte hain (power 0).",
          "Ye ek constant polynomial hai."],
         "Haan, degree = 0"),
        ("Example 10:  x^2 - 9 ko factorise karo.",
         ["Ye a^2 - b^2 form hai: x^2 - 3^2.",
          "Rule: a^2 - b^2 = (a - b)(a + b)."],
         "(x - 3)(x + 3)"),
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
        "5x^3 - 2x + 1 ka degree kya hai?",
        "3x^2 - 7x + 2 me x^2 ka coefficient kya hai?",
        "4x + 9 me constant kya hai?",
        "Kya x^(-2) + 3 ek polynomial hai?",
        "p(x) = x^2 + 1, to p(0) = ?",
        "p(x) = 2x - 8 ka zero kya hai?",
        "ax^2 + bx + c kis type ka polynomial hai?",
        "6x ka degree kya hai?",
        "9 (sirf constant) ka degree kya hai?",
        "x^2 - 9 ko factorise karo.",
        "Quadratic polynomial me maximum kitne zeros hote hain?",
        "x^2 + 7x + 12 ko factorise karo.",
        "Linear polynomial ka graph kaisa hota hai?",
        "Quadratic polynomial ka graph kya kehlata hai?",
        "p(x) = x^2 - 3x + 2, to p(1) = ?",
        "5x^3 - 2x^2 me x^3 ka coefficient kya hai?",
        "Monomial, Binomial aur Trinomial kya hote hain?",
        "x^2 - 5x + 6 ke zeros kya hain?",
        "Splitting middle term me kaunsi 2 conditions chahiye?",
        "Graph jahan x-axis ko cut kare, wo kya hota hai?",
    ]
    for i, q in enumerate(questions, start=1):
        d.label_body(f"Q{i}.", q)
        d.space(2)

    # ---- Step-by-Step Solutions -------------------------------------
    d.h2("Step-by-Step Solutions")
    solutions = [
        ("5x^3 - 2x + 1 ka degree?",
         ["Sabse bada power dhoondo: 3, 1, 0.", "Sabse bada = 3."], "3"),
        ("3x^2 - 7x + 2 me x^2 ka coefficient?",
         ["x^2 ke aage wala number = 3."], "3"),
        ("4x + 9 me constant?",
         ["Bina variable wala number = 9."], "9"),
        ("Kya x^(-2) + 3 polynomial hai?",
         ["Power -2 (negative) hai, jo allowed nahi."], "Nahi"),
        ("p(x) = x^2 + 1, p(0)?",
         ["x ki jagah 0: 0^2 + 1 = 0 + 1."], "1"),
        ("p(x) = 2x - 8 ka zero?",
         ["2x - 8 = 0 -> 2x = 8 -> x = 4."], "4"),
        ("ax^2 + bx + c kis type ka?",
         ["Sabse bada power 2 hai."], "Quadratic"),
        ("6x ka degree?",
         ["6x = 6x^1, power = 1."], "1"),
        ("9 ka degree?",
         ["9 = 9x^0, power = 0."], "0"),
        ("x^2 - 9 factorise?",
         ["x^2 - 3^2 form hai.", "a^2 - b^2 = (a-b)(a+b)."], "(x-3)(x+3)"),
        ("Quadratic me max zeros?",
         ["Degree 2 -> maximum 2 zeros."], "2"),
        ("x^2 + 7x + 12 factorise?",
         ["a x c = 12, p+q=7, pxq=12 -> 3,4.", "(x+3)(x+4)."], "(x+3)(x+4)"),
        ("Linear ka graph?",
         ["Degree 1 ka graph seedhi line hoti hai."], "Seedhi (straight) line"),
        ("Quadratic ka graph?",
         ["Degree 2 ka graph U ya ulta U hota hai."], "Parabola"),
        ("p(x) = x^2 - 3x + 2, p(1)?",
         ["x=1: 1 - 3 + 2 = 0."], "0"),
        ("5x^3 - 2x^2 me x^3 ka coefficient?",
         ["x^3 ke aage = 5."], "5"),
        ("Monomial / Binomial / Trinomial?",
         ["Terms ki ginti se: 1, 2, aur 3 terms."],
         "1 term, 2 terms, 3 terms"),
        ("x^2 - 5x + 6 ke zeros?",
         ["Factorise: (x-2)(x-3) = 0.", "x = 2 ya x = 3."], "2 aur 3"),
        ("Splitting middle term ki 2 conditions?",
         ["Do numbers p, q chahiye."], "p + q = b  AND  p x q = a x c"),
        ("Graph jahan x-axis ko cut kare wo?",
         ["Us point par p(x) = 0 hota hai."], "Zero (root)"),
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
    out_file = "Polynomials_Notes.pdf"
    pages = write_pdf(doc, out_file)
    print(f"Generated '{out_file}' with {pages} page(s).")
