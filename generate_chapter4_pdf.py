"""
PDF generator for Class 10 Maths Chapter 4: Quadratic Equations.
Uses shared pdf_utils.py.
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 4: QUADRATIC EQUATIONS
==========================================

A simplified, detailed guide in Hinglish
For students who missed Class 7-8-9
Based on the official NCERT English Medium textbook
==========================================


==========================================
SECTION 1: FOUNDATION
==========================================


1.1 POLYNOMIAL REVISION (Chapter 2 se)
--------------------------------------

   Yaad hai? Polynomial = variable + power = whole no.
     - Linear:    ax + b           (degree 1)
     - QUADRATIC: ax^2 + bx + c    (degree 2)  <- ye chapter
     - Cubic:     ax^3 + ...       (degree 3)


1.2 EQUATION VS EXPRESSION
--------------------------

   - Expression: 2x^2 + 3x - 5      (sirf likha hua)
   - Equation:   2x^2 + 3x - 5 = 0  ('=' sign hai)


1.3 QUADRATIC EQUATION KYA HAI?
-------------------------------

   DEFINITION: Wo equation jiska standard form:

        ax^2 + bx + c = 0

   jahan a, b, c real numbers AND a != 0.

   IMPORTANT: a != 0 warna linear ban jayegi.


   QUADRATIC EXAMPLES:
     - x^2 - 5x + 6 = 0    (a=1, b=-5, c=6)
     - 2x^2 + 7x = 0       (a=2, b=7,  c=0)
     - 3x^2 - 12 = 0       (a=3, b=0,  c=-12)


   NOT QUADRATIC:
     - 2x + 5 = 0          (no x^2)
     - x^3 + 2x + 1 = 0    (degree 3)
     - x^2 + 1/x = 5       (1/x = x^-1, negative power)


1.4 ROOTS OF A QUADRATIC EQUATION
---------------------------------

   ROOT = value of x jiske liye LHS = RHS = 0.

   Quadratic equation ke 2 roots hote hain (max).


   EXAMPLE: x^2 - 5x + 6 = 0
     Check x = 2: 4 - 10 + 6 = 0  (ok)
     Check x = 3: 9 - 15 + 6 = 0  (ok)

   So roots are 2 and 3.


==========================================
SECTION 2: FACTORISATION METHOD
==========================================


2.1 IDEA
--------

   Quadratic ko (x - p)(x - q) = 0 form mein todo.
   Phir:
     Either x - p = 0  ->  x = p
     Or     x - q = 0  ->  x = q


   LOGIC: Agar do cheezon ka product 0 hai, toh
   kam-se-kam ek toh 0 hi hogi.


2.2 SPLITTING MIDDLE TERM
-------------------------

   ax^2 + bx + c = 0 mein:
     Middle coefficient b ko aise 2 nos. p, q mein todo
     ki:
        p + q = b      AND
        p x q = a x c


   EXAMPLE 1: x^2 + 7x + 12 = 0

   a=1, b=7, c=12, so a x c = 12.
   Find p, q with p + q = 7, p x q = 12.

   Try: 3 and 4   ->  3+4=7, 3x4=12  (ok)

     x^2 + 7x + 12 = 0
     x^2 + 3x + 4x + 12 = 0
     x(x + 3) + 4(x + 3) = 0
     (x + 3)(x + 4) = 0

   So x = -3 or x = -4.


   EXAMPLE 2: 2x^2 - 5x + 3 = 0

   a=2, b=-5, c=3, a x c = 6.
   Find p, q with p + q = -5, p x q = 6.

   Try: -2 and -3  ->  -5, 6  (ok)

     2x^2 - 2x - 3x + 3 = 0
     2x(x - 1) - 3(x - 1) = 0
     (x - 1)(2x - 3) = 0

   So x = 1 or x = 3/2.


   EXAMPLE 3: 6x^2 - x - 2 = 0

   a=6, b=-1, c=-2, a x c = -12.
   p + q = -1, p x q = -12.

   Try: -4 and 3  ->  -1, -12  (ok)

     6x^2 - 4x + 3x - 2 = 0
     2x(3x - 2) + 1(3x - 2) = 0
     (3x - 2)(2x + 1) = 0

   So x = 2/3 or x = -1/2.


==========================================
SECTION 3: QUADRATIC FORMULA
==========================================


3.1 THE MAGIC FORMULA (YAAD RAKH)
---------------------------------

   For ax^2 + bx + c = 0:

              -b +/- sqrt(b^2 - 4ac)
        x  = -------------------------
                       2a


   Ye formula HAR quadratic pe kaam karta hai.


3.2 DISCRIMINANT D KA KAMAAL
----------------------------

   D = b^2 - 4ac

   D ki value se roots ka nature pata chalta hai:

   D ki value      Roots
   ----------      ---------------------------------
   D > 0           Two DISTINCT REAL roots
   D = 0           Two EQUAL real roots (repeated)
   D < 0           NO REAL roots (imaginary)


3.3 EXAMPLES
------------

   EXAMPLE 4: 2x^2 - 7x + 3 = 0

   a=2, b=-7, c=3
   D = 49 - 24 = 25  (>0, distinct real)

     x = (7 +/- sqrt(25)) / 4
     x = (7 +/- 5) / 4

   So x = 3 or x = 1/2.


   EXAMPLE 5: x^2 - 6x + 9 = 0

   a=1, b=-6, c=9
   D = 36 - 36 = 0  (equal roots)

     x = (6 +/- 0) / 2 = 3

   So x = 3 (repeated).


   EXAMPLE 6: x^2 + x + 1 = 0

   a=1, b=1, c=1
   D = 1 - 4 = -3  (<0)

   So NO real roots.


==========================================
SECTION 4: WORD PROBLEMS
==========================================


   EXAMPLE 7: Number problem

   "Ek number aur uska reciprocal ka sum 10/3 hai.
    Number nikaalo."

   Let number = x.
     x + 1/x = 10/3

   Multiply by 3x:
     3x^2 + 3 = 10x
     3x^2 - 10x + 3 = 0

   Splitting (a x c = 9, sum = -10):
     p = -9, q = -1
     3x^2 - 9x - x + 3 = 0
     3x(x - 3) - 1(x - 3) = 0
     (x - 3)(3x - 1) = 0

   So x = 3 or x = 1/3.
   (Dono valid - reciprocals of each other)


   EXAMPLE 8: Speed problem

   "Ek train 360 km fixed speed se cover karti hai.
    Agar speed 5 km/h zyada hoti, toh time 1 hour
    kam lagta. Original speed?"

   Let original speed = x km/h.
   Original time = 360/x
   New time = 360/(x+5)

   Equation:
     360/x - 360/(x+5) = 1

   Multiply by x(x+5):
     360(x+5) - 360x = x(x+5)
     1800 = x^2 + 5x
     x^2 + 5x - 1800 = 0

   Splitting (a x c = -1800, sum = 5):
     45 x (-40) = -1800, sum = 5  (ok)
     (x + 45)(x - 40) = 0

   x = -45 (rejected, speed +ve)
   x = 40 km/h  (Answer)


==========================================
Q AND A TIME
==========================================


   Q1. Inn mein se konsi QUADRATIC equation hai?
       (a) x^2 + 5 = 0
       (b) 2x + 3 = 0
       (c) x^3 - 1 = 0
       (d) 5x^2 - 7x + 1 = 0


   Q2. x^2 - 3x - 10 = 0 ko factorisation se solve kar.


   Q3. 2x^2 + x - 6 = 0 ko quadratic formula se solve kar.


   Q4. Discriminant nikaal aur roots ka nature bata:
       (a) x^2 + 4x + 4 = 0
       (b) 2x^2 - 3x + 5 = 0
       (c) x^2 - 5x + 4 = 0


   Q5. Word problem: "Do consecutive odd positive integers
       ka product 143 hai. Numbers nikaalo."


==========================================
SUMMARY
==========================================


   1. Quadratic equation:  ax^2 + bx + c = 0  (a != 0)

   2. Roots: Maximum 2 hote hain

   3. Methods:
        - FACTORISATION (splitting middle term)
        - QUADRATIC FORMULA: x = (-b +/- sqrt(D)) / 2a

   4. Discriminant D = b^2 - 4ac:
        - D > 0  ->  distinct real roots
        - D = 0  ->  equal roots
        - D < 0  ->  no real roots

   5. Word problems:
        Variable le -> equation banao -> solve ->
        impossible solutions reject karo.


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 4: Quadratic Equations
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch4_Quadratic_Equations.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 4: Quadratic Equations",
        content=CONTENT,
        out_path=out,
    )
