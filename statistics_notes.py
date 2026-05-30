#!/usr/bin/env python3
"""
Chapter 13: Statistics - Hinglish notes PDF.
Red-page core basics (PART A) + main chapter content (PART B), green EXAM tags,
solved examples + step-by-step solutions.
"""

from numbers_notes import (
    PDFBuilder, write_pdf,
    LEFT, RIGHT, PAGE_W, NAVY, GREY,
)


def build_document():
    d = PDFBuilder()

    d.title("Statistics")
    d.subtitle("Chapter 13 - Hinglish Notes, Mean/Median/Mode + Solutions")
    d.hline(LEFT, PAGE_W - RIGHT, d.y + 4, NAVY, 1.2)
    d.space(10)
    d.body("Ye Chapter 13 (Statistics) ka complete guide hai. Pehle red-page ke core "
           "basics (data, mean/median/mode, class interval, class mark, cf), fir chapter "
           "ka main content - mean ke 3 methods, mode aur median ke formulas, aur ogive. "
           "End me solved examples aur 20 practice questions ke step-by-step solutions "
           "hain.", color=GREY)
    d.space(4)
    d.legend_exam()
    d.space(4)

    d.h2("PART A - Core Basics (Miss Mat Karna)")
    d.space(2)

    d.h2("1. Data")
    d.exam_tag()
    d.bullet("Data = collect kiye gaye numbers / observations.")
    d.bullet("Grouped data = intervals me bata hua (0-10, 10-20).")
    d.space(6)

    d.h2("2. Mean, Median, Mode (Basic Meaning)")
    d.exam_tag()
    d.bullet("Mean = average (saara total / count).")
    d.bullet("Median = beech wali value (data sort karke).")
    d.bullet("Mode = sabse zyada baar aane wali value.")
    d.space(6)

    d.h2("3. Class Interval aur Frequency")
    d.exam_tag()
    d.bullet("Class interval = range (jaise 10-20).")
    d.bullet("Frequency (fi) = us interval me kitne items hain.")
    d.space(6)

    d.h2("4. Class Mark (xi)")
    d.exam_tag()
    d.bullet("Class mark = interval ka midpoint.")
    d.bullet("xi = (upper + lower) / 2.   (0-10 -> 5)")
    d.space(6)

    d.h2("5. Summation (Sigma)")
    d.bullet("Sum(fi) = saari frequencies ka total (= n).")
    d.bullet("Sum(fi xi) = har (fi x xi) ka total.")
    d.space(6)

    d.h2("6. Average Nikaalna")
    d.bullet("Average = total / count. Mean isi par based hai.")
    d.space(6)

    d.h2("7. Cumulative Frequency (cf)")
    d.exam_tag()
    d.bullet("cf = frequencies ko add karte jao (running total).")
    d.bullet("Median nikaalne ke liye zaroori hai.")
    d.space(6)

    d.h2("PART B - Chapter 13 ka Main Content")
    d.space(2)

    d.h2("8. Mean - Method 1: Direct Method")
    d.exam_tag()
    d.box_note([
        "Mean = Sum(fi xi) / Sum(fi)",
        "",
        "xi = class mark,  fi = frequency.",
    ])
    d.space(6)

    d.h2("9. Mean - Method 2: Assumed Mean Method")
    d.exam_tag()
    d.box_note([
        "Mean = a + [ Sum(fi di) / Sum(fi) ]",
        "",
        "a = assumed mean,  di = xi - a.",
    ])
    d.space(6)

    d.h2("10. Mean - Method 3: Step Deviation Method")
    d.exam_tag()
    d.box_note([
        "Mean = a + h x [ Sum(fi ui) / Sum(fi) ]",
        "",
        "ui = (xi - a) / h,  h = class size.",
    ])
    d.space(6)

    d.h2("11. Mode (Grouped Data)")
    d.exam_tag()
    d.box_note([
        "Mode = l + [ (f1 - f0) / (2f1 - f0 - f2) ] x h",
        "",
        "l = modal class ki lower limit, f1 = modal class freq,",
        "f0 = pichli class freq, f2 = agli class freq, h = class size.",
    ])
    d.space(6)

    d.h2("12. Median (Grouped Data)")
    d.exam_tag()
    d.box_note([
        "Median = l + [ (n/2 - cf) / f ] x h",
        "",
        "l = median class lower limit, n = Sum(fi),",
        "cf = pichli class tak cumulative freq, f = median class freq, h = class size.",
    ])
    d.space(6)

    d.h2("13. Empirical Relation aur Ogive")
    d.exam_tag()
    d.bullet("Empirical: 3 Median = Mode + 2 Mean.")
    d.bullet("Ogive = cumulative frequency curve.")
    d.bullet("Less-than aur more-than ogive ka intersection point -> Median.")
    d.space(6)

    d.h2("Quick Revision")
    d.box_note([
        "Mean (direct) = Sum(fi xi)/Sum(fi).",
        "Step deviation: a + h x Sum(fi ui)/Sum(fi).",
        "Mode = l + [(f1-f0)/(2f1-f0-f2)] x h.",
        "Median = l + [(n/2 - cf)/f] x h.",
        "3 Median = Mode + 2 Mean.",
    ])
    d.space(6)

    d.h2("Solved Examples - Samjho Kaise Solve Karte Hain")
    d.body("Neeche 10 examples step-by-step solve karke dikhaye gaye hain.", color=GREY)
    d.space(3)

    examples = [
        ("Example 1:  Numbers 4, 6, 8, 10, 12 ka mean?",
         ["Mean = total / count.",
          "= (4+6+8+10+12)/5 = 40/5."],
         "Mean = 8"),
        ("Example 2:  5, 8, 9, 11, 14 ka median?",
         ["Data sorted hai, count = 5 (odd).",
          "Beech wali (3rd) value lo."],
         "Median = 9"),
        ("Example 3:  2, 3, 3, 5, 3, 7 ka mode?",
         ["Sabse zyada baar konsi value? 3 teen baar."],
         "Mode = 3"),
        ("Example 4:  Class mark of 20-30?",
         ["xi = (upper + lower)/2 = (20+30)/2."],
         "25"),
        ("Example 5:  Mean=10, Mode=12. Empirical se Median?",
         ["3 Median = Mode + 2 Mean = 12 + 20 = 32.",
          "Median = 32/3."],
         "Median = 10.67"),
        ("Example 6:  6 numbers, Sum(fi xi)=300, n=6. Mean?",
         ["Mean = Sum(fi xi)/n = 300/6."],
         "Mean = 50"),
        ("Example 7:  Even numbers 2,4,6,8 ka mean?",
         ["= (2+4+6+8)/4 = 20/4."],
         "5"),
        ("Example 8:  Data 7,7,8,9,7,10 ka mode?",
         ["7 sabse zyada (3 baar)."],
         "Mode = 7"),
        ("Example 9:  Median class l=10, n=20, cf=8, f=6, h=10. Median?",
         ["Median = l + [(n/2 - cf)/f] x h.",
          "= 10 + [(10 - 8)/6] x 10 = 10 + (2/6)x10.",
          "= 10 + 3.33."],
         "Median = 13.33"),
        ("Example 10:  Modal class l=20, f1=15, f0=10, f2=12, h=10. Mode?",
         ["Mode = l + [(f1-f0)/(2f1-f0-f2)] x h.",
          "= 20 + [(15-10)/(30-10-12)] x 10.",
          "= 20 + (5/8)x10 = 20 + 6.25."],
         "Mode = 26.25"),
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
        "Mean ka matlab kya hota hai?",
        "Median ka matlab kya hota hai?",
        "Mode ka matlab kya hota hai?",
        "Class mark (xi) ka formula kya hai?",
        "Direct method se mean ka formula kya hai?",
        "Step deviation method ka formula kya hai?",
        "Mode (grouped) ka formula kya hai?",
        "Median (grouped) ka formula kya hai?",
        "Empirical relation kya hai (mean/median/mode)?",
        "Cumulative frequency (cf) kya hoti hai?",
        "3, 5, 7, 9, 11 ka mean?",
        "10, 20, 30, 40, 50 ka median?",
        "4, 4, 5, 6, 4, 7 ka mode?",
        "Class mark of 30-40?",
        "Mean=15, Mode=18 -> median (empirical)?",
        "Ogive kya hota hai?",
        "Do ogive ka intersection point kya deta hai?",
        "2, 4, 6, 8, 10 ka mean?",
        "n=30, n/2 kya hota hai?",
        "Modal class kise kehte hain?",
    ]
    for i, q in enumerate(questions, start=1):
        d.label_body("Q" + str(i) + ".", q)
        d.space(2)

    d.h2("Step-by-Step Solutions")
    solutions = [
        ("Mean ka matlab?", ["Total / count."], "Average"),
        ("Median ka matlab?", ["Sort karke beech wali."], "Beech wali value"),
        ("Mode ka matlab?", ["Sabse zyada baar."], "Sabse zyada aane wali value"),
        ("Class mark formula?", ["Midpoint."], "(upper + lower)/2"),
        ("Direct mean formula?", ["Standard."], "Sum(fi xi)/Sum(fi)"),
        ("Step deviation formula?", ["Standard."], "a + h x Sum(fi ui)/Sum(fi)"),
        ("Mode (grouped) formula?", ["Standard."], "l + [(f1-f0)/(2f1-f0-f2)] x h"),
        ("Median (grouped) formula?", ["Standard."], "l + [(n/2 - cf)/f] x h"),
        ("Empirical relation?", ["Standard."], "3 Median = Mode + 2 Mean"),
        ("cf kya hoti hai?", ["Running total."], "Cumulative (running) frequency"),
        ("3,5,7,9,11 mean?", ["35/5."], "7"),
        ("10..50 median?", ["Beech (3rd) value."], "30"),
        ("4,4,5,6,4,7 mode?", ["4 teen baar."], "4"),
        ("Class mark 30-40?", ["(30+40)/2."], "35"),
        ("Mean=15, Mode=18 median?", ["3M=18+30=48 -> M=16."], "16"),
        ("Ogive kya hota?", ["cf curve."], "Cumulative frequency curve"),
        ("Do ogive intersection?", ["x-coordinate."], "Median"),
        ("2,4,6,8,10 mean?", ["30/5."], "6"),
        ("n=30, n/2?", ["30/2."], "15"),
        ("Modal class?", ["Sabse zyada frequency wali class."], "Highest frequency class"),
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
    out_file = "Statistics_Notes.pdf"
    pages = write_pdf(doc, out_file)
    print("Generated '" + out_file + "' with " + str(pages) + " page(s).")
