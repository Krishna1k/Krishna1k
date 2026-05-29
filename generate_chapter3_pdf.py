"""
Pure-Python PDF generator for Class 10 Maths Chapter 3:
Pair of Linear Equations in Two Variables.

Generates: Class10_Maths_Ch3_Pair_of_Linear_Equations.pdf

Uses shared pdf_utils.py for PDF building (no external libraries).
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 3: PAIR OF LINEAR EQUATIONS IN TWO VARIABLES
==========================================

A simplified, detailed guide in Hinglish
For students who missed Class 7-8-9
Based on the official NCERT English Medium textbook
==========================================


==========================================
SECTION 1: FOUNDATION (Class 7-8-9 ka revision)
==========================================


1.1 EQUATION KYA HOTI HAI?
--------------------------

   EQUATION = ek mathematical statement jisme '=' sign hota hai.

   Example: 2x + 3 = 7 - ye ek equation hai.


1.2 LINEAR EQUATION IN ONE VARIABLE
-----------------------------------

   Sirf ek variable (jaise x) ho aur power 1 ho.

   Form:  ax + b = 0  (a != 0)

   Examples:
     - 3x + 5 = 0   ->  solve: x = -5/3
     - 2x - 8 = 0   ->  x = 4

   Ek variable ki linear equation ka SIRF 1 solution hota hai.


1.3 LINEAR EQUATION IN TWO VARIABLES
------------------------------------

   Ab DO variables hain (x aur y), dono ka power 1.

   Form:  ax + by + c = 0   (a != 0, b != 0)

   Example: 2x + 3y - 12 = 0

   IMPORTANT:
     Iske INFINITE solutions hote hain! Har x ke liye ek y
     mil sakta hai.


   Example check: x + y = 5
     x = 1, y = 4   (ok)
     x = 2, y = 3   (ok)
     x = 0, y = 5   (ok)
     x = -1, y = 6  (ok)
     ... aur bhi infinite


1.4 CARTESIAN PLANE (GRAPH PAPER) - BASICS
------------------------------------------

   Graph paper pe 2 lines hoti hain:
     - X-axis (horizontal, leti hui)
     - Y-axis (vertical, khadi)
     - Dono ka meeting point = ORIGIN (0, 0)

   Point likhne ka tareeka: (x, y) - pehle x, phir y.


           Y-axis
             |
          4 -|     . (3, 4)
          3 -|
          2 -|
          1 -|
             |________________
        --- 0   1  2  3  4    X-axis


1.5 LINEAR EQUATION KA GRAPH
----------------------------

   Linear equation ax + by + c = 0 ka graph HAMESHA
   ek STRAIGHT LINE hota hai. (Isliye naam "linear")

   Plot karne ka tareeka:
     1. Equation se 2-3 (x, y) pairs nikaalo
     2. Graph paper pe points lagao
     3. Sab points ko join karo - seedhi line milegi


==========================================
SECTION 2: PAIR OF LINEAR EQUATIONS
==========================================


2.1 PAIR KYA HOTI HAI?
----------------------

   Pair of Linear Equations = do linear equations ek saath,
   dono mein SAME variables.

   General form:
     a1 x + b1 y + c1 = 0
     a2 x + b2 y + c2 = 0


   Example:
     2x + 3y = 12
     x - y = 1


2.2 SOLUTION KYA HOTA HAI?
--------------------------

   Solution = wo (x, y) jo DONO equations ko satisfy kare.

   Example: Check x = 3, y = 2:
     2(3) + 3(2) = 6 + 6 = 12   (ok)
     3 - 2 = 1                  (ok)

   So (3, 2) solution hai.


2.3 GRAPHICALLY - 3 CASES POSSIBLE
----------------------------------

   Jab dono equations ka graph banaoge, 3 possibilities:


   CASE 1: Lines INTERSECT  ->  UNIQUE solution
     - Ek point pe milengi
     - Wo point hi solution hai
     - System CONSISTENT


   CASE 2: Lines PARALLEL  ->  NO solution
     - Lines kabhi nahi milti
     - Koi common point nahi
     - System INCONSISTENT


   CASE 3: Lines COINCIDENT  ->  INFINITE solutions
     - Dono equations same line
     - Har point common hai
     - System CONSISTENT (Dependent)


2.4 CONDITIONS WITHOUT DRAWING GRAPH
------------------------------------

   Sirf coefficients dekh ke pata laga sakte hain:

   Condition                       Type            Solutions
   ----------------------------    ------------    -----------
   a1/a2  !=  b1/b2                Intersecting    Unique
   a1/a2  =   b1/b2  !=  c1/c2     Parallel        None
   a1/a2  =   b1/b2  =   c1/c2     Coincident      Infinite


   YAAD RAKHNE KA TAREEKA:
     - Sab ratios alag        ->  1 solution
     - 2 ratios same, 1 alag  ->  0 solution
     - Sab ratios same        ->  infinite solutions


   EXAMPLE 1: 2x + 3y = 7  aur  4x + 6y = 14
     a1/a2 = 2/4 = 1/2
     b1/b2 = 3/6 = 1/2
     c1/c2 = 7/14 = 1/2
     -> Sab same: INFINITE solutions, coincident lines


   EXAMPLE 2: x + 2y = 4  aur  2x + 4y = 12
     a1/a2 = 1/2
     b1/b2 = 2/4 = 1/2
     c1/c2 = 4/12 = 1/3
     -> a1/a2 = b1/b2 != c1/c2: NO solution, parallel lines


   EXAMPLE 3: 3x + 2y = 5  aur  2x - 3y = 7
     a1/a2 = 3/2
     b1/b2 = 2/(-3) = -2/3
     -> a1/a2 != b1/b2: UNIQUE solution, intersecting lines


==========================================
SECTION 3: ALGEBRAIC METHODS
==========================================


3.1 METHOD 1: SUBSTITUTION METHOD
---------------------------------

   IDEA: Ek equation se ek variable ko doosre ke terms
   mein nikaalo, phir doosri equation mein daal do.

   STEPS:
     1. Ek equation mein se ek variable (jaise y) ko
        doosre ke terms mein express karo
     2. Doosri equation mein woh value daal do
     3. Single variable equation - solve karo
     4. Pehli equation mein wapas daal ke doosra
        variable nikaalo


   EXAMPLE 4: Solve karo
     x + y = 14    ...(1)
     x - y = 4     ...(2)

     Step 1: (1) se y = 14 - x

     Step 2: (2) mein daal:
       x - (14 - x) = 4
       x - 14 + x = 4
       2x = 18
       x = 9

     Step 3: y = 14 - 9 = 5

     Solution: x = 9, y = 5
     Verify: 9 + 5 = 14 (ok), 9 - 5 = 4 (ok)


   EXAMPLE 5: Solve karo
     2x + 3y = 11   ...(1)
     2x - 4y = -24  ...(2)

     Step 1: (1) se 2x = 11 - 3y, so x = (11 - 3y)/2

     Step 2: (2) mein daal:
       2 * (11 - 3y)/2 - 4y = -24
       (11 - 3y) - 4y = -24
       11 - 7y = -24
       -7y = -35
       y = 5

     Step 3: x = (11 - 3*5)/2 = (11-15)/2 = -2

     Solution: x = -2, y = 5


3.2 METHOD 2: ELIMINATION METHOD
--------------------------------

   IDEA: Equations ko add/subtract karke ek variable
   ko GAYAB kar do.

   STEPS:
     1. Dono equations ko aisa multiply karo ki ek variable
        ke coefficients same ho jayein
     2. Add ya subtract karo to eliminate that variable
     3. Single variable equation solve karo
     4. Pehli mein daal ke doosra variable nikaalo


   EXAMPLE 6: Solve karo
     2x + 3y = 8    ...(1)
     4x + 6y = 7    ...(2)

     Step 1: (1) ko 2 se multiply:
       4x + 6y = 16   ...(1')
       4x + 6y = 7    ...(2)

     Step 2: Subtract (1') - (2):
       0 = 9   <- Possible nahi!

     -> NO solution (lines parallel hain)


   EXAMPLE 7: Solve karo
     3x + 4y = 10   ...(1)
     2x - 2y = 2    ...(2)

     Step 1: (2) ko 2 se multiply (y-coefficient match):
       4x - 4y = 4    ...(2')

     Step 2: Add (1) + (2'):
       3x + 4y + 4x - 4y = 10 + 4
       7x = 14
       x = 2

     Step 3: (2) mein daal:
       2(2) - 2y = 2
       -2y = -2
       y = 1

     Solution: x = 2, y = 1


3.3 KAUNSA METHOD USE KAREIN?
-----------------------------

   Situation                                Best Method
   --------------------------------------   -------------
   Ek variable ka coefficient = 1 or -1     Substitution
   Coefficients bade-bade hain              Elimination
   Equations same form (2x+3y, 4x-3y)       Elimination


==========================================
SECTION 4: WORD PROBLEMS
==========================================


   EXAMPLE 8: Age problem

   "Father ki current age, son ki age se 30 zyada hai.
    5 saal pehle, father ki age son se 4 guna thi.
    Dono ki current ages nikaalo."

   Variables:
     Son ki current age = x
     Father ki current age = y

   Equations:
     y = x + 30                 ...(1)
     y - 5 = 4(x - 5)           ...(2)  (5 saal pehle)

   Substitution:
     (x + 30) - 5 = 4(x - 5)
     x + 25 = 4x - 20
     45 = 3x
     x = 15, y = 45

   Answer: Son 15 saal, Father 45 saal


   EXAMPLE 9: Number problem

   "Do numbers ka sum 25 hai aur difference 5 hai.
    Numbers nikaalo."

   Let numbers = x, y (x > y)
     x + y = 25   ...(1)
     x - y = 5    ...(2)

   Add: 2x = 30, x = 15
   Subtract: 2y = 20, y = 10

   Answer: 15 aur 10


==========================================
Q AND A TIME - SECTION KE BAAD KA TEST
==========================================


   SET A: FOUNDATION

   Q1. Linear equations konsi hain (1 var / 2 var)?
       (a) 3x + 5 = 11
       (b) 2x + 3y = 12
       (c) 5y - 7 = 0
       (d) x - 4y + 1 = 0

   Q2. x + y = 7 ke liye 3 solutions likho.


   SET B: CONDITIONS

   Q3. Bina solve kiye bata, kya hoga
       (unique/no/infinite)?
       (a) x + 2y = 5  aur  2x + 4y = 10
       (b) 2x + y = 6  aur  4x + 2y = 7
       (c) 3x - y = 4  aur  x + 2y = 1


   SET C: SOLVING

   Q4. Substitution method se solve kar:
         x + 2y = 7
         3x - y = 0


   Q5. Elimination method se solve kar:
         2x + 3y = 12
         3x - 2y = 5


   SET D: WORD PROBLEM

   Q6. Do numbers ka sum 50 hai aur ek number doosre
       se 10 zyada hai. Numbers nikaalo.


==========================================
SUMMARY (YAAD RAKH)
==========================================


   1. Linear equation in 2 variables:
        ax + by + c = 0  ka graph STRAIGHT LINE hota hai.


   2. Pair of linear equations ke 3 cases:
        Intersecting -> unique solution (consistent)
        Parallel     -> no solution (inconsistent)
        Coincident   -> infinite solutions (dependent)


   3. Coefficient ratios se pata lagao:
        a1/a2 != b1/b2                 -> Unique
        a1/a2  = b1/b2 != c1/c2        -> None
        a1/a2  = b1/b2  = c1/c2        -> Infinite


   4. Substitution method:
        Ek variable ko doosre se replace karo.


   5. Elimination method:
        Equations add/subtract karke ek variable gayab karo.


   6. Word problems:
        Variables le -> equations banao -> solve -> check.


==========================================
TIPS FOR EXAM
==========================================


   1. Equation banane ke baad HAMESHA verify kar - both
      equations ko satisfy karna chahiye.

   2. Conditions question (a1/a2, b1/b2, c1/c2) sirf 2-3
      marks ka aata hai - bahut easy. Yaad rakh table.

   3. Word problems mein:
        - Variables clearly define kar (with units)
        - Equations sentence-by-sentence banao
        - Final answer mein sentence likh ke bata
          (e.g., "Son ki age 15 saal hai")

   4. Substitution easy hai jab ek variable already
      isolate ho ya 1/-1 coefficient ho.

   5. Elimination easy hai jab same coefficients ho
      ya make karna possible ho.


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 3:
Pair of Linear Equations in Two Variables
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch3_Pair_of_Linear_Equations.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 3: Pair of Linear Equations in Two Variables",
        content=CONTENT,
        out_path=out,
    )
