"""
PDF generator for Class 10 Maths Chapter 5: Arithmetic Progressions
(Core-Basics edition). RED core basics, GREEN exam marks,
8 solved examples (hardest -> easiest). Hinglish.
Uses shared pdf_utils.py (red '@@', green '$$', page breaks).
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 5: ARITHMETIC PROGRESSIONS
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

@@ 1) SEQUENCE KYA HAI?
@@    Sequence = numbers ki list ek pattern mein.
@@    Jaise 2, 4, 6, 8, ... ya 1, 4, 9, 16, ...


@@ 2) TERM
@@    Sequence ka har number ek "term" hai.
@@    Pehla term, doosra term, ... nth term.


@@ 3) DIFFERENCE NIKAALNA
@@    Do terms ka antar = baad wala - pehle wala.
@@    5, 9 -> 9 - 5 = 4. (Negative bhi ho sakta hai.)


@@ 4) VARIABLE / FORMULA SAMAJHNA
@@    a = pehla term, d = common difference,
@@    n = term number, a_n = nth term, S_n = n terms ka sum.


@@ 5) SUBSTITUTION
@@    Formula mein values daal ke calculate karna.
@@    a_n = a + (n-1)d mein a,d,n daal do.


@@ 6) BASIC ALGEBRA (do equations)
@@    Kabhi 2 equations milti hain (a aur d ke liye).
@@    Subtract karke ek variable gayab karte hain.


@@ 7) NEGATIVE NUMBERS
@@    d negative ho toh sequence ghatti hai:
@@    10, 7, 4, 1, ... (d = -3).

<<<PAGEBREAK>>>

==========================================
NOW: ASLI CHAPTER 5 SHURU
==========================================


TOPIC 1: AP KYA HAI?
--------------------

   AP = sequence jisme har term, pichle term mein ek FIXED
   number (common difference d) add karke milta hai.

   Examples: 2,5,8,11 (d=3) ; 10,7,4 (d=-3) ; 5,5,5 (d=0).

@@   [CORE] d = koi bhi do consecutive terms ka antar
@@   (baad wala - pehle wala). Saare antar same hone chahiye.

   General form: a, a+d, a+2d, a+3d, ...


TOPIC 2: nth TERM FORMULA
-------------------------

$$ EXAM ALERT: Ye formula har AP question mein use hota:

$$   a_n = a + (n - 1) d

   a = pehla term, d = common diff, n = kaunsa term.


TOPIC 3: SUM OF FIRST n TERMS
-----------------------------

$$ EXAM ALERT: Dono sum formulas yaad rakh:

$$   S_n = (n/2) [ 2a + (n-1)d ]      (a aur d se)
$$   S_n = (n/2) (a + l)              (l = last term)

   (Doosra formula tab use jab last term l pata ho.)

<<<PAGEBREAK>>>

==========================================
SOLVED EXAMPLES: HARDEST -> EASIEST
==========================================

$$ 8 examples poori tarah solve karke. Upar HARDEST,
$$ neeche EASIEST.


   ------------------------------------------------
   Solved Example 1 (HARDEST) - Sum diya, n nikaalo
   ------------------------------------------------
$$ (Exam favourite - quadratic ban jaata hai)

   AP 2, 5, 8, ... ke kitne terms ka sum 155 hai?

   a=2, d=3, S_n=155.
     155 = (n/2)[2(2) + (n-1)3]
     310 = n[4 + 3n - 3] = n[3n + 1]
     3n^2 + n - 310 = 0
   Split (ac = -930, sum = 1 -> 31, -30):
     3n^2 + 31n - 30n - 310 = 0
     (3n + 31)(n - 10) = 0
     n = 10 (positive lo)

   Answer: 10 terms.


   ------------------------------------------------
   Solved Example 2 - Do terms diye, AP nikaalo
   ------------------------------------------------
$$ (Exam favourite - 2 equations)

   AP ka 4th term 0 hai aur 11th term -7 hai. AP nikaalo.

     a + 3d = 0     ...(1)
     a + 10d = -7   ...(2)
   (2)-(1): 7d = -7 -> d = -1
   (1): a = -3d = 3
   AP: 3, 2, 1, 0, -1, ...


   ------------------------------------------------
   Solved Example 3 - Kaunsa term diya value pe
   ------------------------------------------------

   100, 95, 90, ... ka kaunsa term -50 hai?
     a=100, d=-5, a_n=-50.
     -50 = 100 + (n-1)(-5)
     -150 = -5(n-1) -> n-1 = 30 -> n = 31
   Answer: 31st term.


   ------------------------------------------------
   Solved Example 4 - Sum of n terms
   ------------------------------------------------

   2, 5, 8, ... ke first 20 terms ka sum.
     a=2, d=3, n=20.
     S_20 = (20/2)[2(2) + 19(3)] = 10[4 + 57] = 610.


   ------------------------------------------------
   Solved Example 5 - Word problem (seats/salary)
   ------------------------------------------------
$$ (Exam favourite)

   Theatre ki first row mein 20 seats, har agli row mein
   2 zyada. 30th row mein kitni seats?
     a=20, d=2, n=30.
     a_30 = 20 + 29(2) = 20 + 58 = 78 seats.


   ------------------------------------------------
   Solved Example 6 - nth term basic
   ------------------------------------------------

   7, 13, 19, 25, ... ka 50th term.
     a=7, d=6.
     a_50 = 7 + 49(6) = 7 + 294 = 301.


   ------------------------------------------------
   Solved Example 7 - Sum 1 to 100 (Gauss)
   ------------------------------------------------

   1+2+3+...+100 ka sum.
     a=1, l=100, n=100.
     S_100 = (100/2)(1 + 100) = 50 x 101 = 5050.


   ------------------------------------------------
   Solved Example 8 (EASIEST) - d nikaalo, AP check
   ------------------------------------------------

   Kya 3, 7, 11, 15 AP hai? d kya?
     7-3=4, 11-7=4, 15-11=4. Saare antar same.
     Haan AP hai, d = 4.


==========================================
Q AND A TIME
==========================================

   Q1. CORE: kya 1, 4, 9, 16 AP hai? Kyun/kyun nahi?

   Q2. AP 5, 9, 13, ... ka 20th term nikaal.

   Q3. AP ka 10th term 32, 16th term 56 hai. d nikaal.

   Q4. AP 3, 7, 11, ... ke first 15 terms ka sum.

   Q5. 10, 7, 4, ... ka kaunsa term -20 hai?

   Q6. AP 2, 5, 8, ... ke kitne terms ka sum 95 hai?

   Q7. CORE CHECK: a=4, d=3 wali AP ke pehle 4 terms likho.


==========================================
SUMMARY
==========================================

   1. AP: har term mein fixed d add hota hai.

   2. nth term: a_n = a + (n-1)d.

   3. Sum: S_n = (n/2)[2a + (n-1)d]  ya  (n/2)(a + l).

   4. d = baad wala term - pehle wala (sab same hone chahiye).

   5. Word problems: a, d, n pehchaano -> formula lagao.

@@ CORE (RED page) revise: sequence, term, d nikaalna,
@@ substitution, negative numbers.


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 5: Arithmetic Progressions (Core-Basics edition)
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch5_Arithmetic_Progressions.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 5: Arithmetic Progressions (Core-Basics Edition)",
        content=CONTENT,
        out_path=out,
    )
