#!/usr/bin/env python3
"""
PCB (Physics, Chemistry, Biology) Medical & Science Complete Career Guide PDF Generator
Generates a comprehensive PDF about all career paths after 12th PCB in India
Uses ONLY built-in Python libraries - NO external packages needed
Content in Hinglish (Hindi + English mix)
"""

import re
import zlib
from pathlib import Path

CONTENT = """

=====================================================================
PCB (PHYSICS, CHEMISTRY, BIOLOGY) - COMPLETE CAREER GUIDE AFTER 12TH
=====================================================================
Yeh guide un sabhi students ke liye hai jo 12th mein PCB (Physics,
Chemistry, Biology) stream se pass hue hain ya kar rahe hain.
Is guide mein aapko Medical, Paramedical, Pure Science, Agriculture,
Research aur bahut saare career options ki FULL detail milegi.

=====

[GENERAL PCB INFORMATION - OVERVIEW]

>> PCB Stream Kya Hai?
PCB yaani Physics, Chemistry, Biology - yeh stream un students ke
liye hai jo Medical field ya Life Sciences mein career banana chahte
hain. 12th ke baad PCB students ke paas 50+ career options available
hain - sirf MBBS nahi!

>> Eligibility (General):
- 12th pass with PCB subjects (Physics, Chemistry, Biology)
- Minimum 50% marks (General category) / 40% (Reserved categories)
- NEET UG qualification (for medical courses)
- Age: 17 years minimum at time of admission

>> Important Entrance Exams for PCB Students:
- NEET UG: Medical/Dental/Ayush courses ke liye (Most Important)
- NEET PG: MD/MS/MDS admission ke liye (after MBBS/BDS)
- AIIMS (now merged with NEET), JIPMER (merged with NEET)
- ICAR AIEEA: Agriculture courses ke liye
- CUET: Central Universities mein B.Sc courses ke liye
- NISER/IISER Aptitude Test: Integrated BS-MS ke liye
- State Level: UP CPAT, MH-CET, KCET, WBJEE etc.

>> NEET UG Complete Details:
- Conducting Body: NTA (National Testing Agency)
- Mode: Offline (Pen & Paper)
- Total Marks: 720 (180 questions x 4 marks each)
- Subjects: Physics (45Q), Chemistry (45Q), Biology (90Q)
- Negative Marking: -1 for wrong answer
- Language: English, Hindi + 11 regional languages
- Attempts: No limit (age limit removed by Supreme Court)
- Qualifying Marks: 50th percentile (General), 40th (OBC/SC/ST)
- Seats through NEET: MBBS (1,08,000+), BDS (27,000+), AYUSH (52,000+)

=====


[1. MBBS - BACHELOR OF MEDICINE & BACHELOR OF SURGERY]

>> What is MBBS?
MBBS (Bachelor of Medicine and Bachelor of Surgery) India ka sabse
prestigious medical degree hai. Iske baad aap legally patients ko
treat kar sakte ho. Yeh allopathy (modern medicine) ka course hai.
MBBS doctor ko "Dr." title milta hai aur Medical Council of India
(now NMC - National Medical Commission) se registration hoti hai.

>> Duration: 5.5 years (4.5 years academic + 1 year internship)
   Bond Period: Government colleges mein 1-3 years rural service bond
   (varies state to state - Rajasthan 1yr, Tamil Nadu 2yr, UP 3yr)

>> Eligibility:
- 12th pass with PCB + English
- Minimum 50% marks (General), 40% (SC/ST/OBC)
- NEET UG qualified with valid score
- Age: 17 years minimum (no upper limit now)
- Indian citizen / NRI / OCI

>> Fee Structure:
- Government Medical College: Rs 15,000 - 5,00,000 per year
  (Total 5.5 years: Rs 1 - 25 Lakh approximately)
- State Quota Government: Rs 50,000 - 3,00,000 per year
- Private Medical College: Rs 10 - 25 Lakh per year
  (Total: Rs 50 Lakh - 1.5 Crore)
- Deemed University: Rs 15 - 30 Lakh per year
  (Total: Rs 75 Lakh - 2 Crore)
- Management/NRI Quota: Rs 25 - 50 Lakh per year

>> NEET Score Required (Approximate):
- Government College (AIQ): 550-680+ out of 720
- State Govt College: 450-600+
- Private College: 350-500+
- Deemed University: 300-450+

>> Key Subjects (Year-wise):
  Phase 1 (1st year): Anatomy, Physiology, Biochemistry
  Phase 2 (2nd year): Pathology, Pharmacology, Microbiology,
    Forensic Medicine, Community Medicine (Part 1)
  Phase 3 Part 1 (3rd year): Ophthalmology, ENT (Ear Nose Throat),
    Community Medicine (Part 2)
  Phase 3 Part 2 (4th year): Medicine, Surgery, Pediatrics,
    Obstetrics & Gynaecology, Orthopaedics, Anaesthesia,
    Dermatology, Psychiatry, Radiology

>> Top Medical Colleges in India:
1. AIIMS New Delhi (Rank #1, Fee: Rs 1,628/year only!)
2. JIPMER Puducherry (Rank #2, Fee: Rs 2,750/year)
3. CMC Vellore (Rank #3, Fee: Rs 30,000/year)
4. AFMC Pune (Army, Fee: Rs 50,000/year)
5. Maulana Azad Medical College, Delhi
6. King George Medical University, Lucknow
7. Grant Medical College, Mumbai
8. Madras Medical College, Chennai
9. BHU IMS, Varanasi
10. PGIMER Chandigarh


>> Job Roles after MBBS:
1. General Physician (MBBS Doctor) - OPD/Clinic
2. Medical Officer (Government Hospital)
3. Emergency Medicine Doctor (Casualty/ER)
4. Rural Health Officer (PHC/CHC)
5. Research Associate (Clinical Trials)
6. Medical Advisor (Pharma Companies)
7. Insurance Medical Officer
8. Railway/ESI/Army Medical Officer

>> Salary Breakdown:
- Fresher (After Internship): Rs 40,000 - 80,000/month
- Government Medical Officer: Rs 60,000 - 1,20,000/month + DA + HRA
- Private Hospital (Junior): Rs 50,000 - 1,00,000/month
- After 3-5 years experience: Rs 1,00,000 - 2,50,000/month
- Own Clinic (Established): Rs 2,00,000 - 10,00,000/month
- After MD/MS (Specialist): Rs 2,00,000 - 5,00,000/month
- Super Specialist (DM/MCh): Rs 5,00,000 - 25,00,000/month
- Abroad (USA after USMLE): $2,50,000 - $5,00,000/year
- Abroad (UK after PLAB): 50,000 - 1,00,000 GBP/year

>> Top Recruiters/Hospitals:
- Apollo Hospitals, Fortis Healthcare, Max Healthcare
- Medanta, Narayana Health, Manipal Hospitals
- AIIMS (all branches), Government State Hospitals
- Aster DM, Columbia Asia, Tata Memorial
- WHO, UNICEF, MSF (Doctors Without Borders)

>> Future Scope & PG Options:
- MD (Doctor of Medicine) - 25+ specializations
- MS (Master of Surgery) - 10+ specializations
- DNB (Diplomate National Board)
- Super Specialization: DM, MCh (3 years after MD/MS)
- MBA in Healthcare Management
- MPH (Master of Public Health)
- PhD / Research

>> PG After MBBS - MD Branches:
  MD Medicine, MD Pediatrics, MD Dermatology (Skin),
  MD Radiology, MD Anaesthesia, MD Pathology,
  MD Microbiology, MD Pharmacology, MD Biochemistry,
  MD Community Medicine, MD Forensic Medicine,
  MD Psychiatry, MD Respiratory Medicine (Pulmonology),
  MD Nuclear Medicine, MD Physical Medicine & Rehabilitation

>> PG After MBBS - MS Branches:
  MS General Surgery, MS Orthopaedics, MS Ophthalmology,
  MS ENT, MS Obstetrics & Gynaecology, MS Anatomy

>> Super Specializations (DM - after MD):
  DM Cardiology, DM Neurology, DM Gastroenterology,
  DM Nephrology, DM Pulmonary Medicine, DM Endocrinology,
  DM Rheumatology, DM Hematology, DM Oncology (Medical),
  DM Neonatology, DM Critical Care, DM Hepatology

>> Super Specializations (MCh - after MS):
  MCh Cardiothoracic Surgery, MCh Neurosurgery,
  MCh Plastic Surgery, MCh Urology, MCh Pediatric Surgery,
  MCh Surgical Oncology, MCh Vascular Surgery,
  MCh Surgical Gastroenterology

=====


[2. BDS - BACHELOR OF DENTAL SURGERY]

>> What is BDS?
BDS (Bachelor of Dental Surgery) dental science ka undergraduate
course hai. Isme teeth, gums, jaw aur oral cavity ke treatment ki
padhai hoti hai. BDS ke baad aap Dentist ban sakte ho aur "Dr."
title use kar sakte ho. Dental Council of India se registration hoti hai.

>> Duration: 5 years (4 years academic + 1 year internship)

>> Eligibility:
- 12th pass with PCB + English
- NEET UG qualified
- Minimum 50% marks (General), 40% (Reserved)
- Age: 17 years minimum

>> Fee Structure:
- Government Dental College: Rs 20,000 - 3,00,000/year
  (Total: Rs 1 - 15 Lakh)
- Private Dental College: Rs 3 - 12 Lakh/year
  (Total: Rs 15 - 60 Lakh)
- Deemed University: Rs 5 - 15 Lakh/year

>> NEET Score Required:
- Govt Dental College: 450-580+
- Private Dental: 300-450+

>> Key Subjects (Year-wise):
  1st Year: General Anatomy, Physiology, Biochemistry, Dental Materials
  2nd Year: Dental Anatomy, Oral Histology, General Pathology,
    Microbiology, Pharmacology
  3rd Year: Oral Pathology, Oral Surgery, Conservative Dentistry,
    Prosthodontics, Periodontics
  4th Year: Orthodontics, Pedodontics, Community Dentistry,
    Oral Medicine & Radiology, Public Health Dentistry

>> Top Dental Colleges:
1. Maulana Azad Institute of Dental Sciences, Delhi
2. Manipal College of Dental Sciences
3. SRM Dental College, Chennai
4. Government Dental College, Mumbai
5. King George Medical University Dental Wing
6. SDM College of Dental Sciences, Dharwad
7. AB Shetty Memorial, Mangalore
8. Faculty of Dental Sciences, BHU

>> Job Roles after BDS:
1. General Dentist (Private Practice)
2. Dental Surgeon (Government Hospital)
3. Orthodontist (after MDS)
4. Cosmetic Dentist
5. Oral & Maxillofacial Surgeon
6. Dental Researcher
7. Dental Public Health Officer
8. Dental Material Sales (Companies)

>> Salary Breakdown:
- Fresher BDS: Rs 25,000 - 50,000/month
- Govt Dental Surgeon: Rs 50,000 - 1,00,000/month
- Private Clinic (Employed): Rs 40,000 - 80,000/month
- Own Dental Clinic: Rs 1,00,000 - 5,00,000/month
- After MDS Specialist: Rs 1,50,000 - 4,00,000/month
- Abroad (USA/UK/Gulf): Rs 3 - 10 Lakh/month equivalent

>> MDS Specializations:
- Orthodontics & Dentofacial Orthopaedics (teeth alignment)
- Prosthodontics (artificial teeth/crown/bridge)
- Conservative Dentistry & Endodontics (RCT specialist)
- Oral & Maxillofacial Surgery (jaw surgery)
- Periodontics (gum specialist)
- Pedodontics (children dentist)
- Oral Pathology & Microbiology
- Oral Medicine & Radiology
- Public Health Dentistry

>> Top Recruiters: Apollo Dental, Clove Dental, Sabka Dentist,
   MyDentist, Dental Kraft, Government Hospitals, PHCs

>> Future Scope: Own practice bahut profitable hai. Cosmetic dentistry
   aur Implantology mein bahut scope hai. Abroad jaane ka bhi option
   - USA mein NBDE exam deke practice kar sakte ho.

=====


[3. BAMS - BACHELOR OF AYURVEDIC MEDICINE & SURGERY]

>> What is BAMS?
BAMS ek AYUSH category ka medical degree hai jo Ayurveda (ancient
Indian medicine system) par based hai. BAMS doctors ko bhi "Dr."
title milta hai. Ye log Ayurvedic medicines, Panchkarma therapy,
aur traditional Indian healing practices se treatment karte hain.
NMC recognition ke baad BAMS doctors modern medicine bhi practice
kar sakte hain (Bridge Course ke through).

>> Duration: 5.5 years (4.5 years academic + 1 year internship)

>> Eligibility:
- 12th pass with PCB
- NEET UG qualified
- Minimum 50% marks (General), 40% (SC/ST)

>> Fee Structure:
- Government Ayurvedic College: Rs 10,000 - 1,50,000/year
  (Total: Rs 50,000 - 8 Lakh)
- Private Ayurvedic College: Rs 1 - 5 Lakh/year
  (Total: Rs 5 - 25 Lakh)

>> NEET Score Required: 250-400+ (Government), 150-300 (Private)

>> Key Subjects:
  1st Year: Padarth Vigyan (Basic Principles), Rachana Sharir (Anatomy),
    Kriya Sharir (Physiology), Sanskrit
  2nd Year: Dravyaguna (Pharmacology), Rasa Shastra (Chemistry),
    Rog Nidan (Pathology), Swasthavritta (Preventive Medicine)
  3rd Year: Kayachikitsa (Medicine), Shalya Tantra (Surgery),
    Shalakya Tantra (ENT/Eye), Prasuti Tantra (Obstetrics)
  4th Year: Advanced Kayachikitsa, Panchkarma, Research Methodology

>> Top BAMS Colleges:
1. BHU (Faculty of Ayurveda), Varanasi
2. National Institute of Ayurveda (NIA), Jaipur
3. Gujarat Ayurved University, Jamnagar
4. Tilak Ayurved Mahavidyalaya, Pune
5. SDM College of Ayurveda, Udupi
6. Institute of Medical Sciences, BHU
7. Rajiv Gandhi University of Health Sciences affiliated colleges

>> Job Roles:
1. Ayurvedic Doctor (Clinic/Hospital)
2. Panchkarma Specialist
3. Government Medical Officer (AYUSH)
4. Ayurvedic Researcher
5. Wellness Center Consultant
6. Quality Control (Ayurvedic Pharma)
7. Yoga & Naturopathy Consultant
8. Medical Tourism Consultant

>> Salary Breakdown:
- Fresher BAMS: Rs 20,000 - 40,000/month
- Govt AYUSH Medical Officer: Rs 50,000 - 90,000/month
- Private Practice (1-3 years): Rs 30,000 - 70,000/month
- Established Clinic: Rs 80,000 - 3,00,000/month
- Panchkarma Center (Own): Rs 1,00,000 - 5,00,000/month
- Pharma Industry: Rs 40,000 - 1,00,000/month
- Abroad (Wellness/Spa): Rs 1 - 3 Lakh/month

>> Bridge Course: NMC ne Bridge Course introduce kiya hai jisse BAMS
   doctors modern medicine bhi practice kar sakte hain limited capacity
   mein. Isse BAMS ka scope aur badh gaya hai.

>> Future Scope: Ayurveda ka demand globally badh raha hai. Medical
   Tourism, Wellness Industry, Organic Products mein bahut scope.
   Government bhi AYUSH ko promote kar rahi hai - standalone AYUSH
   ministry ban gayi hai.

=====


[4. BHMS - BACHELOR OF HOMEOPATHIC MEDICINE & SURGERY]

>> What is BHMS?
BHMS (Bachelor of Homeopathic Medicine and Surgery) homeopathy
system of medicine ka degree course hai. Homeopathy mein "like
cures like" principle follow hota hai - bahut diluted doses mein
medicines di jaati hain. India mein homeopathy bahut popular hai
aur government recognized hai.

>> Duration: 5.5 years (4.5 years + 1 year internship)

>> Eligibility:
- 12th with PCB, NEET UG qualified
- Minimum 50% (General), 40% (Reserved)

>> Fee Structure:
- Government: Rs 10,000 - 1,00,000/year (Total: Rs 50K - 5 Lakh)
- Private: Rs 1 - 4 Lakh/year (Total: Rs 5 - 20 Lakh)

>> Key Subjects:
  Organon of Medicine, Materia Medica, Repertory,
  Anatomy, Physiology, Pathology, Forensic Medicine,
  Surgery, Obstetrics & Gynaecology, Community Medicine,
  Practice of Medicine (Homeopathic)

>> Top Colleges:
1. National Institute of Homoeopathy (NIH), Kolkata
2. Bakson Homoeopathic Medical College, Greater Noida
3. Father Muller Homoeopathic Medical College, Mangalore
4. Dr. B.R. Sur Homoeopathic Medical College, Delhi
5. Nehru Homoeopathic Medical College, Delhi
6. BJMC Homeopathic College, Ahmedabad

>> Job Roles:
1. Homeopathic Doctor (Private Practice)
2. Government AYUSH Medical Officer
3. Homeopathic Researcher
4. Homeopathic Pharma Company
5. Clinical Trial Associate
6. Health & Wellness Consultant
7. Homeopathic Dispensary Doctor

>> Salary:
- Fresher: Rs 15,000 - 35,000/month
- Government MO (AYUSH): Rs 45,000 - 85,000/month
- Private Practice (Established): Rs 50,000 - 2,00,000/month
- Own Clinic (5+ years): Rs 1,00,000 - 4,00,000/month

>> PG Options: MD (Homeopathy) in Organon, Materia Medica,
   Repertory, Pediatrics, Psychiatry, Practice of Medicine

>> Future Scope: Chronic diseases mein homeopathy ka demand badh raha
   hai. Skin problems, allergies, mental health mein patients prefer
   karte hain. Europe aur South America mein bhi popular hai.

=====

[5. BUMS - BACHELOR OF UNANI MEDICINE & SURGERY]

>> What is BUMS?
BUMS (Bachelor of Unani Medicine and Surgery) Unani system of
medicine ka course hai. Yeh Greek-Arabic medicine tradition par
based hai jo India mein Mughal era se practice ho raha hai.
Unani medicine mein herbal medicines, diet therapy aur regimenal
therapy use hoti hai.

>> Duration: 5.5 years (4.5 years + 1 year internship)

>> Eligibility: 12th PCB, NEET UG, Urdu/Arabic knowledge preferred

>> Fee Structure:
- Government: Rs 10,000 - 80,000/year
- Private: Rs 50,000 - 3,00,000/year

>> Key Subjects: Kulliyat (Fundamentals), Tashreeh (Anatomy),
   Munafe-ul-Aza (Physiology), Advia (Pharmacology),
   Moalijat (Medicine), Jarahiyat (Surgery), Amraz-e-Niswan (Gynae),
   Ilmul Atfal (Pediatrics), Tahaffuzi-wa-Samaji Tib (PSM)

>> Top Colleges:
1. Jamia Hamdard University, Delhi (Best for Unani)
2. AMU (Aligarh Muslim University)
3. Govt Nizamia Tibbi College, Hyderabad
4. National Institute of Unani Medicine (NIUM), Bangalore
5. A & U Tibbia College, Delhi

>> Job Roles & Salary:
- Unani Doctor: Rs 20,000 - 60,000/month
- Govt AYUSH MO: Rs 45,000 - 85,000/month
- Own Practice: Rs 50,000 - 2,00,000/month
- Unani Pharma: Rs 30,000 - 70,000/month
- Research: Rs 35,000 - 80,000/month

=====


[6. BNYS - BACHELOR OF NATUROPATHY & YOGIC SCIENCES]

>> What is BNYS?
BNYS ek drugless therapy system hai jisme natural methods se
treatment hota hai - Yoga, Diet, Hydrotherapy, Mud therapy,
Acupuncture, Massage etc. India mein PM Modi ke Yoga promotion
se iska scope bahut badha hai.

>> Duration: 5.5 years (4.5 years + 1 year internship)

>> Eligibility: 12th PCB, NEET UG (some states), some colleges
   conduct own entrance exam

>> Fee Structure:
- Government: Rs 15,000 - 1,50,000/year
- Private: Rs 50,000 - 3,00,000/year

>> Key Subjects: Anatomy, Physiology, Biochemistry, Yoga Therapy,
   Naturopathy Principles, Acupuncture, Hydrotherapy, Diet Therapy,
   Massage Therapy, Psychology, Modern Diagnostics, Research Methods

>> Top Colleges:
1. SVYASA (Swami Vivekananda Yoga Anusandhana), Bangalore
2. SDM College of Naturopathy, Ujire
3. Government Yoga & Naturopathy College, Chennai
4. JSS Naturopathy Medical College, Mysore
5. TNMC (Tamil Nadu), Gandhigram Naturopathy

>> Job Roles:
1. Naturopathy Doctor / Yoga Therapist
2. Wellness Center Director
3. Corporate Wellness Consultant
4. Resort/Spa Medical Director
5. Sports Rehabilitation Specialist
6. International Yoga Instructor (certified)

>> Salary:
- Fresher: Rs 20,000 - 40,000/month
- Wellness Center: Rs 40,000 - 1,00,000/month
- Own Center (Established): Rs 1,00,000 - 5,00,000/month
- Corporate Wellness: Rs 50,000 - 1,50,000/month
- International (Yoga Tourism): Rs 1 - 4 Lakh/month

>> Future Scope: Yoga & Naturopathy ka global demand exponentially
   badh raha hai. Medical tourism, corporate wellness, preventive
   healthcare mein bahut scope. Government bhi promote kar rahi hai.

=====

[7. B.PHARMA - BACHELOR OF PHARMACY]

>> What is B.Pharma?
B.Pharma (Bachelor of Pharmacy) pharmaceutical sciences ka
4-year degree course hai. Isme medicine design, manufacturing,
quality control, drug dispensing ki padhai hoti hai. Pharmacy
graduates pharmacist ban sakte hain aur medical store bhi
khol sakte hain (Drug License ke saath).

>> Duration: 4 years (B.Pharma), 2 years (D.Pharma), 6 years (PharmD)

>> Eligibility:
- 12th with PCB/PCM (Both eligible for pharmacy)
- B.Pharma: State entrance exams (WBJEE, KCET, MH-CET etc.)
- D.Pharma: Direct admission or state exams
- PharmD: GPAT/NEET (varies by college)

>> Fee Structure:
- D.Pharma (Govt): Rs 10,000 - 50,000/year (Total: Rs 20K - 1 Lakh)
- D.Pharma (Pvt): Rs 30,000 - 1,50,000/year (Total: Rs 60K - 3 Lakh)
- B.Pharma (Govt): Rs 15,000 - 1,00,000/year (Total: Rs 60K - 4 Lakh)
- B.Pharma (Pvt): Rs 50,000 - 3,00,000/year (Total: Rs 2 - 12 Lakh)
- M.Pharma (Govt): Rs 20,000 - 1,50,000/year
- PharmD (6 yr): Rs 50,000 - 4,00,000/year

>> D.Pharma vs B.Pharma vs M.Pharma vs PharmD:
- D.Pharma: 2 years, basic pharmacy, can open medical store
- B.Pharma: 4 years, more depth, industry jobs better
- M.Pharma: 2 years (after B.Pharma), specialization, research
- PharmD: 6 years (3+3), clinical pharmacy, hospital pharmacist

>> Key Subjects (B.Pharma):
  1st Year: Pharmaceutics, Pharma Chemistry, Pharmacognosy, Anatomy
  2nd Year: Physical Pharmaceutics, Medicinal Chemistry,
    Pharmacology, Microbiology
  3rd Year: Industrial Pharmacy, Biopharmaceutics, Hospital Pharmacy,
    Pharmaceutical Analysis
  4th Year: Pharmaceutical Technology, Clinical Pharmacy,
    Pharmacovigilance, Drug Regulatory Affairs

>> Top Pharmacy Colleges:
1. NIPER (National Institute of Pharma Education & Research)
2. Jamia Hamdard, Delhi
3. ICT Mumbai (Institute of Chemical Technology)
4. Manipal College of Pharmaceutical Sciences
5. JSS College of Pharmacy, Mysore/Ooty
6. Bombay College of Pharmacy
7. LM College of Pharmacy, Ahmedabad
8. BITS Pilani (Pharmacy)


>> Job Roles:
1. Retail Pharmacist (Medical Store)
2. Hospital Pharmacist (Clinical)
3. Drug Inspector (Government)
4. Medical Representative (MR)
5. Production Manager (Pharma Industry)
6. Quality Control/Quality Assurance Analyst
7. Research Scientist (R&D)
8. Drug Regulatory Affairs Officer
9. Pharmacovigilance Associate
10. Clinical Research Associate (CRA)

>> Salary Breakdown:
- D.Pharma (Medical Store): Rs 15,000 - 30,000/month
- B.Pharma Fresher (Industry): Rs 20,000 - 40,000/month
- Medical Representative: Rs 25,000 - 50,000/month + incentives
- Hospital Pharmacist: Rs 25,000 - 60,000/month
- QC/QA (3-5 years): Rs 40,000 - 1,00,000/month
- Drug Inspector (Govt): Rs 50,000 - 1,00,000/month
- M.Pharma (Industry): Rs 35,000 - 80,000/month
- R&D Scientist (5+ yrs): Rs 80,000 - 2,00,000/month
- Pharma Manager (10+ yrs): Rs 1,50,000 - 4,00,000/month
- Own Medical Store: Rs 40,000 - 2,00,000/month (profit)
- Abroad (USA/Canada): Rs 2 - 5 Lakh/month equivalent

>> Top Recruiters:
- Sun Pharma, Cipla, Dr. Reddy's, Lupin, Zydus Cadila
- Ranbaxy (now Sun), Torrent Pharma, Glenmark
- Biocon, Serum Institute, Divis Labs
- MNC: Pfizer, Novartis, Johnson & Johnson, GSK
- Abbott, AstraZeneca, Sanofi, Roche

>> Future Scope: Indian pharma industry $50 billion+ hai aur rapidly
   growing hai. Clinical Research, Pharmacovigilance, Drug Discovery
   mein bahut jobs hain. Pharmacy + MBA = excellent career.

=====

[8. B.SC NURSING - NURSING CAREER PATH]

>> What is B.Sc Nursing?
B.Sc Nursing healthcare ka backbone hai. Nurses patient care,
hospital management, aur healthcare delivery mein crucial role
play karti hain. India mein aur abroad dono jagah nurses ki
bahut demand hai - especially USA, UK, Canada, Australia, Gulf.

>> Course Options in Nursing:
- ANM (Auxiliary Nurse Midwife): 2 years (after 10th/12th)
- GNM (General Nursing & Midwifery): 3.5 years (after 12th)
- B.Sc Nursing: 4 years (after 12th with PCB)
- Post Basic B.Sc Nursing: 2 years (after GNM)
- M.Sc Nursing: 2 years (after B.Sc Nursing)

>> Duration: B.Sc Nursing - 4 years

>> Eligibility:
- 12th with PCB, minimum 45-55% marks
- Age: 17-35 years
- NEET score (for government colleges in some states)
- Some states have separate nursing entrance exams

>> Fee Structure:
- B.Sc Nursing (Govt): Rs 10,000 - 80,000/year (Total: Rs 40K-3.2L)
- B.Sc Nursing (Pvt): Rs 50,000 - 2,50,000/year (Total: Rs 2-10L)
- GNM (Govt): Rs 5,000 - 40,000/year
- GNM (Pvt): Rs 30,000 - 1,50,000/year

>> Key Subjects:
  1st Year: Anatomy, Physiology, Microbiology, Nutrition,
    Psychology, Nursing Foundations
  2nd Year: Pharmacology, Medical-Surgical Nursing,
    Community Health Nursing, Pathology
  3rd Year: Child Health Nursing, Mental Health Nursing,
    Midwifery & Obstetrical Nursing
  4th Year: Nursing Research, Nursing Management,
    Advanced Medical-Surgical Nursing

>> Top Nursing Colleges:
1. AIIMS Delhi (College of Nursing)
2. CMC Vellore (Nursing)
3. PGIMER Chandigarh
4. RAK College of Nursing, Delhi
5. Armed Forces Nursing Service
6. St. John's Medical College Nursing, Bangalore
7. Manipal College of Nursing
8. NIMHANS Nursing, Bangalore

>> Job Roles:
1. Staff Nurse (Hospital/Clinic)
2. ICU/CCU Nurse (Critical Care)
3. Operation Theatre (OT) Nurse
4. Community Health Nurse (PHC)
5. Nursing Superintendent
6. Nurse Educator / Professor
7. Home Care Nurse
8. Industrial Nurse
9. Military Nurse (Armed Forces)
10. International Nurse (Abroad)

>> Salary Breakdown:
- ANM: Rs 12,000 - 25,000/month
- GNM: Rs 15,000 - 35,000/month
- B.Sc Nursing (Fresher): Rs 20,000 - 45,000/month
- Govt Staff Nurse: Rs 35,000 - 80,000/month (7th Pay)
- Private Hospital (3-5 yr): Rs 30,000 - 60,000/month
- M.Sc Nursing: Rs 40,000 - 1,00,000/month
- Nursing Superintendent: Rs 80,000 - 1,50,000/month
- Gulf Countries (Saudi/UAE): Rs 60,000 - 1,50,000/month
- UK Nurse: Rs 2 - 4 Lakh/month equivalent
- USA (RN): Rs 3 - 6 Lakh/month equivalent
- Canada Nurse: Rs 2.5 - 5 Lakh/month equivalent
- Australia: Rs 3 - 5 Lakh/month equivalent

>> Top Recruiters: AIIMS, Apollo, Fortis, Max, Medanta, Narayana,
   Government Hospitals, Indian Army/Navy/Air Force (Nursing),
   Railways, ESI Hospitals, WHO, Red Cross

>> Abroad Options: NCLEX-RN (USA), NMC-CBT (UK), HAAD/DHA (Gulf),
   AHPRA (Australia), NNAS (Canada)

>> Future Scope: Nursing shortage globally - 5.9 million nurses ki
   shortage hai worldwide (WHO report). India se trained nurses ki
   bahut demand hai abroad. Salary aur respect dono badh rahi hai.

=====


[9. BPT - BACHELOR OF PHYSIOTHERAPY]

>> What is BPT?
BPT (Bachelor of Physiotherapy) rehabilitation science ka course
hai. Physiotherapists musculoskeletal problems, sports injuries,
post-surgery recovery, neurological conditions ka treatment
exercises, manual therapy, electrotherapy se karte hain. Surgery
ke bina pain relief karna physiotherapy ka main aim hai.

>> Duration: 4.5 years (4 years + 6 months internship)

>> Eligibility:
- 12th with PCB, minimum 50% marks
- Some states: Entrance exam (state level)
- Common entrance: LPUNEST, IPU CET, MH-CET

>> Fee Structure:
- Government: Rs 15,000 - 1,00,000/year (Total: Rs 60K - 4.5L)
- Private: Rs 50,000 - 3,00,000/year (Total: Rs 2.5 - 15 Lakh)

>> Key Subjects:
  1st Year: Anatomy, Physiology, Biochemistry, Biomechanics
  2nd Year: Pathology, Pharmacology, Exercise Therapy,
    Electrotherapy, Research Methodology
  3rd Year: Orthopaedic PT, Neurological PT, Cardiopulmonary PT
  4th Year: Sports PT, Community PT, Rehabilitation,
    Pediatric PT, Geriatric PT

>> Top BPT Colleges:
1. CMC Vellore (Physiotherapy)
2. AIIMS Delhi (Physiotherapy Dept)
3. Manipal College of Allied Health Sciences
4. SRM College of Physiotherapy
5. ISIC (Indian Spinal Injuries Centre), Delhi
6. KMC Manipal
7. Guru Nanak Dev University
8. MAHE Manipal

>> Job Roles:
1. Clinical Physiotherapist (Hospital)
2. Sports Physiotherapist (Teams/Athletes)
3. Orthopaedic Physiotherapist
4. Neurological Physiotherapist
5. Cardiopulmonary Physiotherapist
6. Pediatric Physiotherapist
7. Rehabilitation Specialist
8. Private Practice (Own Clinic)

>> Salary:
- Fresher BPT: Rs 15,000 - 35,000/month
- Hospital (2-3 years): Rs 30,000 - 60,000/month
- Sports PT (IPL/Teams): Rs 50,000 - 2,00,000/month
- Govt Hospital: Rs 40,000 - 80,000/month
- Own Clinic (Established): Rs 80,000 - 3,00,000/month
- Abroad (USA/Canada/Aus): Rs 2 - 5 Lakh/month
- MPT + 5 years: Rs 60,000 - 1,50,000/month

>> MPT Specializations:
- MPT Orthopaedics, MPT Neurology, MPT Sports,
  MPT Cardiopulmonary, MPT Pediatrics, MPT Community,
  MPT Women's Health, MPT Hand Rehabilitation

>> Future Scope: Sports medicine booming in India (IPL, ISL, PKL
   teams hire physiotherapists). Corporate wellness, geriatric care
   (elderly population growing), post-COVID rehabilitation - demand
   bahut badhi hai. Own clinic = excellent income.

=====

[10. B.V.SC - BACHELOR OF VETERINARY SCIENCE & ANIMAL HUSBANDRY]

>> What is B.V.Sc?
B.V.Sc (Bachelor of Veterinary Science) animal doctor banne ka
course hai. Isme animals (pets, livestock, wildlife) ki diseases,
surgery, breeding, nutrition sab padhai hoti hai. Veterinary
doctors ko bhi "Dr." title milta hai.

>> Duration: 5.5 years (5 years + 6 months internship)

>> Eligibility:
- 12th with PCB, minimum 50% marks
- NEET UG qualified (veterinary colleges accept NEET)
- Some states: State level counselling through NEET

>> Fee Structure:
- Government Veterinary College: Rs 5,000 - 50,000/year
  (Total: Rs 25K - 2.5 Lakh - VERY affordable!)
- Private: Rs 1 - 4 Lakh/year (Total: Rs 5 - 22 Lakh)

>> Key Subjects:
  Anatomy, Physiology, Biochemistry, Veterinary Pharmacology,
  Veterinary Pathology, Veterinary Microbiology, Surgery & Radiology,
  Animal Genetics & Breeding, Livestock Production Management,
  Veterinary Medicine, Veterinary Gynaecology, Veterinary Public
  Health, Meat Technology, Dairy Technology

>> Top Colleges:
1. IVRI (Indian Veterinary Research Institute), Bareilly
2. Bombay Veterinary College (BVC), Mumbai
3. Madras Veterinary College, Chennai
4. College of Veterinary Science, Hyderabad
5. GADVASU, Ludhiana
6. GBPUAT, Pantnagar
7. Kerala Veterinary University
8. Rajasthan University of Vet & Animal Sciences

>> Job Roles:
1. Veterinary Doctor (Pet Clinic)
2. Livestock Officer (Government)
3. Animal Husbandry Officer
4. Wildlife Veterinarian (Forest Dept)
5. Dairy Industry Professional
6. Poultry/Fisheries Expert
7. Veterinary Researcher (ICAR)
8. Pet Food Company (R&D)
9. Zoos & Animal Parks Doctor

>> Salary:
- Fresher: Rs 25,000 - 50,000/month
- Govt Veterinary Officer: Rs 50,000 - 1,20,000/month
- Private Pet Clinic: Rs 30,000 - 80,000/month
- Own Pet Hospital (Established): Rs 1,00,000 - 5,00,000/month
- Wildlife Vet: Rs 40,000 - 1,00,000/month
- Dairy/Poultry Industry: Rs 35,000 - 90,000/month
- Research (MVSc + PhD): Rs 50,000 - 1,50,000/month
- Abroad: Rs 2 - 5 Lakh/month

>> Future Scope: Pet industry booming in India (Rs 3000 Crore market).
   Dairy, poultry, fisheries - India world's largest milk producer.
   Government jobs bahut hain (Animal Husbandry Dept). Pet hospitals
   in metros = very profitable business.

=====


[11. B.SC AGRICULTURE - AGRICULTURAL SCIENCE]

>> What is B.Sc Agriculture?
B.Sc Agriculture 4-year degree course hai jisme farming science,
crop production, soil science, agricultural economics, horticulture
sab padhai hoti hai. India agriculture-based economy hai - isme
government jobs, bank agriculture officer, agri-business ke
bahut options hain.

>> Duration: 4 years

>> Eligibility:
- 12th with PCB/PCM (Biology preferred)
- ICAR AIEEA (All India Entrance Exam for Agriculture)
- State level: EAMCET (AP/TS), KCET, MH-CET, BCECE
- CUET for Central Universities

>> Fee Structure:
- Govt Agriculture University: Rs 5,000 - 50,000/year (Very Low!)
- Private: Rs 30,000 - 2,00,000/year (Total: Rs 1.2 - 8 Lakh)
- ICAR scholarship: Rs 2,000/month stipend available

>> Key Subjects:
  1st Year: Fundamentals of Crop Production, Soil Science,
    Agriculture Chemistry, Agricultural Engineering
  2nd Year: Crop Improvement, Entomology (Insects), Plant Pathology,
    Agronomy, Agricultural Economics
  3rd Year: Seed Technology, Horticulture, Agricultural Extension,
    Livestock Production, Agricultural Marketing
  4th Year: Plant Breeding, Biotechnology, Organic Farming,
    Farm Management, Research Project

>> Top Agriculture Colleges:
1. IARI (Indian Agricultural Research Institute), Delhi - Pusa
2. TNAU (Tamil Nadu Agricultural University)
3. PAU (Punjab Agricultural University), Ludhiana
4. GBPUAT, Pantnagar (1st Agri University in India)
5. UAS Bangalore (University of Agri Sciences)
6. NDRI (National Dairy Research Institute), Karnal
7. JNKVV, Jabalpur
8. Assam Agricultural University

>> Job Roles:
1. Agriculture Officer (Bank - IBPS SO)
2. Agriculture Development Officer (State Govt)
3. Food Corporation of India (FCI) Officer
4. ICAR Scientist (Research)
5. Agronomist (Private Companies)
6. Agri-Business Entrepreneur
7. Farm Manager (Corporate Farming)
8. Agriculture Insurance Officer
9. Seed/Fertilizer Company Sales
10. Agriculture Journalist / Consultant

>> Salary:
- Fresher: Rs 15,000 - 35,000/month
- Bank Agriculture Officer (IBPS): Rs 40,000 - 80,000/month
- Govt ADO: Rs 35,000 - 75,000/month
- ICAR Scientist: Rs 60,000 - 1,50,000/month
- Agri-business (Own): Rs 50,000 - 5,00,000/month
- Corporate Farming Manager: Rs 40,000 - 1,00,000/month
- FCI Officer: Rs 45,000 - 1,00,000/month
- M.Sc + NET: Rs 50,000 - 1,20,000/month (Teaching)

>> Future Scope: Agriculture + Technology = AgriTech (billion dollar
   industry). Organic farming, precision agriculture, agricultural
   drones, farm-to-table startups - isme bahut scope hai. Government
   jobs bhi bahut hain. MBA in Agribusiness = excellent career.

=====

[12. B.SC FORESTRY / HORTICULTURE]

>> What is B.Sc Forestry?
B.Sc Forestry mein forest management, wildlife conservation,
environmental science, timber technology padhai hoti hai. Forest
Officers (IFS through UPSC) banne ka base yahi course hai.

>> What is B.Sc Horticulture?
Horticulture mein fruits, vegetables, flowers, medicinal plants
ki commercial cultivation ki padhai hoti hai.

>> Duration: 4 years (both)

>> Eligibility: 12th PCB, ICAR AIEEA / State entrance exams

>> Fee: Govt: Rs 5,000-40,000/year | Private: Rs 30,000-1,50,000/yr

>> Top Colleges (Forestry):
1. FRI (Forest Research Institute), Dehradun (Best in India)
2. College of Forestry, Thrissur (KAU)
3. Dr. YS Parmar University, Solan (HP)
4. TNAU - FC&RI, Mettupalayam
5. OUAT College of Forestry, Odisha

>> Job Roles:
- Indian Forest Service (IFS) Officer - through UPSC
- Forest Range Officer (State PSC)
- Wildlife Warden / Conservator
- Timber Company Manager
- Horticulture Officer (Govt)
- Floriculture Business Owner
- Nursery Manager / Landscape Designer
- Environmental Consultant

>> Salary:
- Fresher: Rs 15,000 - 30,000/month
- Forest Range Officer: Rs 40,000 - 90,000/month
- IFS Officer: Rs 60,000 - 2,50,000/month (with perks)
- Horticulture Officer: Rs 35,000 - 80,000/month
- Environmental Consultant: Rs 40,000 - 1,50,000/month
- Own Nursery/Farm: Rs 30,000 - 3,00,000/month

=====


[13. B.SC MICROBIOLOGY]

>> What is B.Sc Microbiology?
B.Sc Microbiology mein bacteria, viruses, fungi, protozoa aur
unke applications ki padhai hoti hai. COVID pandemic ke baad
microbiology ka importance aur zyada badh gaya hai. Pharma,
food industry, environmental science mein microbiologists ki
bahut demand hai.

>> Duration: 3 years (B.Sc) + 2 years (M.Sc)

>> Eligibility: 12th with PCB, min 50% marks, CUET/University entrance

>> Fee: Govt: Rs 5,000-30,000/year | Pvt: Rs 30,000-1,50,000/year

>> Key Subjects:
  General Microbiology, Bacteriology, Virology, Mycology,
  Immunology, Medical Microbiology, Industrial Microbiology,
  Food Microbiology, Environmental Microbiology, Molecular Biology,
  Genetic Engineering, Biostatistics, Bioinformatics

>> Top Colleges:
1. St. Xavier's College, Mumbai
2. Fergusson College, Pune
3. Loyola College, Chennai
4. Christ University, Bangalore
5. Delhi University (Colleges)
6. Chandigarh University
7. Amity University

>> Job Roles:
1. Microbiologist (Hospital/Lab)
2. Quality Control Analyst (Pharma/Food)
3. Research Scientist (Biotech/Pharma)
4. Clinical Microbiologist
5. Food Safety Officer
6. Environmental Microbiologist
7. Industrial Fermentation Technologist
8. Epidemiologist

>> Salary:
- B.Sc Fresher: Rs 12,000 - 25,000/month
- M.Sc Microbiology: Rs 25,000 - 50,000/month
- QC Analyst (3-5 yr): Rs 35,000 - 80,000/month
- Research Scientist: Rs 40,000 - 1,20,000/month
- PhD + Post-doc: Rs 60,000 - 1,50,000/month
- Govt (DRDO/ICMR): Rs 50,000 - 1,20,000/month
- Abroad Research: Rs 2 - 4 Lakh/month

>> Future Scope: Post-COVID, microbiology me job market boomed.
   Vaccine development, antimicrobial resistance research, food
   safety - all growing fields. CSIR-NET clear karke professor/
   researcher ban sakte ho.

=====

[14. B.SC BIOTECHNOLOGY]

>> What is B.Sc Biotechnology?
Biotechnology mein living organisms aur biological systems ko use
karke products aur processes develop kiye jaate hain. Genetic
engineering, gene therapy, GMO crops, biofuels, pharmaceutical
biotech - yeh sab biotechnology ka part hai.

>> Duration: 3 years (B.Sc) / 4 years (B.Tech Biotech)
   Higher: M.Sc Biotech (2 yr), M.Tech Biotech (2 yr), PhD

>> Eligibility: 12th PCB with 50%+, CUET / University entrance

>> Fee:
- B.Sc Biotech (Govt): Rs 10,000 - 50,000/year
- B.Sc Biotech (Pvt): Rs 40,000 - 2,00,000/year
- B.Tech Biotech: Rs 1 - 4 Lakh/year (private)

>> Key Subjects:
  Cell Biology, Molecular Biology, Genetics, Biochemistry,
  Genetic Engineering, Immunology, Bioinformatics,
  Plant Biotechnology, Animal Biotechnology,
  Industrial Biotechnology, Environmental Biotechnology,
  Pharmaceutical Biotechnology, Bioprocess Engineering,
  Genomics & Proteomics

>> Top Colleges:
1. JNU (Jawaharlal Nehru University), Delhi
2. Delhi University (South Campus)
3. Anna University, Chennai
4. VIT Vellore (B.Tech Biotech)
5. Amity University
6. SRM University
7. Manipal University
8. IITs (M.Sc/M.Tech Biotech)
9. IISC Bangalore (M.Sc/PhD)

>> Job Roles:
1. Biotech Research Scientist
2. Genetic Engineer
3. Bioinformatics Analyst
4. Clinical Research Associate
5. Quality Control (Biotech Pharma)
6. Medical Writer / Scientific Writer
7. Patent Analyst (Biotech IP)
8. Regulatory Affairs Specialist
9. Bioprocess Engineer

>> Salary:
- B.Sc Fresher: Rs 12,000 - 25,000/month
- M.Sc Biotech: Rs 25,000 - 50,000/month
- Biotech Industry (3-5 yr): Rs 40,000 - 1,00,000/month
- Research (PhD): Rs 50,000 - 1,50,000/month
- Bioinformatics: Rs 35,000 - 1,20,000/month
- Abroad (USA/Europe): Rs 2 - 6 Lakh/month
- Senior Scientist (10+ yr): Rs 1,50,000 - 4,00,000/month

>> Top Recruiters: Biocon, Serum Institute, Bharat Biotech,
   Indian Immunologicals, Novozymes, Monsanto (Bayer), Syngenta,
   Panacea Biotech, Wockhardt, Genentech, Amgen (MNC)

>> Future Scope: Biotechnology 21st century ki most important field
   hai. COVID vaccine (Covaxin - Bharat Biotech) ne dikha diya ki
   biotech ka kitna importance hai. Gene therapy, CRISPR, synthetic
   biology, personalized medicine - future yahi hai.

=====


[15. B.SC GENETICS]

>> What is B.Sc Genetics?
Genetics mein heredity, DNA, genes, chromosomes, mutations aur
genetic disorders ki padhai hoti hai. Human Genome Project ke
baad genetics ek revolution hai medical science mein. Genetic
counselling, gene therapy, forensic genetics - sab growing fields.

>> Duration: 3 years (B.Sc) + 2 years (M.Sc Genetics)

>> Eligibility: 12th PCB, 50%+, CUET / University entrance

>> Fee: Govt: Rs 10,000-40,000/yr | Pvt: Rs 40,000-1,50,000/yr

>> Key Subjects: Mendelian Genetics, Molecular Genetics, Cytogenetics,
   Population Genetics, Microbial Genetics, Human Genetics, Genetic
   Engineering, Bioinformatics, Biostatistics, Genomics, Epigenetics

>> Top Colleges:
1. Delhi University (B.Sc Genetics)
2. Osmania University, Hyderabad
3. Bangalore University
4. University of Madras
5. MS University, Baroda (Gujarat)

>> Job Roles:
1. Genetic Counselor (Hospitals)
2. Research Scientist (Genetics Lab)
3. Forensic Geneticist (DNA profiling)
4. Plant/Animal Geneticist
5. Bioinformatics Specialist
6. Clinical Geneticist (after MD)
7. Pharmaceutical Geneticist

>> Salary:
- B.Sc Fresher: Rs 12,000 - 22,000/month
- M.Sc Genetics: Rs 25,000 - 50,000/month
- Genetic Counselor: Rs 30,000 - 80,000/month
- Research (PhD level): Rs 50,000 - 1,50,000/month
- Forensic Genetics (Govt): Rs 40,000 - 1,00,000/month
- Abroad: Rs 2 - 5 Lakh/month

>> Future Scope: Personalized medicine, pharmacogenomics, gene
   editing (CRISPR), genetic testing companies (23andMe type) -
   India mein bhi MedGenome, Mapmygenome jaise companies grow
   kar rahi hain. Bahut promising field hai.

=====

[16. B.OPTOMETRY - BACHELOR OF OPTOMETRY]

>> What is B.Optometry?
B.Optometry eye care ka specialized course hai. Optometrists
eye examination, vision testing, spectacle prescription, contact
lens fitting, aur eye disease screening karte hain. Ye
ophthalmologist (eye surgeon) se alag hain - optometrist surgery
nahi karte but vision correction aur eye care karte hain.

>> Duration: 4 years (3.5 years + 6 months internship)

>> Eligibility: 12th PCB, 50%+, State entrance / University exam

>> Fee:
- Govt: Rs 10,000 - 60,000/year
- Private: Rs 40,000 - 2,00,000/year (Total: Rs 1.6 - 8 Lakh)

>> Key Subjects:
  Visual Optics, Ocular Anatomy, Physiology of Vision,
  Clinical Optometry, Contact Lens Practice, Binocular Vision,
  Pediatric Optometry, Geriatric Optometry, Low Vision Aids,
  Investigative Optometry, Optical Dispensing, Public Health

>> Top Colleges:
1. AIIMS Delhi (Optometry Dept)
2. LVPEI (LV Prasad Eye Institute), Hyderabad
3. NIMS, Hyderabad
4. Manipal University
5. SRM University
6. Amity University
7. Sankara Nethralaya, Chennai

>> Job Roles:
1. Clinical Optometrist (Hospital/Clinic)
2. Optical Shop Manager
3. Contact Lens Specialist
4. Vision Therapist
5. Low Vision Specialist
6. Industrial Optometrist
7. Research Optometrist
8. Own Optical Store/Clinic

>> Salary:
- Fresher: Rs 15,000 - 30,000/month
- Hospital Optometrist: Rs 25,000 - 60,000/month
- Own Optical Store: Rs 40,000 - 2,00,000/month (profit)
- Corporate Eye Care: Rs 30,000 - 70,000/month
- Abroad (USA/UK): Rs 2 - 4 Lakh/month
- Lenskart/Titan Eye type: Rs 25,000 - 50,000/month

>> Recruiters: Lenskart, Titan Eye Plus, Lawrence & Mayo,
   Eye Hospitals, GKB Opticals, LVPEI, Aravind Eye Hospital

>> Future Scope: Screen time badh rahi hai = eye problems badh rahe
   hain. Young generation mein spectacle use 60%+ ho gayi. Own
   optical store = good profitable business. Tele-optometry growing.

=====


[17. B.SC MLT - MEDICAL LAB TECHNOLOGY]

>> What is B.Sc MLT?
B.Sc MLT (Medical Laboratory Technology) mein blood tests, urine
tests, biopsy, pathological investigations, diagnostic tests
perform karna sikhaya jaata hai. Lab Technicians hospitals ke
behind-the-scenes heroes hain - bina lab reports ke doctor
treatment nahi kar sakte.

>> Duration: 3 years (B.Sc MLT) / 2 years (DMLT - Diploma)

>> Eligibility: 12th PCB, 50%+, State entrance / Direct admission

>> Fee:
- DMLT (Govt): Rs 5,000 - 30,000/year
- B.Sc MLT (Govt): Rs 10,000 - 50,000/year
- Private: Rs 30,000 - 1,50,000/year

>> Key Subjects:
  Clinical Biochemistry, Hematology, Clinical Pathology,
  Microbiology (Clinical), Histopathology, Cytology,
  Blood Banking & Immunohematology, Molecular Diagnostics,
  Clinical Immunology, Parasitology

>> Top Colleges:
1. AIIMS Delhi (MLT)
2. CMC Vellore
3. Manipal University
4. JIPMER Puducherry
5. PGIMER Chandigarh
6. SRM University
7. Amity University

>> Job Roles:
1. Medical Lab Technician/Technologist
2. Pathology Lab In-charge
3. Blood Bank Technologist
4. Microbiologist (Lab)
5. Quality Control Analyst
6. Diagnostic Center Manager
7. Research Lab Technician
8. Own Diagnostic Lab/Pathology Center

>> Salary:
- DMLT Fresher: Rs 10,000 - 20,000/month
- B.Sc MLT Fresher: Rs 15,000 - 30,000/month
- Hospital Lab (3-5 yr): Rs 25,000 - 50,000/month
- Senior Technologist: Rs 40,000 - 80,000/month
- Govt Lab (7th Pay): Rs 35,000 - 70,000/month
- Own Diagnostic Lab: Rs 50,000 - 3,00,000/month (profit)
- Abroad (Gulf/USA): Rs 1 - 3 Lakh/month

>> Recruiters: Dr. Lal PathLabs, SRL Diagnostics, Thyrocare,
   Metropolis, Apollo Diagnostics, Govt Hospitals, ICMR Labs

>> Future Scope: Diagnostic industry Rs 50,000 Crore+ in India.
   Own pathology lab = excellent business. Molecular diagnostics,
   genetic testing - new areas growing fast.

=====

[18. BOT - BACHELOR OF OCCUPATIONAL THERAPY]

>> What is BOT?
BOT (Bachelor of Occupational Therapy) mein patients ko daily life
activities (eating, dressing, bathing, working) independently
perform karne mein help karna sikhaya jaata hai. Yeh specially
disabled persons, accident victims, mentally challenged, elderly
ke liye rehabilitation provide karta hai.

>> Duration: 4.5 years (4 years + 6 months internship)

>> Eligibility: 12th PCB, 50%+, State entrance / Institute exam

>> Fee: Govt: Rs 15,000-80,000/yr | Pvt: Rs 50,000-2,50,000/yr

>> Key Subjects:
  Anatomy, Physiology, Psychology, Kinesiology, Biomechanics,
  OT in Physical Dysfunction, OT in Psychiatry,
  OT in Pediatrics, OT in Geriatrics, Ergonomics,
  Assistive Technology, Rehabilitation, Community OT

>> Top Colleges:
1. AIIMS Delhi
2. CMC Vellore
3. Manipal University
4. NIMS Hyderabad
5. KMC Mangalore
6. Seth GS Medical College, Mumbai
7. SRMC, Chennai

>> Job Roles:
1. Occupational Therapist (Hospital)
2. Pediatric OT (Special Children)
3. Psychiatric OT
4. Hand Therapist
5. Ergonomics Consultant (Corporate)
6. Rehabilitation Specialist
7. Special Educator (assist)
8. Community Rehabilitation Worker

>> Salary:
- Fresher: Rs 15,000 - 30,000/month
- Hospital OT (3-5 yr): Rs 30,000 - 60,000/month
- Govt Hospital: Rs 35,000 - 75,000/month
- Corporate Ergonomics: Rs 40,000 - 1,00,000/month
- Own Clinic: Rs 50,000 - 2,00,000/month
- Abroad (USA/UK/Aus): Rs 2 - 5 Lakh/month

>> Future Scope: Geriatric care (aging population), special needs
   children, corporate ergonomics - demand consistently growing.
   Abroad mein OTs ki bahut shortage hai - immigration easy.

=====


[19. B.SC RADIOLOGY / MEDICAL IMAGING TECHNOLOGY]

>> What is B.Sc Radiology?
B.Sc Radiology (Medical Imaging Technology) mein X-Ray, CT Scan,
MRI, Ultrasound, PET Scan jaise imaging techniques operate karna
sikhaya jaata hai. Radiographers doctors ko disease diagnose karne
mein help karte hain through medical images.

>> Duration: 3-4 years (varies by university)

>> Eligibility: 12th PCB, 50%+, University entrance exam

>> Fee: Govt: Rs 10,000-50,000/yr | Pvt: Rs 40,000-2,00,000/yr

>> Key Subjects:
  Radiographic Techniques, CT Scan Technology, MRI Technology,
  Ultrasound Technology, Nuclear Medicine, Radiation Physics,
  Radiation Safety, Anatomy (Radiological), Digital Imaging,
  Interventional Radiology Basics, Mammography

>> Top Colleges:
1. AIIMS Delhi
2. JIPMER Puducherry
3. Manipal University
4. CMC Vellore
5. PGIMER Chandigarh
6. SRM University
7. Christian Medical College, Ludhiana

>> Job Roles:
1. Radiographer/X-Ray Technologist
2. CT Scan Technologist
3. MRI Technologist
4. Ultrasound Technologist (Sonographer)
5. Nuclear Medicine Technologist
6. Cath Lab Technologist
7. Radiation Therapist (Cancer Treatment)
8. Medical Imaging Specialist

>> Salary:
- Fresher: Rs 15,000 - 30,000/month
- CT/MRI Technologist (2-3 yr): Rs 25,000 - 50,000/month
- Hospital Senior Tech: Rs 35,000 - 70,000/month
- Govt Hospital: Rs 30,000 - 65,000/month
- Diagnostic Center: Rs 25,000 - 55,000/month
- Own CT/MRI Center (investment heavy): Rs 1-5L/month profit
- Abroad (Gulf/USA): Rs 1.5 - 4 Lakh/month

>> Future Scope: Every hospital needs radiographers. AI in radiology
   growing but technologists still essential. Nuclear medicine,
   interventional radiology - advanced fields with high salary.

=====

[20. B.SC FORENSIC SCIENCE]

>> What is B.Sc Forensic Science?
Forensic Science mein crime scene investigation (CSI), evidence
collection, DNA analysis, fingerprint analysis, cyber forensics,
toxicology padhai hoti hai. Police aur courts mein scientific
evidence provide karna forensic scientists ka kaam hai. CBI,
State Police forensic labs mein jobs milti hain.

>> Duration: 3 years (B.Sc) + 2 years (M.Sc Forensic Science)

>> Eligibility: 12th PCB, 50%+, CUET / University entrance

>> Fee: Govt: Rs 10,000-50,000/yr | Pvt: Rs 40,000-2,00,000/yr

>> Key Subjects:
  Forensic Biology, Forensic Chemistry, Forensic Physics,
  Crime Scene Investigation, Fingerprint Science,
  Forensic Toxicology, DNA Profiling, Forensic Ballistics,
  Questioned Document Examination, Cyber Forensics,
  Forensic Psychology, Forensic Medicine & Pathology

>> Top Colleges:
1. LNJN National Institute of Criminology & Forensic Science, Delhi
2. Gujarat Forensic Sciences University (GFSU), Gandhinagar
3. Osmania University, Hyderabad
4. University of Madras
5. Amity University
6. Bundelkhand University
7. Dr. Harisingh Gour University, Sagar (MP)

>> Job Roles:
1. Forensic Scientist (Govt Labs - CFSL/SFSL)
2. Crime Scene Investigator
3. DNA Analyst
4. Fingerprint Expert
5. Cyber Forensic Analyst
6. Toxicologist (Poison Detection)
7. Forensic Auditor (Financial Crimes)
8. Document Examiner (Handwriting Expert)
9. Police Scientific Officer

>> Salary:
- B.Sc Fresher: Rs 12,000 - 25,000/month
- M.Sc Forensic (Govt Lab): Rs 35,000 - 80,000/month
- CFSL Scientist: Rs 50,000 - 1,20,000/month
- Cyber Forensics (Private): Rs 40,000 - 1,50,000/month
- DNA Lab (3-5 yr): Rs 35,000 - 75,000/month
- Forensic Consultant: Rs 50,000 - 2,00,000/month
- Abroad (FBI/Scotland Yard type): Rs 3 - 8 Lakh/month

>> Recruiters: CBI, State FSLs, CFSL (Delhi, Hyderabad, Chandigarh,
   Kolkata), NIA, Police Departments, Private Detective Agencies,
   Insurance Companies (Fraud Investigation)

>> Future Scope: Crime investigation modernize ho raha hai. Digital
   forensics, cyber crime investigation, DNA profiling - sab growing.
   Netflix/movies ne interest bhi badhaya hai. Govt hiring badh rahi.

=====


[21. BSMS - BACHELOR OF SIDDHA MEDICINE & SURGERY]

>> What is BSMS?
BSMS (Bachelor of Siddha Medicine and Surgery) South India ka
traditional medicine system hai. Siddha medicine Tamil Nadu mein
bahut popular hai aur government recognized hai. Minerals, metals,
herbs se medicines banti hain. "Dr." title milta hai.

>> Duration: 5.5 years (4.5 years + 1 year internship)

>> Eligibility: 12th PCB, NEET UG qualified

>> Fee: Govt: Rs 10,000-1,00,000/yr | Pvt: Rs 50,000-3,00,000/yr

>> Key Subjects: Siddha Medicine Principles (Noi Naadal, Noi Mudhal),
   Kunapadam (Pharmacology), Maruthuvam (Medicine), Varma (Vital
   Points), Sirappu Maruthuvam (Special Medicine), Anatomy, Physiology

>> Top Colleges:
1. National Institute of Siddha (NIS), Chennai
2. Govt Siddha Medical College, Palayamkottai
3. Govt Siddha Medical College, Chennai
4. Sri Sairam Siddha Medical College, Chennai

>> Job Roles & Salary:
- Siddha Doctor: Rs 20,000 - 50,000/month
- Govt AYUSH Medical Officer: Rs 45,000 - 85,000/month
- Own Clinic: Rs 50,000 - 2,00,000/month
- Siddha Pharma Company: Rs 25,000 - 60,000/month

>> Future Scope: AYUSH ministry promotion, international demand
   for traditional medicine, Siddha Varma therapy gaining popularity.

=====

[22. BASLP - BACHELOR OF AUDIOLOGY & SPEECH-LANGUAGE PATHOLOGY]

>> What is BASLP?
BASLP mein hearing disorders (deafness, tinnitus) aur speech
disorders (stammering, voice problems, aphasia, autism) ka
diagnosis aur treatment sikhaya jaata hai. Audiologists hearing
aids fit karte hain aur Speech Therapists speech correction
mein help karte hain.

>> Duration: 4 years (3.5 years + 6 months clinical internship)

>> Eligibility: 12th PCB, 50%+, Institute entrance exam

>> Fee: Govt: Rs 10,000-60,000/yr | Pvt: Rs 50,000-2,50,000/yr

>> Key Subjects:
  Acoustics, Anatomy of Ear & Speech Mechanism, Linguistics,
  Audiometry, Hearing Aid Technology, Cochlear Implants,
  Speech & Language Development, Voice Disorders,
  Fluency Disorders (Stammering), Neurogenic Communication,
  Pediatric Audiology, Swallowing Disorders (Dysphagia)

>> Top Colleges:
1. AIISH (All India Institute of Speech & Hearing), Mysore (#1!)
2. AYJNIHH (Ali Yavar Jung Institute), Mumbai
3. NIHCD, Delhi
4. Manipal University
5. SRMC, Chennai
6. CMC Vellore
7. MAHE Manipal

>> Job Roles:
1. Audiologist (Hearing Specialist)
2. Speech-Language Pathologist
3. Cochlear Implant Audiologist
4. Voice Therapist
5. Hearing Aid Consultant
6. Rehabilitation Specialist
7. School Speech Therapist
8. ENT Hospital - Speech & Hearing Dept

>> Salary:
- Fresher: Rs 18,000 - 35,000/month
- Audiologist (2-3 yr): Rs 30,000 - 60,000/month
- Speech Therapist (Private): Rs 25,000 - 70,000/month
- Hearing Aid Company: Rs 30,000 - 80,000/month
- Govt Hospital: Rs 35,000 - 75,000/month
- Own Clinic: Rs 50,000 - 2,50,000/month
- Abroad (USA/UK): Rs 3 - 6 Lakh/month

>> Recruiters: Cochlear (company), Phonak, Siemens Hearing,
   Widex, ENT Hospitals, Special Schools, Rehabilitation Centers

>> Future Scope: Hearing loss ek growing problem hai (noise pollution,
   earphone use). Autism spectrum kids ki population badh rahi -
   speech therapists ki demand bhi. Abroad mein extremely well-paid.

=====


[23. B.SC FOOD SCIENCE & NUTRITION]

>> What is B.Sc Food Science & Nutrition?
Isme food processing, food safety, nutrition science, dietetics
ki padhai hoti hai. Dietitians/Nutritionists disease management
mein diet plan banate hain. Food industry mein quality control,
product development, food safety - bahut scope hai.

>> Duration: 3 years (B.Sc) + 2 years (M.Sc Food Tech/Nutrition)

>> Eligibility: 12th PCB, 50%+, CUET / University entrance

>> Fee: Govt: Rs 5,000-30,000/yr | Pvt: Rs 30,000-1,50,000/yr

>> Key Subjects:
  Food Chemistry, Food Microbiology, Food Processing Technology,
  Nutrition & Dietetics, Clinical Nutrition, Community Nutrition,
  Food Preservation, Food Quality Control, Food Laws & Standards,
  Sports Nutrition, Therapeutic Nutrition

>> Top Colleges:
1. CFTRI (Central Food Technological Research Institute), Mysore
2. Lady Irwin College, Delhi (Delhi University)
3. SNDT Women's University, Mumbai
4. University of Mysore
5. Avinashilingam University, Coimbatore
6. Mount Carmel College, Bangalore

>> Job Roles:
1. Clinical Dietitian (Hospital)
2. Food Technologist (FMCG Companies)
3. Nutrition Consultant (Private)
4. Food Safety Officer (FSSAI)
5. Sports Nutritionist
6. Quality Control (Food Industry)
7. Product Development (R&D)
8. Online Nutrition Coach (Social Media)
9. Celebrity Nutritionist

>> Salary:
- Fresher: Rs 12,000 - 25,000/month
- Hospital Dietitian: Rs 20,000 - 50,000/month
- Food Industry QC: Rs 25,000 - 60,000/month
- FSSAI Officer: Rs 40,000 - 90,000/month
- Sports Nutritionist: Rs 40,000 - 1,50,000/month
- Celebrity Nutritionist: Rs 1 - 5 Lakh/month
- Food Tech (FMCG - Nestle/ITC): Rs 35,000 - 1,00,000/month
- Own Nutrition Clinic: Rs 30,000 - 2,00,000/month
- Online Coach (Instagram/YouTube): Rs 20,000 - 5,00,000/month

>> Recruiters: Nestle, ITC, Amul, Mother Dairy, Britannia, Haldirams,
   Parle, FSSAI (Govt), Hospitals, Wellness Centers, Sports Teams

>> Future Scope: Health consciousness badh rahi hai India mein.
   Organic food, fitness industry, social media nutrition coaching -
   bahut lucrative career. Online business model bhi work karta hai.

=====

[24. B.SC ZOOLOGY / BOTANY / BIOCHEMISTRY - PURE SCIENCES]

>> What are Pure Science Courses?
B.Sc in Zoology, Botany, Biochemistry - yeh traditional pure
science courses hain. Inme deep theoretical knowledge milti hai.
Best for those who want to go into research, teaching, or
competitive exams (UPSC, CSIR-NET, GATE Life Sciences).

>> B.Sc Zoology: Study of animals - classification, physiology,
   ecology, evolution, cell biology, genetics, wildlife
>> B.Sc Botany: Study of plants - taxonomy, plant physiology,
   ecology, plant pathology, ethnobotany, mycology
>> B.Sc Biochemistry: Study of chemical processes in living
   organisms - enzymes, metabolism, molecular biology, proteomics

>> Duration: 3 years (B.Sc) + 2 years (M.Sc) + PhD possible

>> Eligibility: 12th PCB, CUET / State University entrance

>> Fee: Govt College: Rs 3,000-20,000/yr (VERY affordable!)
   Private: Rs 20,000-1,00,000/year

>> Top Colleges:
1. St. Xavier's College, Mumbai
2. Hindu College, Delhi University
3. Loyola College, Chennai
4. Presidency College, Kolkata
5. Fergusson College, Pune
6. Christ University, Bangalore
7. St. Stephen's College, Delhi
8. Miranda House, Delhi (Women)
9. BHU (Banaras Hindu University)

>> Job Roles (after M.Sc + NET):
1. College/University Professor
2. Research Scientist (CSIR/ICMR/DBT Labs)
3. Wildlife Biologist
4. Environmental Consultant
5. Museum Curator (Zoology)
6. Botanist (Botanical Survey of India)
7. Biochemist (Pharma/Biotech)
8. UPSC (IFS - Indian Forest Service)
9. Science Communicator/Writer
10. Patent Analyst (Life Sciences)

>> Salary:
- B.Sc Fresher (Limited options): Rs 10,000 - 20,000/month
- M.Sc + CSIR-NET JRF: Rs 37,000/month (fellowship)
- Assistant Professor: Rs 57,000 - 1,50,000/month (7th Pay)
- CSIR/ICMR Scientist: Rs 60,000 - 2,00,000/month
- PhD (Post-doc abroad): Rs 2 - 5 Lakh/month
- Senior Professor: Rs 1,50,000 - 3,00,000/month

>> Important Exams after B.Sc/M.Sc:
- CSIR-NET/JRF: For research fellowship + lectureship eligibility
- GATE (Life Sciences): For M.Tech/PSU jobs
- IIT-JAM: For M.Sc in IITs
- TIFR/JEST: For research at premier institutes
- UPSC (Optional subjects): Zoology/Botany for IAS/IFS

>> Future Scope: Pure science is the BASE of all applied sciences.
   Teaching, research mein stable career. CSIR-NET clear karo to
   Rs 37,000/month fellowship milta hai PhD ke dauran. Professor
   ka 7th Pay Commission salary = Rs 1.5 Lakh+/month starting.

=====


[25. INTEGRATED BS-MS (IISER / NISER / IISc)]

>> What is Integrated BS-MS?
Yeh 5-year integrated program hai jo India ke best research
institutes offer karte hain. Yahan B.Sc + M.Sc ek saath hota hai
with heavy research exposure from Day 1. IISER, NISER graduates
world ke top universities mein PhD ke liye jaate hain.

>> Duration: 5 years (Integrated BS-MS)

>> Eligibility:
- IISER: KVPY (discontinued, now IAT - IISER Aptitude Test) /
  NEET/JEE top percentile / State Board top 1%
- NISER: NEST (National Entrance Screening Test)
- IISc: KVPY / JEE Advanced / NEET top rank

>> Fee:
- IISER/NISER: Rs 15,000-50,000/semester (Govt funded!)
  Most students get INSPIRE Scholarship: Rs 80,000/year + Rs 20,000
  research grant per year = ALMOST FREE education!
- IISc Bangalore: Nominal fees + fellowship

>> Institutes:
1. IISER Pune, IISER Mohali, IISER Kolkata, IISER Bhopal,
   IISER Thiruvananthapuram, IISER Tirupati, IISER Berhampur
2. NISER Bhubaneswar
3. IISc Bangalore (B.Sc Research - 4 years)
4. UM-DAE CBS Mumbai (5-year integrated)

>> Key Subjects (Biology Major): Cell Biology, Molecular Biology,
   Genetics, Biochemistry, Ecology, Evolution, Neuroscience,
   Biophysics, Computational Biology, Lab Rotations, Research
   Thesis (MS component in 4th-5th year)

>> What's Special:
- Research-oriented from Year 1
- World-class labs and faculty (many from MIT/Harvard/Oxford)
- Summer research internships (India & Abroad)
- Direct PhD admission in top global universities
- INSPIRE scholarship covers most expenses
- Small batch size (50-100 students) = personalized attention

>> Career After BS-MS:
1. PhD in Top Universities (MIT, Stanford, Cambridge, Max Planck)
2. Research Scientist (CSIR, TIFR, NCBS, inStem)
3. Faculty position (IITs, IISERs, Central Universities)
4. Industry R&D (Pharma, Biotech)
5. Science Policy & Communication
6. Data Science / Computational Biology
7. Entrepreneurship (Biotech startups)

>> Salary/Fellowship:
- During BS-MS: Rs 80,000/year (INSPIRE)
- PhD (India - CSIR/DBT): Rs 37,000 - 42,000/month
- PhD (USA): $30,000 - $40,000/year (Rs 25-35L/year!)
- Post-doc (Abroad): Rs 3 - 6 Lakh/month
- Faculty (India): Rs 1,00,000 - 2,50,000/month
- Industry Research: Rs 80,000 - 3,00,000/month

>> Future Scope: Yeh India ka MOST ELITE science program hai after
   IITs. Research mein career banana hai to IISER/NISER se better
   koi jagah nahi. Alumni MIT, Harvard, Stanford mein PhD kar rahe.
   Global research community mein direct entry milti hai.

=====


[SALARY COMPARISON TABLE - ALL PCB COURSES]

>> COURSE-WISE SALARY COMPARISON (Monthly - Indian Market):

  COURSE          | FRESHER        | 5 YEARS EXP    | SENIOR/OWN
  ----------------------------------------------------------------
  MBBS            | 40K-80K        | 1L-2.5L        | 3L-10L+
  MBBS+MD/MS      | 1L-2L          | 2.5L-5L        | 5L-25L+
  BDS             | 25K-50K        | 60K-1.5L       | 1.5L-5L+
  BAMS            | 20K-40K        | 50K-1L         | 1L-5L
  BHMS            | 15K-35K        | 40K-80K        | 80K-4L
  BUMS            | 20K-40K        | 40K-80K        | 60K-2L
  BNYS            | 20K-40K        | 40K-1L         | 1L-5L
  B.Pharma        | 20K-40K        | 40K-1L         | 1L-4L
  B.Sc Nursing    | 20K-45K        | 40K-80K        | 80K-1.5L
  BPT             | 15K-35K        | 40K-80K        | 80K-3L
  B.V.Sc          | 25K-50K        | 50K-1.2L       | 1L-5L
  B.Sc Agri       | 15K-35K        | 40K-80K        | 60K-5L
  B.Sc Forestry   | 15K-30K        | 40K-90K        | 80K-2.5L
  B.Sc Micro      | 12K-25K        | 35K-80K        | 80K-1.5L
  B.Sc Biotech    | 12K-25K        | 40K-1L         | 1L-4L
  B.Sc Genetics   | 12K-22K        | 35K-70K        | 70K-1.5L
  B.Optometry     | 15K-30K        | 30K-70K        | 70K-2L
  B.Sc MLT        | 15K-30K        | 30K-60K        | 60K-3L
  BOT             | 15K-30K        | 35K-70K        | 70K-2L
  B.Sc Radio      | 15K-30K        | 35K-70K        | 60K-1.5L
  B.Sc Forensic   | 12K-25K        | 40K-80K        | 80K-2L
  BSMS            | 20K-40K        | 40K-80K        | 60K-2L
  BASLP           | 18K-35K        | 35K-70K        | 70K-2.5L
  B.Sc Food/Nutr  | 12K-25K        | 30K-70K        | 50K-5L
  B.Sc Zoo/Bot    | 10K-20K        | 40K-80K(NET)   | 1L-3L(Prof)
  BS-MS IISER     | 37K(PhD fell)  | 1L-2L(faculty) | 2L-4L

  Note: K = Thousand, L = Lakh per month
  "Own" means own practice/clinic/business
  Abroad salary 3-10x of Indian salary in most fields

=====

[AFTER MBBS - ALL PG SPECIALIZATIONS DETAILED]

>> MD (Doctor of Medicine) - NON-SURGICAL Branches:
  1. MD General Medicine - Most common, OPD + IPD practice
  2. MD Pediatrics - Children specialist (0-18 years)
  3. MD Dermatology (Skin, VD) - HIGHEST demand, cosmetic procedures
  4. MD Radiology - CT/MRI reporting, interventional radiology
  5. MD Anaesthesia - OT mein anaesthesia, ICU, Pain Management
  6. MD Psychiatry - Mental health, de-addiction
  7. MD Respiratory Medicine (Pulmonology) - Lungs specialist
  8. MD Obstetrics & Gynaecology - Women health, pregnancy, delivery
  9. MD Ophthalmology - Eye specialist + surgeries (LASIK etc)
  10. MD Pathology - Lab diagnosis, histopathology
  11. MD Microbiology - Infections, lab testing
  12. MD Pharmacology - Drug research, clinical trials
  13. MD Biochemistry - Chemical pathology, research
  14. MD Community Medicine (PSM) - Public health, epidemiology
  15. MD Forensic Medicine - Medico-legal cases, postmortem
  16. MD Physical Medicine & Rehabilitation (PMR)
  17. MD Nuclear Medicine - PET scan, radiopharmaceuticals
  18. MD Emergency Medicine - Trauma, emergency care
  19. MD Geriatrics - Elderly care
  20. MD Palliative Medicine - End-of-life care

>> MS (Master of Surgery) - SURGICAL Branches:
  1. MS General Surgery - All types of surgery
  2. MS Orthopaedics - Bones, joints, fractures, replacement
  3. MS Ophthalmology - Eye surgery
  4. MS ENT (Otorhinolaryngology) - Ear, Nose, Throat surgery
  5. MS Obstetrics & Gynaecology - C-section, hysterectomy
  6. MS Anatomy - Teaching + research

>> DNB (Diplomate of National Board):
  - DNB is equivalent to MD/MS
  - Conducted by NBE (National Board of Examinations)
  - Available in corporate hospitals (Apollo, Fortis, Max etc.)
  - DNB in all MD/MS equivalent branches + extra branches

>> EARNING POTENTIAL BY SPECIALIZATION (Monthly):
  MD Dermatology: Rs 3L-15L (cosmetic procedures = gold mine)
  MD Radiology: Rs 2L-8L (teleradiology booming)
  MS Orthopaedics: Rs 3L-12L (joint replacements)
  MD Cardiology (DM): Rs 5L-25L (interventional procedures)
  MCh Neurosurgery: Rs 5L-30L (brain/spine surgery)
  MCh Plastic Surgery: Rs 4L-20L (cosmetic surgery)
  MD Anaesthesia: Rs 2L-6L (freelance OT work)
  MS Ophthalmology: Rs 2L-8L (LASIK/cataract)
  MD Pediatrics: Rs 1.5L-5L
  MS General Surgery: Rs 2L-8L

=====


[GOVERNMENT JOBS FOR PCB STUDENTS]

>> PCB students ke liye Government Jobs (Stable + Pension + Perks):

>> 1. UPSC Civil Services (IAS/IPS with Medical Science optional)
  - Medical Science as optional subject in UPSC CSE
  - MBBS graduates IAS/IPS ban sakte hain
  - Salary: Rs 56,100 - 2,50,000/month (7th Pay)

>> 2. UPSC CMS (Combined Medical Services)
  - For MBBS graduates only
  - Posts: Medical Officer in Railways, ESI, CHS, NDMC
  - Salary: Rs 56,100 - 1,77,500/month (Level 10-13)
  - Age: 32 years (relaxation for reserved)
  - Very good work-life balance

>> 3. State PSC Medical Officer
  - Every state has Medical Officer recruitment
  - Through State PSC exam (UP, MP, Rajasthan, Bihar etc.)
  - Salary: Rs 50,000 - 1,50,000/month (state dependent)
  - Rural posting initially, then transfer to city

>> 4. Railway Medical Officer (RRB)
  - Indian Railways hospitals & health units
  - Salary: Rs 56,100/month + allowances
  - Through UPSC CMS or direct Railway recruitment

>> 5. ESI (Employees State Insurance) Doctor
  - ESI hospitals across India
  - Through UPSC CMS
  - Salary: Rs 60,000 - 1,50,000/month
  - Good work-life balance, no night duties usually

>> 6. Army Medical Corps (AMC) - Indian Army
  - Short Service Commission (SSC) / Permanent Commission
  - AFMS (Armed Forces Medical Services)
  - Salary: Rs 70,000 - 2,50,000/month + accommodation + perks
  - Respect + adventure + travel + job security
  - Entry: Through SSB interview after MBBS

>> 7. Indian Navy / Air Force Medical Branch
  - Similar to AMC but for Navy/Air Force
  - Salary equivalent to Army + additional allowances
  - Flying allowance for Air Force doctors

>> 8. DRDO (Defence Research) - Scientist B
  - For M.Sc/PhD in Life Sciences, Biotech, Micro
  - DRDO RAC recruitment
  - Salary: Rs 56,100/month (Level 10) starting
  - Research + security clearance

>> 9. ICMR (Indian Council of Medical Research)
  - For MBBS/M.Sc/PhD in Medical/Life Sciences
  - ICMR JRF/SRF: Rs 37,000 - 42,000/month (fellowship)
  - Scientist posts: Rs 67,700+/month
  - Pure medical research

>> 10. CSIR Laboratories - Scientist
  - For M.Sc/PhD with CSIR-NET
  - CSIR-NET JRF: Rs 37,000/month during PhD
  - Scientist post: Rs 67,700/month+
  - Labs: CDRI, CCMB, IICB, NII etc.

>> 11. Drug Inspector (State/Central)
  - For B.Pharma/M.Pharma graduates
  - State PSC / UPSC recruitment
  - Salary: Rs 40,000 - 1,00,000/month
  - Regulatory work - very powerful position

>> 12. Food Safety Officer (FSSAI)
  - For B.Sc Food Science/M.Sc graduates
  - State level recruitment
  - Salary: Rs 35,000 - 80,000/month

>> 13. ICAR (Indian Council of Agricultural Research)
  - For B.Sc/M.Sc Agriculture, Veterinary
  - ARS (Agricultural Research Service) exam
  - Scientist: Rs 67,700/month+
  - 100+ research institutes across India

>> 14. Forest Service (IFS - Indian Forest Service)
  - Through UPSC with Botany/Zoology optional
  - DFO rank posting - manage forests & wildlife
  - Salary: Rs 56,100 - 2,50,000/month
  - Accommodation + vehicle + forest bungalow

>> 15. Staff Nurse / Nursing Officer (Govt)
  - AIIMS, Railway, ESI, Army Nursing Service
  - Salary: Rs 35,000 - 80,000/month (7th Pay)
  - Pension + security + promotion

>> 16. Physiotherapist / OT (Government)
  - Central/State Govt hospitals
  - Salary: Rs 35,000 - 75,000/month

>> 17. UPSC (AYUSH Medical Officer)
  - For BAMS/BHMS/BUMS graduates
  - State PSC recruitment mainly
  - Salary: Rs 45,000 - 90,000/month

=====


[RESEARCH CAREER PATH - PHD, POST-DOC, SCIENTIST]

>> Research Career Roadmap:
  12th PCB -> B.Sc/MBBS -> M.Sc/MD -> PhD -> Post-Doc -> Faculty

>> PhD Options after M.Sc:
- CSIR-NET JRF: Clear this exam -> PhD in any Indian university/lab
  Fellowship: Rs 37,000/month (JRF) -> Rs 42,000/month (SRF)
- DBT-JRF: Department of Biotechnology fellowship
  Rs 37,000/month for Biotech/Life Science PhD
- ICMR-JRF: Medical research PhD
  Rs 37,000/month
- UGC-NET JRF: For Humanities + some Science subjects
- DST-INSPIRE Fellowship: Rs 37,000/month for PhD
  Direct for IISER/IISc/IIT graduates
- GATE: Some IITs offer PhD through GATE score
  Fellowship: Rs 37,000/month

>> Where to do PhD in India:
- IISc Bangalore (India's #1 research institute)
- TIFR Mumbai (Tata Institute of Fundamental Research)
- NCBS Bangalore (National Centre for Biological Sciences)
- CCMB Hyderabad (Centre for Cellular & Molecular Biology)
- IITs (Biotech/Chemistry/Biology departments)
- IISER (all 7 institutes)
- CDRI Lucknow (Drug Research)
- NII Delhi (National Institute of Immunology)
- JNCASR Bangalore (Jawaharlal Nehru Centre)
- InStem Bangalore (Institute for Stem Cell Science)

>> PhD Abroad (Fully Funded!):
- USA: 5-6 years, $28,000-$40,000/year stipend
  Top: MIT, Harvard, Stanford, Johns Hopkins, UCSF, NIH
- UK: 3-4 years, 15,000-20,000 GBP/year stipend
  Top: Cambridge, Oxford, Imperial, UCL
- Germany: 3-4 years, 1,800-2,200 EUR/month (Max Planck)
- Singapore: 4 years, $3,000-4,000 SGD/month
- Australia: 3-4 years, AUD 28,000-35,000/year

>> Post-Doctoral Research:
- After PhD, 2-5 years post-doc for faculty position
- Salary: Rs 50,000-80,000/month (India)
- Abroad: $50,000-70,000/year (USA), 35,000-50,000 EUR (Europe)
- DST-INSPIRE Faculty Award: Rs 1,25,000/month + Rs 35 Lakh grant
- Ramalingaswami Fellowship (DBT): Rs 1,10,000/month + Rs 50 Lakh
- Ramanujan Fellowship (DST): Rs 1,10,000/month + Rs 70 Lakh

>> Faculty Career (After PhD + Post-Doc):
- Assistant Professor: Rs 57,700/month + AG + allowances
  (Total: Rs 1,00,000-1,50,000/month in IIT/IISER/Central Univ)
- Associate Professor: Rs 1,31,400/month+
- Professor: Rs 1,44,200 - 2,18,200/month
- Director/VC: Rs 2,00,000 - 2,50,000/month

>> Key Research Funding Agencies:
- DST (Department of Science & Technology)
- DBT (Department of Biotechnology)
- CSIR (Council of Scientific & Industrial Research)
- ICMR (Indian Council of Medical Research)
- SERB (Science & Engineering Research Board)
- ICAR (Indian Council of Agricultural Research)
- DAE (Department of Atomic Energy)

=====

[ABROAD OPTIONS FOR PCB GRADUATES]

>> 1. USA - USMLE (United States Medical Licensing Exam):
  - For MBBS graduates who want to practice in USA
  - Steps: USMLE Step 1 -> Step 2 CK -> Step 2 CS -> Step 3
  - Step 1: Basic Sciences (most important, 3-digit score)
  - Step 2 CK: Clinical Knowledge
  - After Steps: Apply for Residency (Match Day process)
  - Residency: 3-7 years depending on specialty
  - Salary during Residency: $55,000-$70,000/year
  - After Residency (Attending): $2,50,000-$5,00,000/year
  - Timeline: 3-5 years from MBBS completion to USA practice
  - Total Cost: Rs 20-40 Lakh (coaching + exams + applications)
  - Success Rate: Variable, depends on Step scores + research

>> 2. UK - PLAB (Professional & Linguistic Assessment Board):
  - For MBBS graduates wanting to work in UK (NHS)
  - Steps: PLAB 1 (MCQ) -> PLAB 2 (OSCE) -> GMC Registration
  - After registration: Foundation Year / Direct Specialty Training
  - Salary: 29,000 - 1,00,000 GBP/year (depending on grade)
  - NHS benefits: Pension, housing, NHS healthcare
  - Timeline: 6 months - 1 year to start working
  - Cost: Rs 5-10 Lakh total
  - Easier than USMLE, shorter timeline

>> 3. Australia - AMC (Australian Medical Council):
  - AMC MCQ Exam -> AMC Clinical Exam -> Internship
  - Salary: AUD 80,000-3,00,000/year
  - Work-life balance best among all countries
  - PR (Permanent Residency) possible through medical work

>> 4. Canada - MCC Exam:
  - MCCEE -> MCCQE Part 1 -> NAC OSCE -> MCCQE Part 2
  - Residency in Canada (CaRMS matching)
  - Salary: CAD 1,50,000-4,00,000/year
  - PR pathway available

>> 5. Gulf Countries (Saudi/UAE/Qatar):
  - Direct recruitment for MBBS/BDS/Nursing
  - Prometric/HAAD/DHA/MOH exam required
  - Salary: Tax-free Rs 1-4 Lakh/month
  - No exam for nursing - direct recruitment
  - Good savings potential

>> 6. Germany (for Doctors):
  - German Language B2 required + Approbation
  - Salary: EUR 50,000-1,50,000/year
  - Free healthcare, social security
  - No tuition fee for MD equivalent courses

>> For Non-MBBS PCB Graduates (Abroad Options):
- Nursing (UK/USA/Canada/Aus): NCLEX-RN, NMC-CBT, AHPRA
- Pharmacy (USA): FPGEC certification -> Pharmacist license
- Physiotherapy: Registration in respective country
- Lab Technology: Direct jobs available
- PhD: Fully funded in most countries (apply direct!)
- M.Sc: Many scholarships available (Erasmus, DAAD, Chevening)

=====


[TIPS FOR PCB STUDENTS - IMPORTANT ADVICE]

>> Tip 1: NEET is NOT Everything
  NEET nahi clear hua to life khatam nahi hoti! B.Pharma, B.Sc
  Nursing, BPT, B.Sc Biotech, Agriculture - bahut options hain
  jo bina NEET ke ya kam score pe bhi mil jaate hain.

>> Tip 2: Don't Waste Drop Years Blindly
  Maximum 2 drop years lena reasonable hai NEET ke liye. Agar 2
  attempts mein nahi hua to parallel B.Sc/B.Pharma join karo aur
  saath mein NEET prepare karo (allowed hai).

>> Tip 3: Government College > Private College
  Agar 1 Crore loan leke private MBBS karte ho to repay karne mein
  10-15 saal lag sakte hain. Government college ki fees 1-25 Lakh
  total hai - ROI (Return on Investment) bahut better hai.

>> Tip 4: Explore Paramedical Courses
  B.Sc Nursing, BPT, BOT, B.Optometry, BASLP, B.Sc MLT - yeh sab
  underrated courses hain with excellent placement records. Especially
  abroad jaane ke liye nursing sabse easy path hai.

>> Tip 5: Research is a REAL Career
  India mein PhD karne pe Rs 37,000/month milta hai (JRF fellowship).
  Post-doc ke baad faculty position = Rs 1-2 Lakh/month.
  Abroad PhD = fully funded + excellent stipend.

>> Tip 6: Skill Development is KEY
  Sirf degree se kaam nahi chalega. Additional skills seekho:
  - Clinical Research certification (for pharma jobs)
  - Good Communication (for patient handling)
  - Digital Marketing (for own clinic promotion)
  - Basic Data Analysis (for research)
  - Foreign Language (for abroad opportunities)

>> Tip 7: Financial Planning
  Education loan lena ho to SBI/Bank of Baroda/PNB se lo - interest
  rate 7-9% hota hai. Scholarship options explore karo:
  - Central Sector Scholarship (MHRD)
  - State Government Scholarships
  - Institute-specific Merit Scholarships
  - Private Scholarships (Tata Trust, Reliance Foundation etc.)
  - Education Loan + Interest Subsidy for EWS

>> Tip 8: Entrepreneurship in Healthcare
  Doctor banne ke baad sirf job hi nahi - business bhi ban sakta hai:
  - Own Clinic/Hospital
  - Diagnostic Lab Chain
  - Pharma Company
  - HealthTech Startup
  - Online Consultation Platform
  - Healthcare Content Creator (YouTube/Instagram)
  - Medical Coaching Institute

>> Tip 9: Stay Updated
  Medical field mein continuous learning zaroori hai:
  - CME (Continuing Medical Education) credits
  - Research papers padhte raho
  - Conferences attend karo
  - Professional networks banao (LinkedIn, ResearchGate)
  - Specialization ke journals subscribe karo

>> Tip 10: Mental Health Matters
  Medical students mein burnout bahut common hai. Apna dhyan rakhna:
  - Study-life balance maintain karo
  - Exercise regularly
  - Peer support groups join karo
  - Professional help lene mein sharm nahi
  - Long game hai - patience rakhni padegi

=====

DISCLAIMER: Yeh guide informational purposes ke liye hai. Fees,
eligibility criteria, aur entrance exam patterns change hote rehte
hain. Latest information ke liye always official websites check karo.
All salary figures are approximate and may vary based on location,
institution, experience, and individual performance.

Sources: NMC, NTA, UGC, AICTE, ICAR, official university websites.
Guide prepared for educational guidance purposes only.
Last Reference Year: 2024-25 Academic Session.

=====================================================================
     ALL THE BEST FOR YOUR CAREER! - MEHNAT KARO, SAFALTA MILEGI!
=====================================================================
"""


def escape_pdf(s):
    s = s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    return re.sub(r"[^\x20-\x7E]", "", s)

def wrap(line, mx=100):
    if len(line) <= mx:
        return [line]
    ind = re.match(r"^(\s*)", line).group(1)
    words, out, cur = line.split(" "), [], ind
    for w in words:
        if len(cur) + len(w) + 1 > mx:
            out.append(cur.rstrip())
            cur = ind + w
        else:
            cur = (cur + " " + w) if cur.strip() else (ind + w)
    if cur.strip():
        out.append(cur.rstrip())
    return out

PAGE_W, PAGE_H = 595, 842
ML, MR, MT, MB = 45, 45, 55, 50
BODY_SIZE = 9.5
HEAD_SIZE = 13
SUB_SIZE = 11
LINE_H = 12.5
HEAD_LINE_H = 17
SUB_LINE_H = 14


def paginate(content):
    raw = content.splitlines()
    lines = []
    for ln in raw:
        s = ln.strip()
        if s.startswith("====="):
            lines.append(("rule", ""))
        elif s.startswith("[") and s.endswith("]") and len(s) < 80:
            lines.append(("head", s))
        elif s and s == s.upper() and len(s) > 5 and not s.startswith("-") \
                and not s.startswith("*") and re.match(r"^[A-Z0-9 &/().,\'\-\[\]|:=+!?]+$", s):
            lines.append(("head", s))
        elif s.startswith(">>"):
            lines.append(("sub", s))
        else:
            for w in wrap(ln):
                lines.append(("body", w))
    pages, cur, y = [], [], PAGE_H - MT
    for kind, text in lines:
        lh = HEAD_LINE_H if kind == "head" else (SUB_LINE_H if kind == "sub" else LINE_H)
        if y - lh < MB:
            pages.append(cur)
            cur, y = [], PAGE_H - MT
        cur.append((kind, text, y))
        y -= lh
    if cur:
        pages.append(cur)
    return pages

def stream(page_lines):
    parts = []
    for kind, text, y in page_lines:
        if kind == "rule":
            parts.append(f"0.3 0.3 0.7 RG {ML} {y+4} m {PAGE_W-MR} {y+4} l S 0 0 0 RG")
            continue
        if not text.strip():
            continue
        if kind == "head":
            font, size = "/F2", HEAD_SIZE
            parts.append(f"0.1 0.1 0.5 rg")
        elif kind == "sub":
            font, size = "/F2", SUB_SIZE
            parts.append(f"0.0 0.3 0.0 rg")
        else:
            font, size = "/F1", BODY_SIZE
            parts.append(f"0 0 0 rg")
        parts.append(f"BT {font} {size} Tf {ML} {y} Td ({escape_pdf(text)}) Tj ET")
    parts.append(f"BT /F1 8 Tf {PAGE_W-MR-30} {MB-20} Td (Page) Tj ET")
    return "\n".join(parts).encode("latin-1")


def make_pdf(out_path):
    pages = paginate(CONTENT)
    objs = []
    cat_n, pages_n, f1_n, f2_n = 1, 2, 3, 4
    pg_nums, ct_nums = [], []
    n = 5
    for _ in pages:
        pg_nums.append(n); n += 1
        ct_nums.append(n); n += 1
    objs = [None] * (n - 1)
    objs[0] = f"<< /Type /Catalog /Pages {pages_n} 0 R >>".encode()
    kids = " ".join(f"{x} 0 R" for x in pg_nums)
    objs[1] = f"<< /Type /Pages /Count {len(pages)} /Kids [ {kids} ] >>".encode()
    objs[2] = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>"
    objs[3] = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>"
    for i, pl in enumerate(pages):
        s = stream(pl)
        c = zlib.compress(s)
        objs[ct_nums[i]-1] = (f"<< /Length {len(c)} /Filter /FlateDecode >>\nstream\n").encode() + c + b"\nendstream"
        objs[pg_nums[i]-1] = (f"<< /Type /Page /Parent {pages_n} 0 R /MediaBox [0 0 {PAGE_W} {PAGE_H}] /Resources << /Font << /F1 {f1_n} 0 R /F2 {f2_n} 0 R >> >> /Contents {ct_nums[i]} 0 R >>").encode()
    buf = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offs = [0]
    for i, body in enumerate(objs, 1):
        offs.append(len(buf))
        buf += f"{i} 0 obj\n".encode() + body + b"\nendobj\n"
    xref = len(buf)
    buf += f"xref\n0 {len(objs)+1}\n".encode()
    buf += b"0000000000 65535 f \n"
    for o in offs[1:]:
        buf += f"{o:010d} 00000 n \n".encode()
    buf += f"trailer\n<< /Size {len(objs)+1} /Root {cat_n} 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
    out_path.write_bytes(buf)
    print(f"PDF Generated: {out_path.name}")
    print(f"  Size: {len(buf):,} bytes")
    print(f"  Pages: {len(pages)}")

if __name__ == "__main__":
    out = Path(__file__).parent / "PCB_Medical_Science_Complete_Guide.pdf"
    make_pdf(out)
    print("Done!")
