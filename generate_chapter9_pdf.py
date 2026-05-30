"""
PDF generator for Class 10 Maths Chapter 9: Some Applications of
Trigonometry (Core-Basics edition). RED core basics, GREEN exam marks,
8 solved examples (hardest -> easiest). Hinglish.
Uses shared pdf_utils.py (red '@@', green '$$', page breaks).
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 9: SOME APPLICATIONS OF TRIGONOMETRY
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

@@ 1) TRIG RATIOS (Chapter 8 recap)
@@    sin = Perp/Hyp, cos = Base/Hyp, tan = Perp/Base.


@@ 2) SPECIAL ANGLE VALUES (zaroori)
@@    tan 30 = 1/sqrt3, tan 45 = 1, tan 60 = sqrt3.
@@    sin 30 = 1/2, sin 45 = 1/sqrt2, sin 60 = sqrt3/2.


@@ 3) sqrt VALUES
@@    sqrt3 = 1.732, sqrt2 = 1.414 (decimal answer ke liye).


@@ 4) HORIZONTAL AUR VERTICAL
@@    Horizontal = leti (zameen ke parallel).
@@    Vertical = khadi (tower/building ki height).


@@ 5) RIGHT TRIANGLE BANTA HAI
@@    Tower (vertical) + zameen (horizontal) + line of sight
@@    milke right-angled triangle banate hain.


@@ 6) ALTERNATE ANGLES (parallel lines)
@@    Do horizontal lines parallel ho toh angle of
@@    elevation = angle of depression.


@@ 7) SOLVE FOR UNKNOWN
@@    tan(angle) = opposite/adjacent. Ek pata ho toh
@@    doosra nikaal lo (multiply/divide).

<<<PAGEBREAK>>>

==========================================
NOW: ASLI CHAPTER 9 SHURU
==========================================


TOPIC 1: LINE OF SIGHT
----------------------

   Line of sight = aankh se object tak ki seedhi line.


TOPIC 2: ANGLE OF ELEVATION
---------------------------

   Object UPAR ho (jaise building top), horizontal se upar
   wala angle = ANGLE OF ELEVATION (upar dekhna).


TOPIC 3: ANGLE OF DEPRESSION
----------------------------

   Object NEECHE ho (jaise cliff se boat), horizontal se
   neeche wala angle = ANGLE OF DEPRESSION (neeche dekhna).

@@   [CORE] Angle of elevation = angle of depression
@@   (alternate angles, RED page point 6).


TOPIC 4: SOLVING APPROACH
-------------------------

$$ EXAM ALERT: Har question ka same tareeka:
$$   1. Diagram banao (right triangle)
$$   2. tan/sin/cos choose karo (zyadatar tan)
$$   3. Equation banao aur solve karo

   tan = height / base (sabse zyada use hota).

<<<PAGEBREAK>>>

==========================================
SOLVED EXAMPLES: HARDEST -> EASIEST
==========================================

$$ 8 examples poori tarah solve karke. Upar HARDEST,
$$ neeche EASIEST.


   ------------------------------------------------
   Solved Example 1 (HARDEST) - Do angles (2 positions)
   ------------------------------------------------
$$ (Exam favourite)

   Tower ke base se kuch door se top ka elevation 30 hai.
   20 m paas aane par 60 ho jaata. Tower ki height?

   Let height = h, paas wali distance = x.
     tan 60 = h/x -> h = x sqrt3       ...(1)
     tan 30 = h/(x+20) -> h sqrt3 = x+20 ...(2)
   (1) ko (2) mein: (x sqrt3) sqrt3 = x + 20
     3x = x + 20 -> x = 10
     h = 10 sqrt3 = 17.32 m.


   ------------------------------------------------
   Solved Example 2 - Depression (boat)
   ------------------------------------------------
$$ (Exam favourite)

   20 m unchi cliff ke top se boat ka depression 30.
   Boat kitni door?
     (depression = elevation = 30)
     tan 30 = 20/d -> 1/sqrt3 = 20/d
     d = 20 sqrt3 = 34.64 m.


   ------------------------------------------------
   Solved Example 3 - Kite (string length)
   ------------------------------------------------
$$ (Exam favourite)

   Patang ki dori 100 m, ground se 60 angle. Patang ki
   height?
     sin 60 = h/100 -> h = 100 x (sqrt3/2) = 50 sqrt3
     h = 86.6 m.


   ------------------------------------------------
   Solved Example 4 - Simple tower (elevation 60)
   ------------------------------------------------

   Base se 30 m door, top ka elevation 60. Tower height?
     tan 60 = h/30 -> h = 30 sqrt3 = 51.96 m.


   ------------------------------------------------
   Solved Example 5 - Find distance (elevation 45)
   ------------------------------------------------

   15 m unchi building ka top, ground point ka elevation
   45. Point kitni door?
     tan 45 = 15/d -> 1 = 15/d -> d = 15 m.


   ------------------------------------------------
   Solved Example 6 - Ladder (cos)
   ------------------------------------------------

   Ladder ground se 60 angle, foot wall se 2.5 m door.
   Ladder length?
     cos 60 = 2.5/L -> 1/2 = 2.5/L -> L = 5 m.


   ------------------------------------------------
   Solved Example 7 - Tower height (45, base 40)
   ------------------------------------------------

   Base se 40 m door, elevation 45. Height?
     tan 45 = h/40 -> 1 = h/40 -> h = 40 m.


   ------------------------------------------------
   Solved Example 8 (EASIEST) - Concept
   ------------------------------------------------

   Angle of elevation aur depression mein fark?
     Elevation = object upar (upar dekhte).
     Depression = object neeche (neeche dekhte).


==========================================
Q AND A TIME
==========================================

   Q1. CORE: angle of elevation aur depression ek line mein.

   Q2. Tower base se 50 m door, elevation 45. Height nikaal.

   Q3. 30 m cliff top se boat depression 30. Boat door?
       (tan 30 = 1/sqrt3)

   Q4. Patang ki dori 200 m, ground se 30 angle. Height?
       (sin 30 = 1/2)

   Q5. Tower 60 m. Base se 60 m door se top ka elevation?
       (tan = 60/60 = 1 -> angle?)

   Q6. Tower base se kuch door se elevation 30. 10 m paas
       aane par 60. Height nikaal.

   Q7. CORE CHECK: tan 60 ki value kya hai?


==========================================
SUMMARY
==========================================

   1. Line of sight: aankh se object tak seedhi line.

   2. Elevation: object upar; Depression: object neeche.

   3. Elevation = Depression (alternate angles).

   4. Steps: diagram -> tan/sin/cos choose -> solve.

   5. tan = height/base (zyadatar use hota).

@@ CORE (RED page) revise: trig ratios, special angles,
@@ sqrt values, alternate angles, right triangle banna.


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 9: Some Applications of Trigonometry (Core-Basics edition)
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch9_Applications_of_Trigonometry.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 9: Some Applications of Trigonometry (Core-Basics Edition)",
        content=CONTENT,
        out_path=out,
    )
