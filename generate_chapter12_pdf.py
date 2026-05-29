"""
PDF generator for Class 10 Maths Chapter 12: Surface Areas and Volumes.
Uses shared pdf_utils.py.
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 12: SURFACE AREAS AND VOLUMES
==========================================

A simplified, detailed guide in Hinglish
For students who missed Class 7-8-9
Based on the official NCERT English Medium textbook
==========================================


==========================================
SECTION 1: FOUNDATION
==========================================


1.1 SURFACE AREA VS VOLUME
--------------------------

   SURFACE AREA (SA): solid ke bahar ki total area
   (paint karne layak). Unit = cm^2 / m^2.

   VOLUME: solid ke andar ki jagah (paani bharne layak).
   Unit = cm^3 / m^3.

   Do tarah ki surface area:
     - CSA (Curved/Lateral): sirf curved/side part
       (top-bottom chhod ke)
     - TSA (Total): sab kuch (curved + flat faces)


1.2 pi REMINDER
---------------

   pi = 22/7 (radius 7 ka multiple) ya 3.14


==========================================
SECTION 2: BASIC SOLIDS KE FORMULAS
==========================================


2.1 CUBE (side = a)
-------------------
   TSA    = 6 a^2
   Volume = a^3


2.2 CUBOID (l, b, h)
--------------------
   TSA    = 2(lb + bh + hl)
   Volume = l x b x h


2.3 CYLINDER (radius r, height h)
---------------------------------
   CSA    = 2 pi r h
   TSA    = 2 pi r (r + h)
   Volume = pi r^2 h


2.4 CONE (radius r, height h, slant l)
--------------------------------------
   slant height l = sqrt(r^2 + h^2)
   CSA    = pi r l
   TSA    = pi r (l + r)
   Volume = (1/3) pi r^2 h


2.5 SPHERE (radius r)
---------------------
   Surface Area = 4 pi r^2
   Volume       = (4/3) pi r^3


2.6 HEMISPHERE (radius r) - aadha sphere
----------------------------------------
   CSA    = 2 pi r^2
   TSA    = 3 pi r^2  (curved + flat circle)
   Volume = (2/3) pi r^3


==========================================
SECTION 3: EXAMPLES (SINGLE SOLIDS)
==========================================


   EXAMPLE 1: Cylinder r=7 cm, h=10 cm. Volume & CSA.
              (pi = 22/7)

     Volume = pi r^2 h = (22/7) x 7 x 7 x 10
            = 22 x 7 x 10 = 1540 cm^3
     CSA = 2 pi r h = 2 x (22/7) x 7 x 10 = 440 cm^2


   EXAMPLE 2: Cone r=6 cm, h=8 cm. Slant & volume.

     l = sqrt(r^2 + h^2) = sqrt(36 + 64) = sqrt 100 = 10 cm
     Volume = (1/3) pi r^2 h
            = (1/3) x 3.14 x 36 x 8 = 301.44 cm^3


   EXAMPLE 3: Sphere r=7 cm. Surface area. (pi = 22/7)

     SA = 4 pi r^2 = 4 x (22/7) x 7 x 7
        = 4 x 22 x 7 = 616 cm^2


==========================================
SECTION 4: COMBINATION OF SOLIDS
==========================================


   Class 10 mein zyadatar solids JODKE banaye jaate hain -
   jaise ice-cream (cone + hemisphere), capsule (cylinder
   + 2 hemispheres), etc.


4.1 GOLDEN RULE
---------------

   Jab solids jodte hain:
     - Surface area: sirf EXPOSED (dikhne wale) surfaces
       ADD karo. (chhupa hua surface mat ginna)
     - Volume: hamesha simply ADD karo.


4.2 EXAMPLE 4: ICE-CREAM (cone + hemisphere on top)
---------------------------------------------------

   Cone (r=3.5, h=12) ke upar hemisphere (r=3.5).
   Total volume. (pi = 22/7)

     Cone vol = (1/3) pi r^2 h
              = (1/3) x (22/7) x 3.5 x 3.5 x 12
              = 154 cm^3

     Hemisphere vol = (2/3) pi r^3
                    = (2/3) x (22/7) x 42.875
                    = 89.83 cm^3 (approx)

     Total = 154 + 89.83 = 243.83 cm^3 (approx)


4.3 SURFACE AREA LOGIC (CAPSULE)
--------------------------------

   Capsule = cylinder + 2 hemispheres (ends).
     Total SA = (CSA cylinder) + 2 x (CSA hemisphere)
              = 2 pi r h + 2 x (2 pi r^2)
     Cylinder ke flat ends count NAHI (hemisphere se dhake).


==========================================
SECTION 5: FRUSTUM OF A CONE (ADVANCED)
==========================================


   FRUSTUM = cone ka upar wala hissa kaat do, neeche
   jo bachta hai (jaise bucket, glass).

   Radii R (bada, neeche), r (chhota, upar), height h:

     slant l = sqrt(h^2 + (R - r)^2)
     CSA     = pi (R + r) l
     TSA     = pi (R + r) l + pi R^2 + pi r^2
     Volume  = (1/3) pi h (R^2 + r^2 + R r)


==========================================
Q AND A TIME
==========================================


   Q1. Cube ka side 5 cm. TSA aur volume nikaal.


   Q2. Cylinder r=7 cm, h=20 cm. Volume. (pi = 22/7)


   Q3. Cone r=9 cm, h=12 cm. Slant height l nikaal.


   Q4. Sphere r=3 cm. Volume nikaal. (pi = 3.14)


   Q5. Capsule (cylinder + 2 hemispheres) ka surface
       area kaise nikaalte hain? Logic bata.


   Q6. Hemisphere ka TSA aur CSA mein kya difference?
       (formula bata)


==========================================
SUMMARY (FORMULA CHEAT SHEET)
==========================================


   Solid       CSA/LSA      TSA/SA          Volume
   ---------   ----------   -------------   -----------
   Cube        4a^2         6a^2            a^3
   Cuboid      2h(l+b)      2(lb+bh+hl)     lbh
   Cylinder    2 pi r h     2 pi r(r+h)     pi r^2 h
   Cone        pi r l       pi r(l+r)       (1/3)pi r^2 h
   Sphere      -            4 pi r^2        (4/3)pi r^3
   Hemisphere  2 pi r^2     3 pi r^2        (2/3)pi r^3

   Combination rule:
     SA -> only EXPOSED surfaces add karo
     Volume -> simply add

   Cone slant: l = sqrt(r^2 + h^2)


==========================================
TIPS FOR EXAM
==========================================


   1. Saare formulas ki cheat sheet HARD yaad kar -
      ye chapter pura formula-based hai.

   2. Combination problems mein diagram banao aur decide
      karo konsa surface dikhta hai (exposed) - wahi add.

   3. Volume hamesha simply add hota hai - SA mein
      dhyaan rakhna padta hai.

   4. Units check kar: SA -> cm^2, Volume -> cm^3.

   5. Cone mein l (slant) aur h (height) alag hote hain -
      l = sqrt(r^2 + h^2). Confuse mat ho.


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 12: Surface Areas and Volumes
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch12_Surface_Areas_and_Volumes.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 12: Surface Areas and Volumes",
        content=CONTENT,
        out_path=out,
    )
