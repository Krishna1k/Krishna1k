"""
PDF generator for Class 10 Maths Chapter 10: Circles
(Core-Basics edition). RED core basics, GREEN exam marks,
8 solved examples (hardest -> easiest). Hinglish.
Uses shared pdf_utils.py (red '@@', green '$$', page breaks).
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 10: CIRCLES
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

@@ 1) CIRCLE KE PARTS
@@    Centre = beech ka point. Radius (r) = centre se
@@    circle tak. Diameter = 2r. Chord = circle pe do
@@    points ko jodne wali line.


@@ 2) PERPENDICULAR (90 degree)
@@    Do lines jo 90 degree pe milti hain. Symbol: chhota
@@    square corner pe.


@@ 3) RIGHT TRIANGLE + PYTHAGORAS
@@    90 degree wale triangle mein:
@@    hyp^2 = side1^2 + side2^2.


@@ 4) SQUARE / SQUARE ROOT
@@    a^2 = a x a. sqrt(100) = 10.
@@    Tangent ki length nikaalne mein use hota.


@@ 5) TANGENT vs SECANT (is chapter ka dil)
@@    SECANT = line jo circle ko 2 points pe CUT kare.
@@    TANGENT = line jo circle ko 1 point pe TOUCH kare.
@@    Touch point = "point of contact".


@@ 6) NUMBER OF TANGENTS
@@    Andar ke point se: 0. Circle pe: 1. Bahar se: 2.


@@ 7) ANGLE BISECTOR
@@    Ek line jo angle ko 2 barabar hisson mein baant-ti hai.

<<<PAGEBREAK>>>

==========================================
NOW: ASLI CHAPTER 10 SHURU
==========================================


TOPIC 1: TANGENT TO A CIRCLE
----------------------------

   Tangent = line jo circle ko sirf 1 point pe touch kare
   (cut nahi karti). Us point ko point of contact kehte.


TOPIC 2: THEOREM 1 (TANGENT-RADIUS)
-----------------------------------

$$ EXAM ALERT: "Tangent radius ke perpendicular hota hai" -
$$ statement aur use har exam mein.

   "Point of contact pe tangent, radius ke PERPENDICULAR
    (90 degree) hota hai."

@@   [CORE] Isi se right triangle banta hai (radius +
@@   tangent + centre line) -> Pythagoras laga sakte ho.


TOPIC 3: THEOREM 2 (TWO TANGENTS)
---------------------------------

$$ EXAM ALERT: "Bahar ke point se 2 tangents barabar hote
$$ hain" - bahut questions ispe.

   "External point se circle pe khinchi do tangents ki
    LENGTH barabar hoti hai (PA = PB)."

   Extra: centre se point join karo -> wo angle APB ko
   bisect karta hai.

<<<PAGEBREAK>>>

==========================================
SOLVED EXAMPLES: HARDEST -> EASIEST
==========================================

$$ 8 examples poori tarah solve karke. Upar HARDEST,
$$ neeche EASIEST.


   ------------------------------------------------
   Solved Example 1 (HARDEST) - Two tangents + angle
   ------------------------------------------------
$$ (Exam favourite)

   P se do tangents PA, PB khinche. Angle APB = 60.
   Prove triangle PAB equilateral (sab side barabar).

     PA = PB (equal tangents) -> triangle isosceles.
     Isosceles mein base angles barabar:
       angle PAB = angle PBA.
     Sum of angles = 180:
       60 + 2(angle PAB) = 180 -> angle PAB = 60.
     Saare angle 60 -> equilateral triangle. (Proved)


   ------------------------------------------------
   Solved Example 2 - Tangent length (Pythagoras)
   ------------------------------------------------
$$ (Exam favourite)

   Radius 7 cm. Centre se 25 cm door point P. Tangent
   length PT?
     Angle OTP = 90 (tangent perp radius).
     OP^2 = OT^2 + PT^2
     25^2 = 7^2 + PT^2 -> PT^2 = 625-49 = 576
     PT = 24 cm. (7-24-25 triplet!)


   ------------------------------------------------
   Solved Example 3 - Angle between tangents
   ------------------------------------------------
$$ (Exam favourite)

   Tangents 70 ka angle banate hain P pe. Radius aur
   tangent ke beech ka angle (centre wale quadrilateral se):
     OAPB quadrilateral: angle OAP = angle OBP = 90.
     Sum = 360 -> angle AOB = 360 - 90 - 90 - 70 = 110.


   ------------------------------------------------
   Solved Example 4 - Equal tangents
   ------------------------------------------------

   P se PA aur PB tangents. PA = 10 cm. PB?
     Equal tangents -> PB = PA = 10 cm.


   ------------------------------------------------
   Solved Example 5 - Tangent length (8-15-17)
   ------------------------------------------------

   Radius 8 cm, centre se 17 cm door. Tangent length?
     PT^2 = 17^2 - 8^2 = 289 - 64 = 225 -> PT = 15 cm.


   ------------------------------------------------
   Solved Example 6 - Bisected angle
   ------------------------------------------------

   Tangents 80 ka angle banate P pe. angle OPA?
     OP bisect karta hai -> angle OPA = 80/2 = 40.


   ------------------------------------------------
   Solved Example 7 - Tangent-radius angle
   ------------------------------------------------

   Tangent aur radius (point of contact pe) ke beech angle?
     Hamesha 90 degree (Theorem 1).


   ------------------------------------------------
   Solved Example 8 (EASIEST) - Number of tangents
   ------------------------------------------------

   Circle ke bahar ke point se kitne tangents?
     2 tangents (bahar ke point se hamesha 2).


==========================================
Q AND A TIME
==========================================

   Q1. CORE: secant aur tangent mein fark ek line mein.

   Q2. Radius 9 cm, centre se 15 cm door point. Tangent
       length nikaal. (Pythagoras)

   Q3. P se PA, PB tangents. PA = 12 cm. PB?

   Q4. Tangent aur radius ke beech (contact point pe) angle?

   Q5. Tangents 90 ka angle P pe. angle OPA?

   Q6. Circle ke andar ke point se kitne tangents khinch
       sakte hain?

   Q7. CORE CHECK: 5-12-13 triplet use karke - radius 5,
       tangent 12 ho toh OP (centre se distance)?


==========================================
SUMMARY
==========================================

   1. Tangent = 1 point pe touch; Secant = 2 points pe cut.

   2. Theorem 1: tangent point of contact pe radius ke
      perpendicular (90).

   3. Theorem 2: external point se 2 tangents barabar
      (PA = PB).

   4. Tangent problems mein right triangle banta hai ->
      Pythagoras.

   5. Tangents count: inside 0, on circle 1, outside 2.

@@ CORE (RED page) revise: circle parts, perpendicular,
@@ Pythagoras, tangent vs secant, number of tangents.


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 10: Circles (Core-Basics edition)
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch10_Circles.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 10: Circles (Core-Basics Edition)",
        content=CONTENT,
        out_path=out,
    )
