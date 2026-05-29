#!/usr/bin/env python3
"""
"10th ke Baad Courses (India)" study/career-notes ki PDF - Hinglish.
numbers_notes.py ka pure-Python PDF engine reuse karta hai
(koi external library nahi chahiye), taaki style baaki notes jaisi rahe.

Output: Courses_After_10th_India.pdf
"""

from numbers_notes import (
    PDFBuilder, write_pdf,
    LEFT, RIGHT, PAGE_W, NAVY, GREY,
)


def build_document():
    d = PDFBuilder()

    # ---- Title -------------------------------------------------------
    d.title("10th ke Baad Courses")
    d.subtitle("India - Aasan Hinglish Career Guide + Practice Questions")
    d.hline(LEFT, PAGE_W - RIGHT, d.y + 4, NAVY, 1.2)
    d.space(10)
    d.body("10th ke baad bahut saare raaste khulte hain - Science, Commerce, Arts, "
           "Diploma, ITI, Defence aur vocational courses. Ye guide har path ko simple "
           "Hinglish me samjhati hai, aur end me 22 practice questions (answer key ke "
           "saath) deti hai jisse aap apni samajh check kar sako.", color=GREY)
    d.space(6)

    # ---- 1. Academic Path -------------------------------------------
    d.h2("1. Academic Path (11th - 12th / 10+2)")

    d.label_body("A) Science Stream:", "")
    d.bullet("PCM (Physics, Chemistry, Maths) -> Engineering (B.Tech: CSE, Mechanical, "
             "Civil, ECE, AI/Data Science), B.Arch, B.Sc, NDA, Pilot (CPL), BCA.")
    d.bullet("PCB (Physics, Chemistry, Biology) -> MBBS (NEET se), BDS, BAMS, B.Pharma, "
             "B.Sc Nursing, Physiotherapy (BPT), B.V.Sc (animal doctor), B.Sc Agriculture.")
    d.bullet("PCMB -> dono options (engineering + medical) khule rehte hain.")

    d.label_body("B) Commerce Stream:", "")
    d.bullet("With/Without Maths -> B.Com, BBA/BMS, CA, CS, CMA, CFA, B.Com (Banking), "
             "Economics, BHM (Hotel Management).")

    d.label_body("C) Arts / Humanities Stream:", "")
    d.bullet("BA (History, Pol. Science, Psychology, English...), BA-LLB (Law), "
             "Journalism (BJMC), B.Ed, Fine Arts, Fashion/Interior Design, Animation, "
             "Hotel Management, UPSC prep (graduation ke baad).")
    d.space(6)

    # ---- 2. Diploma / Polytechnic -----------------------------------
    d.h2("2. Diploma / Polytechnic (10th ke baad, ~3 saal)")
    d.bullet("Engineering Diplomas: Mechanical, Civil, Electrical, Computer/IT, "
             "Automobile, Chemical. (Diploma ke baad Lateral Entry se direct B.Tech "
             "ke 2nd year me admission.)")
    d.bullet("Paramedical: DMLT (Lab Tech), D.Pharm, GNM/ANM Nursing, X-Ray Technician.")
    d.bullet("Design & Creative: Fashion, Interior, Graphic Design, Animation.")
    d.bullet("Hotel Management & Culinary (Chef), Agriculture/Horticulture diplomas.")
    d.space(6)

    # ---- 3. ITI -----------------------------------------------------
    d.h2("3. ITI (Industrial Training Institute) - 6 mahine se 2 saal")
    d.bullet("Engineering Trades: Electrician, Fitter, Welder, Turner, Mechanic, "
             "Plumber, AC Mechanic, COPA (Computer Operator).")
    d.bullet("Non-Engineering Trades: Stenography, Tailoring, Hair & Skin Care, "
             "Photography, Desktop Publishing.")
    d.bullet("Fayda: kam samay me skill + jaldi job/self-employment.")
    d.space(6)

    # ---- 4. Defence / Govt ------------------------------------------
    d.h2("4. Defence / Government Path")
    d.bullet("Sainik School / RIMC (school ke dauran admission).")
    d.bullet("NDA (12th ke baad), Indian Navy/Army/Air Force entries, Agniveer Scheme.")
    d.bullet("Police Constable, BSF/CRPF/CISF, Railway (RRB Group D, NTPC), SSC MTS/GD.")
    d.space(6)

    # ---- 5. Vocational ----------------------------------------------
    d.h2("5. Vocational & Short-term Courses")
    d.bullet("Beauty & Wellness: Beautician, Cosmetology.")
    d.bullet("IT & Computer: DCA/PGDCA, Web Designing, Tally, Digital Marketing, "
             "Mobile Repairing, Hardware & Networking.")
    d.bullet("Media: Video Editing, Sound Engineering, RJ, YouTube/Content Creation.")
    d.bullet("Food & Hospitality: Bakery, Chef courses, Cafe Management.")
    d.space(6)

    # ---- 6. Other paths ---------------------------------------------
    d.h2("6. Sports, Open Schooling & Self-Employment")
    d.bullet("Sports: SAI Academies, B.P.Ed, Yoga Instructor, Gym Trainer certification.")
    d.bullet("Open Schooling: NIOS, State Open Boards, IGNOU diplomas.")
    d.bullet("Self-Employment: Family business, Skill India/PMKVY, MUDRA loan, "
             "Freelancing, Online business.")
    d.space(6)

    # ---- Quick decision guide ---------------------------------------
    d.h2("Quick Decision Guide")
    d.box_note([
        "Engineer banna hai     -> PCM -> JEE -> B.Tech / Polytechnic",
        "Doctor banna hai       -> PCB -> NEET -> MBBS",
        "Business / Paisa       -> Commerce -> CA / BBA / B.Com",
        "Jaldi Govt Job         -> ITI / 12th -> SSC / Railway / Defence",
        "Creative ho            -> Arts -> Design / Animation / Media",
        "Defence join karna hai -> NDA / Agniveer / Sainik School",
        "Teacher banna hai      -> Graduation -> B.Ed",
        "IAS / IPS banna hai    -> Graduation -> UPSC",
    ])
    d.space(6)

    # ---- Tips --------------------------------------------------------
    d.h2("Choose Karne se Pehle Tips")
    d.bullet("Apni INTEREST pehchaano - kis cheez me sabse zyada maza aata hai?")
    d.bullet("Apni STRENGTH dekho - Maths / Biology / Creativity / Sports?")
    d.bullet("FAMILY situation socho - lamba course ya jaldi earning?")
    d.bullet("Confuse ho to Career Counsellor se baat karo.")
    d.bullet("Doston ko blindly follow mat karo - career YOUR future hai.")
    d.space(6)

    # ---- Practice Questions -----------------------------------------
    d.h2("Practice Questions (Khud Try Karo!)")
    d.body("In 22 questions ke jawab khud sochne ki koshish karo. Answers neeche answer "
           "key me diye gaye hain.", color=GREY)
    d.space(3)

    questions = [
        "Engineer banne ke liye 11th me kaunsa stream/subjects lene chahiye?",
        "Doctor (MBBS) banne ke liye kaunsa entrance exam dena padta hai?",
        "PCB ka full form kya hai?",
        "CA banne ke liye 12th ke baad pehla exam kaunsa hota hai?",
        "Diploma / Polytechnic 10th ke baad kitne saal ka hota hai?",
        "Diploma ke baad B.Tech me kis entry se direct 2nd year milta hai?",
        "NDA exam kab de sakte hain?",
        "ITI ka 'Electrician' kis category ka trade hai?",
        "Law (integrated 5-year) ke liye 12th ke baad kaunsa course?",
        "Architect banne ke liye kaunsa course hai?",
        "Commerce me bina Maths ke kaunse career options hain (2 batao)?",
        "Pilot banne ke liye kaunsa license chahiye?",
        "Teacher banne ke liye graduation ke baad kaunsa course?",
        "IAS / IPS banne ke liye kaunsa exam dena padta hai?",
        "NIOS kis cheez ke liye hota hai?",
        "Merchant Navy ke liye Science me kaunsa course hai?",
        "Fashion Designing ke liye 2 famous institutes batao.",
        "Veterinary (animal) doctor banne ka course kaunsa hai?",
        "Hotel Management ka degree course kaunsa hai?",
        "Agniveer scheme kis path me aati hai?",
        "Jaldi paisa + skill chahiye to kaunsa path best hai?",
        "B.Ed kis ke liye zaroori hota hai?",
    ]
    for i, q in enumerate(questions, start=1):
        d.label_body(f"Q{i}.", q)
        d.space(2)

    # ---- Answer Key --------------------------------------------------
    d.h2("Answer Key")
    answers = [
        "Science stream - PCM (Physics, Chemistry, Maths)",
        "NEET",
        "Physics, Chemistry, Biology",
        "CA Foundation",
        "Lagbhag 3 saal",
        "Lateral Entry",
        "12th ke baad",
        "Engineering trade",
        "BA-LLB ya BBA-LLB (5 saal)",
        "B.Arch (5 saal)",
        "B.Com, BBA, CA, CS me se koi 2",
        "CPL (Commercial Pilot License)",
        "B.Ed",
        "UPSC (Civil Services) - graduation ke baad",
        "Open schooling / distance learning",
        "B.Sc Nautical Science",
        "NIFT aur NID",
        "B.V.Sc (Veterinary Science)",
        "BHM (Bachelor of Hotel Management)",
        "Defence (Army / Navy / Air Force)",
        "ITI / Diploma / Vocational course",
        "Teacher banne ke liye",
    ]
    for i, a in enumerate(answers, start=1):
        d.bullet(f"Q{i}: {a}")

    return d


if __name__ == "__main__":
    doc = build_document()
    out_file = "Courses_After_10th_India.pdf"
    pages = write_pdf(doc, out_file)
    print(f"Generated '{out_file}' with {pages} page(s).")
