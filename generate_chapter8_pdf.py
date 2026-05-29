"""
PDF generator for Class 10 Maths Chapter 8: Introduction to Trigonometry.
Uses shared pdf_utils.py.
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 8: INTRODUCTION TO TRIGONOMETRY
==========================================

A simplified, detailed guide in Hinglish
For students who missed Class 7-8-9
Based on the official NCERT English Medium textbook
==========================================


==========================================
SECTION 1: FOUNDATION
==========================================


1.1 TRIGONOMETRY KYA HAI?
-------------------------

   "Tri-gon-metry" = teen (tri) + kona/angle (gon) +
   measurement (metry).

   Matlab: TRIANGLES ke angles aur sides ka rishta study
   karna - khaaskar RIGHT-ANGLED triangle.


1.2 RIGHT-ANGLED TRIANGLE KE PARTS
----------------------------------

   Ek angle theta (let's call it) ke reference se:

              C
              |\
              | \
   PERPEN-    |  \   HYPOTENUSE
   DICULAR    |   \  (always opposite to 90 deg)
   (opposite  |    \
    to theta) |     \  theta
              |______\
              B  BASE  A
              (adjacent to theta)


   3 sides:
     - HYPOTENUSE: 90 degree ke saamne wali (longest)
     - PERPENDICULAR (Opposite): theta ke saamne wali
     - BASE (Adjacent): theta ke saath wali (na hyp)


1.3 RATIO YAAD KARNE KA TRICK
-----------------------------

   "Pandit Badri Prasad
    Har Har Bole
    Sona Chandi Tole"

   P / H = Perpendicular / Hypotenuse  = sin
   B / H = Base / Hypotenuse           = cos
   P / B = Perpendicular / Base        = tan

   (Pehla letter pair upar/neeche dekh)


==========================================
SECTION 2: SIX TRIGONOMETRIC RATIOS
==========================================


2.1 THE THREE MAIN RATIOS
-------------------------

   For angle theta in a right triangle:

     sin(theta) = Perpendicular / Hypotenuse  =  P/H
     cos(theta) = Base / Hypotenuse           =  B/H
     tan(theta) = Perpendicular / Base        =  P/B


2.2 THE THREE RECIPROCAL RATIOS
-------------------------------

     cosec(theta) = 1/sin = H/P
     sec(theta)   = 1/cos = H/B
     cot(theta)   = 1/tan = B/P


2.3 USEFUL RELATIONS
--------------------

     tan(theta) = sin(theta) / cos(theta)
     cot(theta) = cos(theta) / sin(theta)

     sin x cosec = 1
     cos x sec   = 1
     tan x cot   = 1


2.4 EXAMPLE
-----------

   EXAMPLE 1: Right triangle: Perpendicular=3, Base=4.
              Hypotenuse aur ratios nikaal.

     Hyp = sqrt(3^2 + 4^2) = sqrt(25) = 5  (3-4-5 triplet)

     sin = 3/5,   cos = 4/5,   tan = 3/4
     cosec = 5/3, sec = 5/4,   cot = 4/3


==========================================
SECTION 3: SPECIFIC ANGLES (YAAD RAKH!)
==========================================


3.1 THE MASTER TABLE
--------------------

   Angle:     0     30     45     60     90
   ------    ---   ----   ----   ----   ----
   sin        0    1/2   1/sq2  sq3/2    1
   cos        1   sq3/2  1/sq2   1/2     0
   tan        0   1/sq3   1     sq3    undef

   (sq2 = sqrt2 = 1.414, sq3 = sqrt3 = 1.732)


3.2 YAAD KARNE KA EASY TRICK (sin ke liye)
------------------------------------------

   sin values: write 0,1,2,3,4 -> divide by 4 -> sqrt

     Angle:   0    30    45    60    90
     Step1:   0     1     2     3     4
     /4:     0/4   1/4   2/4   3/4   4/4
     sqrt: sqrt0 sqrt(1/4) ...

     = 0, 1/2, 1/sqrt2, sqrt3/2, 1

   cos = same table ULTA (reverse order)
   tan = sin / cos


3.3 EXAMPLES
------------

   EXAMPLE 2: sin 30 + cos 60 = ?
     = 1/2 + 1/2 = 1

   EXAMPLE 3: tan 45 + cos 0 = ?
     = 1 + 1 = 2

   EXAMPLE 4: 2 sin 30 x cos 60 = ?
     = 2 x (1/2) x (1/2) = 1/2


==========================================
SECTION 4: TRIGONOMETRIC IDENTITIES
==========================================


4.1 THE THREE IDENTITIES (BAHUT IMPORTANT)
------------------------------------------

     1.  sin^2(theta) + cos^2(theta) = 1

     2.  1 + tan^2(theta) = sec^2(theta)

     3.  1 + cot^2(theta) = cosec^2(theta)


   In se aur bhi forms nikalte hain:
     sin^2 = 1 - cos^2
     cos^2 = 1 - sin^2
     sec^2 - tan^2 = 1
     cosec^2 - cot^2 = 1


4.2 EXAMPLES
------------

   EXAMPLE 5: Agar sin(theta) = 3/5, cos(theta) nikaal.

     sin^2 + cos^2 = 1
     (3/5)^2 + cos^2 = 1
     9/25 + cos^2 = 1
     cos^2 = 16/25
     cos = 4/5


   EXAMPLE 6: Prove: (1 - cos^2 A) x cosec^2 A = 1

     LHS = (1 - cos^2 A) x cosec^2 A
         = sin^2 A x cosec^2 A   [1-cos^2 = sin^2]
         = sin^2 A x (1/sin^2 A)
         = 1 = RHS   (Proved)


==========================================
Q AND A TIME
==========================================


   Q1. Right triangle: Perpendicular = 5, Base = 12.
       Hypotenuse aur sin, cos, tan nikaal.


   Q2. Value nikaal:
       (a) sin 60 + cos 30
       (b) tan 30 x tan 60
       (c) cos 0 - sin 90


   Q3. Agar cos(theta) = 12/13, toh sin(theta) nikaal
       (identity use kar).


   Q4. Prove: sin^2 30 + cos^2 30 = 1
       (values daal ke verify kar)


   Q5. sec^2 45 - tan^2 45 = ? (identity ya values se)


==========================================
SUMMARY
==========================================


   1. 6 ratios:
        sin = P/H, cos = B/H, tan = P/B
        cosec = H/P, sec = H/B, cot = B/P

   2. Trick: "Pandit Badri Prasad..." for sin, cos, tan.

   3. Special angles table (0,30,45,60,90) yaad rakh.

   4. Three identities:
        sin^2 + cos^2 = 1
        1 + tan^2 = sec^2
        1 + cot^2 = cosec^2

   5. tan = sin/cos, reciprocals: sin-cosec, cos-sec,
      tan-cot.


==========================================
TIPS FOR EXAM
==========================================


   1. Special angle table HARD yaad kar - har question
      mein use hoti hai.

   2. sin trick (0,1,2,3,4 / 4 -> sqrt) se table jaldi
      bana sakta hai agar bhool jaye.

   3. Identity proofs mein hamesha COMPLEX side se shuru
      karke simple side tak pahuncho.

   4. sin^2 ka matlab (sin theta)^2 hota hai, sin(theta^2)
      nahi - dhyaan rakh.

   5. tan 90 aur sec 90 UNDEFINED hote hain (denominator 0).


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 8: Introduction to Trigonometry
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch8_Introduction_to_Trigonometry.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 8: Introduction to Trigonometry",
        content=CONTENT,
        out_path=out,
    )
