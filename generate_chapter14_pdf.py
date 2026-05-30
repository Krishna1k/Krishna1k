"""
PDF generator for Class 10 Maths Chapter 14: Probability
(Core-Basics edition). RED core basics, GREEN exam marks,
8 solved examples (hardest -> easiest). Hinglish.
Uses shared pdf_utils.py (red '@@', green '$$', page breaks).
"""

from pathlib import Path
from pdf_utils import build_pdf


CONTENT = r"""
CLASS 10 NCERT MATHS
CHAPTER 14: PROBABILITY
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

@@ 1) PROBABILITY KYA HAI?
@@    Probability = kisi cheez ke hone ki sambhavna
@@    (chance). 0 se 1 ke beech hoti hai.


@@ 2) EXPERIMENT, OUTCOME, EVENT
@@    Experiment = jo karte ho (coin uchhalna).
@@    Outcome = ek result (Head ya Tail).
@@    Event = outcomes ka group (jaise "even number aaye").


@@ 3) FAVOURABLE OUTCOMES
@@    Favourable = jo hum chahte hain wale outcomes ki ginti.


@@ 4) TOTAL OUTCOMES (saare possible)
@@    Coin: 2 (H,T). Dice: 6 (1-6).
@@    Deck of cards: 52.


@@ 5) FRACTION
@@    Probability ek fraction hota hai:
@@    favourable / total. (Jaise 3/6 = 1/2)


@@ 6) DECK OF CARDS (52)
@@    4 suits: Hearts, Diamonds (laal); Spades, Clubs (kaali).
@@    Har suit 13 cards. Face cards = J,Q,K (12 total).
@@    Aces = 4.


@@ 7) SURE vs IMPOSSIBLE
@@    Sure event -> probability 1. Impossible -> 0.

<<<PAGEBREAK>>>

==========================================
NOW: ASLI CHAPTER 14 SHURU
==========================================


TOPIC 1: PROBABILITY FORMULA
----------------------------

$$ EXAM ALERT: Sabse important formula:

$$   P(E) = (Number of favourable outcomes) /
$$          (Total number of outcomes)

   P(E) hamesha 0 aur 1 ke beech (0 <= P(E) <= 1).


TOPIC 2: COMPLEMENT (not E)
---------------------------

$$ EXAM ALERT: "E nahi hone" ki probability:

$$   P(not E) = 1 - P(E)

   (Dono ka sum hamesha 1 hota hai.)


TOPIC 3: SURE AUR IMPOSSIBLE EVENTS
-----------------------------------

   Sure event (pakka hoga) -> P = 1.
   Impossible event (kabhi nahi) -> P = 0.

@@   [CORE] Probability kabhi 1 se zyada ya 0 se kam nahi
@@   ho sakti.

<<<PAGEBREAK>>>

==========================================
SOLVED EXAMPLES: HARDEST -> EASIEST
==========================================

$$ 8 examples poori tarah solve karke. Upar HARDEST,
$$ neeche EASIEST.


   ------------------------------------------------
   Solved Example 1 (HARDEST) - Two dice sum
   ------------------------------------------------
$$ (Exam favourite)

   Do dice ek saath. P(sum = 8)?
     Total outcomes = 6 x 6 = 36.
     Sum 8 wale: (2,6),(3,5),(4,4),(5,3),(6,2) = 5.
     P = 5/36.


   ------------------------------------------------
   Solved Example 2 - Cards (face card)
   ------------------------------------------------
$$ (Exam favourite)

   52 cards me se 1 nikaali. P(face card)?
     Face cards = J,Q,K har suit -> 3 x 4 = 12.
     P = 12/52 = 3/13.


   ------------------------------------------------
   Solved Example 3 - Cards (red king)
   ------------------------------------------------
$$ (Exam favourite)

   P(red king)? Red kings = 2 (hearts, diamonds).
     P = 2/52 = 1/26.


   ------------------------------------------------
   Solved Example 4 - Bag of balls
   ------------------------------------------------

   Bag: 5 red, 3 blue, 2 green (total 10). P(red)?
     Favourable = 5, total = 10.
     P = 5/10 = 1/2.


   ------------------------------------------------
   Solved Example 5 - Complement
   ------------------------------------------------

   P(E) = 0.3 hai. P(not E)?
     P(not E) = 1 - 0.3 = 0.7.


   ------------------------------------------------
   Solved Example 6 - Single die
   ------------------------------------------------

   Ek dice. P(even number)?
     Even: 2,4,6 -> 3 favourable, total 6.
     P = 3/6 = 1/2.


   ------------------------------------------------
   Solved Example 7 - Coin
   ------------------------------------------------

   Ek coin. P(Head)?
     Favourable 1 (H), total 2 (H,T).
     P = 1/2.


   ------------------------------------------------
   Solved Example 8 (EASIEST) - Numbers
   ------------------------------------------------

   1 se 10 tak ek number choose. P(number = 7)?
     Favourable 1, total 10.
     P = 1/10.


==========================================
Q AND A TIME
==========================================

   Q1. CORE: probability ki value kis range mein hoti hai?

   Q2. Ek dice. P(number > 4) nikaal.

   Q3. 52 cards. P(an ace) nikaal.

   Q4. Bag: 4 red, 6 black (total 10). P(black)?

   Q5. P(E) = 0.45 hai. P(not E)?

   Q6. Do dice. P(sum = 7) nikaal.

   Q7. CORE CHECK: ek coin pe Head aane ki probability?


==========================================
SUMMARY
==========================================

   1. P(E) = favourable outcomes / total outcomes.

   2. 0 <= P(E) <= 1 (hamesha is range mein).

   3. P(not E) = 1 - P(E).

   4. Sure event P=1, impossible event P=0.

   5. Total outcomes: coin 2, dice 6, cards 52.

@@ CORE (RED page) revise: experiment/outcome/event,
@@ favourable vs total, fraction, deck of cards, sure/impossible.


==========================================
Generated by Kiro for Krishna1k
Class 10 NCERT Maths - Chapter 14: Probability (Core-Basics edition)
==========================================
"""


if __name__ == "__main__":
    out = Path(__file__).parent / "Class10_Maths_Ch14_Probability.pdf"
    build_pdf(
        title="Class 10 NCERT Maths",
        subtitle="Chapter 14: Probability (Core-Basics Edition)",
        content=CONTENT,
        out_path=out,
    )
