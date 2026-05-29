"""
PDF generator for Class 10 Maths Chapter 7: Coordinate Geometry.
Uses shared pdf_utils.py.
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 7: COORDINATE GEOMETRY
==========================================

A simplified, detailed guide in Hinglish
For students who missed Class 7-8-9
Based on the official NCERT English Medium textbook
==========================================


==========================================
SECTION 1: FOUNDATION
==========================================


1.1 COORDINATE GEOMETRY KYA HAI?
--------------------------------

   Coordinate Geometry = geometry ko numbers/algebra se
   jodne ka tareeka. Points ko numbers (coordinates) se
   represent karte hain aur graph paper pe plot karte hain.


1.2 CARTESIAN PLANE (RECAP)
---------------------------

   Do lines milti hain:
     - X-axis -> horizontal (leti hui)
     - Y-axis -> vertical (khadi)
     - Meeting point = ORIGIN (0, 0)


                  Y-axis
                    |
          Q2        |        Q1
       (-x, +y)     |     (+x, +y)
                    |
      --------------O-------------- X-axis
                    |
          Q3        |        Q4
       (-x, -y)     |     (+x, -y)
                    |


1.3 COORDINATES OF A POINT
--------------------------

   Har point ko (x, y) se likhte hain:
     - x = ABSCISSA -> X-axis pe distance
                       (right +ve, left -ve)
     - y = ORDINATE -> Y-axis pe distance
                       (up +ve, down -ve)

   IMPORTANT: Order matters!
   (3, 5) aur (5, 3) alag points hain.


1.4 FOUR QUADRANTS
------------------

   Quadrant   x sign   y sign   Example
   --------   ------   ------   ----------
   Q1         +        +        (3, 4)
   Q2         -        +        (-3, 4)
   Q3         -        -        (-3, -4)
   Q4         +        -        (3, -4)

   SPECIAL POINTS:
     Origin = (0, 0)
     On X-axis -> y = 0, jaise (5, 0)
     On Y-axis -> x = 0, jaise (0, 7)


==========================================
SECTION 2: DISTANCE FORMULA
==========================================


2.1 THE FORMULA (IMPORTANT)
---------------------------

   Do points A(x1, y1) aur B(x2, y2) ke beech distance:

        AB = sqrt[ (x2 - x1)^2 + (y2 - y1)^2 ]

   KAHAN SE AAYA? Ye PYTHAGORAS theorem se banaa hai!
   (x diff)^2 + (y diff)^2 = (distance)^2


2.2 DISTANCE FROM ORIGIN
------------------------

   Point P(x, y) ka origin (0,0) se distance:

        OP = sqrt( x^2 + y^2 )


2.3 EXAMPLES
------------

   EXAMPLE 1: A(2, 3) aur B(5, 7) ke beech distance

     AB = sqrt[ (5-2)^2 + (7-3)^2 ]
        = sqrt[ 3^2 + 4^2 ]
        = sqrt[ 9 + 16 ]
        = sqrt 25
        = 5

   Distance = 5 units


   EXAMPLE 2: P(-4, 3) ka origin se distance

     OP = sqrt[ (-4)^2 + 3^2 ]
        = sqrt[ 16 + 9 ]
        = sqrt 25
        = 5

   Distance = 5 units


   EXAMPLE 3: Kya A(1,5), B(2,3), C(-2,-11) collinear?

   Collinear = ek hi line pe. Check: AB + BC = AC?

     AB = sqrt[ (2-1)^2 + (3-5)^2 ]  = sqrt 5
     BC = sqrt[ (-2-2)^2 + (-11-3)^2 ] = sqrt 212
     AC = sqrt[ (-2-1)^2 + (-11-5)^2 ] = sqrt 265

   AB + BC != AC  ->  Not collinear.


==========================================
SECTION 3: SECTION FORMULA
==========================================


3.1 KYA HAI?
------------

   Agar point P, line segment AB ko m1 : m2 ratio mein
   INTERNALLY divide karta hai, toh P ke coordinates:

     P(x, y) =
       ( (m1*x2 + m2*x1)/(m1 + m2) ,
         (m1*y2 + m2*y1)/(m1 + m2) )

   jahan A = (x1, y1), B = (x2, y2).


3.2 EXAMPLE
-----------

   EXAMPLE 4: A(4, -1) aur B(-2, 3) ko 2:1 ratio mein
              divide karne wala point.

   m1=2, m2=1

     x = (2*(-2) + 1*4)/(2+1) = (-4 + 4)/3 = 0
     y = (2*3 + 1*(-1))/(2+1) = (6 - 1)/3 = 5/3

   Point = (0, 5/3)


==========================================
SECTION 4: MIDPOINT FORMULA
==========================================


4.1 THE FORMULA
---------------

   MIDPOINT = jab point segment ko exactly beech mein
   (1:1) divide kare.

     Midpoint M =
       ( (x1 + x2)/2 , (y1 + y2)/2 )

   (Bas dono x ka average, dono y ka average!)


4.2 EXAMPLES
------------

   EXAMPLE 5: A(4, 6) aur B(8, 10) ka midpoint

     M = ( (4+8)/2 , (6+10)/2 )
       = ( 12/2 , 16/2 )
       = (6, 8)

   Midpoint = (6, 8)


   EXAMPLE 6: Midpoint (3, 4) hai, ek end A(1, 2).
              Doosra end B nikaal.

   Let B = (x, y).
     (1+x)/2 = 3  ->  x = 5
     (2+y)/2 = 4  ->  y = 6

   B = (5, 6)


==========================================
Q AND A TIME
==========================================


   Q1. Inn points ka quadrant bata:
       (a) (5, -3)
       (b) (-2, -7)
       (c) (4, 8)
       (d) (-1, 6)


   Q2. A(0, 0) aur B(6, 8) ke beech distance nikaal.


   Q3. P(3, 4) ka origin se distance kya hai?


   Q4. A(-1, 2) aur B(5, 8) ka midpoint nikaal.


   Q5. A(1, 2) aur B(7, 8) ko 1:2 ratio mein divide
       karne wala point nikaal (section formula).


   Q6. Check: kya A(0,0), B(3,4) ke beech distance 5 hai?
       (Pythagorean triplet use kar)


==========================================
SUMMARY
==========================================


   1. Point: (x, y) -> x = abscissa, y = ordinate.
      Order matters!

   2. Quadrants: Q1(+,+), Q2(-,+), Q3(-,-), Q4(+,-)

   3. Distance Formula:
        AB = sqrt[ (x2-x1)^2 + (y2-y1)^2 ]

   4. Distance from origin: sqrt(x^2 + y^2)

   5. Section Formula (m1:m2):
        ( (m1*x2+m2*x1)/(m1+m2) ,
          (m1*y2+m2*y1)/(m1+m2) )

   6. Midpoint Formula:
        ( (x1+x2)/2 , (y1+y2)/2 )


==========================================
TIPS FOR EXAM
==========================================


   1. Distance formula mein x aur y differences ko square
      karte ho - sign apne aap positive ho jaata hai,
      tension mat le.

   2. Pythagorean triplets (3-4-5, 5-12-13) yaad rakh -
      distance jaldi nikaal sakta hai.

   3. Midpoint = section formula ka special case (1:1).
      Alag se ratnumbers daalne ki zarurat nahi.

   4. Section formula mein dhyaan rakh: m1 ko x2/y2 ke
      saath multiply karte hain (cross pattern).

   5. Collinear check: 3 points ke distances nikaalo,
      do chhote ka sum = bada wala ho toh collinear.


==========================================
NOTE
==========================================

   Latest NCERT (2023-24) syllabus mein "Area of Triangle"
   wala topic Coordinate Geometry se hata diya gaya hai,
   isliye yahan include nahi kiya.


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 7: Coordinate Geometry
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch7_Coordinate_Geometry.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 7: Coordinate Geometry",
        content=CONTENT,
        out_path=out,
    )
