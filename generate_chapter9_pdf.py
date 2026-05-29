"""
PDF generator for Class 10 Maths Chapter 9: Some Applications of Trigonometry.
Uses shared pdf_utils.py.
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 9: SOME APPLICATIONS OF TRIGONOMETRY
==========================================

A simplified, detailed guide in Hinglish
For students who missed Class 7-8-9
Based on the official NCERT English Medium textbook
==========================================


==========================================
SECTION 1: FOUNDATION
==========================================


1.1 IS CHAPTER MEIN KYA HAI?
----------------------------

   Chapter 8 mein trigonometry seekhi. Ab use real-life
   mein lagayenge - HEIGHTS aur DISTANCES nikaalne ke liye.

   Bina pahaadi/building pe chadhe uski height nikaal sakte
   hain - sirf angle aur distance se! Ye magic trig se hota.


1.2 LINE OF SIGHT
-----------------

   LINE OF SIGHT = aankh se object tak ki seedhi line
   (jab hum kisi cheez ko dekhte hain).


1.3 ANGLE OF ELEVATION (Upar dekhna)
------------------------------------

   Jab object hamse UPAR ho (jaise building ka top), toh
   horizontal line se upar wala angle = ANGLE OF ELEVATION.


                        * (top of tower)
                       /|
                      / |
       line of sight /  |
                    /   |
                   /    |
        (eye) ____/_____|
              angle of
              elevation
            (horizontal line)


1.4 ANGLE OF DEPRESSION (Neeche dekhna)
---------------------------------------

   Jab object hamse NEECHE ho (jaise cliff se boat dekhna),
   toh horizontal line se neeche wala angle = ANGLE OF
   DEPRESSION.


        (eye)________________ horizontal
              \  angle of
               \ depression
                \
                 \ line of sight
                  \
                   * (boat below)


   IMPORTANT FACT:
     Angle of elevation (neeche se upar)
       = Angle of depression (upar se neeche)
     (Alternate angles - parallel horizontal lines)


==========================================
SECTION 2: KEY APPROACH (HOW TO SOLVE)
==========================================


2.1 STEPS TO SOLVE ANY PROBLEM
------------------------------

   1. DIAGRAM banao (right triangle banta hai)
   2. Known angle aur known side mark karo
   3. Unknown (height/distance) ko x maan lo
   4. Decide karo konsa ratio use karna hai:

        sin = Opp/Hyp   ->  use jab Hyp involved
        cos = Adj/Hyp   ->  use jab Hyp involved
        tan = Opp/Adj   ->  MOST USED (height & base)

   5. Equation banao aur solve karo


2.2 SPECIAL ANGLE VALUES (RECAP)
--------------------------------

   tan 30 = 1/sqrt3 = 0.577
   tan 45 = 1
   tan 60 = sqrt3 = 1.732

   (Height/distance problems mein zyadatar tan use hota)


==========================================
SECTION 3: WORKED EXAMPLES
==========================================


   EXAMPLE 1: SIMPLE TOWER

   "Ek tower ki base se 30 m door khade ho. Tower ke top
    ka angle of elevation 60 degree hai. Tower ki height?"

   Diagram: right triangle
     Base = 30 m, angle = 60, height = h (opposite)

   Use tan (opp/adj):
     tan 60 = h / 30
     sqrt3 = h / 30
     h = 30 x sqrt3 = 30 x 1.732
     h = 51.96 m

   Tower ki height = 30*sqrt3 m (approx 51.96 m)


   EXAMPLE 2: FINDING DISTANCE

   "Ek 15 m unchi building ke top se ek car ka angle of
    depression 45 degree hai. Car building se kitni door?"

   Angle of depression = angle of elevation = 45 (alternate)
     height = 15 m, distance = d

   tan 45 = 15 / d
     1 = 15 / d
     d = 15 m

   Car 15 m door hai.


   EXAMPLE 3: LADDER PROBLEM

   "Ek ladder wall se 60 degree angle banati hai. Ladder
    ka foot wall se 2.5 m door hai. Ladder ki length?"

   Here: base (adjacent) = 2.5 m, ladder = hypotenuse = L
   angle with ground = 60

   cos 60 = adj / hyp = 2.5 / L
     1/2 = 2.5 / L
     L = 5 m

   Ladder ki length = 5 m


   EXAMPLE 4: TWO ANGLES (slightly harder)

   "Ek tower ke base se kuch door se top ka angle of
    elevation 30 hai. 20 m aur paas aane par 60 ho jaata.
    Tower ki height nikaal."

   Let height = h, near distance (from base) = x.
   Far point = (x + 20).

   From near point: tan 60 = h/x   ->  h = x*sqrt3   ...(1)
   From far point:  tan 30 = h/(x+20)
                    1/sqrt3 = h/(x+20)
                    h*sqrt3 = x + 20   ...(2)

   Put (1) in (2):
     (x*sqrt3)*sqrt3 = x + 20
     3x = x + 20
     2x = 20
     x = 10

   h = x*sqrt3 = 10*sqrt3 = 17.32 m

   Tower height = 10*sqrt3 m (approx 17.32 m)


==========================================
Q AND A TIME
==========================================


   Q1. Angle of elevation aur angle of depression mein
       kya difference hai? Ek line mein bata.


   Q2. "Tower ki base se 40 m door se top ka angle of
        elevation 45 hai. Tower ki height?"


   Q3. "Ek 20 m unchi cliff ke top se boat ka angle of
        depression 30 hai. Boat kitni door hai?"
        (tan 30 = 1/sqrt3 use kar)


   Q4. "Ek patang (kite) ki dori 100 m lambi hai aur
        ground se 30 degree angle banati hai. Patang ki
        height kitni hai?"  (sin 30 = 1/2 use kar)


   Q5. Ek tower 50*sqrt3 m unchi hai. Uski base se kuch
       door se top ka angle of elevation 60 hai. Door
       ki distance nikaal.


==========================================
SUMMARY
==========================================


   1. Line of sight: aankh se object tak seedhi line.

   2. Angle of ELEVATION: object upar ho (upar dekhna).

   3. Angle of DEPRESSION: object neeche ho (neeche dekhna).

   4. Elevation angle = Depression angle (alternate angles).

   5. Solving steps:
        - Diagram banao
        - tan/sin/cos choose karo
        - Equation banao aur solve karo

   6. tan zyadatar use hota hai (height aur base ka rishta).


==========================================
TIPS FOR EXAM
==========================================


   1. DIAGRAM zaroor banao - aadha kaam wahin ho jaata hai.

   2. Angle of depression ko triangle ke andar wale angle
      mein convert kar (alternate angle = elevation).

   3. tan = height/base yaad rakh - 90% problems isi se.

   4. Answer mein sqrt3 = 1.732, sqrt2 = 1.414 use karke
      decimal bhi likh sakte ho (agar poocha jaye).

   5. Units (m, km) final answer mein likhna mat bhoolna.


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 9: Some Applications of Trigonometry
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch9_Applications_of_Trigonometry.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 9: Some Applications of Trigonometry",
        content=CONTENT,
        out_path=out,
    )
