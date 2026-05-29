"""
PDF generator for Class 10 Maths Chapter 13: Statistics.
Uses shared pdf_utils.py.
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 13: STATISTICS
==========================================

A simplified, detailed guide in Hinglish
For students who missed Class 7-8-9
Based on the official NCERT English Medium textbook
==========================================


==========================================
SECTION 1: FOUNDATION
==========================================


1.1 STATISTICS KYA HAI?
-----------------------

   STATISTICS = data ko collect, organize, aur analyse
   karne ki vidya. Is chapter mein GROUPED data
   (intervals mein bante data) ka central tendency
   nikaalte hain.


1.2 TEEN CENTRAL TENDENCY MEASURES
----------------------------------

   MEAN (average): sab values ka total / count
   MEDIAN: beech wali value (sort karne ke baad)
   MODE: sabse zyada baar aane wali value


1.3 GROUPED DATA KE TERMS
-------------------------

   Example data:

     Class Interval    Frequency (fi)
     --------------    --------------
     0-10              5
     10-20             8
     20-30             12

   - CLASS INTERVAL: range (jaise 0-10)
   - FREQUENCY (fi): us interval mein kitne items
   - CLASS MARK (xi): interval ka midpoint
                      = (upper + lower)/2
       0-10 ka class mark = (0+10)/2 = 5


==========================================
SECTION 2: MEAN OF GROUPED DATA (3 METHODS)
==========================================


2.1 METHOD 1: DIRECT METHOD
---------------------------

   Mean = Sum(fi xi) / Sum(fi)

   STEPS:
     1. Har interval ka class mark xi nikaalo
     2. fi x xi nikaalo har row
     3. Sum(fi xi) aur Sum(fi) ka total
     4. Divide karo


   EXAMPLE 1:

     CI       fi    xi    fi*xi
     -----    --    --    -----
     0-10     5     5     25
     10-20    8     15    120
     20-30    12    25    300
     30-40    5     35    175
     -----    --          ----
     Total    30          620

     Mean = 620 / 30 = 20.67


2.2 METHOD 2: ASSUMED MEAN METHOD
---------------------------------

   Jab numbers bade ho, assumed mean 'a' le lo
   (usually beech wala class mark), deviation di = xi - a.

     Mean = a + ( Sum(fi di) / Sum(fi) )


2.3 METHOD 3: STEP DEVIATION METHOD
-----------------------------------

   Jab class size h saman ho:

     ui = (xi - a) / h

     Mean = a + h x ( Sum(fi ui) / Sum(fi) )

   (Calculation aur easy - chhote numbers)


==========================================
SECTION 3: MODE OF GROUPED DATA
==========================================


3.1 MODAL CLASS
---------------

   MODAL CLASS = sabse zyada frequency wala interval.


3.2 FORMULA
-----------

   Mode = l + [ (f1 - f0) / (2 f1 - f0 - f2) ] x h

   l  = modal class ka lower limit
   f1 = modal class ki frequency
   f0 = modal class se PEHLE wali frequency
   f2 = modal class ke BAAD wali frequency
   h  = class size


3.3 EXAMPLE 2
-------------

     CI       Frequency
     -----    ---------
     0-10     3
     10-20    8     <- f0
     20-30    12    <- f1 (modal class)
     30-40    7     <- f2

     l = 20, f1 = 12, f0 = 8, f2 = 7, h = 10

     Mode = 20 + [(12-8)/(2*12 - 8 - 7)] x 10
          = 20 + [4/(24-15)] x 10
          = 20 + (4/9) x 10
          = 20 + 4.44
          = 24.44


==========================================
SECTION 4: MEDIAN OF GROUPED DATA
==========================================


4.1 MEDIAN CLASS
----------------

   Pehle CUMULATIVE FREQUENCY (cf) nikaalo (frequencies
   add karte jao). Phir n/2 dekho - jis class mein n/2
   aata hai wahi MEDIAN CLASS.


4.2 FORMULA
-----------

   Median = l + [ (n/2 - cf) / f ] x h

   l  = median class ka lower limit
   n  = total frequency (Sum fi)
   cf = median class se PEHLE wali cumulative frequency
   f  = median class ki frequency
   h  = class size


4.3 EXAMPLE 3
-------------

     CI       f     cf
     -----    --    --
     0-10     5     5
     10-20    8     13
     20-30    12    25   <- median class
     30-40    5     30

     n = 30, so n/2 = 15
     n/2 = 15 first crosses at cf = 25 -> class 20-30
     l = 20, cf(before) = 13, f = 12, h = 10

     Median = 20 + [(15 - 13)/12] x 10
            = 20 + (2/12) x 10
            = 20 + 1.67
            = 21.67


==========================================
SECTION 5: EMPIRICAL RELATIONSHIP
==========================================


   In teeno ke beech approximate relation:

     3 Median = Mode + 2 Mean

   (Ya: Mode = 3 Median - 2 Mean)

   Ek nikaalna ho aur do pata ho toh ye use kar sakte ho.


==========================================
Q AND A TIME
==========================================


   Q1. Class interval 30-40 ka class mark (xi) kya hoga?


   Q2. Mean nikaal (direct method):
         CI       fi
         0-10     4
         10-20    6
         20-30    10


   Q3. Mode formula likho aur batao f0, f1, f2 kya hote.


   Q4. Median formula mein cf ka kya matlab hai?


   Q5. Agar Mean = 30 aur Median = 28, empirical relation
       se Mode nikaal.


   Q6. Modal class aur median class mein kya difference?


==========================================
SUMMARY
==========================================


   1. Class mark xi = (upper + lower)/2

   2. Mean (Direct): xbar = Sum(fi xi) / Sum(fi)

   3. Mean (Step dev): xbar = a + h(Sum(fi ui)/Sum fi),
      ui = (xi - a)/h

   4. Mode: l + [(f1-f0)/(2 f1 - f0 - f2)] x h

   5. Median: l + [(n/2 - cf)/f] x h

   6. Empirical: 3 Median = Mode + 2 Mean


==========================================
TIPS FOR EXAM
==========================================


   1. Table banao with columns: CI, fi, xi, fi*xi (mean),
      ya cf (median). Organized rehne se mistake nahi.

   2. Mode: pehle modal class (max frequency) dhundo,
      phir formula. f0 aur f2 ko sahi pick karo.

   3. Median: cumulative frequency table zaroor banao,
      n/2 cross karne wali class = median class.

   4. Step deviation method bade numbers mein time
      bachata hai - prefer karo.

   5. Empirical relation se shortcut nikaal sakte ho
      agar do measures diye ho.


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 13: Statistics
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch13_Statistics.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 13: Statistics",
        content=CONTENT,
        out_path=out,
    )
