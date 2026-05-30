"""
PDF generator for Class 10 Maths Chapter 7: Coordinate Geometry
(Core-Basics edition). RED core basics, GREEN exam marks,
8 solved examples (hardest -> easiest). Hinglish.
Uses shared pdf_utils.py (red '@@', green '$$', page breaks).
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 7: COORDINATE GEOMETRY
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

@@ 1) X-AXIS, Y-AXIS, ORIGIN
@@    X-axis = leti (horizontal) line. Y-axis = khadi line.
@@    Dono milte hain ORIGIN (0, 0) pe.


@@ 2) COORDINATES (x, y)
@@    Point ko (x, y) likhte hain. x = abscissa (X pe),
@@    y = ordinate (Y pe). Order important: (3,5) != (5,3).


@@ 3) SIGNS / QUADRANTS
@@    Q1 (+,+), Q2 (-,+), Q3 (-,-), Q4 (+,-).
@@    X-axis pe y=0, Y-axis pe x=0.


@@ 4) SQUARE AUR SQUARE ROOT
@@    a^2 = a x a. sqrt(25) = 5.
@@    Distance formula mein squares aur sqrt use hote hain.


@@ 5) NEGATIVE KA SQUARE
@@    (-4)^2 = 16 (negative ka square POSITIVE hota hai).


@@ 6) AVERAGE (mean)
@@    Do numbers ka average = (a + b)/2.
@@    Midpoint formula mein bas average lena hai.


@@ 7) RATIO (m1 : m2)
@@    Section formula mein point segment ko m1:m2 mein
@@    baant-ta hai. Ratio = do hisson ki tulna.

<<<PAGEBREAK>>>

==========================================
NOW: ASLI CHAPTER 7 SHURU
==========================================


TOPIC 1: DISTANCE FORMULA
-------------------------

$$ EXAM ALERT: Distance formula har exam mein use hota:

$$   AB = sqrt[ (x2 - x1)^2 + (y2 - y1)^2 ]

   (Ye Pythagoras se banaa hai.)
   Origin se distance: sqrt(x^2 + y^2).

@@   [CORE] differences ko square karte hain, isliye sign
@@   automatically positive ho jaata (RED page point 5).


TOPIC 2: SECTION FORMULA
------------------------

$$ EXAM ALERT: Point jo A,B ko m1:m2 mein baant-ta hai:

$$   P = ( (m1 x2 + m2 x1)/(m1+m2) ,
$$         (m1 y2 + m2 y1)/(m1+m2) )


TOPIC 3: MIDPOINT FORMULA
-------------------------

$$ EXAM ALERT: Midpoint (1:1 ka special case):

$$   M = ( (x1 + x2)/2 , (y1 + y2)/2 )

   (Bas dono x ka average, dono y ka average.)

   NOTE: Latest NCERT (2023-24) mein "Area of Triangle"
   wala part hata diya gaya hai, isliye include nahi kiya.

<<<PAGEBREAK>>>

==========================================
SOLVED EXAMPLES: HARDEST -> EASIEST
==========================================

$$ 8 examples poori tarah solve karke. Upar HARDEST,
$$ neeche EASIEST.


   ------------------------------------------------
   Solved Example 1 (HARDEST) - Type of triangle
   ------------------------------------------------
$$ (Exam favourite - distance ka use)

   A(3,4), B(-4,3), O(0,0). Dikhao OA = OB (isosceles).

     OA = sqrt(3^2 + 4^2) = sqrt(9+16) = sqrt25 = 5
     OB = sqrt((-4)^2 + 3^2) = sqrt(16+9) = sqrt25 = 5
   OA = OB = 5 -> triangle OAB isosceles hai.


   ------------------------------------------------
   Solved Example 2 - Collinear points
   ------------------------------------------------
$$ (Exam favourite)

   Kya A(1,5), B(2,3), C(-2,-11) collinear hain?
   (Collinear = AB + BC = AC ho.)

     AB = sqrt((2-1)^2+(3-5)^2) = sqrt(1+4) = sqrt5 = 2.24
     BC = sqrt((-2-2)^2+(-11-3)^2) = sqrt(16+196)=sqrt212=14.56
     AC = sqrt((-2-1)^2+(-11-5)^2)=sqrt(9+256)=sqrt265=16.28
   AB + BC (16.8) != AC (16.28) -> NOT collinear.


   ------------------------------------------------
   Solved Example 3 - Section formula
   ------------------------------------------------
$$ (Exam favourite)

   A(4,-1), B(-2,3) ko 2:1 mein baant-ne wala point.
     m1=2, m2=1.
     x = (2(-2) + 1(4))/3 = (-4+4)/3 = 0
     y = (2(3) + 1(-1))/3 = (6-1)/3 = 5/3
   Point = (0, 5/3).


   ------------------------------------------------
   Solved Example 4 - Find missing end (midpoint)
   ------------------------------------------------

   Midpoint (3,4) hai, ek end A(1,2). Doosra end B?
     (1+x)/2 = 3 -> x = 5
     (2+y)/2 = 4 -> y = 6
   B = (5, 6).


   ------------------------------------------------
   Solved Example 5 - Distance between 2 points
   ------------------------------------------------

   A(2,3), B(5,7). Distance?
     AB = sqrt((5-2)^2+(7-3)^2) = sqrt(9+16) = sqrt25 = 5.


   ------------------------------------------------
   Solved Example 6 - Midpoint
   ------------------------------------------------

   A(4,6), B(8,10). Midpoint?
     M = ((4+8)/2, (6+10)/2) = (6, 8).


   ------------------------------------------------
   Solved Example 7 - Distance from origin
   ------------------------------------------------

   P(6,8) ka origin se distance?
     OP = sqrt(6^2 + 8^2) = sqrt(36+64) = sqrt100 = 10.


   ------------------------------------------------
   Solved Example 8 (EASIEST) - Quadrant batao
   ------------------------------------------------

   (5,-3) kis quadrant mein? -> x +ve, y -ve -> Q4.
   (-2,-7) -> dono -ve -> Q3.


==========================================
Q AND A TIME
==========================================

   Q1. CORE: in points ka quadrant: (4,8), (-1,6), (3,-2).

   Q2. A(0,0), B(6,8) ke beech distance.

   Q3. P(3,4) ka origin se distance.

   Q4. A(-1,2), B(5,8) ka midpoint.

   Q5. A(1,2), B(7,8) ko 1:2 mein baant-ne wala point.

   Q6. Kya A(0,0),B(3,4) ke beech distance 5 hai? (Check)

   Q7. CORE CHECK: (-3)^2 kya hota hai?


==========================================
SUMMARY
==========================================

   1. Point = (x, y); x abscissa, y ordinate.

   2. Distance: sqrt[(x2-x1)^2 + (y2-y1)^2].

   3. Section (m1:m2): ((m1x2+m2x1)/(m1+m2),
      (m1y2+m2y1)/(m1+m2)).

   4. Midpoint: ((x1+x2)/2, (y1+y2)/2).

   5. Quadrants: Q1(+,+),Q2(-,+),Q3(-,-),Q4(+,-).

@@ CORE (RED page) revise: axes/origin, coordinates, signs,
@@ square aur sqrt, average, ratio.


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 7: Coordinate Geometry (Core-Basics edition)
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch7_Coordinate_Geometry.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 7: Coordinate Geometry (Core-Basics Edition)",
        content=CONTENT,
        out_path=out,
    )
