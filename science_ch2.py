"""
science_ch2.py
--------------
Generates a detailed, simplified Hinglish study guide for
NCERT Class 10 Science, Chapter 2: "Acids, Bases and Salts".

Outputs:
  - Science_Class10_Ch2_Acids_Bases_Salts.pdf  (colour PDF)
  - Science_Class10_Ch2_Acids_Bases_Salts.md   (markdown, red=red green=green)

Markup conventions inside CONTENT (handled by pdf_utils):
  @@  -> RED   line  (CORE BASICS / extra ke liye)
  $$  -> GREEN line  (exam me baar-baar aane wale topics)
  <<<PAGEBREAK>>>     -> nayi page
"""

import re
from pathlib import Path

import pdf_utils


CONTENT = r"""ACIDS, BASES AND SALTS
NCERT Class 10 Science - Chapter 2 (Hinglish Detailed Notes)
=========================================================

@@ COLOUR CODE: RED = Core Basics / extra help (Class 7-8-9 wali cheezein jo yaad honi chahiye).
$$ COLOUR CODE: GREEN = Board exam me ye topics BAAR-BAAR aate hain - pakka yaad karo.
   Baaki normal black text = main chapter content (detail me, simple bhasha me).

<<<PAGEBREAK>>>

CORE BASICS - PEHLE YE PADHO (CLASS 7-8-9 KA FOUNDATION)
=========================================================
@@ Tune 7-8-9 nahi padhi - tension mat le. Ye page is chapter ki base hai.
@@ Ek baar achhe se padh le, fir chapter aasaani se samajh aayega.

@@ 1) ACID, BASE, SALT (Class 7 ka idea):
@@    - Acid = swaad me KHATTA (nimbu, sirka, imli). Litmus ko NEELA->LAAL karta.
@@    - Base/Alkali = swaad me KADWA, chhune me saboon jaisa (NaOH, chuna).
@@      Litmus ko LAAL->NEELA karta.
@@    - Salt = acid + base ki reaction se banta padaarth (jaise NaCl - namak).

@@ 2) LITMUS (natural indicator - Class 7):
@@    - Lichen (ek plant) se banta. Blue litmus + acid = laal. Red litmus + base = neela.
@@    - "Indicator" = jo rang badal ke acid/base ka pata de.

@@ 3) ION, H+ aur OH- (Class 8-9):
@@    - Ion = charge wala atom/group. Cation = +ve, Anion = -ve.
@@    - Acid paani me H+ (hydrogen ion) deta hai.
@@    - Base paani me OH- (hydroxide ion) deta hai. YAHI poora chapter ka core hai.

@@ 4) AQUEOUS, SOLUBLE, DISSOCIATION:
@@    - Aqueous (aq) = paani me ghula hua.
@@    - Soluble = ghul jaata; Insoluble = nahi ghulta (precipitate).
@@    - Dissociation/Ionisation = paani me compound ka ion me tut-na (HCl -> H+ + Cl-).

@@ 5) DILUTE vs CONCENTRATED:
@@    - Dilute = paani zyada, acid/base kam. Concentrated = acid/base zyada.
@@    - Dilution = paani milana (concentration kam karna).

@@ 6) METAL vs NON-METAL (Class 8):
@@    - Metal = Na, K, Zn, Fe, Cu, Ca (chamakdaar, electricity conduct).
@@    - Non-metal = C, S, O, Cl (mostly dull). Metal oxide = basic,
@@      Non-metal oxide = acidic (ye baat aage kaam aayegi).

@@ 7) IMPORTANT FORMULAE (rat lo - baar baar aayenge):
@@    - Acids: HCl, H2SO4 (sulphuric), HNO3 (nitric), H2CO3, CH3COOH (acetic/vinegar).
@@    - Bases: NaOH (caustic soda), KOH, Ca(OH)2 (slaked lime), NH4OH.
@@    - Salts: NaCl, Na2CO3 (washing soda), NaHCO3 (baking soda), CaCO3.

@@ 8) NEUTRALISATION (Class 7):
@@    Acid + Base -> Salt + Water. (Dono ek dusre ka asar khatam karte hain.)

@@ 9) VALENCY / FORMULA (Ch-1 wala):
@@    Criss-cross se formula: Na(1)+SO4(2) => Na2SO4. Subscript mat badlo balancing me.

<<<PAGEBREAK>>>

1. ACIDS aur BASES KE CHEMICAL PROPERTIES
=========================================================

1.1 INDICATORS (rang badal ke pehchaan kराते hain)
---------------------------------------------------------
$$ Indicators table (exam me 100% kaam ka):
$$   - Litmus:        acid me LAAL,  base me NEELA
$$   - Methyl orange: acid me LAAL,  base me PEELA (yellow)
$$   - Phenolphthalein: acid me COLOURLESS, base me PINK (gulabi)

   @@ OLFACTORY INDICATORS = smell (gandh) se pata chale: pyaaz (onion),
   @@ vanilla, laung (clove). Base in ki smell khatam kar deta, acid nahi.

1.2 ACID/BASE ka METAL ke saath REACTION
---------------------------------------------------------
$$ ACID + METAL -> SALT + HYDROGEN gas (H2)
$$    Zn + H2SO4 -> ZnSO4 + H2
$$    2Na + 2HCl -> 2NaCl + H2
   Gas test: jalti hui tili paas le jao -> "POP" (pop) awaaz = Hydrogen gas.

$$ BASE + METAL -> SALT + HYDROGEN (sirf kuch reactive metal jaise Zn/Al ke saath)
$$    2NaOH + Zn -> Na2ZnO2 (sodium zincate) + H2

1.3 METAL CARBONATE / HYDROGENCARBONATE + ACID
---------------------------------------------------------
$$ Metal carbonate/bicarbonate + Acid -> Salt + CO2 + Water  (3 cheez banti)
$$    Na2CO3 + 2HCl -> 2NaCl + H2O + CO2
$$    NaHCO3 + HCl -> NaCl + H2O + CO2

$$ LIME WATER TEST (CO2 gas pehchaan-ne ka famous test):
$$    CO2 + Ca(OH)2 -> CaCO3 + H2O   (lime water DOODHIYA/milky ho jaata)
   @@ Zyada CO2 daalo to milkiness gayab (CaCO3 + CO2 + H2O -> Ca(HCO3)2 soluble).

1.4 NEUTRALISATION (Acid + Base aapas me)
---------------------------------------------------------
$$ ACID + BASE -> SALT + WATER
$$    NaOH + HCl -> NaCl + H2O
$$    Ca(OH)2 + 2HCl -> CaCl2 + 2H2O
   H+ (acid se) + OH- (base se) -> H2O. Isi wajah se dono ka asar khatam.

1.5 METAL OXIDE (basic) + ACID ;  NON-METAL OXIDE (acidic) + BASE
---------------------------------------------------------
$$ METAL OXIDE = BASIC. Acid ke saath salt + water deta (neutralisation jaisa):
$$    CuO + 2HCl -> CuCl2 + H2O   (black CuO ghul ke neela-hara CuCl2)
$$ NON-METAL OXIDE = ACIDIC. Base ke saath salt + water:
$$    CO2 + Ca(OH)2 -> CaCO3 + H2O

<<<PAGEBREAK>>>

2. SAARE ACID/BASE ME COMMON KYA HAI?
=========================================================
$$ Saare ACID paani me H+ ion (asal me H3O+, hydronium) dete hain - isiliye
$$ unke properties same (khatta, litmus laal, etc.).
$$ Saare BASE paani me OH- ion dete hain.

   Reaction: HCl + H2O -> H3O+ + Cl-     (acid ne H+ diya)
             NaOH --(water)--> Na+ + OH-  (base ne OH- diya)

$$ IMPORTANT: Acid apna acidic behaviour SIRF PAANI ME dikhata hai. Bina paani
$$ ke H+ ion nahi bante (jaise sukha HCl gas litmus nahi badalta). Isiliye paani
$$ zaroori hai ionisation ke liye.

   STRONG vs WEAK:
   $$ - Strong acid/base = paani me POORI tarah ionise (HCl, H2SO4, HNO3, NaOH, KOH).
   $$ - Weak acid/base = THODA sa ionise (CH3COOH/acetic, H2CO3, NH4OH).

@@ DILUTION (acid/base ko paani me ghol-na) - SAFETY RULE:
@@ HAMESHA acid ko PAANI me daalo (dheere-dheere, hilate hue), paani ko acid me NAHI.
@@ Kyunki dilution EXOTHERMIC hai (bahut garmi + chheente nikalte) - ulta karne par
@@ acid uchhal ke jal sakta hai. Dilution se ion ki concentration ghat-ti hai.

3. SOLUTION KITNA STRONG HAI? - pH SCALE
=========================================================
$$ pH scale = 0 se 14 tak. H+ ion ki concentration batata hai ("p" = potenz/power of H).
$$    - pH = 7  -> NEUTRAL (jaise shudh paani)
$$    - pH < 7  -> ACIDIC (jitna kam, utna strong acid; pH 0 = sabse strong acid)
$$    - pH > 7  -> BASIC/ALKALINE (jitna zyada, utna strong base; pH 14 = strongest)

$$ Zyada H+ => kam pH => zyada acidic. Universal indicator alag-alag pH par
$$ alag rang deta (laal=strong acid ... green=neutral ... blue/violet=strong base).

3.1 pH KA ROZMARRA ME MAHATVA (IMPORTANCE OF pH)
---------------------------------------------------------
$$ (a) Sharir/Digestion: pet me HCl khaana pachata. Acidity (zyada acid) hone par
$$     ANTACID (milk of magnesia = Mg(OH)2, ya baking soda) lete hain - base acid
$$     ko neutralise karta.
$$ (b) Daant ke cavity/decay: muh ka pH 5.5 se NEECHE jaaye to enamel ghisne lagta.
$$     Bacteria sugar se acid banate. Basic toothpaste se neutralise karte hain.
$$ (c) Mitti (soil) ka pH: paudho ko sahi pH chahiye - zyada acidic mitti me chuna
$$     (base), zyada basic me organic khaad daalte hain.
$$ (d) Self-defence: Madhumakkhi (bee) ka dank ACIDIC (methanoic acid) - baking soda
$$     (base) lagao. Bichhu booti (nettle) me methanoic acid - dock plant ragadte.
$$ (e) Acid rain: barish ka pH 5.6 se kam ho to "acid rain" - nadi/building nuksaan.

<<<PAGEBREAK>>>

4. SALTS KE BAARE ME AUR (MORE ABOUT SALTS)
=========================================================

4.1 SALT KA pH (kis acid + kis base se bana)
---------------------------------------------------------
$$    - Strong acid + Strong base  -> NEUTRAL salt (pH 7).  e.g. NaCl
$$    - Strong acid + Weak base    -> ACIDIC salt (pH < 7). e.g. NH4Cl
$$    - Weak acid + Strong base    -> BASIC salt (pH > 7).  e.g. Na2CO3, CH3COONa

4.2 COMMON SALT (NaCl) SE BANNE WALE CHEMICALS
---------------------------------------------------------
$$ (A) SODIUM HYDROXIDE - CHLOR-ALKALI PROCESS (bahut important):
$$     Namak ke paani (brine) me electricity guzaarne par:
$$     2NaCl + 2H2O --(electricity)--> 2NaOH + Cl2 + H2
$$     - Cathode par: HYDROGEN gas (H2)
$$     - Anode par:   CHLORINE gas (Cl2)
$$     - Solution me: SODIUM HYDROXIDE (NaOH)
   @@ "Chlor-alkali" naam: chlor = chlorine, alkali = NaOH. Saare products useful:
   @@ Cl2 -> bleach/PVC, H2 -> fuel, NaOH -> soap, HCl -> Cl2 se.

$$ (B) BLEACHING POWDER (Calcium oxychloride, CaOCl2):
$$     Ca(OH)2 + Cl2 -> CaOCl2 + H2O
$$     Uses: kapda/kaagaz factory me bleaching, paani ko disinfect (germ-free)
$$     karna, oxidising agent.

$$ (C) BAKING SODA (Sodium hydrogencarbonate, NaHCO3):
$$     NaCl + H2O + CO2 + NH3 -> NH4Cl + NaHCO3
$$     - Garam karne par: 2NaHCO3 --(heat)--> Na2CO3 + H2O + CO2
$$     - Uses: baking (baking powder = baking soda + tartaric acid; CO2 se cake
$$       phoolta, tartaric acid se kadwa swaad nahi aata), antacid (acidity me),
$$       soda-acid fire extinguisher.

$$ (D) WASHING SODA (Sodium carbonate, Na2CO3.10H2O):
$$     Na2CO3 + 10H2O -> Na2CO3.10H2O   (recrystallisation se)
$$     - Uses: glass/soap/paper industry, paani ki HARDNESS hatana, ghar safai.

4.3 WATER OF CRYSTALLISATION  +  PLASTER OF PARIS
---------------------------------------------------------
$$ WATER OF CRYSTALLISATION = kisi salt ke ek formula unit me fixed number of
$$ paani ke molecule. e.g. CuSO4.5H2O (neela thotha - 5 paani; garam karo to
$$ paani udta aur safed ho jaata), Na2CO3.10H2O.

$$ PLASTER OF PARIS (POP) = CaSO4.(1/2)H2O  [calcium sulphate hemihydrate]:
$$    Gypsum (CaSO4.2H2O) ko 373 K (100 C) par garam karke banta:
$$    CaSO4.2H2O --(373K heat)--> CaSO4.(1/2)H2O + (3/2)H2O
$$    - Paani milao to wapas gypsum ban ke SAKHT (set) ho jaata:
$$    CaSO4.(1/2)H2O + (3/2)H2O -> CaSO4.2H2O
$$    - Uses: tooti haddi ka plaster, khilone/murti, decoration, deewar smooth.
   @@ POP ko AIRTIGHT rakhte hain - nami se pehle hi set ho jaata to bekaar.

<<<PAGEBREAK>>>

5. SOLVED EXAMPLES (HARDEST -> EASIEST)
=========================================================
$$ Ye type ke questions exam me pakka aate hain - steps khud likh ke practice karo.

EXAMPLE 1 (Hardest): Chlor-alkali process me 3 products aur woh kahan milte hain?
   Reaction: 2NaCl + 2H2O --(electricity)--> 2NaOH + Cl2 + H2
   - Cathode (-) par: Hydrogen gas (H2)
   - Anode (+) par:   Chlorine gas (Cl2)
   - Bache solution me: Sodium hydroxide (NaOH)
   (Yaad: naam "chlor-alkali" = Chlorine + Alkali NaOH.)

EXAMPLE 2: Inn salt ka nature (acidic/basic/neutral) batao aur kyun -
   (a) NaCl  (b) NH4Cl  (c) Na2CO3
   (a) NaCl = strong acid (HCl) + strong base (NaOH) -> NEUTRAL (pH 7).
   (b) NH4Cl = strong acid (HCl) + weak base (NH4OH) -> ACIDIC (pH < 7).
   (c) Na2CO3 = weak acid (H2CO3) + strong base (NaOH) -> BASIC (pH > 7).

EXAMPLE 3: Sodium carbonate par dilute HCl daala - gas nikli jisne lime water
   doodhiya kar diya. Reactions likho aur gas batao.
   Na2CO3 + 2HCl -> 2NaCl + H2O + CO2
   Gas = CO2. Test: CO2 + Ca(OH)2 -> CaCO3(milky) + H2O.

EXAMPLE 4: Baking soda ko garam karne par kya hota hai? Equation do + 1 use.
   2NaHCO3 --(heat)--> Na2CO3 + H2O + CO2
   Use: cake banane me (CO2 nikal ke phoolta) / antacid.

EXAMPLE 5: Bleaching powder kaise banta hai? Equation + 1 use.
   Ca(OH)2 + Cl2 -> CaOCl2 + H2O
   Use: paani ko disinfect karna / kapda bleaching.

EXAMPLE 6: 5 mL HCl me Zn ka tukda daala - bubble nikle. Equation + gas test.
   Zn + 2HCl -> ZnCl2 + H2
   Gas = Hydrogen; jalti tili "pop" awaaz karti hai.

EXAMPLE 7 (Easiest): Neutralisation reaction ka ek example + general equation.
   NaOH + HCl -> NaCl + H2O
   General: Acid + Base -> Salt + Water.

<<<PAGEBREAK>>>

6. QUICK Q&A - PADHNE KE BAAD KHUD CHECK KARO
=========================================================
$$ Pehle khud answer socho, fir niche milao. Ye board-style questions hain.

Q1. Acid aur base me COMMON kya hai (ions ke hisaab se)?
A1. Acid paani me H+ (H3O+) deta hai, base paani me OH- deta hai. Isi se unke
    properties decide hote hain.

Q2. Acid ko paani me milate waqt kya savdhaani? Kyun?
A2. Hamesha acid ko paani me dheere daalo (paani ko acid me nahi), kyunki dilution
    exothermic hai - bahut garmi/chheente nikalte, ulta karne par jal sakte ho.

Q3. pH 7, pH<7, pH>7 ka matlab?
A3. 7 = neutral, <7 = acidic, >7 = basic. Kam pH = zyada acidic (zyada H+).

Q4. Acidity (pet me) me antacid kyun lete hain? Ek example.
A4. Antacid base hota - extra HCl ko neutralise karta. e.g. Mg(OH)2 (milk of
    magnesia) ya baking soda (NaHCO3).

Q5. Daant ka decay kab shuru hota hai aur kaise rokte hain?
A5. Jab muh ka pH 5.5 se neeche jaaye (bacteria + sugar -> acid). Basic toothpaste
    se neutralise karke rokte hain.

Q6. CO2 gas ko kaise test karte hain?
A6. Lime water [Ca(OH)2] me guzaaro - doodhiya/milky ho jaaye to CO2.
    CO2 + Ca(OH)2 -> CaCO3 + H2O.

Q7. Washing soda aur Baking soda ke chemical formula + 1-1 use.
A7. Washing soda = Na2CO3.10H2O (paani ki hardness hatana). Baking soda =
    NaHCO3 (baking/antacid).

Q8. Plaster of Paris ka formula aur ek use. Airtight kyun rakhte hain?
A8. CaSO4.(1/2)H2O. Use: tooti haddi ka plaster. Airtight isliye ki nami se
    pehle set ho jaata to kaam ka nahi rehta.

Q9. Bleaching powder ka chemical naam aur formula?
A9. Calcium oxychloride, CaOCl2.

Q10. Strong acid aur weak acid me farak?
A10. Strong acid paani me POORI tarah ionise hota (HCl), weak acid sirf THODA
     ionise hota (CH3COOH/acetic acid).

=========================================================
EXAM STRATEGY (1 minute revision):
$$  - Indicators ki table (litmus/methyl orange/phenolphthalein) ratlo.
$$  - 4 reactions ke general form: acid+metal, carbonate+acid, neutralisation,
$$    metal/non-metal oxide. Har ek ka 1 balanced example.
$$  - pH ke 5 daily-life uses likhna aana chahiye.
$$  - Chlor-alkali + bleaching powder + baking/washing soda + POP ke formula,
$$    banane ki equation aur uses - ye scoring topics hain.
@@  - CORE BASICS page (H+/OH-, ion, formula) bhool jaao to wapas pehle padho.
=========================================================
Generated by Kiro for Krishna1k - All the best!
"""


def to_markdown(content: str) -> str:
    """Convert the markup CONTENT into GitHub-friendly markdown."""
    out = ["# Acids, Bases and Salts",
           "### NCERT Class 10 Science - Chapter 2 (Hinglish Detailed Notes)",
           "",
           "> Colour key: red dot = Core Basics / extra help &nbsp;|&nbsp; "
           "green dot = comes often in board exams",
           ""]
    for raw in content.splitlines():
        line = raw.rstrip()
        if line.strip() == pdf_utils.PAGEBREAK_TOKEN:
            out.append("\n---\n")
            continue
        if set(line.strip()) <= {"="} and line.strip():
            continue
        m = re.match(r"^(\s*)(@@|\$\$)(.*)$", line)
        if m:
            indent, marker, rest = m.groups()
            emoji = "\U0001F534" if marker == "@@" else "\U0001F7E2"
            out.append(f"{indent}{emoji}{rest}")
            continue
        if pdf_utils._is_header(line.strip()):
            out.append(f"\n## {line.strip().title()}\n")
            continue
        out.append(line)
    return "\n".join(out) + "\n"


def main():
    here = Path(__file__).parent
    pdf_path = here / "Science_Class10_Ch2_Acids_Bases_Salts.pdf"
    md_path = here / "Science_Class10_Ch2_Acids_Bases_Salts.md"

    pdf_utils.text_to_pdf(
        CONTENT,
        pdf_path,
        title="Acids, Bases and Salts",
        subtitle="NCERT Class 10 Science - Ch 2 | Hinglish Detailed Notes",
    )
    md_path.write_text(to_markdown(CONTENT), encoding="utf-8")
    print(f"Wrote {md_path}")


if __name__ == "__main__":
    main()
