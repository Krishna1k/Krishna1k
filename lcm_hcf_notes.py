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
           "par based hain. Is guide me dono ko simple Hinglish me examples ke saath "
           "samjhaya gaya hai - methods, relationship, aur end me 22 practice questions "
           "(answer key ke saath) diye gaye hain.", color=GREY)
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

    # ---- Practice Questions -----------------------------------------
    d.h2("7. Practice Questions (Khud Try Karo!)")
    d.body("In 22 questions ko khud solve karne ki koshish karo. Answers neeche answer "
           "key me diye gaye hain.", color=GREY)
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

    # ---- Answer Key --------------------------------------------------
    d.h2("8. Answer Key")
    answers = [
        "HCF = 4   (12 = 2^2 x 3, 16 = 2^4, common = 2^2 = 4)",
        "LCM = 18  (6 = 2 x 3, 9 = 3^2, LCM = 2 x 3^2 = 18)",
        "HCF = 12  (24 = 2^3 x 3, 36 = 2^2 x 3^2, common = 2^2 x 3 = 12)",
        "LCM = 24  (8 = 2^3, 12 = 2^2 x 3, LCM = 2^3 x 3 = 24)",
        "HCF = 5   (15 = 3 x 5, 25 = 5^2, common = 5)",
        "LCM = 30  (10 = 2 x 5, 15 = 3 x 5, LCM = 2 x 3 x 5 = 30)",
        "HCF = 9   (18 = 2 x 3^2, 27 = 3^3, common = 3^2 = 9)",
        "LCM = 36  (9 = 3^2, 12 = 2^2 x 3, LCM = 2^2 x 3^2 = 36)",
        "HCF = 10  (20 = 2^2 x 5, 30 = 2 x 3 x 5, common = 2 x 5 = 10)",
        "LCM = 60  (4 = 2^2, 5 = 5, 6 = 2 x 3, LCM = 2^2 x 3 x 5 = 60)",
        "HCF = 8   (16 = 2^4, 24 = 2^3 x 3, common = 2^3 = 8)",
        "LCM = 42  (14 = 2 x 7, 21 = 3 x 7, LCM = 2 x 3 x 7 = 42)",
        "HCF = 7   (7 = 7, 14 = 2 x 7, common = 7)",
        "LCM = 18  (3, 6 = 2 x 3, 9 = 3^2, LCM = 2 x 3^2 = 18)",
        "HCF = 12  (36 = 2^2 x 3^2, 48 = 2^4 x 3, common = 2^2 x 3 = 12)",
        "LCM = 35  (5 aur 7 co-prime hain, LCM = 5 x 7 = 35)",
        "Dusra number = 12   ((HCF x LCM) / 16 = (4 x 48) / 16 = 192 / 16 = 12)",
        "36 minute baad   (LCM of 9 aur 12 = 36)",
        "HCF = 14  (28 = 2^2 x 7, 42 = 2 x 3 x 7, common = 2 x 7 = 14)",
        "LCM = 40  (8 = 2^3, 10 = 2 x 5, LCM = 2^3 x 5 = 40)",
        "HCF = 15  (30 = 2 x 3 x 5, 45 = 3^2 x 5, common = 3 x 5 = 15)",
        "LCM = 24  (6 = 2 x 3, 8 = 2^3, 12 = 2^2 x 3, LCM = 2^3 x 3 = 24)",
    ]
    for i, a in enumerate(answers, start=1):
        d.bullet(f"Q{i}: {a}")

    return d


if __name__ == "__main__":
    doc = build_document()
    out_file = "HCF_and_LCM_Notes.pdf"
    pages = write_pdf(doc, out_file)
    print(f"Generated '{out_file}' with {pages} page(s).")
