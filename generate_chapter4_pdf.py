"""
PDF generator for Class 10 Maths Chapter 4: Quadratic Equations
(Core-Basics edition). RED core basics, GREEN exam marks,
8 solved examples (hardest -> easiest). Hinglish.
Uses shared pdf_utils.py (red '@@', green '$$', page breaks).
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 4: QUADRATIC EQUATIONS
==========================================

A simplified, detailed guide in Hinglish
Special edition for students who skipped Class 7-8-9
==========================================

   IS PDF MEIN RANG KA MATLAB:
@@ RED text = core basic / prerequisite (Class 7-8-9 ka).
$$ GREEN text = exam mein BAAR-BAAR aata hai (zaroor yaad rakh).
   (Aur black = normal explanation.)

<<<PAGEBREAK>>>

==========================================
@@ CORE BASICS - MISS MAT KARNA (RED PAGE)
==========================================

@@ 1) POWER / SQUARE
@@    x^2 = x times x. x^2 ko "x square" bolte hain.


@@ 2) EQUATION VS EXPRESSION
@@    Expression: 2x^2 + 3x - 5 (sirf likha).
@@    Equation: 2x^2 + 3x - 5 = 0 ('=' sign hai).


@@ 3) DEGREE
@@    Degree = sabse bada power. x^2 wala = degree 2.


@@ 4) COEFFICIENT (a, b, c)
@@    ax^2 + bx + c mein a = x^2 ka, b = x ka, c = constant.
@@    3x^2 - 5x + 2 -> a=3, b=-5, c=2.


@@ 5) ROOT / ZERO / SOLUTION
@@    Root = woh x jiske liye equation 0 ho jaye.
@@    (Quadratic ke max 2 roots hote hain.)


@@ 6) FACTORISATION (splitting middle term)
@@    ax^2+bx+c ko (..)(..) mein todo.
@@    Middle term b ko p,q mein todo: p+q=b, p x q = a x c.


@@ 7) SQUARE ROOT (sqrt)
@@    sqrt(25)=5 kyunki 5x5=25. Power ka ulta.
@@    sqrt(D) ka matlab D ka square root.


@@ 8) ZERO PRODUCT RULE
@@    Agar A x B = 0, toh ya A=0 ya B=0 (ya dono).
@@    Yahi factorisation method ka base hai.


@@ 9) PLUS-MINUS (+/-)
@@    Quadratic formula mein +/- ka matlab DO answers:
@@    ek + wala, ek - wala.

<<<PAGEBREAK>>>

==========================================
NOW: ASLI CHAPTER 4 SHURU
==========================================


TOPIC 1: QUADRATIC EQUATION KYA HAI?
------------------------------------

   Standard form: a x^2 + b x + c = 0  (a != 0).
   Degree 2 ki equation. Max 2 roots.

   Quadratic: x^2-5x+6=0, 2x^2+7x=0.
   Not: 2x+5=0 (no x^2), x^3+1=0 (degree 3).


TOPIC 2: SOLVE BY FACTORISATION
-------------------------------

$$ EXAM ALERT: Factorisation se solve karna pakka aata hai.

   Steps: middle term todo (p+q=b, pq=ac), factor banao,
   phir har factor = 0 karke x nikaalo.

   EXAMPLE: x^2 + 7x + 12 = 0
     p+q=7, pq=12 -> 3 aur 4
     x^2+3x+4x+12 = 0 -> (x+3)(x+4)=0
     x = -3 ya x = -4


TOPIC 3: QUADRATIC FORMULA
--------------------------

$$ EXAM ALERT: Formula har quadratic pe chalta hai. Ratta maar:

$$   x = ( -b +/- sqrt(b^2 - 4ac) ) / (2a)

   Yahan b^2 - 4ac ko DISCRIMINANT (D) kehte hain.


TOPIC 4: DISCRIMINANT (D = b^2 - 4ac)
-------------------------------------

$$ EXAM ALERT: D se roots ka NATURE batana aata hai:

$$   D > 0  -> 2 distinct real roots
$$   D = 0  -> 2 equal real roots (repeated)
$$   D < 0  -> no real roots

<<<PAGEBREAK>>>

==========================================
SOLVED EXAMPLES: HARDEST -> EASIEST
==========================================

$$ 8 examples poori tarah solve karke. Upar HARDEST,
$$ neeche EASIEST.


   ------------------------------------------------
   Solved Example 1 (HARDEST) - Speed word problem
   ------------------------------------------------
$$ (Exam favourite)

   Ek train 360 km fixed speed se chalti hai. Speed 5 km/h
   zyada hoti toh 1 ghanta kam lagta. Original speed?

   Let speed = x km/h.
     360/x - 360/(x+5) = 1
   Multiply by x(x+5):
     360(x+5) - 360x = x(x+5)
     1800 = x^2 + 5x
     x^2 + 5x - 1800 = 0
   Split (ac=-1800, sum=5 -> 45, -40):
     (x+45)(x-40) = 0
     x = -45 (reject) ya x = 40

   Original speed = 40 km/h.


   ------------------------------------------------
   Solved Example 2 - Number (reciprocal) problem
   ------------------------------------------------
$$ (Exam favourite)

   Ek number aur uske reciprocal ka sum 10/3 hai. Number?

   Let number = x.
     x + 1/x = 10/3
   Multiply by 3x:
     3x^2 + 3 = 10x -> 3x^2 - 10x + 3 = 0
   Split (ac=9, sum=-10 -> -9,-1):
     3x^2 - 9x - x + 3 = 0 -> (x-3)(3x-1)=0
     x = 3 ya x = 1/3.


   ------------------------------------------------
   Solved Example 3 - Consecutive integers
   ------------------------------------------------

   Do consecutive odd positive integers ka product 143.
   Numbers?

   Let numbers = x aur (x+2).
     x(x+2) = 143 -> x^2 + 2x - 143 = 0
   Split (ac=-143, sum=2 -> 13,-11):
     (x+13)(x-11) = 0 -> x = 11 (positive)
   Numbers = 11 aur 13.


   ------------------------------------------------
   Solved Example 4 - Quadratic formula
   ------------------------------------------------

   2x^2 - 7x + 3 = 0. (a=2, b=-7, c=3)
     D = (-7)^2 - 4(2)(3) = 49 - 24 = 25
     x = (7 +/- sqrt(25)) / 4 = (7 +/- 5)/4
     x = 3 ya x = 1/2.


   ------------------------------------------------
   Solved Example 5 - Nature of roots (D)
   ------------------------------------------------
$$ (Exam favourite)

   (a) x^2 + 4x + 4 = 0: D = 16-16 = 0 -> equal roots
   (b) 2x^2 - 3x + 5 = 0: D = 9-40 = -31 -> no real roots
   (c) x^2 - 5x + 4 = 0: D = 25-16 = 9 -> 2 distinct roots


   ------------------------------------------------
   Solved Example 6 - Find k (equal roots)
   ------------------------------------------------
$$ (Exam favourite)

   Kis k ke liye x^2 - 4x + k = 0 ke EQUAL roots honge?
     Equal roots -> D = 0
     (-4)^2 - 4(1)(k) = 0 -> 16 - 4k = 0 -> k = 4.


   ------------------------------------------------
   Solved Example 7 - Simple factorisation
   ------------------------------------------------

   x^2 - 3x - 10 = 0
     Split (ac=-10, sum=-3 -> -5, 2):
     (x-5)(x+2) = 0 -> x = 5 ya x = -2.


   ------------------------------------------------
   Solved Example 8 (EASIEST) - Pure quadratic
   ------------------------------------------------

   x^2 - 9 = 0
     x^2 = 9 -> x = +/- 3 (yani 3 ya -3).


==========================================
Q AND A TIME
==========================================

   Q1. CORE: kya 3x^2 - 2x + 1 = 0 quadratic hai? a,b,c bata.

   Q2. Factorisation se solve: x^2 - 7x + 10 = 0.

   Q3. Quadratic formula se solve: 2x^2 + x - 6 = 0.

   Q4. Discriminant nikaal aur nature bata:
       (a) x^2 - 6x + 9 = 0   (b) x^2 + x + 1 = 0

   Q5. Word problem: do consecutive integers ka product
       56 hai. Numbers nikaal.

   Q6. Kis k ke liye x^2 + kx + 9 = 0 ke equal roots? (D=0)

   Q7. CORE CHECK: agar (x-2)(x+5)=0, toh x ki values?


==========================================
SUMMARY
==========================================

   1. Quadratic: a x^2 + b x + c = 0 (a != 0), max 2 roots.

   2. Factorisation: middle term todo, (..)(..)=0, har
      factor=0 karke x nikaalo.

   3. Quadratic formula: x = (-b +/- sqrt(b^2-4ac)) / 2a.

   4. Discriminant D = b^2 - 4ac:
        D>0 distinct, D=0 equal, D<0 no real roots.

   5. Word problems: variable lo -> equation banao ->
      solve -> impossible answer reject karo.

@@ CORE (RED page) revise: coefficient a,b,c, factorisation,
@@ zero product rule, sqrt, +/- ka matlab.


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 4: Quadratic Equations (Core-Basics edition)
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch4_Quadratic_Equations.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 4: Quadratic Equations (Core-Basics Edition)",
        content=CONTENT,
        out_path=out,
    )
