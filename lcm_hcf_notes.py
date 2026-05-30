#!/usr/bin/env python3
"""
HCF aur LCM ke study-notes ki PDF (Hinglish).
numbers_notes.py ka pure-Python PDF engine reuse karta hai
(koi external library nahi chahiye).
"""

from numbers_notes import (
    PDFBuilder, write_pdf,
    LEFT, RIGHT, PAGE_W, NAVY, GREY,
)


def build_document():
    d = PDFBuilder()

    # ---- Title -------------------------------------------------------
    d.title("HCF aur LCM")
    d.subtitle("Aasan Hinglish Notes, Methods, Examples aur Practice Questions")
    d.hline(LEFT, PAGE_W - RIGHT, d.y + 4, NAVY, 1.2)
    d.space(10)
    d.body("HCF aur LCM do important concepts hain jo numbers ke factors aur multiples "
           "par based hain. Is guide me dono ko simple Hinglish me samjhaya gaya hai - "
           "methods, relationship, fir 10 SOLVED EXAMPLES (samjho kaise solve karte "
           "hain), aur end me 22 practice questions ke STEP-BY-STEP solutions diye gaye "
           "hain.", color=GREY)
    d.space(6)

    # ---- Quick recap -------------------------------------------------
    d.h2("1. Quick Recap: Factor aur Multiple")
    d.label_body("Factor:", "Wo number jo kisi dusre number ko poora-poora divide kare "
                 "(remainder zero). Jaise 12 ke factors = 1, 2, 3, 4, 6, 12.")
    d.label_body("Multiple:", "Kisi number ko 1, 2, 3, ... se multiply karne par jo "
                 "aaye. Jaise 4 ke multiples = 4, 8, 12, 16, 20 ...")
    d.space(6)

    # ---- HCF ---------------------------------------------------------
    d.h2("2. HCF (Highest Common Factor)")
    d.label_body("Definition:", "Wo sabse bada number jo do ya zyada numbers ko exactly "
                 "divide kar de. Ise GCD (Greatest Common Divisor) bhi kehte hain.")
    d.label_body("Example:", "12 aur 18 ka HCF:")
    d.bullet("12 = 2 x 2 x 3")
    d.bullet("18 = 2 x 3 x 3")
    d.bullet("Common factors = 2 x 3 = 6, isliye HCF = 6")
    d.label_body("Yaad rakho:", "")
    d.bullet("HCF hamesha sabse chhote number se chhota ya barabar hota hai.")
    d.bullet("Co-prime numbers (jaise 8 aur 9) ka HCF 1 hota hai.")
    d.space(6)

    # ---- LCM ---------------------------------------------------------
    d.h2("3. LCM (Least Common Multiple)")
    d.label_body("Definition:", "Wo sabse chhota number jo do ya zyada numbers se exactly "
                 "divide ho jaye (sabse chhota common multiple).")
    d.label_body("Example:", "4 aur 6 ka LCM:")
    d.bullet("4 ke multiples = 4, 8, 12, 16, 20 ...")
    d.bullet("6 ke multiples = 6, 12, 18, 24 ...")
    d.bullet("Sabse chhota common multiple = 12, isliye LCM = 12")
    d.label_body("Yaad rakho:", "")
    d.bullet("LCM hamesha sabse bade number se bada ya barabar hota hai.")
    d.space(6)

    # ---- Methods -----------------------------------------------------
    d.h2("4. HCF aur LCM Nikalne ke Methods")
    d.label_body("(a) Prime Factorisation:", "Har number ko prime factors me todo.")
    d.bullet("HCF = common prime factors ka product (lowest power lo).")
    d.bullet("LCM = saare prime factors ka product (highest power lo).")
    d.bullet("Example: 12 = 2^2 x 3 aur 18 = 2 x 3^2  ->  HCF = 2 x 3 = 6, "
             "LCM = 2^2 x 3^2 = 36")
    d.label_body("(b) Division Method (HCF ke liye):", "Bade number ko chhote se divide "
                 "karo, fir divisor ko remainder se divide karo, aise repeat karo jab tak "
                 "remainder 0 na ho. Last divisor hi HCF hai.")
    d.label_body("(c) Common Division (LCM ke liye):", "Saare numbers ko common prime se "
                 "step-by-step divide karo, fir saare divisors ko multiply kar do.")
    d.space(6)

    # ---- Relationship ------------------------------------------------
    d.h2("5. HCF aur LCM ka Relationship")
    d.body("Kisi bhi do numbers ke liye ye rule hamesha sahi hota hai:", color=GREY)
    d.space(2)
    d.box_note([
        "HCF x LCM = Pehla number x Dusra number",
        "",
        "Example (12 aur 18):",
        "HCF x LCM = 6 x 36 = 216   aur   12 x 18 = 216   (dono barabar)",
    ])
    d.space(6)

    # ---- Difference -------------------------------------------------
    d.h2("6. HCF vs LCM (Main Antar)")
    d.bullet("HCF ka relation FACTORS se hai; LCM ka relation MULTIPLES se.")
    d.bullet("HCF = sabse bada common factor; LCM = sabse chhota common multiple.")
    d.bullet("HCF <= chhota number; LCM >= bada number.")
    d.space(6)

    # ---- Solved Examples (teaching) ---------------------------------
    d.h2("7. Solved Examples - Samjho Kaise Solve Karte Hain")
    d.body("Neeche 10 examples step-by-step solve karke dikhaye gaye hain, taaki HCF/LCM "
           "ke saare methods clear ho jayein (prime factorisation, division method, "
           "relationship aur word problems).", color=GREY)
    d.space(3)

    examples = [
        ("Example 1:  12 aur 18 ka HCF  (Prime Factorisation)",
         ["12 = 2 x 2 x 3",
          "18 = 2 x 3 x 3",
          "Common factors chuno (jo dono me hain): ek 2 aur ek 3.",
          "HCF = 2 x 3"],
         "HCF = 6"),
        ("Example 2:  12 aur 18 ka LCM  (Prime Factorisation)",
         ["12 = 2^2 x 3",
          "18 = 2 x 3^2",
          "Har prime ki HIGHEST power lo: 2^2 aur 3^2.",
          "LCM = 2^2 x 3^2 = 4 x 9"],
         "LCM = 36"),
        ("Example 3:  24 aur 36 ka HCF",
         ["24 = 2^3 x 3",
          "36 = 2^2 x 3^2",
          "Common primes ki LOWEST power: 2^2 aur 3.",
          "HCF = 2^2 x 3 = 4 x 3"],
         "HCF = 12"),
        ("Example 4:  48 aur 36 ka HCF  (Division Method)",
         ["Bade ko chhote se divide: 48 div 36 = 1, remainder 12.",
          "Ab divisor (36) ko remainder (12) se: 36 div 12 = 3, remainder 0.",
          "Remainder 0 aa gaya -> last divisor hi HCF hai."],
         "HCF = 12"),
        ("Example 5:  8, 12, 16 ka LCM  (Common Division)",
         ["2 | 8, 12, 16   ->   4, 6, 8",
          "2 | 4, 6, 8     ->   2, 3, 4",
          "2 | 2, 3, 4     ->   1, 3, 2",
          "3 | 1, 3, 2     ->   1, 1, 2",
          "2 | 1, 1, 2     ->   1, 1, 1",
          "Saare divisors multiply: 2 x 2 x 2 x 3 x 2"],
         "LCM = 48"),
        ("Example 6:  10 aur 15 ka LCM",
         ["10 = 2 x 5",
          "15 = 3 x 5",
          "Saare primes (highest power): 2, 3, 5.",
          "LCM = 2 x 3 x 5"],
         "LCM = 30"),
        ("Example 7:  HCF=6, LCM=36, ek number=12 -> dusra?",
         ["Rule: HCF x LCM = dono numbers ka product.",
          "6 x 36 = 12 x dusra   ->   216 = 12 x dusra.",
          "dusra = 216 / 12"],
         "Dusra number = 18"),
        ("Example 8:  Bells 9 aur 12 min par bajti hain, saath kab?",
         ["'Saath bajna' matlab LCM nikalo.",
          "9 = 3^2,  12 = 2^2 x 3.",
          "LCM = 2^2 x 3^2"],
         "36 minute baad"),
        ("Example 9:  Sabse bada number jo 28 aur 42 ko divide kare",
         ["'Sabse bada divide karne wala' = HCF.",
          "28 = 2^2 x 7,  42 = 2 x 3 x 7.",
          "Common = 2 x 7"],
         "HCF = 14"),
        ("Example 10:  8 aur 9 ka HCF aur LCM  (co-prime)",
         ["8 = 2^3,  9 = 3^2.",
          "Koi common prime factor nahi -> HCF = 1.",
          "LCM = dono ka product = 8 x 9"],
         "HCF = 1,  LCM = 72"),
    ]

    for q, steps, ans in examples:
        d.label_body(q, "")
        for s in steps:
            d.bullet(f"Step: {s}")
        d.label_body("   Answer:", ans)
        d.space(5)

    # ---- Practice Questions -----------------------------------------
    d.h2("8. Practice Questions")
    d.body("Pehle khud solve karne ki koshish karo. Neeche har question ka step-by-step "
           "solution diya gaya hai.", color=GREY)
    d.space(3)

    questions = [
        "12 aur 16 ka HCF nikalo.",
        "6 aur 9 ka LCM nikalo.",
        "24 aur 36 ka HCF nikalo.",
        "8 aur 12 ka LCM nikalo.",
        "15 aur 25 ka HCF nikalo.",
        "10 aur 15 ka LCM nikalo.",
        "18 aur 27 ka HCF nikalo.",
        "9 aur 12 ka LCM nikalo.",
        "20 aur 30 ka HCF nikalo.",
        "4, 5 aur 6 ka LCM nikalo.",
        "16 aur 24 ka HCF nikalo.",
        "14 aur 21 ka LCM nikalo.",
        "7 aur 14 ka HCF nikalo.",
        "3, 6 aur 9 ka LCM nikalo.",
        "36 aur 48 ka HCF nikalo.",
        "5 aur 7 ka LCM nikalo.",
        "Do numbers ka HCF 4 aur LCM 48 hai. Ek number 16 hai, dusra number batao.",
        "Do ghantiyan 9 aur 12 minute ke interval par bajti hain. Kitne minute baad "
        "saath bajengi?",
        "Sabse bada number jo 28 aur 42 dono ko exactly divide kare?",
        "8 aur 10 ka LCM nikalo.",
        "30 aur 45 ka HCF nikalo.",
        "6, 8 aur 12 ka LCM nikalo.",
    ]
    for i, q in enumerate(questions, start=1):
        d.label_body(f"Q{i}.", q)
        d.space(2)

    # ---- Step-by-Step Solutions -------------------------------------
    d.h2("9. Step-by-Step Solutions")

    solutions = [
        ("12 aur 16 ka HCF",
         ["12 = 2 x 2 x 3 = 2^2 x 3", "16 = 2 x 2 x 2 x 2 = 2^4",
          "Common (lowest power) = 2^2"],
         "HCF = 4"),
        ("6 aur 9 ka LCM",
         ["6 = 2 x 3", "9 = 3^2", "Highest powers: 2 aur 3^2 -> 2 x 3^2"],
         "LCM = 18"),
        ("24 aur 36 ka HCF",
         ["24 = 2^3 x 3", "36 = 2^2 x 3^2", "Common (lowest) = 2^2 x 3"],
         "HCF = 12"),
        ("8 aur 12 ka LCM",
         ["8 = 2^3", "12 = 2^2 x 3", "Highest powers: 2^3 x 3"],
         "LCM = 24"),
        ("15 aur 25 ka HCF",
         ["15 = 3 x 5", "25 = 5^2", "Common = 5"],
         "HCF = 5"),
        ("10 aur 15 ka LCM",
         ["10 = 2 x 5", "15 = 3 x 5", "Saare primes: 2 x 3 x 5"],
         "LCM = 30"),
        ("18 aur 27 ka HCF",
         ["18 = 2 x 3^2", "27 = 3^3", "Common (lowest) = 3^2"],
         "HCF = 9"),
        ("9 aur 12 ka LCM",
         ["9 = 3^2", "12 = 2^2 x 3", "Highest powers: 2^2 x 3^2"],
         "LCM = 36"),
        ("20 aur 30 ka HCF",
         ["20 = 2^2 x 5", "30 = 2 x 3 x 5", "Common (lowest) = 2 x 5"],
         "HCF = 10"),
        ("4, 5 aur 6 ka LCM",
         ["4 = 2^2,  5 = 5,  6 = 2 x 3", "Highest powers: 2^2, 3, 5",
          "LCM = 2^2 x 3 x 5"],
         "LCM = 60"),
        ("16 aur 24 ka HCF",
         ["16 = 2^4", "24 = 2^3 x 3", "Common (lowest) = 2^3"],
         "HCF = 8"),
        ("14 aur 21 ka LCM",
         ["14 = 2 x 7", "21 = 3 x 7", "Saare primes: 2 x 3 x 7"],
         "LCM = 42"),
        ("7 aur 14 ka HCF",
         ["7 = 7 (prime)", "14 = 2 x 7", "Common = 7"],
         "HCF = 7"),
        ("3, 6 aur 9 ka LCM",
         ["3 = 3,  6 = 2 x 3,  9 = 3^2", "Highest powers: 2, 3^2",
          "LCM = 2 x 3^2"],
         "LCM = 18"),
        ("36 aur 48 ka HCF",
         ["36 = 2^2 x 3^2", "48 = 2^4 x 3", "Common (lowest) = 2^2 x 3"],
         "HCF = 12"),
        ("5 aur 7 ka LCM",
         ["5 aur 7 dono prime (co-prime) hain", "Koi common factor nahi",
          "LCM = 5 x 7"],
         "LCM = 35"),
        ("HCF=4, LCM=48, ek number=16 -> dusra?",
         ["Rule: HCF x LCM = pehla x dusra", "4 x 48 = 16 x dusra -> 192 = 16 x dusra",
          "dusra = 192 / 16"],
         "Dusra number = 12"),
        ("Bells 9 aur 12 min, saath kab?",
         ["'Saath bajna' = LCM nikalo", "9 = 3^2,  12 = 2^2 x 3",
          "LCM = 2^2 x 3^2"],
         "36 minute baad"),
        ("Sabse bada number jo 28 aur 42 ko divide kare",
         ["Ye HCF hota hai", "28 = 2^2 x 7,  42 = 2 x 3 x 7",
          "Common = 2 x 7"],
         "HCF = 14"),
        ("8 aur 10 ka LCM",
         ["8 = 2^3", "10 = 2 x 5", "Highest powers: 2^3 x 5"],
         "LCM = 40"),
        ("30 aur 45 ka HCF",
         ["30 = 2 x 3 x 5", "45 = 3^2 x 5", "Common (lowest) = 3 x 5"],
         "HCF = 15"),
        ("6, 8 aur 12 ka LCM",
         ["6 = 2 x 3,  8 = 2^3,  12 = 2^2 x 3", "Highest powers: 2^3, 3",
          "LCM = 2^3 x 3"],
         "LCM = 24"),
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
    out_file = "HCF_and_LCM_Notes.pdf"
    pages = write_pdf(doc, out_file)
    print(f"Generated '{out_file}' with {pages} page(s).")
