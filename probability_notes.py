#!/usr/bin/env python3
"""
Chapter 14: Probability - Hinglish notes PDF.
Red-page core basics (PART A) + main chapter content (PART B), green EXAM tags,
solved examples + step-by-step solutions.
"""

from numbers_notes import (
    PDFBuilder, write_pdf,
    LEFT, RIGHT, PAGE_W, NAVY, GREY,
)


def build_document():
    d = PDFBuilder()

    d.title("Probability")
    d.subtitle("Chapter 14 - Hinglish Notes, Formula, Examples + Solutions")
    d.hline(LEFT, PAGE_W - RIGHT, d.y + 4, NAVY, 1.2)
    d.space(10)
    d.body("Ye Chapter 14 (Probability) ka complete guide hai. Pehle red-page ke core "
           "basics (probability kya hai, experiment/outcome/event, favourable/total, "
           "deck of cards), fir chapter ka main content - formula, complement, coin/"
           "dice/cards ke problems. End me solved examples aur 20 practice questions ke "
           "step-by-step solutions hain.", color=GREY)
    d.space(4)
    d.legend_exam()
    d.space(4)

    d.h2("PART A - Core Basics (Miss Mat Karna)")
    d.space(2)

    d.h2("1. Probability Kya Hai?")
    d.exam_tag()
    d.bullet("Probability = kisi cheez ke hone ki sambhavna (chance).")
    d.bullet("Hamesha 0 se 1 ke beech hoti hai.")
    d.space(6)

    d.h2("2. Experiment, Outcome, Event")
    d.exam_tag()
    d.bullet("Experiment = jo karte ho (coin uchhalna).")
    d.bullet("Outcome = ek result (Head ya Tail).")
    d.bullet("Event = outcomes ka group (jaise 'even number aaye').")
    d.space(6)

    d.h2("3. Favourable Outcomes")
    d.exam_tag()
    d.bullet("Favourable = jo hum chahte hain wale outcomes ki ginti.")
    d.space(6)

    d.h2("4. Total Outcomes (Saare Possible)")
    d.exam_tag()
    d.bullet("Coin: 2 (H, T).  Dice: 6 (1-6).")
    d.bullet("Deck of cards: 52.")
    d.space(6)

    d.h2("5. Fraction")
    d.exam_tag()
    d.bullet("Probability ek fraction hota hai: favourable / total.")
    d.bullet("Jaise 3/6 = 1/2.")
    d.space(6)

    d.h2("6. Deck of Cards (52)")
    d.exam_tag()
    d.bullet("4 suits: Hearts, Diamonds (laal); Spades, Clubs (kaali).")
    d.bullet("Har suit 13 cards. Face cards = J, Q, K (12 total).")
    d.bullet("Aces = 4.  Red = 26, Black = 26.")
    d.space(6)

    d.h2("7. Sure vs Impossible")
    d.exam_tag()
    d.bullet("Sure event -> probability 1.")
    d.bullet("Impossible event -> probability 0.")
    d.space(6)

    d.h2("PART B - Chapter 14 ka Main Content")
    d.space(2)

    d.h2("8. Probability ka Formula")
    d.exam_tag()
    d.box_note([
        "P(E) = (Favourable outcomes) / (Total outcomes)",
        "",
        "0 <= P(E) <= 1 (hamesha is range me).",
    ])
    d.space(6)

    d.h2("9. Complement of an Event")
    d.exam_tag()
    d.box_note([
        "P(not E) = 1 - P(E)",
        "",
        "P(E) + P(not E) = 1.",
    ])
    d.bullet("Example: P(head) = 1/2 -> P(not head) = 1 - 1/2 = 1/2.")
    d.space(6)

    d.h2("10. Coin Problems")
    d.exam_tag()
    d.bullet("1 coin: outcomes {H, T} -> total 2.")
    d.bullet("2 coins: {HH, HT, TH, TT} -> total 4.")
    d.bullet("P(at least 1 head, 2 coins) = 3/4.")
    d.space(6)

    d.h2("11. Dice Problems")
    d.exam_tag()
    d.bullet("Total outcomes = 6 (1,2,3,4,5,6).")
    d.bullet("Even {2,4,6} -> P = 3/6 = 1/2.")
    d.bullet("Prime {2,3,5} -> P = 3/6 = 1/2.")
    d.space(6)

    d.h2("12. Card Problems (52 cards)")
    d.exam_tag()
    d.bullet("P(a King) = 4/52 = 1/13.")
    d.bullet("P(red card) = 26/52 = 1/2.")
    d.bullet("P(face card) = 12/52 = 3/13.")
    d.space(6)

    d.h2("Quick Revision")
    d.box_note([
        "P(E) = favourable / total.",
        "0 <= P(E) <= 1.  Sure=1, Impossible=0.",
        "P(not E) = 1 - P(E).",
        "Coin=2, Dice=6, Cards=52 outcomes.",
        "King=4/52=1/13, Red=1/2, Face=12/52=3/13.",
    ])
    d.space(6)

    d.h2("Solved Examples - Samjho Kaise Solve Karte Hain")
    d.body("Neeche 10 examples step-by-step solve karke dikhaye gaye hain.", color=GREY)
    d.space(3)

    examples = [
        ("Example 1:  Ek coin uchhala. P(head)?",
         ["Favourable (head) = 1, Total = 2.",
          "P = 1/2."],
         "1/2"),
        ("Example 2:  Ek dice fenka. P(even number)?",
         ["Even = {2,4,6} -> 3 favourable. Total = 6.",
          "P = 3/6 = 1/2."],
         "1/2"),
        ("Example 3:  Ek dice. P(number > 4)?",
         ["{5, 6} -> 2 favourable. Total = 6.",
          "P = 2/6 = 1/3."],
         "1/3"),
        ("Example 4:  52 cards me se P(a King)?",
         ["Kings = 4. Total = 52.",
          "P = 4/52 = 1/13."],
         "1/13"),
        ("Example 5:  52 cards. P(red card)?",
         ["Red = 26. Total = 52.",
          "P = 26/52 = 1/2."],
         "1/2"),
        ("Example 6:  P(head) = 1/2. P(not head)?",
         ["P(not E) = 1 - P(E) = 1 - 1/2."],
         "1/2"),
        ("Example 7:  Dice. P(prime number)?",
         ["Primes = {2,3,5} -> 3. Total = 6.",
          "P = 3/6 = 1/2."],
         "1/2"),
        ("Example 8:  Bag me 3 red, 2 blue balls. P(red)?",
         ["Favourable = 3, Total = 3+2 = 5.",
          "P = 3/5."],
         "3/5"),
        ("Example 9:  52 cards. P(face card)?",
         ["Face cards = J,Q,K x 4 suits = 12. Total = 52.",
          "P = 12/52 = 3/13."],
         "3/13"),
        ("Example 10:  2 coins. P(at least one head)?",
         ["Outcomes: HH, HT, TH, TT (total 4).",
          "At least 1 head = HH, HT, TH = 3.",
          "P = 3/4."],
         "3/4"),
    ]
    for q, steps, ans in examples:
        d.label_body(q, "")
        for s in steps:
            d.bullet("Step: " + s)
        d.label_body("   Answer:", ans)
        d.space(5)

    d.h2("Practice Questions")
    d.body("Pehle khud solve karne ki koshish karo. Neeche har question ka step-by-step "
           "solution diya gaya hai.", color=GREY)
    d.space(3)

    questions = [
        "Probability ki value kis range me hoti hai?",
        "Probability ka formula kya hai?",
        "Sure event ki probability kitni hoti hai?",
        "Impossible event ki probability kitni hoti hai?",
        "P(not E) ka formula kya hai?",
        "Ek coin me total outcomes kitne hote hain?",
        "Ek dice me total outcomes kitne hote hain?",
        "Deck me total cards kitne hote hain?",
        "Ek coin. P(tail)?",
        "Ek dice. P(odd number)?",
        "Ek dice. P(number 3)?",
        "52 cards. P(a Queen)?",
        "52 cards. P(black card)?",
        "52 cards. P(an Ace)?",
        "Bag me 4 red, 6 green. P(green)?",
        "Dice. P(number <= 2)?",
        "P(E)=2/5 ho to P(not E)?",
        "52 cards me face cards kitne hote hain?",
        "2 coins. Total outcomes kitne?",
        "Ek dice. P(multiple of 3)?",
    ]
    for i, q in enumerate(questions, start=1):
        d.label_body("Q" + str(i) + ".", q)
        d.space(2)

    d.h2("Step-by-Step Solutions")
    solutions = [
        ("Probability range?", ["0 se 1."], "0 <= P <= 1"),
        ("Probability formula?", ["Standard."], "favourable / total"),
        ("Sure event probability?", ["Pakka hoga."], "1"),
        ("Impossible event probability?", ["Kabhi nahi hoga."], "0"),
        ("P(not E) formula?", ["Complement."], "1 - P(E)"),
        ("Coin total outcomes?", ["H, T."], "2"),
        ("Dice total outcomes?", ["1 se 6."], "6"),
        ("Deck total cards?", ["Standard deck."], "52"),
        ("Coin P(tail)?", ["1 favourable / 2."], "1/2"),
        ("Dice P(odd)?", ["{1,3,5} = 3/6."], "1/2"),
        ("Dice P(3)?", ["1 favourable / 6."], "1/6"),
        ("52 cards P(Queen)?", ["4/52."], "1/13"),
        ("52 cards P(black)?", ["26/52."], "1/2"),
        ("52 cards P(Ace)?", ["4/52."], "1/13"),
        ("4 red, 6 green P(green)?", ["6/(4+6) = 6/10."], "3/5"),
        ("Dice P(<=2)?", ["{1,2} = 2/6."], "1/3"),
        ("P(E)=2/5 -> P(not E)?", ["1 - 2/5."], "3/5"),
        ("Face cards count?", ["J,Q,K x 4."], "12"),
        ("2 coins total outcomes?", ["HH,HT,TH,TT."], "4"),
        ("Dice P(multiple of 3)?", ["{3,6} = 2/6."], "1/3"),
    ]
    for i, (q, steps, ans) in enumerate(solutions, start=1):
        d.label_body("Q" + str(i) + ".", q)
        for s in steps:
            d.bullet("Step: " + s)
        d.label_body("   Answer:", ans)
        d.space(4)

    return d


if __name__ == "__main__":
    doc = build_document()
    out_file = "Probability_Notes.pdf"
    pages = write_pdf(doc, out_file)
    print("Generated '" + out_file + "' with " + str(pages) + " page(s).")
