"""
PDF generator for Class 10 Maths Chapter 12: Surface Areas and Volumes
(Core-Basics edition). RED core basics, GREEN exam marks,
8 solved examples (hardest -> easiest). Hinglish.
Uses shared pdf_utils.py (red '@@', green '$$', page breaks).
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 12: SURFACE AREAS AND VOLUMES
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

@@ 1) SURFACE AREA vs VOLUME
@@    Surface Area = bahar ki area (paint, unit cm^2).
@@    Volume = andar ki jagah (paani, unit cm^3).


@@ 2) CSA vs TSA
@@    CSA = Curved/side surface (top-bottom chhod ke).
@@    TSA = Total surface (sab milake).


@@ 3) pi (PI)
@@    pi = 22/7 (radius 7 ka multiple) ya 3.14.


@@ 4) SQUARE AUR CUBE
@@    a^2 = a x a (area). a^3 = a x a x a (volume).


@@ 5) SQUARE ROOT (slant height ke liye)
@@    sqrt(r^2 + h^2). Cone mein slant height aise nikalti.


@@ 6) BASIC SHAPES KE NAAM
@@    Cube, Cuboid, Cylinder (belan), Cone (shanku),
@@    Sphere (gol), Hemisphere (aadha sphere).


@@ 7) UNITS
@@    Area -> cm^2, Volume -> cm^3. Mat bhoolna.

<<<PAGEBREAK>>>

==========================================
NOW: ASLI CHAPTER 12 SHURU
==========================================


TOPIC 1: FORMULA SHEET (yaad rakh)
----------------------------------

$$ EXAM ALERT: Saare formula ratta maar - chapter inhi pe.

   CUBE (side a):      TSA = 6a^2 ;  Vol = a^3
   CUBOID (l,b,h):     TSA = 2(lb+bh+hl) ; Vol = lbh
$$   CYLINDER (r,h):  CSA = 2 pi r h ; TSA = 2 pi r(r+h)
$$                    Vol = pi r^2 h
$$   CONE (r,h,l):    CSA = pi r l ; TSA = pi r(l+r)
$$                    Vol = (1/3) pi r^2 h ; l = sqrt(r^2+h^2)
$$   SPHERE (r):      SA = 4 pi r^2 ; Vol = (4/3) pi r^3
$$   HEMISPHERE (r):  CSA = 2 pi r^2 ; TSA = 3 pi r^2
$$                    Vol = (2/3) pi r^3


TOPIC 2: COMBINATION OF SOLIDS
------------------------------

$$ EXAM ALERT: Class 10 mein solids JODKE aate hain
$$ (ice-cream = cone+hemisphere, capsule = cylinder+2 hemi).

   GOLDEN RULE:
$$   - Surface area: sirf DIKHNE wale (exposed) surface add.
$$   - Volume: hamesha simply ADD karo.

<<<PAGEBREAK>>>

==========================================
SOLVED EXAMPLES: HARDEST -> EASIEST
==========================================

$$ 8 examples poori tarah solve karke. Upar HARDEST,
$$ neeche EASIEST.


   ------------------------------------------------
   Solved Example 1 (HARDEST) - Combination volume
   ------------------------------------------------
$$ (Exam favourite - ice cream)

   Cone (r=3.5, h=12) ke upar hemisphere (r=3.5). Total
   volume? (pi=22/7)
     Cone vol = (1/3)(22/7)(3.5)^2(12)
              = (1/3)(22/7)(12.25)(12) = 154 cm^3
     Hemi vol = (2/3)(22/7)(3.5)^3
              = (2/3)(22/7)(42.875) = 89.83 cm^3
     Total = 154 + 89.83 = 243.83 cm^3 (approx).


   ------------------------------------------------
   Solved Example 2 - Combination surface area
   ------------------------------------------------
$$ (Exam favourite - capsule)

   Capsule = cylinder (r=3.5, h=10) + 2 hemisphere (r=3.5).
   Total surface area? (pi=22/7)
     Cylinder CSA = 2(22/7)(3.5)(10) = 220
     2 hemi = 2 x 2(22/7)(3.5)^2 = 2 x 77 = 154
     Total SA = 220 + 154 = 374 cm^2.
   (Cylinder ke flat ends count NAHI - hemi se dhake.)


   ------------------------------------------------
   Solved Example 3 - Cone slant + volume
   ------------------------------------------------

   Cone r=6, h=8. Slant l aur volume? (pi=3.14)
     l = sqrt(6^2 + 8^2) = sqrt(100) = 10
     Vol = (1/3)(3.14)(36)(8) = 301.44 cm^3.


   ------------------------------------------------
   Solved Example 4 - Cylinder volume + CSA
   ------------------------------------------------

   Cylinder r=7, h=10. Vol aur CSA? (pi=22/7)
     Vol = (22/7)(49)(10) = 1540 cm^3
     CSA = 2(22/7)(7)(10) = 440 cm^2.


   ------------------------------------------------
   Solved Example 5 - Sphere SA + volume
   ------------------------------------------------

   Sphere r=7. SA aur volume? (pi=22/7)
     SA = 4(22/7)(49) = 616 cm^2
     Vol = (4/3)(22/7)(343) = 1437.33 cm^3 (approx).


   ------------------------------------------------
   Solved Example 6 - Cube
   ------------------------------------------------

   Cube side 5. TSA aur volume?
     TSA = 6(5)^2 = 150 cm^2
     Vol = 5^3 = 125 cm^3.


   ------------------------------------------------
   Solved Example 7 - Cuboid
   ------------------------------------------------

   Cuboid 4x3x2. TSA aur volume?
     TSA = 2(4x3 + 3x2 + 2x4) = 2(12+6+8) = 52 cm^2
     Vol = 4 x 3 x 2 = 24 cm^3.


   ------------------------------------------------
   Solved Example 8 (EASIEST) - Hemisphere volume
   ------------------------------------------------

   Hemisphere r=3. Volume? (pi=3.14)
     Vol = (2/3)(3.14)(27) = 56.52 cm^3.


==========================================
Q AND A TIME
==========================================

   Q1. CORE: cylinder ka volume aur CSA formula likho.

   Q2. Cube side 6. TSA aur volume nikaal.

   Q3. Cylinder r=7, h=20. Volume. (pi=22/7)

   Q4. Cone r=9, h=12. Slant height l nikaal.

   Q5. Sphere r=3. Volume. (pi=3.14)

   Q6. Capsule (cylinder + 2 hemisphere) ka surface area
       kaise nikaalte hain? Logic bata.

   Q7. CORE CHECK: area aur volume ke units kya hote hain?


==========================================
SUMMARY
==========================================

   1. Cube: TSA=6a^2, Vol=a^3. Cuboid: TSA=2(lb+bh+hl),
      Vol=lbh.

   2. Cylinder: CSA=2 pi r h, Vol=pi r^2 h.

   3. Cone: CSA=pi r l, Vol=(1/3)pi r^2 h, l=sqrt(r^2+h^2).

   4. Sphere: SA=4 pi r^2, Vol=(4/3)pi r^3.
      Hemisphere: TSA=3 pi r^2, Vol=(2/3)pi r^3.

   5. Combination: SA -> only exposed add; Volume -> add.

@@ CORE (RED page) revise: SA vs Volume, CSA vs TSA, pi,
@@ square vs cube, slant height sqrt, units.


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 12: Surface Areas and Volumes (Core-Basics edition)
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch12_Surface_Areas_and_Volumes.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 12: Surface Areas and Volumes (Core-Basics Edition)",
        content=CONTENT,
        out_path=out,
    )
