#!/usr/bin/env python3
"""
Square Roots study-notes PDF.
Reuses the pure-Python PDF engine defined in numbers_notes.py
(no external libraries required).
"""

from numbers_notes import (
    PDFBuilder, write_pdf,
    LEFT, RIGHT, PAGE_W, NAVY, ACCENT, GREY, BLACK,
)


def build_document():
    d = PDFBuilder()

    # ---- Title -------------------------------------------------------
    d.title("Square Roots")
    d.subtitle("Simple Notes, Examples, Methods & Q\\&A (100 - 200)")
    d.hline(LEFT, PAGE_W - RIGHT, d.y + 4, NAVY, 1.2)
    d.space(10)
    d.body("A square root is the reverse of squaring a number. This guide explains the "
           "idea in simple words with examples, the main methods to find square roots, "
           "and ends with a set of solved questions for numbers between 100 and 200.",
           color=GREY)
    d.space(6)

    # ---- What is a square root --------------------------------------
    d.h2("1. What is a Square Root?")
    d.label_body("Definition:", "The square root of a number is the value which, when "
                 "multiplied by itself, gives that number. It is the opposite (inverse) "
                 "of squaring.")
    d.label_body("Symbol:", "The radical sign  sqrt( )  is used. Example: sqrt(25).")
    d.label_body("Examples:", "")
    d.bullet("sqrt(25) = 5   because 5 x 5 = 25")
    d.bullet("sqrt(81) = 9   because 9 x 9 = 81")
    d.bullet("Squaring:  6 x 6 = 36   ->   Square root:  sqrt(36) = 6")
    d.space(6)

    # ---- Perfect squares --------------------------------------------
    d.h2("2. Perfect Squares")
    d.label_body("Definition:", "A perfect square is a number whose square root is a "
                 "whole number.")
    d.label_body("Examples:", "1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144 ...")
    d.label_body("Notes:", "")
    d.bullet("Square roots of perfect squares are exact whole numbers.")
    d.bullet("Numbers like 2, 3, 5, 7 are NOT perfect squares; their roots are "
             "non-ending decimals (irrational), e.g. sqrt(2) = 1.414...")
    d.bullet("A perfect square never ends in 2, 3, 7 or 8.")
    d.space(6)

    # ---- Methods -----------------------------------------------------
    d.h2("3. Methods to Find a Square Root")
    d.label_body("(a) Prime Factorisation:", "Break the number into prime factors, make "
                 "pairs, and take one factor from each pair.")
    d.bullet("Example: 144 = 2x2 x 2x2 x 3x3  ->  take 2 x 2 x 3 = 12, so sqrt(144) = 12")
    d.label_body("(b) Long Division:", "Used for large numbers and non-perfect squares "
                 "to get the answer step by step (even in decimals).")
    d.label_body("(c) Estimation:", "Find the two nearest perfect squares to guess the "
                 "approximate value.")
    d.bullet("Example: sqrt(150) lies between sqrt(144)=12 and sqrt(169)=13, so it is "
             "about 12.2")
    d.space(6)

    # ---- Properties --------------------------------------------------
    d.h2("4. Useful Properties")
    d.bullet("sqrt(a x b) = sqrt(a) x sqrt(b)")
    d.bullet("sqrt(a / b) = sqrt(a) / sqrt(b)")
    d.bullet("sqrt(0) = 0  and  sqrt(1) = 1")
    d.bullet("A negative number has no real square root.")
    d.space(6)

    # ---- Perfect squares between 100 and 200 ------------------------
    d.h2("5. Perfect Squares Between 100 and 200")
    d.body("There are only five perfect squares in this range:", color=GREY)
    d.space(2)
    d.box_note([
        "sqrt(100) = 10        (10 x 10 = 100)",
        "sqrt(121) = 11        (11 x 11 = 121)",
        "sqrt(144) = 12        (12 x 12 = 144)",
        "sqrt(169) = 13        (13 x 13 = 169)",
        "sqrt(196) = 14        (14 x 14 = 196)",
    ])
    d.space(6)

    # ---- Q&A ---------------------------------------------------------
    d.h2("6. Questions & Answers (100 - 200)")

    qa = [
        ("Q1.", "What is sqrt(100)?",
         "Ans: 10   (because 10 x 10 = 100)"),
        ("Q2.", "What is sqrt(121)?",
         "Ans: 11   (because 11 x 11 = 121)"),
        ("Q3.", "What is sqrt(144)?",
         "Ans: 12   (because 12 x 12 = 144)"),
        ("Q4.", "What is sqrt(169)?",
         "Ans: 13   (because 13 x 13 = 169)"),
        ("Q5.", "What is sqrt(196)?",
         "Ans: 14   (because 14 x 14 = 196)"),
        ("Q6.", "Which numbers between 100 and 200 are perfect squares?",
         "Ans: 100, 121, 144, 169 and 196."),
        ("Q7.", "Is 150 a perfect square?",
         "Ans: No. sqrt(150) is about 12.25, which is not a whole number."),
        ("Q8.", "Between which two whole numbers does sqrt(180) lie?",
         "Ans: Between 13 and 14 (since 13x13 = 169 and 14x14 = 196)."),
        ("Q9.", "Find the value of sqrt(169) + sqrt(144).",
         "Ans: 13 + 12 = 25."),
        ("Q10.", "A square park has an area of 196 square metres. Find the length of "
                 "one side.",
         "Ans: Side = sqrt(196) = 14 metres."),
    ]

    for label, q, a in qa:
        d.label_body(label, q)
        d.bullet(a)
        d.space(3)

    # ---- Tip box -----------------------------------------------------
    d.space(2)
    d.box_note([
        "Quick tip: To check if a number is a perfect square, find its square root.",
        "If the root is a whole number, it is a perfect square; otherwise it is not.",
    ])

    return d


if __name__ == "__main__":
    doc = build_document()
    out_file = "Square_Roots_Notes.pdf"
    pages = write_pdf(doc, out_file)
    print(f"Generated '{out_file}' with {pages} page(s).")
