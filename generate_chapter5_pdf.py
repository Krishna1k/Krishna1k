"""
PDF generator for Class 10 Maths Chapter 5: Arithmetic Progressions.
Uses shared pdf_utils.py.
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 5: ARITHMETIC PROGRESSIONS
==========================================

A simplified, detailed guide in Hinglish
For students who missed Class 7-8-9
Based on the official NCERT English Medium textbook
==========================================


==========================================
SECTION 1: FOUNDATION
==========================================


1.1 SEQUENCE KYA HOTI HAI?
--------------------------

   SEQUENCE = numbers ki ek list jo kisi specific
   pattern follow karti hai.

   EXAMPLES:
     1, 3, 5, 7, 9, ...     (odd numbers)
     2, 4, 8, 16, 32, ...   (powers of 2)
     1, 4, 9, 16, 25, ...   (squares)
     5, 10, 15, 20, ...     (multiples of 5)

   Har number ko TERM kehte hain - 1st term,
   2nd term, etc.


1.2 ARITHMETIC PROGRESSION (AP) - DEFINITION
--------------------------------------------

   AP = wo sequence jisme har term, PREVIOUS term
   mein ek FIXED number ADD karke milti hai.

   Wo fixed number ko COMMON DIFFERENCE (d) kehte hain.


   EXAMPLES OF AP:
     2, 5, 8, 11, 14, ...     (d = 3)
     10, 7, 4, 1, -2, ...     (d = -3)
     5, 5, 5, 5, ...          (d = 0)
     -1, 2, 5, 8, ...         (d = 3)


   NOT AP:
     1, 4, 9, 16, ...   (squares - diff. badalti hai)
     2, 4, 8, 16, ...   (multiplication, not addition)


1.3 AP KE NOTATIONS
-------------------

   Notation       Matlab
   --------       ------
   a (or a1)      First term
   d              Common difference
   a_n            nth term
   n              Number of terms
   S_n            Sum of first n terms
   l              Last term


1.4 COMMON DIFFERENCE D KAISE NIKAALEIN?
----------------------------------------

   FORMULA: d = a_n - a_(n-1)
            (any term minus previous term)

   EXAMPLE: AP: 5, 9, 13, 17, ...
     d = 9 - 5 = 4
     d = 13 - 9 = 4   (ok)
     d = 17 - 13 = 4  (ok)

   IMPORTANT: Saare consecutive differences same
   hone chahiye, warna AP nahi hai.


1.5 GENERAL FORM OF AP
----------------------

     a, a+d, a+2d, a+3d, a+4d, ...

   So:
     1st term  = a
     2nd term  = a + d
     3rd term  = a + 2d
     4th term  = a + 3d
     nth term  = a + (n-1)d


==========================================
SECTION 2: nth TERM FORMULA
==========================================


2.1 THE FORMULA (IMPORTANT)
---------------------------

        a_n = a + (n-1) d

   Yahan:
     a_n = nth term (jo nikaalna hai)
     a   = first term
     d   = common difference
     n   = term number


2.2 EXAMPLES
------------

   EXAMPLE 1: AP 2, 5, 8, 11, ... ka 20th term

   a=2, d=3, n=20
     a_20 = 2 + (20-1)(3)
          = 2 + 57
          = 59

   Answer: 59


   EXAMPLE 2: AP ka 4th term 0 hai aur 11th term -7
              hai. AP nikaalo.

     a + 3d = 0    ...(1)
     a + 10d = -7  ...(2)

     (2) - (1): 7d = -7  ->  d = -1
     From (1): a = -3d = 3  ->  a = 3

   So AP: 3, 2, 1, 0, -1, -2, -3, -4, ...


   EXAMPLE 3: 100, 95, 90, ... ka kaunsa term -50 hai?

   a=100, d=-5, a_n = -50

     -50 = 100 + (n-1)(-5)
     -150 = -5(n-1)
     n - 1 = 30
     n = 31

   So 31st term -50 hai.


==========================================
SECTION 3: SUM OF FIRST n TERMS
==========================================


3.1 THE FORMULAS (DONO YAAD RAKH)
---------------------------------

   Formula 1 (a aur d known ho):

        S_n = (n/2) x [2a + (n-1) d]


   Formula 2 (a aur last term l known ho):

        S_n = (n/2) x (a + l)

   jahan l = last term = a_n.


   YAAD RAKH: a_n = a + (n-1)d, isliye dono
   formulas connected hain.


3.2 EXAMPLES
------------

   EXAMPLE 4: 2, 5, 8, 11, ... ke first 20 terms ka sum

   a=2, d=3, n=20
     S_20 = (20/2) x [2(2) + 19(3)]
          = 10 x [4 + 57]
          = 10 x 61
          = 610


   EXAMPLE 5: 1+2+3+...+100 (Gauss formula)

   AP: 1, 2, 3, ..., 100
   a=1, l=100, n=100

     S_100 = (100/2) x (1 + 100)
           = 50 x 101
           = 5050


   EXAMPLE 6: AP 2, 5, 8, ... ka kitne terms ka sum
              155 hoga?

   a=2, d=3, S_n = 155

     155 = (n/2)[4 + 3(n-1)]
     310 = n[3n + 1]
     3n^2 + n - 310 = 0

   Splitting (a x c = -930, sum = 1):
     31 x -30 -> sum = 1, product = -930  (ok)
     (3n + 31)(n - 10) = 0

   n = 10 (positive)

   So 10 terms.


==========================================
SECTION 4: WORD PROBLEMS
==========================================


   EXAMPLE 7: Theatre seats

   "First row mein 20 seats. Har next row mein 2
    seats zyada. 30th row mein kitne seats?"

   a=20, d=2, n=30
     a_30 = 20 + 29 x 2 = 78

   Answer: 78 seats.


   EXAMPLE 8: Salary problem

   "Starting salary Rs.8000. Har saal Rs.500 increment.
    10 saal ki total earnings?"

   AP: 8000, 8500, 9000, ...  (a=8000, d=500)

     S_10 = (10/2) x [2(8000) + 9(500)]
          = 5 x [16000 + 4500]
          = 5 x 20500
          = Rs. 1,02,500


==========================================
Q AND A TIME
==========================================


   Q1. Inn sequences mein se kaunsi AP hai? d bata.
       (a) 2, 4, 6, 8, ...
       (b) 1, 4, 9, 16, ...
       (c) -3, -1, 1, 3, ...
       (d) 1, 3, 9, 27, ...


   Q2. AP: 7, 13, 19, 25, ... ka 50th term nikaal.


   Q3. AP ka 10th term 32 hai aur 20th term 72 hai.
       AP nikaal.


   Q4. AP: 1, 4, 7, 10, ... ke first 25 terms ka sum.


   Q5. AP 9, 17, 25, ... mein kaunsa term 105 hoga?


   Q6. "Ek admi 8 din mein har din 5 km zyada distance
        cover karta hai. Pehle din 3 km. 8 dino mein
        total km?"


==========================================
SUMMARY
==========================================


   1. AP: Sequence with constant common difference d.

   2. General form: a, a+d, a+2d, a+3d, ...

   3. nth term: a_n = a + (n-1) d

   4. Sum formulas:
        S_n = (n/2)[2a + (n-1)d]   (d known)
        S_n = (n/2)(a + l)         (l known)

   5. d nikaalna: any term minus previous term.

   6. Word problems: identify a, d, n; pick formula.


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 5: Arithmetic Progressions
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch5_Arithmetic_Progressions.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 5: Arithmetic Progressions",
        content=CONTENT,
        out_path=out,
    )
