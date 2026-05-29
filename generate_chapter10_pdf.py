"""
PDF generator for Class 10 Maths Chapter 10: Circles.
Uses shared pdf_utils.py.
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 10: CIRCLES
==========================================

A simplified, detailed guide in Hinglish
For students who missed Class 7-8-9
Based on the official NCERT English Medium textbook
==========================================


==========================================
SECTION 1: FOUNDATION
==========================================


1.1 CIRCLE KI BASICS (RECAP)
----------------------------

   - CIRCLE: ek point (centre) se same distance pe sabhi
     points ka set.
   - RADIUS (r): centre se circle tak ki distance.
   - DIAMETER (d): circle ke aar-paar (= 2 x radius).
   - CHORD: circle pe do points ko jodne wali line.
   - DIAMETER = sabse badi chord.


1.2 SECANT VS TANGENT (IS CHAPTER KA DIL)
-----------------------------------------

   SECANT: ek line jo circle ko DO points pe cut kare.

   TANGENT: ek line jo circle ko SIRF EK point pe touch
            kare (cut nahi karti).


             secant            tangent
          ____*____*____      ________*________
         /          \        /         |        \
        |            |      |          (touch     |
        |    O       |      |    O      point)    |
         \          /        \                   /
          \________/          \_________________/


   TANGENT ka touch point = "POINT OF CONTACT"


1.3 NUMBER OF TANGENTS
----------------------

   - Circle ke ANDAR ke point se: 0 tangents
   - Circle PE wale point se:      1 tangent
   - Circle ke BAAHAR point se:    2 tangents


==========================================
SECTION 2: THEOREM 1 (TANGENT-RADIUS)
==========================================


2.1 STATEMENT (BAHUT IMPORTANT)
-------------------------------

   "The tangent at any point of a circle is PERPENDICULAR
   to the radius through the point of contact."

   MATLAB: Tangent aur radius (touch point pe) ke beech
   ka angle hamesha 90 degree hota hai.


              tangent line
        ________*________
                |  <- 90 degree
                |
                | radius
                |
                O (centre)


2.2 USE
-------

   Jab bhi tangent involved ho, ek RIGHT-ANGLED triangle
   banta hai (radius + tangent + line to centre).
   Phir Pythagoras laga sakte hain!


2.3 EXAMPLE
-----------

   EXAMPLE 1: Ek circle ka radius 7 cm hai. Centre se
              25 cm door ek point P hai. P se tangent
              ki length nikaal.

   Tangent PT, radius OT = 7, OP = 25.
   Angle OTP = 90 (tangent perp to radius).

   Pythagoras in triangle OTP:
     OP^2 = OT^2 + PT^2
     25^2 = 7^2 + PT^2
     625 = 49 + PT^2
     PT^2 = 576
     PT = 24 cm

   Tangent length = 24 cm  (7-24-25 triplet!)


==========================================
SECTION 3: THEOREM 2 (TWO TANGENTS)
==========================================


3.1 STATEMENT (BAHUT IMPORTANT)
-------------------------------

   "The lengths of tangents drawn from an EXTERNAL point
   to a circle are EQUAL."

   MATLAB: Circle ke bahar ke ek point se 2 tangents
   khinche, dono ki length BARABAR hogi.


                    * A (touch point)
                   /|
                  / |
        P -------/  O (centre)
                \  |
                 \ |
                  \|
                   * B (touch point)

   PA = PB  (dono tangents equal)


3.2 EXTRA FACTS (from same theorem)
-----------------------------------

   - PA = PB (tangent lengths equal)
   - Centre O point P ko join kare toh OP angle APB
     ko bisect karta hai (do barabar hisse)
   - angle OPA = angle OPB


3.3 EXAMPLE
-----------

   EXAMPLE 2: P se circle pe do tangents PA aur PB
              khinche. Agar PA = 10 cm, toh PB = ?

   Theorem 2 se: PB = PA = 10 cm. (Equal tangents)


   EXAMPLE 3: Do tangents 60 degree ka angle banate
              hain point P pe. Har tangent ka touch
              centre ke saath kya angle banayega?

   angle APB = 60. OP bisect karta hai:
     angle OPA = angle OPB = 30 degree.


==========================================
SECTION 4: COMMON RESULTS
==========================================


   1. Tangent perpendicular to radius (90 degree).

   2. Tangents from external point are equal.

   3. Quadrilateral made by 2 radii + 2 tangents:
        Opposite angles sum = 180 (cyclic-like result),
        aur radius-tangent angles 90-90 hote hain.

   4. Tangent + radius + centre line = right triangle
        -> Pythagoras use karo.


==========================================
Q AND A TIME
==========================================


   Q1. Secant aur tangent mein kya difference hai?


   Q2. Circle ke bahar ke point se kitne tangents
       khinche ja sakte hain?


   Q3. Radius 8 cm. Centre se 17 cm door point P se
       tangent ki length nikaal. (Pythagoras)


   Q4. P se do tangents PA aur PB khinche. PA = 12 cm.
       PB kitna hoga? Kyun?


   Q5. Tangent aur radius ke beech (touch point pe)
       angle kitna hota hai?


   Q6. Do tangents 80 degree ka angle banate hain P pe.
       angle OPA (O = centre) kitna hoga?


==========================================
SUMMARY
==========================================


   1. Secant: 2 points pe cut. Tangent: 1 point pe touch.

   2. Tangents count:
        inside point = 0, on circle = 1, outside = 2.

   3. THEOREM 1: Tangent perpendicular to radius at
      point of contact (90 degree).

   4. THEOREM 2: Tangents from external point are equal
      (PA = PB).

   5. Tangent problems mein right triangle banta hai
      -> Pythagoras laga.


==========================================
TIPS FOR EXAM
==========================================


   1. Tangent + radius = 90 degree - ye yaad rakh, har
      tangent question mein use hota hai.

   2. External point se equal tangents (PA = PB) -
      bahut questions isi pe based hote hain.

   3. Diagram banao aur 90 degree mark karo - phir
      Pythagoras ya geometry easily lag jaati hai.

   4. Pythagorean triplets (7-24-25, 8-15-17, 3-4-5,
      5-12-13) yaad rakh - calculation fast hoti hai.

   5. Theorem statements word-to-word yaad rakh -
      exam mein "state the theorem" aata hai.


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 10: Circles
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch10_Circles.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 10: Circles",
        content=CONTENT,
        out_path=out,
    )
