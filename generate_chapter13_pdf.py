"""
PDF generator for Class 10 Maths Chapter 13: Statistics
(Core-Basics edition). RED core basics, GREEN exam marks,
8 solved examples (hardest -> easiest). Hinglish.
Uses shared pdf_utils.py (red '@@', green '$$', page breaks).
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 13: STATISTICS
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

@@ 1) DATA
@@    Data = collected numbers/observations.
@@    Grouped data = intervals mein bata hua (0-10, 10-20).


@@ 2) MEAN, MEDIAN, MODE (basic meaning)
@@    Mean = average. Median = beech wali value.
@@    Mode = sabse zyada baar aane wali value.


@@ 3) CLASS INTERVAL AUR FREQUENCY
@@    Class interval = range (jaise 10-20).
@@    Frequency (fi) = us interval mein kitne items.


@@ 4) CLASS MARK (xi)
@@    Class mark = interval ka midpoint
@@    = (upper + lower)/2. (0-10 -> 5)


@@ 5) SUMMATION (sigma)
@@    Sum(fi) = saari frequencies ka total.
@@    Sum(fi xi) = har (fi x xi) ka total.


@@ 6) AVERAGE NIKAALNA
@@    Average = total / count. Mean isi pe based hai.


@@ 7) CUMULATIVE FREQUENCY (cf)
@@    cf = frequencies ko add karte jao (running total).
@@    Median nikaalne ke liye zaroori.

<<<PAGEBREAK>>>

==========================================
NOW: ASLI CHAPTER 13 SHURU
==========================================


TOPIC 1: MEAN OF GROUPED DATA
-----------------------------

$$ EXAM ALERT: Mean (direct method) bahut aata hai:

$$   Mean = Sum(fi xi) / Sum(fi)

   Steps: class mark xi nikaalo -> fi*xi -> dono ke sum
   -> divide.

   (Assumed-mean aur step-deviation alternate methods hain
    jab numbers bade ho.)


TOPIC 2: MODE OF GROUPED DATA
-----------------------------

$$ EXAM ALERT: Mode formula:

$$   Mode = l + [ (f1 - f0) / (2 f1 - f0 - f2) ] x h

   l = modal class lower limit, f1 = uski frequency,
   f0 = pehle wali, f2 = baad wali, h = class size.
   Modal class = sabse zyada frequency wala interval.


TOPIC 3: MEDIAN OF GROUPED DATA
-------------------------------

$$ EXAM ALERT: Median formula:

$$   Median = l + [ (n/2 - cf) / f ] x h

   Pehle cumulative frequency banao. n/2 jis class mein
   aaye = median class. cf = uske pehle wali cf,
   f = uski frequency, h = class size.


TOPIC 4: EMPIRICAL RELATIONSHIP
-------------------------------

$$   3 Median = Mode + 2 Mean

   (Do pata ho toh teesra nikaal sakte ho.)

<<<PAGEBREAK>>>

==========================================
SOLVED EXAMPLES: HARDEST -> EASIEST
==========================================

$$ 8 examples poori tarah solve karke. Upar HARDEST,
$$ neeche EASIEST.


   ------------------------------------------------
   Solved Example 1 (HARDEST) - Median (full table)
   ------------------------------------------------
$$ (Exam favourite)

   CI: 0-10,10-20,20-30,30-40 ; f: 5,8,12,5.
   Median nikaalo.

   cf: 5, 13, 25, 30. n=30, n/2=15.
   n/2=15 pehli baar cf=25 (class 20-30) pe cross hota.
   Median class = 20-30: l=20, cf(before)=13, f=12, h=10.
     Median = 20 + [(15-13)/12] x 10
            = 20 + (2/12)x10 = 20 + 1.67 = 21.67.


   ------------------------------------------------
   Solved Example 2 - Mean (direct method)
   ------------------------------------------------
$$ (Exam favourite)

   CI: 0-10,10-20,20-30,30-40 ; f: 5,8,12,5.
   xi: 5,15,25,35. fi*xi: 25,120,300,175.
     Sum(fi)=30, Sum(fi*xi)=620.
     Mean = 620/30 = 20.67.


   ------------------------------------------------
   Solved Example 3 - Mode
   ------------------------------------------------
$$ (Exam favourite)

   CI: 0-10,10-20,20-30,30-40 ; f: 3,8,12,7.
   Modal class = 20-30 (max freq 12).
     l=20, f1=12, f0=8, f2=7, h=10.
     Mode = 20 + [(12-8)/(24-8-7)] x 10
          = 20 + (4/9)x10 = 20 + 4.44 = 24.44.


   ------------------------------------------------
   Solved Example 4 - Empirical relation
   ------------------------------------------------

   Mean=30, Median=28. Mode nikaalo.
     Mode = 3 Median - 2 Mean = 3(28) - 2(30)
          = 84 - 60 = 24.


   ------------------------------------------------
   Solved Example 5 - Class mark
   ------------------------------------------------

   30-40 ka class mark? -> (30+40)/2 = 35.


   ------------------------------------------------
   Solved Example 6 - Simple mean
   ------------------------------------------------

   CI: 0-10,10-20,20-30 ; f: 4,6,10.
   xi: 5,15,25. fi*xi: 20,90,250 -> sum=360. Sum(fi)=20.
     Mean = 360/20 = 18.


   ------------------------------------------------
   Solved Example 7 - Cumulative frequency
   ------------------------------------------------

   f: 5,8,12,5. cf banao.
     cf = 5, 13, 25, 30.


   ------------------------------------------------
   Solved Example 8 (EASIEST) - Modal class
   ------------------------------------------------

   f: 3,8,12,7. Modal class konsa?
     Max frequency 12 -> modal class wahi interval.


==========================================
Q AND A TIME
==========================================

   Q1. CORE: 20-30 ka class mark kya hoga?

   Q2. Mean nikaal: CI 0-10,10-20,20-30 ; f 4,6,10.

   Q3. Mode formula likho aur f0,f1,f2 kya hote hain bata.

   Q4. Mean=25, Median=24. Empirical se Mode nikaal.

   Q5. f: 6,10,8,4. Cumulative frequency banao.

   Q6. Median formula mein cf ka matlab kya hai?

   Q7. CORE CHECK: mean kaise nikaalte hain (formula)?


==========================================
SUMMARY
==========================================

   1. Class mark xi = (upper + lower)/2.

   2. Mean = Sum(fi xi) / Sum(fi).

   3. Mode = l + [(f1-f0)/(2f1-f0-f2)] x h.

   4. Median = l + [(n/2 - cf)/f] x h.

   5. 3 Median = Mode + 2 Mean.

@@ CORE (RED page) revise: data, mean/median/mode meaning,
@@ class mark, frequency, summation, cumulative frequency.


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 13: Statistics (Core-Basics edition)
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch13_Statistics.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 13: Statistics (Core-Basics Edition)",
        content=CONTENT,
        out_path=out,
    )
