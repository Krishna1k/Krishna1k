#!/usr/bin/env python3
"""
HCF & LCM study-notes PDF.
Reuses the pure-Python PDF engine defined in numbers_notes.py
(no external libraries required).
"""

from numbers_notes import (
    PDFBuilder, write_pdf,
    LEFT, RIGHT, PAGE_W, NAVY, GREY,
)


def build_document():
    d = PDFBuilder()

    # ---- Title -------------------------------------------------------
    d.title("HCF and LCM")
    d.subtitle("Simple Notes, Methods, Examples & Q\\&A")
    d.hline(LEFT, PAGE_W - RIGHT, d.y + 4, NAVY, 1.2)
    d.space(10)
    d.body("HCF and LCM are two important ideas based on the factors and multiples of "
           "numbers. This guide explains both in simple words with examples, the main "
           "methods to find them, their relationship, and a set of solved questions.",
           color=GREY)
    d.space(6)

    # ---- Quick recap -------------------------------------------------
    d.h2("1. Quick Recap: Factors & Multiples")
    d.label_body("Factor:", "A number that divides another number exactly (no remainder). "
                 "Factors of 12 = 1, 2, 3, 4, 6, 12.")
    d.label_body("Multiple:", "The result of multiplying a number by 1, 2, 3, ... "
                 "Multiples of 4 = 4, 8, 12, 16, 20 ...")
    d.space(6)

    # ---- HCF ---------------------------------------------------------
    d.h2("2. HCF (Highest Common Factor)")
    d.label_body("Definition:", "The largest number that divides two or more numbers "
                 "exactly. It is also called GCD (Greatest Common Divisor).")
    d.label_body("Example:", "HCF of 12 and 18:")
    d.bullet("12 = 2 x 2 x 3")
    d.bullet("18 = 2 x 3 x 3")
    d.bullet("Common factors = 2 x 3 = 6, so HCF = 6")
    d.label_body("Notes:", "")
    d.bullet("HCF is always less than or equal to the smallest number.")
    d.bullet("HCF of two co-prime numbers (like 8 and 9) is 1.")
    d.space(6)

    # ---- LCM ---------------------------------------------------------
    d.h2("3. LCM (Least Common Multiple)")
    d.label_body("Definition:", "The smallest number that is exactly divisible by two "
                 "or more numbers (the smallest common multiple).")
    d.label_body("Example:", "LCM of 4 and 6:")
    d.bullet("Multiples of 4 = 4, 8, 12, 16, 20 ...")
    d.bullet("Multiples of 6 = 6, 12, 18, 24 ...")
    d.bullet("Smallest common multiple = 12, so LCM = 12")
    d.label_body("Notes:", "")
    d.bullet("LCM is always greater than or equal to the largest number.")
    d.space(6)

    # ---- Methods -----------------------------------------------------
    d.h2("4. Methods to Find HCF & LCM")
    d.label_body("(a) Prime Factorisation:", "Write each number as a product of primes.")
    d.bullet("HCF = product of the COMMON prime factors (lowest powers).")
    d.bullet("LCM = product of ALL prime factors (highest powers).")
    d.bullet("Example: 12 = 2^2 x 3 and 18 = 2 x 3^2  ->  HCF = 2 x 3 = 6, "
             "LCM = 2^2 x 3^2 = 36")
    d.label_body("(b) Division Method (for HCF):", "Divide the bigger number by the "
                 "smaller, then divide the divisor by the remainder, and repeat until "
                 "the remainder is 0. The last divisor is the HCF.")
    d.label_body("(c) Common Division (for LCM):", "Divide all numbers together by common "
                 "prime numbers step by step, then multiply all the divisors.")
    d.space(6)

    # ---- Relationship ------------------------------------------------
    d.h2("5. Relationship Between HCF and LCM")
    d.body("For any two numbers, this rule is always true:", color=GREY)
    d.space(2)
    d.box_note([
        "HCF x LCM = First number x Second number",
        "",
        "Example for 12 and 18:",
        "HCF x LCM = 6 x 36 = 216   and   12 x 18 = 216   (both equal)",
    ])
    d.space(6)

    # ---- Difference -------------------------------------------------
    d.h2("6. HCF vs LCM (Key Difference)")
    d.bullet("HCF deals with FACTORS; LCM deals with MULTIPLES.")
    d.bullet("HCF is the GREATEST common factor; LCM is the LEAST common multiple.")
    d.bullet("HCF <= smallest number; LCM >= largest number.")
    d.space(6)

    # ---- Q&A ---------------------------------------------------------
    d.h2("7. Questions & Answers")

    qa = [
        ("Q1.", "Find the HCF of 12 and 18.",
         "Ans: 6   (common factors 2 x 3)"),
        ("Q2.", "Find the LCM of 4 and 6.",
         "Ans: 12   (smallest common multiple)"),
        ("Q3.", "Find the HCF of 24 and 36.",
         "Ans: 12   (24 = 2^3 x 3, 36 = 2^2 x 3^2, common = 2^2 x 3 = 12)"),
        ("Q4.", "Find the LCM of 8 and 12.",
         "Ans: 24   (8 = 2^3, 12 = 2^2 x 3, LCM = 2^3 x 3 = 24)"),
        ("Q5.", "The HCF of two numbers is 6 and their LCM is 36. If one number is 12, "
                "find the other.",
         "Ans: (HCF x LCM) / 12 = (6 x 36) / 12 = 216 / 12 = 18"),
        ("Q6.", "Find the LCM of 5, 10 and 15.",
         "Ans: 30"),
        ("Q7.", "Find the HCF of 16 and 24.",
         "Ans: 8"),
        ("Q8.", "Two bells ring at intervals of 6 and 8 minutes. After how many minutes "
                "will they ring together?",
         "Ans: LCM(6, 8) = 24 minutes."),
        ("Q9.", "Find the greatest number that divides both 20 and 25 exactly.",
         "Ans: HCF(20, 25) = 5"),
        ("Q10.", "Find the LCM of 9 and 12.",
         "Ans: 36   (9 = 3^2, 12 = 2^2 x 3, LCM = 2^2 x 3^2 = 36)"),
    ]

    for label, q, a in qa:
        d.label_body(label, q)
        d.bullet(a)
        d.space(3)

    # ---- Tip box -----------------------------------------------------
    d.space(2)
    d.box_note([
        "Memory tip: HCF -> Highest common Factor -> small answer (a factor).",
        "LCM -> Least common Multiple -> big answer (a multiple).",
    ])

    return d


if __name__ == "__main__":
    doc = build_document()
    out_file = "HCF_and_LCM_Notes.pdf"
    pages = write_pdf(doc, out_file)
    print(f"Generated '{out_file}' with {pages} page(s).")
