"""
PDF generator for Class 10 Maths Chapter 6: Triangles
(Core-Basics edition). RED core basics, GREEN exam marks,
8 solved examples (hardest -> easiest). Hinglish.
Uses shared pdf_utils.py (red '@@', green '$$', page breaks).
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 6: TRIANGLES
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

@@ 1) TRIANGLE
@@    3 side, 3 angle. Teeno angle ka sum = 180 degree.


@@ 2) RATIO AUR PROPORTION
@@    Ratio = tulna (4/6 = 2/3).
@@    Proportion = do ratio barabar (a/b = c/d).


@@ 3) CONGRUENT vs SIMILAR (bahut important fark)
@@    Congruent = bilkul same (shape AND size).
@@    Similar = same shape, size alag (sides PROPORTIONAL).
@@    Photo aur uski zoom copy = similar.


@@ 4) CORRESPONDING (aamne-saamne wale)
@@    Similar triangles mein corresponding angles equal
@@    aur corresponding sides proportional hote hain.
@@    Order important: ABC ~ PQR -> A=P, B=Q, C=R.


@@ 5) PARALLEL LINES (||)
@@    Do lines jo kabhi nahi milti. Symbol: ||.


@@ 6) SQUARE / SQUARE ROOT
@@    a^2 = a x a. sqrt(25) = 5.
@@    Pythagoras mein squares use hote hain.


@@ 7) PROPORTION SOLVE KARNA (cross multiply)
@@    a/b = c/d  ->  a x d = b x c.
@@    Isi se unknown side nikalti hai.

<<<PAGEBREAK>>>

==========================================
NOW: ASLI CHAPTER 6 SHURU
==========================================


TOPIC 1: SIMILAR TRIANGLES
--------------------------

   Do triangles similar hain agar:
     1. Corresponding angles equal, AUR
     2. Corresponding sides proportional.
   Likha: triangle ABC ~ triangle PQR.

@@   [CORE] "~" ka matlab similar. Order se corresponding
@@   parts pata chalte hain (RED page point 4).


TOPIC 2: BPT / THALES THEOREM
-----------------------------

$$ EXAM ALERT: BPT statement aur use HAR exam mein aata hai.

   "Agar triangle ke ek side ke parallel line baaki do
    sides ko cut kare, toh wo dono sides SAME RATIO mein
    bant-te hain."

   Agar DE || BC (triangle ABC mein), toh:
$$     AD/DB = AE/EC

   CONVERSE: agar AD/DB = AE/EC, toh DE || BC.


TOPIC 3: SIMILARITY CRITERIA
----------------------------

$$ EXAM ALERT: Ye criteria yaad rakh (similar prove karne):

$$   AA  : do angles equal -> similar (most used)
$$   SSS : teeno sides proportional -> similar
$$   SAS : do sides proportional + beech ka angle equal


TOPIC 4: PYTHAGORAS THEOREM
---------------------------

$$ EXAM ALERT: Right triangle mein:

$$   (Hypotenuse)^2 = (side1)^2 + (side2)^2

   CONVERSE: agar bada side^2 = baaki do ke squares ka sum,
   toh triangle right-angled hai.

@@   [CORE] Triplets yaad rakh: (3,4,5), (5,12,13),
@@   (8,15,17), (7,24,25). Calculation fast hoti hai.

<<<PAGEBREAK>>>

==========================================
SOLVED EXAMPLES: HARDEST -> EASIEST
==========================================

$$ 8 examples poori tarah solve karke. Upar HARDEST,
$$ neeche EASIEST.


   ------------------------------------------------
   Solved Example 1 (HARDEST) - BPT do unknown
   ------------------------------------------------
$$ (Exam favourite)

   Triangle ABC mein DE || BC. AD = x, DB = x-2,
   AE = x+2, EC = x-1. x nikaalo.

   BPT: AD/DB = AE/EC
     x/(x-2) = (x+2)/(x-1)
   Cross multiply:
     x(x-1) = (x-2)(x+2)
     x^2 - x = x^2 - 4
     -x = -4 -> x = 4.


   ------------------------------------------------
   Solved Example 2 - Similar triangles, side nikaalo
   ------------------------------------------------
$$ (Exam favourite)

   triangle ABC ~ triangle DEF. AB=6, BC=8, CA=10, DE=9.
   EF aur FD nikaalo.

   Sides proportional: AB/DE = BC/EF = CA/FD
     6/9 = 8/EF -> EF = (8 x 9)/6 = 12
     6/9 = 10/FD -> FD = (10 x 9)/6 = 15.


   ------------------------------------------------
   Solved Example 3 - Pythagoras (ladder/height)
   ------------------------------------------------
$$ (Exam favourite)

   Ek ladder wall pe lagi hai. Foot wall se 9 m door,
   ladder ki length 41 m. Wall pe kitni unchai chhui?

   h^2 + 9^2 = 41^2
     h^2 = 1681 - 81 = 1600
     h = 40 m.


   ------------------------------------------------
   Solved Example 4 - SSS similarity check
   ------------------------------------------------

   triangle ABC: 4,6,8 ; triangle DEF: 6,9,12. Similar?
     4/6 = 2/3, 6/9 = 2/3, 8/12 = 2/3 (sab same)
     Haan, similar (by SSS).


   ------------------------------------------------
   Solved Example 5 - BPT simple
   ------------------------------------------------

   DE || BC. AD=2.5, DB=3, AE=4. EC nikaalo.
     AD/DB = AE/EC -> 2.5/3 = 4/EC
     EC = (4 x 3)/2.5 = 4.8.


   ------------------------------------------------
   Solved Example 6 - Pythagoras hypotenuse
   ------------------------------------------------

   Right triangle, sides 6 aur 8. Hypotenuse?
     h^2 = 6^2 + 8^2 = 36 + 64 = 100 -> h = 10.


   ------------------------------------------------
   Solved Example 7 - Right angle check (converse)
   ------------------------------------------------

   Kya 5, 12, 13 right triangle banate hain?
     Bada side 13: 13^2 = 169.
     5^2 + 12^2 = 25 + 144 = 169 (same!)
     Haan, right-angled triangle hai.


   ------------------------------------------------
   Solved Example 8 (EASIEST) - Angle sum
   ------------------------------------------------

   Triangle ke do angle 50 aur 60 hain. Teesra?
     Teesra = 180 - (50 + 60) = 70 degree.


==========================================
Q AND A TIME
==========================================

   Q1. CORE: congruent aur similar mein fark ek line mein.

   Q2. triangle PQR ~ triangle XYZ. PQ=6, QR=8, RP=10,
       XY=9. YZ aur ZX nikaal.

   Q3. DE || BC. AD=1.5, DB=3, AE=1. EC nikaal (BPT).

   Q4. Right triangle ke sides 9 aur 12. Hypotenuse nikaal.

   Q5. Kya 8, 15, 17 right triangle ke sides hain? Check kar.

   Q6. Konsa similarity criterion: 2 angles equal hain?

   Q7. CORE CHECK: triangle ke do angle 90 aur 45 hain.
       Teesra angle?


==========================================
SUMMARY
==========================================

   1. Similar = same shape, sides proportional, angles equal.

   2. BPT: DE || BC -> AD/DB = AE/EC.

   3. Criteria: AA, SSS, SAS.

   4. Pythagoras: hyp^2 = side1^2 + side2^2.

   5. Triplets: (3,4,5),(5,12,13),(8,15,17),(7,24,25).

@@ CORE (RED page) revise: ratio/proportion, congruent vs
@@ similar, corresponding parts, cross multiply, squares.


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 6: Triangles (Core-Basics edition)
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch6_Triangles.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 6: Triangles (Core-Basics Edition)",
        content=CONTENT,
        out_path=out,
    )
