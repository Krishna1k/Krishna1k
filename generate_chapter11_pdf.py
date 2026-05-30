"""
PDF generator for Class 10 Maths Chapter 11: Areas Related to Circles
(Core-Basics edition). RED core basics, GREEN exam marks,
8 solved examples (hardest -> easiest). Hinglish.
Uses shared pdf_utils.py (red '@@', green '$$', page breaks).
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 11: AREAS RELATED TO CIRCLES
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

@@ 1) CIRCLE - RADIUS, DIAMETER
@@    Radius (r) = centre se circle tak. Diameter = 2r.


@@ 2) pi (PI) KYA HAI?
@@    pi = circumference / diameter = 3.14 (ya 22/7).
@@    Radius 7 ka multiple ho -> 22/7 use karo, warna 3.14.


@@ 3) AREA vs PERIMETER
@@    Area = andar ki jagah (cm^2). Perimeter/circumference
@@    = boundary ki length (cm).


@@ 4) CIRCLE KE 2 FORMULA
@@    Circumference = 2 pi r. Area = pi r^2.


@@ 5) ANGLE (degree)
@@    Pura circle = 360 degree. Sector ek hissa hai jiska
@@    apna angle theta hota hai.


@@ 6) FRACTION OF CIRCLE
@@    Sector = circle ka theta/360 hissa. Isi se area aur
@@    arc nikalte hain.


@@ 7) SQUARE / UNITS
@@    r^2 = r x r. Area ka unit hamesha square (cm^2).

<<<PAGEBREAK>>>

==========================================
NOW: ASLI CHAPTER 11 SHURU
==========================================


TOPIC 1: CIRCLE BASICS
----------------------

$$ EXAM ALERT: Ye 2 formula base hain:

$$   Circumference = 2 pi r
$$   Area = pi r^2


TOPIC 2: SECTOR (pizza slice)
-----------------------------

   Sector = 2 radii + arc ke beech ka area, angle theta.

$$ EXAM ALERT: Sector formulas:

$$   Area of sector = (theta/360) x pi r^2
$$   Length of arc  = (theta/360) x 2 pi r
     Perimeter of sector = arc + 2r


TOPIC 3: SEGMENT
----------------

   Segment = chord aur arc ke beech ka area.

$$   Area of segment = Area of sector - Area of triangle

   Triangle area (do side r, beech angle theta):
     = (1/2) r^2 sin(theta)


TOPIC 4: MINOR vs MAJOR
-----------------------

   Minor = chhota (angle < 180). Major = bada (angle > 180).
   Major area = (total circle) - (minor area).

<<<PAGEBREAK>>>

==========================================
SOLVED EXAMPLES: HARDEST -> EASIEST
==========================================

$$ 8 examples poori tarah solve karke. Upar HARDEST,
$$ neeche EASIEST.


   ------------------------------------------------
   Solved Example 1 (HARDEST) - Segment area
   ------------------------------------------------
$$ (Exam favourite)

   Radius 10 cm, angle 90. Minor segment area? (pi=3.14)
     Sector = (90/360) x 3.14 x 100 = (1/4) x 314 = 78.5
     Triangle = (1/2) x 10 x 10 x sin90 = (1/2)(100)(1) = 50
     Segment = 78.5 - 50 = 28.5 cm^2.


   ------------------------------------------------
   Solved Example 2 - Sector area (22/7)
   ------------------------------------------------
$$ (Exam favourite)

   Radius 21 cm, angle 60. Sector area? (pi=22/7)
     = (60/360) x (22/7) x 21 x 21
     = (1/6) x 22 x 3 x 21
     = (1/6) x 1386 = 231 cm^2.


   ------------------------------------------------
   Solved Example 3 - Arc length
   ------------------------------------------------

   Radius 7 cm, angle 90. Arc length? (pi=22/7)
     = (90/360) x 2 x (22/7) x 7
     = (1/4) x 44 = 11 cm.


   ------------------------------------------------
   Solved Example 4 - Area of circle
   ------------------------------------------------

   Radius 14 cm. Area? (pi=22/7)
     = (22/7) x 14 x 14 = 22 x 28 = 616 cm^2.


   ------------------------------------------------
   Solved Example 5 - Circumference
   ------------------------------------------------

   Radius 7 cm. Circumference? (pi=22/7)
     = 2 x (22/7) x 7 = 44 cm.


   ------------------------------------------------
   Solved Example 6 - Sector perimeter
   ------------------------------------------------

   Radius 7, angle 90. Sector perimeter? (pi=22/7)
     Arc = (1/4) x 44 = 11. Perimeter = arc + 2r
         = 11 + 14 = 25 cm.


   ------------------------------------------------
   Solved Example 7 - Find radius from area
   ------------------------------------------------

   Area = 154 cm^2. Radius? (pi=22/7)
     pi r^2 = 154 -> (22/7) r^2 = 154
     r^2 = 154 x 7 / 22 = 49 -> r = 7 cm.


   ------------------------------------------------
   Solved Example 8 (EASIEST) - Diameter
   ------------------------------------------------

   Radius 9 cm. Diameter? -> 2r = 18 cm.


==========================================
Q AND A TIME
==========================================

   Q1. CORE: circumference aur area ke formula likho.

   Q2. Radius 14 cm circle ka area aur circumference.
       (pi=22/7)

   Q3. Radius 6 cm, angle 60. Sector area. (pi=3.14)

   Q4. Radius 14 cm, angle 90. Arc length. (pi=22/7)

   Q5. Radius 4 cm, angle 90. Minor segment area.
       (pi=3.14, sin90=1)

   Q6. Sector perimeter ka formula kya hai?

   Q7. CORE CHECK: kab 22/7 use karte hain, kab 3.14?


==========================================
SUMMARY
==========================================

   1. Circumference = 2 pi r ; Area = pi r^2.

   2. Sector area = (theta/360) pi r^2.

   3. Arc length = (theta/360) 2 pi r.

   4. Segment = sector - triangle
        = (theta/360) pi r^2 - (1/2) r^2 sin(theta).

   5. pi = 22/7 (radius 7 ka multiple) ya 3.14.

@@ CORE (RED page) revise: radius/diameter, pi, area vs
@@ perimeter, fraction of circle (theta/360), units.


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 11: Areas Related to Circles (Core-Basics edition)
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch11_Areas_Related_to_Circles.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 11: Areas Related to Circles (Core-Basics Edition)",
        content=CONTENT,
        out_path=out,
    )
