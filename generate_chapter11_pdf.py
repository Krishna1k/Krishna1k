"""
PDF generator for Class 10 Maths Chapter 11: Areas Related to Circles.
Uses shared pdf_utils.py.
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 11: AREAS RELATED TO CIRCLES
==========================================

A simplified, detailed guide in Hinglish
For students who missed Class 7-8-9
Based on the official NCERT English Medium textbook
==========================================


==========================================
SECTION 1: FOUNDATION
==========================================


1.1 CIRCLE KE BASIC FORMULAS (YAAD RAKH)
----------------------------------------

   Circumference (perimeter) = 2 x pi x r   (or pi x d)
   Area of circle            = pi x r^2
   Diameter                  = 2r

   r  = radius
   pi = 22/7  (or 3.14)


1.2 pi (PI) KYA HAI?
--------------------

   pi = circumference / diameter ka ratio.
   Har circle ke liye SAME hota hai = 3.14159...

   EXAM MEIN:
     - Radius 7 ka multiple ho   -> use pi = 22/7
     - Warna                     -> use pi = 3.14


1.3 EXAMPLE: BASIC
------------------

   EXAMPLE 1: Radius 7 cm circle ka area aur circumference

     Area = pi r^2 = (22/7) x 7 x 7 = 22 x 7 = 154 cm^2
     Circumference = 2 pi r = 2 x (22/7) x 7 = 44 cm


==========================================
SECTION 2: SECTOR OF A CIRCLE
==========================================


2.1 SECTOR KYA HAI?
-------------------

   SECTOR = circle ka ek "pizza slice" - do radii aur
   ek arc ke beech ka area.

   Angle theta us slice ka angle hai (centre pe).


               arc
              ____
            /      \
           / sector \
          /  theta   \
         *-----O------*
         radius  radius


2.2 FORMULAS (theta in degrees)
-------------------------------

   Area of sector      = (theta/360) x pi x r^2
   Length of arc       = (theta/360) x 2 x pi x r
   Perimeter of sector = arc length + 2r

   LOGIC: Pura circle 360 degree hai. Sector us ka
   theta/360 hissa hai. So area aur arc bhi utna fraction.


2.3 EXAMPLES
------------

   EXAMPLE 2: Radius 21 cm, angle 60. Sector area.

     Area = (60/360) x (22/7) x 21 x 21
          = (1/6) x (22/7) x 441
          = (1/6) x 22 x 63
          = (1/6) x 1386
          = 231 cm^2


   EXAMPLE 3: Radius 7 cm, angle 90. Arc length.

     Arc = (90/360) x 2 x (22/7) x 7
         = (1/4) x 44
         = 11 cm


==========================================
SECTION 3: SEGMENT OF A CIRCLE
==========================================


3.1 SEGMENT KYA HAI?
--------------------

   SEGMENT = chord aur arc ke beech ka area (sector mein
   se triangle nikaal do).


            ____
          /  seg  \
         /._______.\    <- chord
        /  triangle \
       *------O------*


3.2 FORMULA
-----------

   Area of (minor) segment
       = Area of sector - Area of triangle

   Area of sector   = (theta/360) x pi x r^2
   Area of triangle = (1/2) x r^2 x sin(theta)

   So:
     Segment = (theta/360) pi r^2 - (1/2) r^2 sin(theta)


3.3 EXAMPLE
-----------

   EXAMPLE 4: Radius 10 cm, angle 90. Minor segment area.
              (pi = 3.14)

     Sector area = (90/360) x 3.14 x 10 x 10
                 = (1/4) x 314 = 78.5 cm^2

     Triangle area = (1/2) x r^2 x sin 90
                   = (1/2) x 100 x 1 = 50 cm^2

     Segment = 78.5 - 50 = 28.5 cm^2


==========================================
SECTION 4: MINOR VS MAJOR
==========================================


   - MINOR sector/segment: chhota wala (angle < 180)
   - MAJOR sector/segment: bada wala (angle > 180)

   - Major area  = total circle area - minor area
   - Major angle = 360 - minor angle


==========================================
Q AND A TIME
==========================================


   Q1. Radius 14 cm circle ka area aur circumference.
       (pi = 22/7)


   Q2. Radius 6 cm, angle 60. Sector area. (pi = 3.14)


   Q3. Radius 14 cm, angle 90. Arc length. (pi = 22/7)


   Q4. Sector ka perimeter kaise nikaalte hain?
       (formula bata)


   Q5. Radius 4 cm, angle 90. Minor segment area.
       (pi = 3.14, sin 90 = 1)


   Q6. Minor aur major sector mein kya difference hai?


==========================================
SUMMARY
==========================================


   1. Circumference = 2 pi r,  Area = pi r^2

   2. pi = 22/7 (radius 7 ka multiple) ya 3.14

   3. Sector area = (theta/360) x pi r^2

   4. Arc length  = (theta/360) x 2 pi r

   5. Perimeter of sector = arc length + 2r

   6. Segment area = sector area - triangle area
        = (theta/360) pi r^2 - (1/2) r^2 sin(theta)

   7. Major = total - minor


==========================================
TIPS FOR EXAM
==========================================


   1. theta/360 ka fraction pehle simplify kar lo
      (jaise 90/360 = 1/4) - calculation easy.

   2. pi = 22/7 vs 3.14 sahi choose karo - radius dekho.

   3. Segment = sector - triangle. Triangle ke liye
      (1/2) r^2 sin(theta) formula yaad rakh.

   4. Units: area = cm^2, length/perimeter = cm.

   5. Combination figures (square mein circle, etc.)
      mein areas ko ADD/SUBTRACT karo - diagram banao.


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 11: Areas Related to Circles
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch11_Areas_Related_to_Circles.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 11: Areas Related to Circles",
        content=CONTENT,
        out_path=out,
    )
