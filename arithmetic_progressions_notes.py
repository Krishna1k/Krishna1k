#!/usr/bin/env python3
"""
Chapter 5: Arithmetic Progressions (AP) - Hinglish notes PDF.
Red-page core basics + main chapter content, green EXAM tags,
solved examples + step-by-step solutions.
numbers_notes.py ka pure-Python PDF engine reuse karta hai.

Output: Arithmetic_Progressions_Notes.pdf
"""

from numbers_notes import (
    PDFBuilder, write_pdf,
    LEFT, RIGHT, PAGE_W, NAVY, GREY,
)


def build_document():
    d = PDFBuilder()

    d.title("Arithmetic Progressions (AP)")
    d.subtitle("Chapter 5 - Hinglish Notes, Formulas, Examples + Solutions")
    d.hline(LEFT, PAGE_W - RIGHT, d.y + 4, NAVY, 1.2)
    d.space(10)
    d.body("Ye Chapter 5 (Arithmetic Progressions) ka complete guide hai. Pehle red-page "
           "ke core basics (sequence, term, common difference, a/d/n/an/Sn), fir chapter "
           "ka main content - nth term aur sum ke formulas. End me solved examples aur "
           "20 practice questions ke step-by-step solutions hain.", color=GREY)
    d.space(4)
    d.legend_exam()
    d.space(4)

    # ================= PART A : CORE BASICS =========================
    d.h2("PART A - Core Basics (Miss Mat Karna)")
    d.space(2)

    d.h2("1. Sequence Kya Hai?")
    d.exam_tag()
    d.label_body("Definition:", "Numbers ki list jo ek pattern me ho.")
    d.bullet("Jaise 2, 4, 6, 8, ...  ya  1, 4, 9, 16, ...")
    d.space(6)

    d.h2("2. Term")
    d.exam_tag()
    d.label_body("Definition:", "Sequence ka har number ek 'term' hota hai.")
    d.bullet("Pehla term, doosra term, ... nth term.")
    d.space(6)

    d.h2("3. Difference Nikaalna")
    d.exam_tag()
    d.label_body("Rule:", "Do terms ka antar = baad wala - pehle wala.")
    d.bullet("Example: 5, 9  ->  9 - 5 = 4.  (Antar negative bhi ho sakta hai.)")
    d.space(6)

    d.h2("4. Variable / Formula Samajhna")
    d.exam_tag()
    d.bullet("a  = pehla term (first term)")
    d.bullet("d  = common difference")
    d.bullet("n  = term number")
    d.bullet("an = nth term (n-wa term)")
    d.bullet("Sn = pehle n terms ka sum")
    d.space(6)

    d.h2("5. Substitution")
    d.exam_tag()
    d.label_body("Matlab:", "Formula me values daal kar calculate karna.")
    d.bullet("an = a + (n-1)d  me  a, d, n  ki values daal do.")
    d.space(6)

    d.h2("6. Basic Algebra (Do Equations)")
    d.bullet("Kabhi a aur d ke liye 2 equations milti hain.")
    d.bullet("Unhe subtract karke ek variable gayab (eliminate) kar do, fir solve karo.")
    d.space(6)

    d.h2("7. Negative Numbers (Ghatti AP)")
    d.bullet("Agar d negative ho to sequence ghatti (decrease) hoti hai.")
    d.bullet("Example: 10, 7, 4, 1, ...  (d = -3).")
    d.space(6)

    # ================= PART B : MAIN CONTENT ========================
    d.h2("PART B - Chapter 5 ka Main Content")
    d.space(2)

    d.h2("8. Arithmetic Progression (AP) Kya Hai?")
    d.exam_tag()
    d.label_body("Definition:", "Aisi sequence jisme har do lagatar terms ka antar "
                 "(difference) HAMESHA same ho. Usi same antar ko common difference (d) "
                 "kehte hain.")
    d.bullet("Example: 3, 7, 11, 15, ...  (har baar +4, to d = 4).")
    d.bullet("General AP: a, a+d, a+2d, a+3d, ...")
    d.space(6)

    d.h2("9. Common Difference (d)")
    d.exam_tag()
    d.label_body("Formula:", "d = a2 - a1 = a3 - a2  (kisi bhi term me se uska pichla "
                 "term ghatao).")
    d.bullet("Agar d same nahi aaye to wo AP nahi hai.")
    d.space(6)

    d.h2("10. nth Term ka Formula")
    d.exam_tag()
    d.box_note([
        "an = a + (n - 1) d",
        "",
        "a = pehla term,  d = common difference,  n = term number.",
    ])
    d.bullet("Example: 2, 5, 8, ... ka 10-wa term = 2 + (10-1) x 3 = 29.")
    d.space(6)

    d.h2("11. Sum of First n Terms")
    d.exam_tag()
    d.box_note([
        "Sn = n/2 [ 2a + (n - 1) d ]",
        "",
        "Agar last term 'l' pata ho to:",
        "Sn = n/2 ( a + l )",
    ])
    d.bullet("Example: 1 + 2 + 3 + ... + 100 = 100/2 (1 + 100) = 5050.")
    d.space(6)

    d.h2("12. AP Hai ya Nahi - Kaise Check Karein")
    d.bullet("Lagatar terms ka difference nikalo: a2-a1, a3-a2, a4-a3 ...")
    d.bullet("Agar saare difference same hain -> AP hai; warna nahi.")
    d.space(6)

    d.h2("13. Word Problems")
    d.bullet("Pehle a (first term) aur d (common difference) pehchaano.")
    d.bullet("Fir question ke hisaab se an ya Sn ka formula lagao.")
    d.bullet("Common: savings/salary badhna, seats in rows, etc.")
    d.space(6)

    d.h2("Quick Revision")
    d.box_note([
        "AP = constant common difference (d).",
        "d = baad wala term - pehle wala term.",
        "nth term:  an = a + (n-1)d.",
        "Sum:  Sn = n/2 [2a + (n-1)d]  ya  n/2 (a + l).",
        "d positive -> badhti AP; d negative -> ghatti AP.",
    ])
    d.space(6)

    # ---- Solved Examples --------------------------------------------
    d.h2("Solved Examples - Samjho Kaise Solve Karte Hain")
    d.body("Neeche 10 examples step-by-step solve karke dikhaye gaye hain.", color=GREY)
    d.space(3)

    examples = [
        ("Example 1:  AP 3, 7, 11, 15 ... ka common difference?",
         ["d = baad wala - pehle wala.", "d = 7 - 3 = 4."],
         "d = 4"),
        ("Example 2:  2, 5, 8, ... ka 10-wa term (a10)?",
         ["a = 2, d = 5 - 2 = 3, n = 10.",
          "an = a + (n-1)d = 2 + (10-1) x 3.", "= 2 + 27."],
         "a10 = 29"),
        ("Example 3:  5, 8, 11, ... ka kaunsa term 50 hai?",
         ["a = 5, d = 3. an = 50 rakho.",
          "5 + (n-1)3 = 50 -> (n-1)3 = 45.", "n - 1 = 15 -> n = 16."],
         "16-wa term"),
        ("Example 4:  2, 4, 6, ... ke pehle 10 terms ka sum?",
         ["a = 2, d = 2, n = 10.",
          "Sn = n/2[2a + (n-1)d] = 10/2[2x2 + 9x2].", "= 5[4 + 18] = 5 x 22."],
         "S10 = 110"),
        ("Example 5:  1 + 2 + 3 + ... + 100 ka sum?",
         ["a = 1, last term l = 100, n = 100.",
          "Sn = n/2 (a + l) = 100/2 (1 + 100).", "= 50 x 101."],
         "5050"),
        ("Example 6:  Kya 1, 4, 9, 16 ek AP hai?",
         ["Differences: 4-1=3, 9-4=5, 16-9=7.", "Difference same nahi (3, 5, 7)."],
         "Nahi (AP nahi hai)"),
        ("Example 7:  10, 7, 4, 1 ka common difference?",
         ["d = 7 - 10 = -3 (negative)."],
         "d = -3 (ghatti AP)"),
        ("Example 8:  Ek AP ka 3rd term 5 aur 7th term 9 hai. a aur d?",
         ["a + 2d = 5  ... (i)", "a + 6d = 9  ... (ii)",
          "(ii)-(i): 4d = 4 -> d = 1.", "a + 2(1) = 5 -> a = 3."],
         "a = 3, d = 1"),
        ("Example 9:  a = 7, d = -2 -> a5?",
         ["an = a + (n-1)d = 7 + (5-1)(-2).", "= 7 - 8."],
         "a5 = -1"),
        ("Example 10 (Word):  Pehle mahine Rs 100 bachat, har mahine Rs 50 zyada. "
         "12-we mahine?",
         ["a = 100, d = 50, n = 12.",
          "an = 100 + (12-1) x 50 = 100 + 550."],
         "Rs 650"),
    ]
    for q, steps, ans in examples:
        d.label_body(q, "")
        for s in steps:
            d.bullet(f"Step: {s}")
        d.label_body("   Answer:", ans)
        d.space(5)

    # ---- Practice Questions -----------------------------------------
    d.h2("Practice Questions")
    d.body("Pehle khud solve karne ki koshish karo. Neeche har question ka step-by-step "
           "solution diya gaya hai.", color=GREY)
    d.space(3)

    questions = [
        "AP (Arithmetic Progression) kya hota hai?",
        "AP me common difference (d) kaise nikalte hain?",
        "nth term ka formula kya hai?",
        "Sum of n terms ka formula kya hai?",
        "2, 5, 8, 11 ka common difference kya hai?",
        "3, 7, 11, ... ka 10-wa term kya hai?",
        "1, 2, 3, ..., 50 ka sum kya hai?",
        "Kya 2, 4, 8, 16 ek AP hai?",
        "10, 8, 6, 4 ka common difference kya hai?",
        "a = 5, d = 3, n = 4 -> a4 kya hai?",
        "AP 7, 10, 13, ... ka 20-wa term?",
        "Pehle 5 even numbers (2,4,6,8,10) ka sum?",
        "a = 3, d = 2 ho to pehle 3 terms kya honge?",
        "d negative ho to sequence badhti hai ya ghatti?",
        "Sum formula me 'l' (last term) ka kya matlab hai?",
        "Last term l ke saath sum ka formula kya hai?",
        "AP 2, 4, 6, ..., 20 ka sum kya hai?",
        "3, 6, 9, ... ka kaunsa term 30 hai?",
        "a = 1, d = 1 ho to S10 kya hai?",
        "5, 2, -1, -4 ka common difference?",
    ]
    for i, q in enumerate(questions, start=1):
        d.label_body(f"Q{i}.", q)
        d.space(2)

    # ---- Step-by-Step Solutions -------------------------------------
    d.h2("Step-by-Step Solutions")
    solutions = [
        ("AP kya hota hai?",
         ["Aisi sequence jisme har do terms ka antar same ho."],
         "Constant common difference wali sequence"),
        ("Common difference kaise?",
         ["Kisi term me se uska pichla term ghatao."], "d = a2 - a1"),
        ("nth term ka formula?",
         ["Standard AP formula."], "an = a + (n-1)d"),
        ("Sum of n terms?",
         ["Standard sum formula."], "Sn = n/2 [2a + (n-1)d]"),
        ("2,5,8,11 ka d?",
         ["5 - 2 = 3."], "d = 3"),
        ("3,7,11,... ka 10-wa term?",
         ["a=3, d=4. a10 = 3 + 9x4 = 3 + 36."], "39"),
        ("1+2+...+50 ka sum?",
         ["n=50, a=1, l=50. S = 50/2(1+50) = 25x51."], "1275"),
        ("Kya 2,4,8,16 AP hai?",
         ["Diff: 2, 4, 8 (same nahi)."], "Nahi"),
        ("10,8,6,4 ka d?",
         ["8 - 10 = -2."], "d = -2"),
        ("a=5,d=3,n=4 -> a4?",
         ["5 + (4-1)3 = 5 + 9."], "14"),
        ("7,10,13,... ka 20-wa term?",
         ["a=7,d=3. a20 = 7 + 19x3 = 7 + 57."], "64"),
        ("Pehle 5 even numbers ka sum?",
         ["a=2,d=2,n=5. S = 5/2[4 + 4x2] = 5/2[12]."], "30"),
        ("a=3,d=2 ke pehle 3 terms?",
         ["3, 3+2, 5+2."], "3, 5, 7"),
        ("d negative ho to?",
         ["Terms chhote hote jaate hain."], "Ghatti (decreasing)"),
        ("'l' ka matlab?",
         ["Sequence ka aakhri term."], "Last term"),
        ("Last term ke saath sum?",
         ["Chhota formula."], "Sn = n/2 (a + l)"),
        ("2,4,6,...,20 ka sum?",
         ["a=2,l=20,n=10. S = 10/2(2+20) = 5x22."], "110"),
        ("3,6,9,... ka kaunsa term 30?",
         ["a=3,d=3. 3+(n-1)3=30 -> (n-1)=9 -> n=10."], "10-wa term"),
        ("a=1,d=1 -> S10?",
         ["S = 10/2[2 + 9] = 5 x 11."], "55"),
        ("5,2,-1,-4 ka d?",
         ["2 - 5 = -3."], "d = -3"),
    ]
    for i, (q, steps, ans) in enumerate(solutions, start=1):
        d.label_body(f"Q{i}.", q)
        for s in steps:
            d.bullet(f"Step: {s}")
        d.label_body("   Answer:", ans)
        d.space(4)

    return d


if __name__ == "__main__":
    doc = build_document()
    out_file = "Arithmetic_Progressions_Notes.pdf"
    pages = write_pdf(doc, out_file)
    print(f"Generated '{out_file}' with {pages} page(s).")
