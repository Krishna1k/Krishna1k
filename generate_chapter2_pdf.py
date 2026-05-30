"""
PDF generator for Class 10 Maths Chapter 2: Polynomials (Core-Basics edition).

Rebuilt for a student who skipped Class 7-8-9:
  - Dedicated RED "Core Basics" page (prerequisites, must not miss).
  - GREEN = topics that come in exams again and again.
  - 8 fully-solved examples ordered HARDEST -> EASIEST.
  - Detailed but trimmed of unnecessary clutter.

Uses shared pdf_utils.py (red via '@@', green via '$$', page breaks).
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 2: POLYNOMIALS
==========================================

A simplified, detailed guide in Hinglish
Special edition for students who skipped Class 7-8-9
==========================================

   IS PDF MEIN RANG KA MATLAB:
@@ RED text = core basic / prerequisite (Class 7-8-9 ka).
@@ Ye woh cheezein hain jo tujhe pehle se aani chahiye thi.
$$ GREEN text = exam mein BAAR-BAAR aata hai (zaroor yaad rakh).
   (Aur black = normal explanation.)

   Agle page pe SAARE core basics (RED) ek saath diye hain.
   Phir asli Chapter 2, solved examples, aur Q&A.

<<<PAGEBREAK>>>

==========================================
@@ CORE BASICS - MISS MAT KARNA (RED PAGE)
==========================================

@@ Ye page sirf un cheezon ka hai jo Class 7-8-9 mein
@@ padhayi jaati hain. 10th ka Chapter 2 inhi pe khada hai.


@@ 1) VARIABLE AUR CONSTANT
@@    Variable = badalne wala (jaise x, y) - unknown number.
@@    Constant = fixed number (jaise 5, -3, 1/2).


@@ 2) POWER / EXPONENT
@@    x^2 = x times x. x^3 = x times x times x.
@@    x^2 ko "x square", x^3 ko "x cube" bolte hain.


@@ 3) POLYNOMIAL KYA HAI?
@@    Polynomial = expression jisme variable ke power
@@    sirf WHOLE numbers ho (0,1,2,3...) - negative ya
@@    fraction power nahi.
@@    Hai:   2x+3, x^2-5x+6, 7
@@    Nahi:  x^(-1)+2, sqrt(x)+1 (in mein galat power)


@@ 4) DEGREE
@@    Degree = polynomial ka sabse bada power.
@@    2x+5 -> degree 1, x^2-3x+1 -> degree 2.


@@ 5) TYPES (degree ke hisab se)
@@    Degree 1 = LINEAR   : ax + b
@@    Degree 2 = QUADRATIC: ax^2 + bx + c
@@    Degree 3 = CUBIC    : ax^3 + bx^2 + cx + d
@@    (a hamesha != 0 hona chahiye.)


@@ 6) COEFFICIENT
@@    Coefficient = variable ke aage wala number.
@@    3x^2 - 5x + 7 mein:  a=3 (x^2 ka), b=-5 (x ka),
@@    c=7 (constant). Inhi ko a,b,c bolenge.


@@ 7) p(x) NOTATION AUR SUBSTITUTION
@@    p(x) = polynomial ka naam.
@@    p(2) = x ki jagah 2 daal do.
@@    p(x)=x^2-4 -> p(2) = 2^2 - 4 = 0.


@@ 8) ZERO / ROOT OF POLYNOMIAL
@@    Zero = woh x jiske liye p(x) = 0 ho jaye.
@@    p(x)=2x-6 -> 2x-6=0 -> x=3. So zero = 3.
@@    (Graph jahan x-axis ko cut kare, wahi zero hota hai.)


@@ 9) FACTORISATION (splitting middle term) - recap
@@    ax^2+bx+c ko (..)(..) mein todna.
@@    Middle term b ko 2 numbers p,q mein todo jahan
@@    p+q = b  AND  p x q = a x c.


@@ 10) GRAPH BASICS
@@    X-axis = leti (horizontal) line, Y-axis = khadi.
@@    Linear ka graph = seedhi line.
@@    Quadratic ka graph = "U" ya ulta "U" (PARABOLA).
@@    Graph jahan x-axis ko touch/cut kare = zero.

<<<PAGEBREAK>>>

==========================================
NOW: ASLI CHAPTER 2 SHURU
==========================================


TOPIC 1: GEOMETRICAL MEANING OF ZEROES
--------------------------------------

   Polynomial ka graph x-axis ko jitni baar CUT karta hai,
   utne uske ZEROES hote hain.

   - LINEAR (ax+b): graph seedhi line, x-axis ko 1 baar
     cut -> 1 zero.
   - QUADRATIC (ax^2+bx+c): graph PARABOLA (U shape).
       * x-axis ko 2 jagah cut -> 2 zeroes
       * 1 jagah touch          -> 1 zero (repeated)
       * cut hi nahi karta      -> 0 real zeroes
   - CUBIC: x-axis ko zyada se zyada 3 baar -> up to 3 zeroes.

@@   [CORE] "Cut karna" = graph aur x-axis ka milna.
@@   Wahi point zero hota hai (RED page point 8 & 10).


TOPIC 2: ZEROES AUR COEFFICIENTS KA RISHTA
------------------------------------------

$$ EXAM ALERT: Ye relationship aur ispe based questions
$$ HAR exam mein aate hain. Formula ratta maar lo.

   QUADRATIC p(x) = ax^2 + bx + c ke liye, agar zeroes
   alpha aur beta hain:

$$   Sum of zeroes:     alpha + beta = -b/a
$$   Product of zeroes: alpha x beta =  c/a

   (Yaad: sum mein -b/a, product mein c/a.)

   EXAMPLE: x^2 - 5x + 6 (a=1, b=-5, c=6)
     Sum     = -b/a = -(-5)/1 = 5
     Product =  c/a = 6/1     = 6
     (Zeroes 2 aur 3: 2+3=5 ok, 2x3=6 ok.)

   CUBIC (ax^3+bx^2+cx+d) ke liye (sirf jaan-kaari):
     sum = -b/a, sum of pairs = c/a, product = -d/a.


TOPIC 3: QUADRATIC POLYNOMIAL BANANA (sum & product se)
-------------------------------------------------------

$$ EXAM ALERT: "Sum aur product diya hai, polynomial
$$ banao" - ye bhi baar-baar aata hai. Formula:

$$   Polynomial = x^2 - (sum)x + (product)
$$              = x^2 - (alpha+beta)x + (alpha x beta)

   EXAMPLE: sum = 5, product = 6 ho toh
     polynomial = x^2 - 5x + 6.

<<<PAGEBREAK>>>

==========================================
SOLVED EXAMPLES: HARDEST -> EASIEST
==========================================

$$ Ye 8 examples poori tarah solve karke dikhaye hain.
$$ Step-by-step padh - "kaise solve karte hain" samajh aayega.
   (Upar HARDEST, neeche jaake EASIEST hote jaate hain.)


   ------------------------------------------------
   Solved Example 1 (HARDEST) - alpha^2 + beta^2 etc.
   ------------------------------------------------
$$ (Exam favourite - identities ka use)

   alpha, beta zeroes hain x^2 - 5x + 6 ke. Nikaalo:
   (a) alpha^2 + beta^2     (b) 1/alpha + 1/beta

   Pehle: alpha+beta = 5,  alpha x beta = 6.

   (a) alpha^2 + beta^2 = (alpha+beta)^2 - 2(alpha x beta)
                        = 5^2 - 2(6) = 25 - 12 = 13

   (b) 1/alpha + 1/beta = (alpha+beta)/(alpha x beta)
                        = 5/6


   ------------------------------------------------
   Solved Example 2 - Ek zero diya ho
   ------------------------------------------------
$$ (Exam favourite)

   x^2 - 4x + k ka ek zero 3 hai. k aur doosra zero?

   3 zero hai -> p(3)=0:
     3^2 - 4(3) + k = 0  ->  9 - 12 + k = 0  ->  k = 3
   Product of zeroes = c/a = k/1 = 3.
     3 x (doosra) = 3  ->  doosra zero = 1.
   (Check sum: 3+1 = 4 = -b/a = 4. ok)


   ------------------------------------------------
   Solved Example 3 - Zeroes nikaal + verify rishta
   ------------------------------------------------
$$ (Exam favourite - factorisation + relationship)

   6x^2 - 7x - 3 ke zeroes nikaalo aur rishta verify karo.

   Split middle term: a x c = 6 x (-3) = -18,
   do numbers jinka sum -7, product -18 -> -9 aur +2.
     6x^2 - 9x + 2x - 3
     3x(2x - 3) + 1(2x - 3)
     (2x - 3)(3x + 1)
   Zeroes: 2x-3=0 -> x=3/2 ; 3x+1=0 -> x=-1/3

   Verify:
     Sum = 3/2 + (-1/3) = 9/6 - 2/6 = 7/6 = -b/a = 7/6  (ok)
     Product = (3/2)(-1/3) = -1/2 = c/a = -3/6 = -1/2 (ok)


   ------------------------------------------------
   Solved Example 4 - Polynomial banao (zeroes diye)
   ------------------------------------------------
$$ (Exam favourite)

   Zeroes 3 aur -2 wala quadratic banao.
     Sum = 3 + (-2) = 1
     Product = 3 x (-2) = -6
     Polynomial = x^2 - (sum)x + product
                = x^2 - (1)x + (-6)
                = x^2 - x - 6


   ------------------------------------------------
   Solved Example 5 - Polynomial banao (sum/product diye)
   ------------------------------------------------

   Sum = -3, Product = 2 wala quadratic.
     Polynomial = x^2 - (sum)x + product
                = x^2 - (-3)x + 2
                = x^2 + 3x + 2


   ------------------------------------------------
   Solved Example 6 - Graph se zeroes count
   ------------------------------------------------

   Graph dekh ke zeroes batao:
     - x-axis ko 2 jagah cut kare -> 2 zeroes
     - 1 jagah sirf touch kare    -> 1 zero (repeated)
     - x-axis ko chhuye hi nahi   -> 0 real zeroes
   (Number of zeroes = number of cutting points.)


   ------------------------------------------------
   Solved Example 7 - Verify rishta (simple)
   ------------------------------------------------

   x^2 - 2x - 8 ke zeroes aur rishta.
     Factor: (x - 4)(x + 2) -> zeroes 4 aur -2.
     Sum = 4 + (-2) = 2 = -b/a = 2 (ok)
     Product = 4 x (-2) = -8 = c/a = -8 (ok)


   ------------------------------------------------
   Solved Example 8 (EASIEST) - Linear zero & p(2)
   ------------------------------------------------

   (a) 2x - 6 ka zero: 2x - 6 = 0 -> x = 3.
   (b) p(x) = x^2 - 4 -> p(2) = 2^2 - 4 = 0.
       (Matlab 2 bhi ek zero hai is polynomial ka.)


==========================================
Q AND A TIME
==========================================

   (Pehle khud try kar, phir mujhe bhej - main check karunga)

   Q1. p(x) = 3x^2 + 5x - 2 ka degree aur type bata.

   Q2. p(x) = x^2 - 4 ke liye p(2) aur p(-2) nikaal.

   Q3. x^2 - 7x + 12 ke zeroes nikaal aur sum/product
       rishta verify kar.

   Q4. Zeroes 5 aur -3 wala quadratic polynomial banao.

   Q5. Sum = 4, Product = -5 wala quadratic banao.

   Q6. alpha, beta zeroes hain x^2 - 6x + 8 ke.
       alpha^2 + beta^2 nikaal.

   Q7. CORE CHECK: x^(-1) + 3 polynomial hai ya nahi? Kyun?

   Q8. CORE CHECK: 2x^2 + 3x - 1 mein a, b, c kya hain?


==========================================
SUMMARY
==========================================

   1. Zeroes = jahan p(x) = 0 (graph x-axis ko cut kare).

   2. Number of zeroes = graph x-axis ko jitni baar cut kare
      (linear 1, quadratic up to 2, cubic up to 3).

   3. Quadratic ax^2+bx+c ke liye:
        Sum of zeroes     = -b/a
        Product of zeroes =  c/a

   4. Polynomial banao: x^2 - (sum)x + (product).

   5. Useful identity: alpha^2 + beta^2
        = (alpha+beta)^2 - 2(alpha x beta).

@@ CORE BASICS (RED page) revise karna - polynomial,
@@ degree, coefficient (a,b,c), zero, p(x), parabola.


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 2: Polynomials (Core-Basics edition)
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch2_Polynomials.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 2: Polynomials (Core-Basics Edition)",
        content=CONTENT,
        out_path=out,
    )
