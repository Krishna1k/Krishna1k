"""
PDF generator for Class 10 Maths Chapter 6: Triangles.
Uses shared pdf_utils.py.
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 6: TRIANGLES
==========================================

A simplified, detailed guide in Hinglish
For students who missed Class 7-8-9
Based on the official NCERT English Medium textbook
==========================================


==========================================
SECTION 1: FOUNDATION
==========================================


1.1 TRIANGLE KI BASICS
----------------------

   - Triangle = 3 lines, 3 angles
   - Sum of angles = 180 degrees
   - Types (by sides):
       Equilateral: sab sides equal, sab angles 60
       Isosceles:   2 sides equal
       Scalene:     sab sides different
   - Types (by angles):
       Acute:   sab angles < 90
       Right:   ek angle = 90
       Obtuse:  ek angle > 90


1.2 CONGRUENT VS SIMILAR (CRITICAL!)
------------------------------------

   Property   Congruent       Similar
   --------   ----------      -----------------
   Shape      Same            Same
   Size       SAME            MAY DIFFER
   Sides      Equal           PROPORTIONAL
   Angles     Equal           Equal

   EASY:
     Photo aur uski xerox copy   = congruent
     Photo aur uski enlarged     = similar


1.3 SIMILAR FIGURES
-------------------

   Two figures similar agar:
     1. Corresponding ANGLES equal ho
     2. Corresponding SIDES proportional ho

   EXAMPLES:
     - Sab squares similar (lekin sab congruent nahi)
     - Sab equilateral triangles similar
     - Sab circles similar


==========================================
SECTION 2: SIMILAR TRIANGLES
==========================================


2.1 DEFINITION
--------------

   Triangle ABC aur Triangle PQR similar agar:
     1. angle A = angle P
        angle B = angle Q
        angle C = angle R
     2. AB/PQ = BC/QR = CA/RP

   Likha jaata hai: Triangle ABC ~ Triangle PQR

   IMPORTANT: Letters ka ORDER matters - corresponding
   angles dikhata hai.


2.2 EXAMPLE
-----------

   Triangle ABC ~ Triangle DEF
   AB=6, BC=8, CA=10, DE=9.
   Find EF and FD.

     AB/DE = BC/EF = CA/FD
     6/9 = 8/EF = 10/FD
     2/3 = 8/EF  ->  EF = 12
     2/3 = 10/FD ->  FD = 15

   So EF = 12, FD = 15.


==========================================
SECTION 3: BPT (BASIC PROPORTIONALITY THEOREM)
==========================================


3.1 STATEMENT (AKA THALES THEOREM)
----------------------------------

   "If a line is drawn parallel to one side of a triangle
   to intersect the other two sides in distinct points,
   then the other two sides are divided in the same ratio."

   AASAAN BHASHA:
     Triangle ke ek side ke parallel line khichi jaye,
     jo baaki dono sides ko cut kare, toh wo dono sides
     SAME RATIO mein divide hote hain.


3.2 DIAGRAM
-----------

              A
             /|\
            / | \
           /  |  \
          D---+---E      <- DE parallel to BC
         /    |    \
        /     |     \
       B------+------C


   Agar DE parallel BC, toh:

        AD/DB = AE/EC


3.3 CONVERSE OF BPT
-------------------

   "If a line divides any two sides of a triangle in
    the same ratio, then the line is parallel to the
    third side."

   Agar AD/DB = AE/EC, toh DE parallel BC.


3.4 EXAMPLE
-----------

   Triangle ABC mein DE parallel BC.
   AD = 2.5 cm, DB = 3 cm, AE = 4 cm. EC = ?

     AD/DB = AE/EC
     2.5/3 = 4/EC
     EC = (4 x 3)/2.5 = 4.8 cm


==========================================
SECTION 4: SIMILARITY CRITERIA
==========================================


   3 main criteria hain - ek bhi satisfy ho toh
   triangles similar hain.


4.1 AAA (ANGLE-ANGLE-ANGLE) SIMILARITY
--------------------------------------

   Do triangles ke corresponding TEEN angles equal
   ho - similar hain.


4.2 AA (ANGLE-ANGLE) SIMILARITY
-------------------------------

   Do triangles ke corresponding DO angles equal
   ho - similar hain.

   (Kyunki sum = 180, do same hone se teesra bhi same)

   MOST USED CRITERION!


4.3 SSS (SIDE-SIDE-SIDE) SIMILARITY
-----------------------------------

   Do triangles ke corresponding TEENO sides
   PROPORTIONAL ho - similar hain.


4.4 SAS (SIDE-ANGLE-SIDE) SIMILARITY
------------------------------------

   Do triangles ke DO sides proportional aur unke
   BEECH KA angle equal ho - similar hain.


4.5 EXAMPLE
-----------

   Triangle ABC: AB=4, BC=6, AC=8
   Triangle DEF: DE=6, EF=9, DF=12

   Check ratios:
     AB/DE = 4/6 = 2/3
     BC/EF = 6/9 = 2/3
     AC/DF = 8/12 = 2/3

   Sab same -> Triangle ABC ~ Triangle DEF (by SSS)


==========================================
SECTION 5: PYTHAGORAS THEOREM
==========================================


5.1 STATEMENT (FAMOUS!)
-----------------------

   "In a right-angled triangle, the SQUARE of the
   hypotenuse is equal to the SUM of squares of the
   other two sides."


   DIAGRAM:
              A
              |\
              | \
            p |  \  h (hypotenuse)
              |   \
              |    \
              |_____\
              B  b   C

   If angle B = 90:

        AC^2 = AB^2 + BC^2
        h^2 = p^2 + b^2


5.2 PYTHAGOREAN TRIPLETS (YAAD RAKH)
------------------------------------

   Famous triplets - exam mein bahut use hote hain:

     3, 4, 5      ->  9 + 16 = 25
     5, 12, 13    ->  25 + 144 = 169
     8, 15, 17    ->  64 + 225 = 289
     7, 24, 25    ->  49 + 576 = 625


5.3 CONVERSE OF PYTHAGORAS
--------------------------

   "Agar triangle ke kisi side ka square baaki do
   sides ke squares ke sum ke barabar ho, toh wo
   triangle right-angled hota hai."


5.4 EXAMPLE
-----------

   3, 4, 5 sides wala triangle right-angled hai?

     Largest side = 5
     5^2 = 25
     3^2 + 4^2 = 9 + 16 = 25  (same)

   Haan, right-angled triangle hai!


==========================================
Q AND A TIME
==========================================


   Q1. Congruent aur similar mein basic difference?


   Q2. Triangle PQR ~ Triangle XYZ. PQ=6, QR=8, RP=10,
       XY=9. YZ aur ZX nikaalo.


   Q3. Triangle ABC mein DE parallel BC. AD=1.5, DB=3,
       AE=1. EC = ?


   Q4. Konsi similarity criterion lagegi?
       (a) Do triangles ke 2 angles equal
       (b) Do triangles ke saare 3 sides proportional
       (c) Do triangles ke 2 sides proportional aur
           included angle equal


   Q5. Pythagoras: 6 cm aur 8 cm sides wale right
       triangle ka hypotenuse?


   Q6. Check: kya 5, 12, 13 right triangle ke sides hain?


==========================================
SUMMARY
==========================================


   1. Similar triangles: angles equal + sides proportional.

   2. Congruent vs Similar:
        Congruent = same size, same shape
        Similar   = same shape, different size

   3. BPT (Thales): Parallel line in triangle splits
      other two sides in same ratio.
        DE parallel BC  ->  AD/DB = AE/EC

   4. Similarity Criteria:
        AAA / AA: angles equal
        SSS:      all sides proportional
        SAS:      2 sides proportional + included angle

   5. Pythagoras: hyp^2 = side1^2 + side2^2

   6. Famous triplets: (3,4,5), (5,12,13), (8,15,17),
                       (7,24,25)


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 6: Triangles
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch6_Triangles.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 6: Triangles",
        content=CONTENT,
        out_path=out,
    )
