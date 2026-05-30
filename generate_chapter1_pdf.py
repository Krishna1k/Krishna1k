"""
PDF generator for Class 10 Maths Chapter 1: Real Numbers (Core-Basics edition).

This version is rebuilt for a student who skipped Class 7-8-9:
  - A dedicated RED "Core Basics" page of prerequisites (must not miss).
  - Core/extra concepts highlighted in RED throughout (lines marked '@@').
  - Detailed but trimmed of unnecessary clutter.

Uses shared pdf_utils.py (red via '@@', green via '$$', page breaks).
  - RED  = core basics / prerequisites (Class 7-8-9).
  - GREEN = topics asked in exams again and again (frequently asked).
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 1: REAL NUMBERS
==========================================

A simplified, detailed guide in Hinglish
Special edition for students who skipped Class 7-8-9
Core basics (RED) ko miss mat karna!
==========================================

   IS PDF MEIN RANG KA MATLAB:
@@ RED text = core basic / prerequisite (Class 7-8-9 ka).
@@ Ye woh cheezein hain jo tujhe pehle se aani chahiye thi.
$$ GREEN text = exam mein BAAR-BAAR aata hai (zaroor yaad rakh).
   (Aur black = normal explanation.)

   Agle page pe SAARE core basics (RED) ek saath diye hain.
   Phir asli Chapter 1, solved examples, aur Q&A.

<<<PAGEBREAK>>>

==========================================
@@ CORE BASICS - MISS MAT KARNA (RED PAGE)
==========================================

@@ Ye page sirf un cheezon ka hai jo Class 7-8-9 mein
@@ padhayi jaati hain. 10th ka Chapter 1 inhi pe khada hai.


@@ 1) FACTOR KYA HOTA HAI?
@@    Factor = jo number kisi doosre number ko POORA
@@    (bina remainder) divide kar de.
@@    Example: 12 ke factors = 1, 2, 3, 4, 6, 12
@@    (kyunki ye sab 12 ko poora divide karte hain)


@@ 2) MULTIPLE KYA HOTA HAI?
@@    Multiple = number ki "table" ke numbers.
@@    Example: 3 ke multiples = 3, 6, 9, 12, 15, ...
@@    (Factor chhota hota hai, multiple bada.)


@@ 3) PRIME, COMPOSITE, AUR 1
@@    PRIME = sirf 2 factors (1 aur khud). Jaise 2,3,5,7,11
@@    COMPOSITE = 2 se zyada factors. Jaise 4,6,8,9,10
@@    1 NA prime hai NA composite (sirf 1 factor hai).
@@    2 ekloti EVEN prime number hai.


@@ 4) POWER / EXPONENT (chhota upar wala number)
@@    2^3 ka matlab 2 ko 3 baar multiply = 2x2x2 = 8.
@@    Yahan 2 = base, 3 = power/exponent.
@@    a^2 ko "a square", a^3 ko "a cube" bolte hain.


@@ 5) SQUARE ROOT (sqrt ya the root symbol)
@@    Square root = power ka ULTA.
@@    sqrt(9) = 3 kyunki 3x3 = 9.
@@    sqrt(25) = 5 kyunki 5x5 = 25.
@@    Symbol: tick-jaisa nishaan (root sign) number ke upar.
@@    Is PDF mein hum "sqrt(n)" likhte hain (jaise sqrt2).


@@ 6) p/q MEIN q ZERO KYUN NAHI HO SAKTA?
@@    p/q ka matlab p ko q se DIVIDE karna.
@@    Kisi cheez ko 0 se divide karna ALLOWED nahi
@@    (5/0 ka koi answer exist nahi karta - undefined).
@@    Isliye rational number p/q mein hamesha q != 0.


@@ 7) HCF (Highest Common Factor)
@@    HCF = do numbers ka sabse BADA common factor.
@@    12 ke factors: 1,2,3,4,6,12
@@    18 ke factors: 1,2,3,6,9,18
@@    Common: 1,2,3,6 -> sabse bada = 6 -> HCF = 6


@@ 8) LCM (Least Common Multiple)
@@    LCM = do numbers ka sabse CHHOTA common multiple.
@@    12 ke multiples: 12,24,36,48...
@@    18 ke multiples: 18,36,54...
@@    Common sabse chhota = 36 -> LCM = 36


@@ 9) NUMBER TYPES (jaldi recap)
@@    Natural (N): 1,2,3,...      Whole (W): 0,1,2,3,...
@@    Integers (Z): ...-2,-1,0,1,2...
@@    Rational (Q): p/q form (q!=0), jaise 1/2, 0.25
@@    Irrational: p/q mein nahi aata, jaise sqrt2, pi
@@    Real (R): rational + irrational dono.


@@ 10) TERMINATING vs NON-TERMINATING DECIMAL
@@    Terminating = decimal khatam ho jaye: 0.5, 0.25
@@    Non-terminating repeating = pattern repeat: 0.333...
@@    Non-terminating non-repeating = na khatam na pattern:
@@    sqrt2 = 1.41421356... (ye IRRATIONAL hota hai)


@@ 11) CO-PRIME NUMBERS
@@    Co-prime = do numbers jinka HCF = 1 (1 ke alawa
@@    koi common factor nahi).
@@    Example: 8 aur 15 -> common factor sirf 1 -> co-prime.
@@    (Dono ka khud prime hona zaroori nahi - 8,15 dono
@@     composite hain par phir bhi co-prime hain.)

<<<PAGEBREAK>>>

==========================================
NOW: ASLI CHAPTER 1 SHURU
==========================================


TOPIC 1: FUNDAMENTAL THEOREM OF ARITHMETIC
------------------------------------------

   STATEMENT:
     "Har composite number ko prime numbers ke product
      (multiplication) ke roop mein likha ja sakta hai,
      aur ye tareeka UNIQUE hota hai (order chhod ke)."

@@   [CORE] "Product of primes" matlab prime numbers ko
@@   multiply karna. Pehle prime/factor wala page dekh.


   EXAMPLE 1: 156 ka prime factorisation

     156 / 2 = 78
      78 / 2 = 39
      39 / 3 = 13
      13 / 13 = 1

     156 = 2 x 2 x 3 x 13 = 2^2 x 3 x 13

@@   [CORE] 2^2 ka matlab 2x2 (power wala page yaad kar).


   EXAMPLE 2: 3825 ka prime factorisation

     3825 / 3 = 1275
     1275 / 3 = 425
      425 / 5 = 85
       85 / 5 = 17
       17 / 17 = 1

     3825 = 3^2 x 5^2 x 17


TOPIC 2: HCF AND LCM BY PRIME FACTORISATION
-------------------------------------------

   METHOD:
     HCF = common prime factors ka product (LOWEST power)
     LCM = saare prime factors ka product (HIGHEST power)

@@   [CORE] HCF/LCM ka basic matlab RED page pe diya hai
@@   (point 7 aur 8). Pehle wo samajh, phir ye method.


   EXAMPLE 3: 96 aur 404 ka HCF aur LCM

     96  = 2^5 x 3
     404 = 2^2 x 101

     HCF = 2^2 = 4         (common prime 2, lowest power)
     LCM = 2^5 x 3 x 101 = 9696   (all primes, highest power)

     Verify: HCF x LCM = 4 x 9696 = 38784
             96 x 404  = 38784   (match!)

@@   [CORE] Sirf 2 numbers ke liye: HCF x LCM = product
@@   of the two numbers. (3 numbers pe ye rule nahi chalta.)


   EXAMPLE 4: Ek diya ho toh doosra nikaalo

     Do numbers ka HCF = 9, LCM = 90, ek number = 18.
     Doosra number = ?

     HCF x LCM = number1 x number2
     9 x 90 = 18 x number2
     810 = 18 x number2
     number2 = 810 / 18 = 45


TOPIC 2B: HCF / LCM WORD PROBLEMS (EXAM IMPORTANT)
--------------------------------------------------

$$ EXAM ALERT: Ye topic exam mein BAAR-BAAR aata hai
$$ (har saal lagbhag). Word problems pakka tayyar rakh.

   PEHCHAAN (kaunsa use karna hai):
@@   - "Ek saath", "together", "same time" -> LCM
@@   - "Sabse bada", "maximum", "largest" -> HCF


   EXAMPLE 5: Bells (ek saath bajna) -> LCM

     Teen ghantiyan 6, 12 aur 18 second pe bajti hain.
     Kab dobara ek saath bajengi?

     -> LCM of 6, 12, 18
        6  = 2 x 3
        12 = 2^2 x 3
        18 = 2 x 3^2
        LCM = 2^2 x 3^2 = 36

     Answer: 36 second baad ek saath bajengi.


   EXAMPLE 6: Sabse badi tape (exact measure) -> HCF

     Do rassiyan 18 m aur 24 m hain. Sabse badi tape
     jo dono ko exact (poora) naap sake?

     -> HCF of 18, 24
        18 = 2 x 3^2
        24 = 2^3 x 3
        HCF = 2 x 3 = 6

     Answer: 6 m ki tape.


TOPIC 3: IRRATIONAL NUMBERS (sqrt2 is irrational)
-------------------------------------------------

$$ EXAM ALERT: "Prove that sqrt(p) is irrational" aur
$$ "a + b*sqrt(p) is irrational" - ye 2-3 marks ka
$$ question lagbhag HAR exam mein aata hai. Ratta maar.

@@   [CORE] sqrt(2) ka matlab "woh number jisko square
@@   karne pe 2 aaye". Root symbol RED page point 5 mein.

   THEOREM USED:
     Agar prime p, a^2 ko divide karta hai, toh p, a ko
     bhi divide karta hai.

   PROOF: sqrt2 is irrational (Proof by Contradiction)

     Step 1: Maan le sqrt2 rational hai. Toh sqrt2 = p/q
             where q != 0 and HCF(p,q) = 1 (simplest form).

@@           [CORE] q != 0 kyun? RED page point 6 dekh.
@@           HCF(p,q)=1 matlab fraction simplest form mein.

     Step 2: Square dono side:
             2 = p^2 / q^2  ->  2 q^2 = p^2     ...(i)

     Step 3: 2 divides p^2  ->  2 divides p.
     Step 4: So p = 2c.
     Step 5: (i) mein daal: 2 q^2 = 4 c^2 -> q^2 = 2 c^2
     Step 6: 2 divides q^2  ->  2 divides q.
     Step 7: Ab p aur q dono ko 2 divide karta hai, par
             humne kaha tha HCF = 1. CONTRADICTION!

     CONCLUSION: Assumption galat. sqrt2 IRRATIONAL hai.


   EXAMPLE 7: sqrt3 bhi irrational hai (same method)

     1. Maan le sqrt3 = p/q (HCF=1, q!=0)
     2. 3 q^2 = p^2  ->  3 divides p^2  ->  3 divides p
     3. p = 3c  ->  3 q^2 = 9 c^2  ->  q^2 = 3 c^2
        ->  3 divides q
     4. p,q dono ko 3 divide kar raha -> HCF=1 toot gaya
     5. Contradiction -> sqrt3 IRRATIONAL hai.


   QUICK RESULTS (yaad rakh):
     - sqrt(p) irrational hota hai jab p prime ho.
     - Rational + Irrational = Irrational
     - (non-zero) Rational x Irrational = Irrational

<<<PAGEBREAK>>>

==========================================
SOLVED EXAMPLES: HARDEST -> EASIEST
==========================================

$$ Ye 8 examples poori tarah solve karke dikhaye hain.
$$ Step-by-step padh - "kaise solve karte hain" samajh aayega.
   (Upar HARDEST, neeche jaake EASIEST hote jaate hain.)


   ------------------------------------------------
   Solved Example 1 (HARDEST) - sqrt2 + sqrt3 irrational
   ------------------------------------------------
$$ (Exam favourite - thoda twist wala proof)

   Prove: sqrt2 + sqrt3 is irrational.

   Step 1: Maan le sqrt2 + sqrt3 RATIONAL hai = r.
   Step 2: sqrt3 = r - sqrt2. Dono side square karo:
           3 = r^2 - 2 r sqrt2 + 2
           3 = r^2 + 2 - 2 r sqrt2
   Step 3: 2 r sqrt2 = r^2 + 2 - 3 = r^2 - 1
           sqrt2 = (r^2 - 1) / (2r)
   Step 4: RHS rational hai (r rational hai). Toh sqrt2
           rational ban gaya. Par sqrt2 IRRATIONAL hai
           (proved). CONTRADICTION!
   Step 5: So sqrt2 + sqrt3 IRRATIONAL hai. (Proved)


   ------------------------------------------------
   Solved Example 2 - Largest number, remainders bachein
   ------------------------------------------------
$$ (Exam favourite - "leaving remainder" type = HCF)

   Sabse bada number jo 2053 aur 967 ko divide kare aur
   remainder 5 aur 7 bachein.

   Trick: pehle remainder GHATA do, phir HCF nikaalo.
     2053 - 5 = 2048
     967  - 7 = 960
   Ab HCF(2048, 960):
     2048 = 2^11
     960  = 2^6 x 3 x 5
     HCF  = 2^6 = 64

   Answer: 64.


   ------------------------------------------------
   Solved Example 3 - Smallest number, remainders type
   ------------------------------------------------
$$ (Exam favourite - "same shortfall" type = LCM)

   Sabse chhota number jo 28 aur 32 se divide hone par
   remainder 8 aur 12 chhode.

   Trick: dono mein shortfall same? 28-8=20, 32-12=20.
     Same (20)! Toh: number = LCM - 20.
   LCM(28, 32):
     28 = 2^2 x 7
     32 = 2^5
     LCM = 2^5 x 7 = 224
   Number = 224 - 20 = 204

   Check: 204/28 = 7 baar (196), remainder 8. (ok)
          204/32 = 6 baar (192), remainder 12. (ok)


   ------------------------------------------------
   Solved Example 4 - 6^n kabhi 0 pe khatam nahi hota
   ------------------------------------------------
$$ (Exam favourite - Fundamental Theorem ka use)

   Dikhao: 6^n kisi bhi natural n ke liye digit 0 pe
   khatam nahi ho sakta.

   Logic: kisi number ko 0 pe khatam hone ke liye usme
   prime factor 5 (aur 2) hona zaroori hai.
     6^n = (2 x 3)^n = 2^n x 3^n
   Isme 5 hai hi nahi! Isliye 6^n kabhi 0 pe end nahi hoga.
   (Unique prime factorisation se ye pakka hai.)


   ------------------------------------------------
   Solved Example 5 - Traffic lights (clock time)
   ------------------------------------------------
$$ (Exam favourite - LCM word problem with time)

   Teen lights 48, 72, 108 second pe badalti hain. 8:00:00
   pe saath badli. Dobara saath kab badlengi?

   LCM(48, 72, 108):
     48  = 2^4 x 3
     72  = 2^3 x 3^2
     108 = 2^2 x 3^3
     LCM = 2^4 x 3^3 = 16 x 27 = 432 second
   432 sec = 7 min 12 sec.

   Answer: 8:07:12 baje dobara saath badlengi.


   ------------------------------------------------
   Solved Example 6 - HCF & LCM of THREE numbers (+verify)
   ------------------------------------------------

   6, 72, 120 ka HCF aur LCM.
     6   = 2 x 3
     72  = 2^3 x 3^2
     120 = 2^3 x 3 x 5
     HCF = 2 x 3 = 6        (common, lowest power)
     LCM = 2^3 x 3^2 x 5 = 360  (all, highest power)

@@ NOTE: 3 numbers pe HCF x LCM = product wala rule
@@ NAHI chalta (sirf 2 numbers ke liye). Yaad rakh!


   ------------------------------------------------
   Solved Example 7 - 5 - sqrt3 irrational
   ------------------------------------------------
$$ (Exam favourite - a + b*sqrt(p) type)

   Prove: 5 - sqrt3 is irrational.

   Step 1: Maan le 5 - sqrt3 RATIONAL = r.
   Step 2: sqrt3 = 5 - r.
   Step 3: 5 - r rational hai (rational - rational).
           Toh sqrt3 rational ban gaya.
   Step 4: Par sqrt3 IRRATIONAL hai. CONTRADICTION!
   Step 5: So 5 - sqrt3 IRRATIONAL hai. (Proved)


   ------------------------------------------------
   Solved Example 8 (EASIEST) - HCF & LCM of 12 and 15
   ------------------------------------------------

   12 = 2^2 x 3
   15 = 3 x 5
   HCF = 3              (common prime, lowest power)
   LCM = 2^2 x 3 x 5 = 60   (all primes, highest power)

   Verify: HCF x LCM = 3 x 60 = 180 ; 12 x 15 = 180 (match!)


==========================================
Q AND A TIME
==========================================

   (Pehle khud try kar, phir mujhe bhej - main check karunga)

   Q1. 140 ko prime factors ke product mein likho.

   Q2. 26 aur 91 ka HCF aur LCM nikaal (prime
       factorisation se).

   Q3. sqrt(5) ko irrational prove kar (sqrt2 wala
       method copy kar).

   Q4. CORE CHECK: 1 prime hai ya composite? Kyun?

   Q5. CORE CHECK: 5/0 ka answer kya hai? p/q mein q ke
       baare mein kya rule hai?

   Q6. 3 + 2 x sqrt(5) ko irrational dikhao.

   Q7. WORD PROBLEM: Do ghantiyan 8 aur 12 minute pe
       bajti hain. Kab dobara ek saath bajengi?
       (HCF ya LCM use hoga?)

   Q8. CORE CHECK: 14 aur 25 co-prime hain ya nahi? Kyun?


==========================================
SUMMARY
==========================================

   1. Fundamental Theorem: har composite number = unique
      product of primes.

   2. HCF = common primes x lowest power.
      LCM = all primes x highest power.

   3. 2 numbers ke liye: HCF x LCM = product of numbers.

   4. sqrt(p) irrational hai jab p prime ho.

   5. Rational + Irrational = Irrational.

@@ CORE BASICS (RED page) ek baar aur revise kar lena -
@@ factor, multiple, prime, power, root, q!=0, HCF, LCM.
@@ Inke bina ye chapter adhoora rahega.


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 1: Real Numbers (Core-Basics edition)
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch1_Real_Numbers.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 1: Real Numbers (Core-Basics Edition)",
        content=CONTENT,
        out_path=out,
    )
