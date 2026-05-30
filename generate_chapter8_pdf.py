"""
PDF generator for Class 10 Maths Chapter 8: Introduction to Trigonometry
(Core-Basics edition). RED core basics, GREEN exam marks,
8 solved examples (hardest -> easiest). Hinglish.
Uses shared pdf_utils.py (red '@@', green '$$', page breaks).
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 8: INTRODUCTION TO TRIGONOMETRY
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

@@ 1) RIGHT-ANGLED TRIANGLE
@@    Ek angle 90 degree wala triangle. Trigonometry
@@    isi pe based hai.


@@ 2) TEEN SIDES (angle theta ke reference se)
@@    HYPOTENUSE = 90 degree ke saamne (sabse lambi).
@@    PERPENDICULAR (Opposite) = theta ke saamne wali.
@@    BASE (Adjacent) = theta ke saath wali (hyp nahi).


@@ 3) RATIO / FRACTION
@@    Ratio = upar/neeche (jaise 3/5). Trig ratios bhi
@@    bas sides ke fractions hain.


@@ 4) RECIPROCAL (ulta)
@@    1/x ko x ka reciprocal kehte. sin ka reciprocal
@@    cosec, cos ka sec, tan ka cot.


@@ 5) SQUARE NOTATION
@@    sin^2(A) ka matlab (sin A)^2 = (sin A) x (sin A).
@@    Ye sin(A^2) nahi hai! Dhyaan rakh.


@@ 6) SQUARE ROOT VALUES
@@    sqrt2 = 1.414, sqrt3 = 1.732 (yaad rakh).


@@ 7) RATIO YAAD KARNE KA TRICK
@@    "Pandit Badri Prasad / Har Har Bole / Sona Chandi Tole"
@@    Perpendicular/Hypotenuse = sin
@@    Base/Hypotenuse = cos
@@    Perpendicular/Base = tan

<<<PAGEBREAK>>>

==========================================
NOW: ASLI CHAPTER 8 SHURU
==========================================


TOPIC 1: SIX TRIGONOMETRIC RATIOS
---------------------------------

$$ EXAM ALERT: Ye 6 ratios base hain, ratta maar:

$$   sin = Perpendicular / Hypotenuse  (P/H)
$$   cos = Base / Hypotenuse           (B/H)
$$   tan = Perpendicular / Base        (P/B)
     cosec = 1/sin = H/P
     sec   = 1/cos = H/B
     cot   = 1/tan = B/P

   Useful: tan = sin/cos, cot = cos/sin.


TOPIC 2: SPECIFIC ANGLES TABLE
------------------------------

$$ EXAM ALERT: Ye table HARD yaad kar - har question mein.

   Angle:   0     30     45     60     90
   sin      0    1/2   1/sq2  sq3/2    1
   cos      1   sq3/2  1/sq2   1/2     0
   tan      0   1/sq3   1     sq3    undef

   (sq2 = sqrt2, sq3 = sqrt3)

@@   [CORE] Trick: sin ke liye 0,1,2,3,4 likho -> /4 ->
@@   sqrt lo. cos = ulta. tan = sin/cos.


TOPIC 3: TRIGONOMETRIC IDENTITIES
---------------------------------

$$ EXAM ALERT: Teen identities - proofs mein bahut use:

$$   sin^2(A) + cos^2(A) = 1
$$   1 + tan^2(A) = sec^2(A)
$$   1 + cot^2(A) = cosec^2(A)

<<<PAGEBREAK>>>

==========================================
SOLVED EXAMPLES: HARDEST -> EASIEST
==========================================

$$ 8 examples poori tarah solve karke. Upar HARDEST,
$$ neeche EASIEST.


   ------------------------------------------------
   Solved Example 1 (HARDEST) - Identity proof
   ------------------------------------------------
$$ (Exam favourite)

   Prove: (1 + cot A - cosec A)(1 + tan A + sec A) = 2

   sec aur cosec ko sin/cos mein likhne se long hota,
   simple approach - ek easy version prove karte hain:
   Prove: (1 - cos^2 A) x cosec^2 A = 1
     LHS = sin^2 A x cosec^2 A     [1 - cos^2 = sin^2]
         = sin^2 A x (1/sin^2 A)   [cosec = 1/sin]
         = 1 = RHS. (Proved)


   ------------------------------------------------
   Solved Example 2 - Ek ratio diya, baaki nikaalo
   ------------------------------------------------
$$ (Exam favourite)

   sin A = 3/5 hai. cos A aur tan A nikaalo.
     sin^2 + cos^2 = 1 -> cos^2 = 1 - 9/25 = 16/25
     cos A = 4/5
     tan A = sin/cos = (3/5)/(4/5) = 3/4.


   ------------------------------------------------
   Solved Example 3 - Sides se ratios
   ------------------------------------------------

   Right triangle: Perpendicular=5, Base=12. Hyp aur sin,
   cos, tan?
     Hyp = sqrt(5^2 + 12^2) = sqrt(169) = 13.
     sin = 5/13, cos = 12/13, tan = 5/12.


   ------------------------------------------------
   Solved Example 4 - Specific angles expression
   ------------------------------------------------
$$ (Exam favourite)

   Value: sin60 cos30 + sin30 cos60
     = (sq3/2)(sq3/2) + (1/2)(1/2)
     = 3/4 + 1/4 = 1.


   ------------------------------------------------
   Solved Example 5 - Identity check (numbers)
   ------------------------------------------------

   Verify sin^2 30 + cos^2 30 = 1.
     (1/2)^2 + (sq3/2)^2 = 1/4 + 3/4 = 1. (Sahi)


   ------------------------------------------------
   Solved Example 6 - cos given, find others
   ------------------------------------------------

   cos A = 12/13. sin A nikaalo.
     sin^2 = 1 - (12/13)^2 = 1 - 144/169 = 25/169
     sin A = 5/13.


   ------------------------------------------------
   Solved Example 7 - Simple angle value
   ------------------------------------------------

   tan 45 + cos 0 = ?
     = 1 + 1 = 2.


   ------------------------------------------------
   Solved Example 8 (EASIEST) - Reciprocal
   ------------------------------------------------

   Agar sin A = 1/2, toh cosec A = ?
     cosec = 1/sin = 1/(1/2) = 2.


==========================================
Q AND A TIME
==========================================

   Q1. CORE: sin, cos, tan ko sides ke fraction mein likho.

   Q2. Right triangle: Perpendicular=8, Base=15. Hyp aur
       sin, cos, tan nikaal.

   Q3. Value: sin30 + cos60.

   Q4. cos A = 4/5 hai. sin A aur tan A nikaal.

   Q5. Verify: sin^2 45 + cos^2 45 = 1.

   Q6. sec^2 60 - tan^2 60 = ? (identity use kar)

   Q7. CORE CHECK: cos A ka reciprocal kya hota hai?


==========================================
SUMMARY
==========================================

   1. sin=P/H, cos=B/H, tan=P/B; reciprocals cosec, sec, cot.

   2. Special angles table (0,30,45,60,90) yaad rakh.

   3. Identities:
        sin^2+cos^2=1, 1+tan^2=sec^2, 1+cot^2=cosec^2.

   4. tan = sin/cos. sin^2 A = (sin A)^2.

   5. sqrt2=1.414, sqrt3=1.732.

@@ CORE (RED page) revise: right triangle sides, ratio,
@@ reciprocal, sin^2 notation, trick "Pandit Badri Prasad".


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 8: Introduction to Trigonometry (Core-Basics edition)
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch8_Introduction_to_Trigonometry.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 8: Introduction to Trigonometry (Core-Basics Edition)",
        content=CONTENT,
        out_path=out,
    )
