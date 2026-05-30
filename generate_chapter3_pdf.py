"""
PDF generator for Class 10 Maths Chapter 3:
Pair of Linear Equations in Two Variables (Core-Basics edition).

Format: RED core-basics page, GREEN exam-frequent marks,
8 solved examples (hardest -> easiest). Hinglish.

Uses shared pdf_utils.py (red via '@@', green via '$$', page breaks).
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 3: PAIR OF LINEAR EQUATIONS IN TWO VARIABLES
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

@@ Ye page sirf un cheezon ka hai jo Class 7-8-9 mein
@@ padhayi jaati hain. Pura Chapter 3 inhi pe khada hai.


@@ 1) VARIABLE AUR EQUATION
@@    Variable = unknown (x, y). Equation = jisme '=' ho.
@@    Example: 2x + 3 = 7 ek equation hai.


@@ 2) LINEAR EQUATION IN ONE VARIABLE
@@    Sirf ek variable, power 1. Form: ax + b = 0.
@@    3x - 6 = 0 -> x = 2. (Ek hi solution hota hai.)


@@ 3) LINEAR EQUATION IN TWO VARIABLES
@@    Do variables, power 1. Form: ax + by + c = 0.
@@    Example: 2x + 3y = 12.
@@    Iske INFINITE solutions hote hain (har x ke liye ek y).


@@ 4) SOLUTION KYA HAI?
@@    Solution = (x, y) jo equation ko sahi (satisfy) kare.
@@    x+y=5 ke liye (2,3) solution hai kyunki 2+3=5.


@@ 5) GRAPH BASICS
@@    X-axis horizontal, Y-axis vertical, milte hain ORIGIN
@@    (0,0) pe. Point = (x, y).
@@    Linear equation ka graph hamesha SEEDHI LINE hota hai.


@@ 6) RATIO (a1/a2 type)
@@    Ratio = do numbers ki tulna (jaise 2/4 = 1/2).
@@    Is chapter mein coefficients ke ratio compare karenge:
@@    a1/a2, b1/b2, c1/c2.


@@ 7) SIMPLE EQUATION SOLVE KARNA
@@    Ek side ki cheez doosri side le jao to sign badalta:
@@    2x = 18 -> x = 18/2 = 9. (divide karke nikalo.)

<<<PAGEBREAK>>>

==========================================
NOW: ASLI CHAPTER 3 SHURU
==========================================


TOPIC 1: PAIR OF LINEAR EQUATIONS
---------------------------------

   Do linear equations ek saath, same variables:
     a1 x + b1 y + c1 = 0
     a2 x + b2 y + c2 = 0

   SOLUTION = woh (x, y) jo DONO ko satisfy kare.


TOPIC 2: GRAPHICAL - 3 CASES
----------------------------

   Dono lines ka graph banao, 3 possibilities:
     - INTERSECTING (ek point pe milti) -> 1 solution
       (Consistent)
     - PARALLEL (kabhi nahi milti)       -> 0 solution
       (Inconsistent)
     - COINCIDENT (ek hi line)           -> infinite
       (Consistent / dependent)


TOPIC 3: CONDITIONS BY RATIOS (bina graph ke)
---------------------------------------------

$$ EXAM ALERT: Ye table ratta maar - har exam mein aata hai.

$$   a1/a2 != b1/b2            -> Unique solution (intersecting)
$$   a1/a2  = b1/b2 != c1/c2   -> No solution (parallel)
$$   a1/a2  = b1/b2  = c1/c2   -> Infinite (coincident)

   Yaad: sab alag -> 1, do same ek alag -> 0, sab same -> infinite.


TOPIC 4: ALGEBRAIC METHODS
--------------------------

$$ EXAM ALERT: Substitution aur Elimination se solve karna
$$ pakka aata hai (3 marks). Dono aane chahiye.

   SUBSTITUTION:
     1. Ek equation se ek variable doosre ke terms mein nikaalo
     2. Doosri equation mein daal do
     3. Single variable solve karo, phir wapas daalo

   ELIMINATION:
     1. Coefficients match karo (multiply karke)
     2. Add/subtract karke ek variable gayab karo
     3. Solve karo, phir wapas daalo

<<<PAGEBREAK>>>

==========================================
SOLVED EXAMPLES: HARDEST -> EASIEST
==========================================

$$ 8 examples poori tarah solve karke. Upar HARDEST,
$$ neeche EASIEST. Step-by-step samajh.


   ------------------------------------------------
   Solved Example 1 (HARDEST) - Fraction word problem
   ------------------------------------------------
$$ (Exam favourite)

   Ek fraction 9/11 ban jaata hai agar numerator aur
   denominator dono mein 2 add karein. 3 add karein toh
   5/6 ban jaata hai. Fraction nikaalo.

   Let fraction = x/y.
     (x+2)/(y+2) = 9/11 -> 11(x+2)=9(y+2)
        -> 11x - 9y = -4    ...(1)
     (x+3)/(y+3) = 5/6  -> 6(x+3)=5(y+3)
        -> 6x - 5y = -3     ...(2)

   (1)x5: 55x - 45y = -20
   (2)x9: 54x - 45y = -27
   Subtract: x = 7
   (2) mein: 6(7) - 5y = -3 -> 42 + 3 = 5y -> y = 9

   Fraction = 7/9.


   ------------------------------------------------
   Solved Example 2 - Age word problem
   ------------------------------------------------
$$ (Exam favourite)

   5 saal pehle Nuri, Sonu se 3 guna umar ki thi. 10 saal
   baad Nuri, Sonu se 2 guna hogi. Dono ki umar?

   Let Nuri = x, Sonu = y.
     x - 5 = 3(y - 5) -> x - 3y = -10   ...(1)
     x + 10 = 2(y + 10) -> x - 2y = 10  ...(2)

   (1) - (2): -y = -20 -> y = 20
   (2) mein: x - 40 = 10 -> x = 50

   Nuri 50 saal, Sonu 20 saal.


   ------------------------------------------------
   Solved Example 3 - Elimination method
   ------------------------------------------------

   2x + 3y = 12   ...(1)
   3x - 2y = 5    ...(2)

   (1)x2: 4x + 6y = 24
   (2)x3: 9x - 6y = 15
   Add:   13x = 39 -> x = 3
   (1) mein: 2(3) + 3y = 12 -> 3y = 6 -> y = 2

   Solution: x = 3, y = 2.


   ------------------------------------------------
   Solved Example 4 - Substitution method
   ------------------------------------------------

   x + 2y = 7   ...(1)
   3x - y = 0   ...(2)

   (2) se: y = 3x
   (1) mein daal: x + 2(3x) = 7 -> 7x = 7 -> x = 1
   y = 3(1) = 3

   Solution: x = 1, y = 3.


   ------------------------------------------------
   Solved Example 5 - Conditions (kaunsa case)
   ------------------------------------------------
$$ (Exam favourite - ratios se decide)

   (a) x+2y=5 & 2x+4y=10:
       1/2 = 2/4 = 5/10 (sab same) -> INFINITE (coincident)
   (b) 2x+y=6 & 4x+2y=7:
       2/4 = 1/2, par 6/7 alag -> NO solution (parallel)
   (c) 3x-y=4 & x+2y=1:
       3/1 != -1/2 -> UNIQUE solution (intersecting)


   ------------------------------------------------
   Solved Example 6 - Find k (infinite solutions)
   ------------------------------------------------
$$ (Exam favourite)

   Kis k ke liye 2x+3y=7 aur (k-1)x+(k+2)y=3k ke
   INFINITE solutions honge?

   Condition: a1/a2 = b1/b2 = c1/c2
     2/(k-1) = 3/(k+2) = 7/(3k)

   2/(k-1) = 3/(k+2):
     2(k+2) = 3(k-1) -> 2k+4 = 3k-3 -> k = 7

   Check 7/(3k): k=7 -> 2/6 = 1/3 aur 7/21 = 1/3 (match!)
   So k = 7.


   ------------------------------------------------
   Solved Example 7 - Simple word (sum & difference)
   ------------------------------------------------

   Do numbers ka sum 50, difference 10. Numbers?
     x + y = 50  ...(1)
     x - y = 10  ...(2)
   Add: 2x = 60 -> x = 30 ; y = 20.


   ------------------------------------------------
   Solved Example 8 (EASIEST) - Solution check
   ------------------------------------------------

   (a) Kya (2,3), 2x+y=7 ka solution hai?
       2(2)+3 = 7 -> haan, satisfy karta hai. Solution hai.
   (b) x+y=4 ka ek solution: x=1,y=3 (kyunki 1+3=4).
       (Aise infinite solutions ho sakte hain.)


==========================================
Q AND A TIME
==========================================

   Q1. CORE: x+y=6 ke 3 solutions likho.

   Q2. Bina solve kiye batao (unique/no/infinite):
       (a) x+2y=4 & 2x+4y=12
       (b) 3x-y=2 & 6x-2y=4
       (c) 2x+y=5 & x-y=1

   Q3. Substitution se solve: x+y=14, x-y=4.

   Q4. Elimination se solve: 3x+4y=10, 2x-2y=2.

   Q5. Do numbers ka sum 25, difference 5. Numbers nikaal.

   Q6. Kis k ke liye kx+2y=5 aur 3x+y=1 ka UNIQUE
       solution hoga? (Hint: a1/a2 != b1/b2)

   Q7. CORE CHECK: linear equation in 2 variables ke
       kitne solutions hote hain?


==========================================
SUMMARY
==========================================

   1. Pair of linear equations -> common (x,y) dhoondhna.

   2. 3 cases: intersecting (1), parallel (0),
      coincident (infinite).

   3. Ratios se:
        a1/a2 != b1/b2          -> unique
        a1/a2 = b1/b2 != c1/c2  -> none
        a1/a2 = b1/b2 = c1/c2   -> infinite

   4. Substitution: ek variable replace karo.

   5. Elimination: add/subtract karke ek variable gayab.

@@ CORE (RED page) revise: solution ka matlab, graph =
@@ seedhi line, ratio compare karna.


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 3: Pair of Linear Equations (Core-Basics edition)
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch3_Pair_of_Linear_Equations.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 3: Pair of Linear Equations (Core-Basics Edition)",
        content=CONTENT,
        out_path=out,
    )
