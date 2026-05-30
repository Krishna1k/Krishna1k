"""
science_ch3.py
--------------
Generates a detailed, simplified Hinglish study guide for
NCERT Class 10 Science, Chapter 3: "Metals and Non-metals".

Outputs:
  - Science_Class10_Ch3_Metals_NonMetals.pdf  (colour PDF)
  - Science_Class10_Ch3_Metals_NonMetals.md   (markdown, red/green via emoji)

Markup conventions inside CONTENT (handled by pdf_utils):
  @@  -> RED   line  (CORE BASICS / extra ke liye)
  $$  -> GREEN line  (exam me baar-baar aane wale topics)
  <<<PAGEBREAK>>>     -> nayi page
"""

import re
from pathlib import Path

import pdf_utils


CONTENT = r"""METALS AND NON-METALS
NCERT Class 10 Science - Chapter 3 (Hinglish Detailed Notes)
=========================================================

@@ COLOUR CODE: RED = Core Basics / extra help (Class 7-8-9 wali cheezein jo yaad honi chahiye).
$$ COLOUR CODE: GREEN = Board exam me ye topics BAAR-BAAR aate hain - pakka yaad karo.
   Baaki normal black text = main chapter content (detail me, simple bhasha me).

<<<PAGEBREAK>>>

CORE BASICS - PEHLE YE PADHO (CLASS 7-8-9 KA FOUNDATION)
=========================================================
@@ Tune 7-8-9 nahi padhi - koi tension nahi. Ye page is chapter ki base hai.
@@ Ek baar achhe se padh le, fir chapter aasaani se samajh aayega.

@@ 1) METAL vs NON-METAL (Class 8 ka idea):
@@    - Metal = chamakdaar, hard, electricity/heat conduct karta (Fe, Cu, Al, Au).
@@    - Non-metal = mostly dull, electricity conduct nahi karta (C, S, O, N, Cl).

@@ 2) ATOM, ELECTRON, SHELL (Class 9):
@@    - Atom ke beech nucleus (proton+neutron), bahar electron ghoomte (shells K,L,M).
@@    - Sabse bahar wale electron = VALENCE electron - reaction inhi se hoti hai.

@@ 3) ION, CATION, ANION (bahut zaroori is chapter ke liye):
@@    - Electron CHHOD-ne par +ve charge = CATION (metal banata: Na -> Na+).
@@    - Electron LENE par -ve charge = ANION (non-metal banata: Cl -> Cl-).
@@    - Atom apna outer shell 8 (ya 2) electron se "full" karna chahta hai.

@@ 4) VALENCY (combining power):
@@    - Na=1, Mg=2, Al=3, O=2, Cl=1. Criss-cross se formula: Mg(2)+Cl(1)=>MgCl2.

@@ 5) OXIDE aur uska NATURE:
@@    - Oxide = element + oxygen (MgO, CO2). Metal oxide = BASIC,
@@      Non-metal oxide = ACIDIC. (Ye baat baar baar kaam aayegi.)

@@ 6) DISPLACEMENT (Ch-1 se):
@@    - Zyada reactive metal, kam reactive ko uske salt se hata deta:
@@      Fe + CuSO4 -> FeSO4 + Cu.

@@ 7) CONDUCTOR vs INSULATOR (Class 7):
@@    - Conductor = current paas hone de (metal). Insulator = na de (rubber, plastic).

@@ 8) COMPOUND vs MIXTURE (alloy samajhne ke liye):
@@    - Compound = chemically jude fixed ratio. Mixture = bas mile hue (alloy ek
@@      "solid solution"/mixture jaisa hota hai - metal + metal/non-metal).

@@ 9) EXOTHERMIC (Ch-1 se): reaction jisme heat NIKALTI hai (thermit, Na+water).

<<<PAGEBREAK>>>

1. PHYSICAL PROPERTIES
=========================================================

1.1 METALS KE PHYSICAL PROPERTIES
---------------------------------------------------------
$$ (yaad rakhne ke liye properties + definition):
$$   - LUSTRE: chamakdaar surface (polish karne par).
$$   - MALLEABLE: hathodi se patli SHEET ban sakti (malleability). e.g. Au, Ag, Al.
$$   - DUCTILE: patle TAAR (wire) me kheech sakte (ductility). e.g. Cu, Al.
$$   - GOOD CONDUCTOR of heat & electricity (best: silver, copper).
$$   - SONOROUS: thok-ne par awaaz (ghanti).
$$   - High melting point, mostly hard, room temp par SOLID.

   @@ EXCEPTIONS (exam ke favourite):
   @@   - Mercury (Hg) = room temp par LIQUID metal.
   @@   - Sodium (Na), Potassium (K) = itne SOFT ki chaaku se kat jaate.
   @@   - Cs aur Ga = haath ki garmi se pighal jaate (low melting point).

1.2 NON-METALS KE PHYSICAL PROPERTIES
---------------------------------------------------------
   - Lustre nahi (dull), brittle (toot-te), non-malleable, non-ductile.
   - Heat/electricity ke BAD conductor, non-sonorous.
   - Solid/liquid/gas teeno me ho sakte (Br liquid; O2, N2 gas; C, S solid).

   @@ EXCEPTIONS:
   @@   - IODINE = non-metal par CHAMAKDAAR (lustrous).
   @@   - GRAPHITE (carbon ka roop) = non-metal par electricity CONDUCT karta.
   @@   - DIAMOND (carbon) = sabse HARD natural padaarth, high melting point.

<<<PAGEBREAK>>>

2. METALS KE CHEMICAL PROPERTIES
=========================================================
$$ Ye section exam me sabse zyada marks deta - 4 reactions + reactivity series.

2.1 OXYGEN (HAWA) KE SAATH - Metal Oxide (basic)
---------------------------------------------------------
$$ Metal + Oxygen -> Metal oxide (ye BASIC hota hai)
$$    2Cu + O2 -> 2CuO  (black)
$$    4Al + 3O2 -> 2Al2O3
$$    2Mg + O2 -> 2MgO  (white, tej safed roshni ke saath jalta)

$$ AMPHOTERIC OXIDES = jo acid AUR base DONO ke saath react karein.
$$    e.g. Al2O3 aur ZnO. (Exam me definition + example puchte hain.)
   - Na2O, K2O paani me ghul ke alkali (NaOH, KOH) banate.
   @@ Reactivity alag-alag: Na/K bahut tezi se (isliye kerosene me rakhte),
   @@ Mg/Al par protective oxide layer ban jaata, Au/Ag oxidise nahi hote.
   @@ ANODISING = Al par jaan-bujh ke moti oxide layer chadhana (corrosion se bachne).

2.2 PAANI (WATER) KE SAATH
---------------------------------------------------------
$$ Metal + Water -> Metal hydroxide/oxide + Hydrogen (H2)
$$    2Na + 2H2O -> 2NaOH + H2 + heat  (bahut tej - aag pakad leta!)
$$    Ca + 2H2O -> Ca(OH)2 + H2        (kam tej, gas ke bubble metal pe chipakte)
$$    3Fe + 4H2O(steam) -> Fe3O4 + 4H2 (Fe sirf BHAAP/steam ke saath)
   @@ Cu, Ag, Au paani ke saath bilkul react NAHI karte (kam reactive).

2.3 ACID KE SAATH
---------------------------------------------------------
$$ Metal + dilute Acid -> Salt + Hydrogen (H2)
$$    Fe + 2HCl -> FeCl2 + H2
$$    Mg + 2HCl -> MgCl2 + H2
   @@ Copper (Cu) tanu HCl ke saath react NAHI karta (H se kam reactive).
   @@ HNO3 (nitric acid) aam taur par H2 nahi deta (oxidising hai) - paani bana
   @@ deta hai; sirf bahut tanu HNO3 ke saath Mg/Mn H2 dete hain.
   @@ AQUA REGIA = 3:1 (conc. HCl : conc. HNO3) - Gold/Platinum tak ko ghol deta.

2.4 DUSRE METAL KE SALT-SOLUTION KE SAATH (DISPLACEMENT)
---------------------------------------------------------
$$ Zyada reactive metal, kam reactive ko uske salt se hata (displace) deta:
$$    Fe + CuSO4 -> FeSO4 + Cu   (neela rang halka hara, Cu jam jaata)
$$    Zn + CuSO4 -> ZnSO4 + Cu

3. REACTIVITY SERIES (ACTIVITY SERIES)
=========================================================
$$ Metals ko reactivity ke order me lagana (ZYADA se KAM reactive):
$$    K > Na > Ca > Mg > Al > Zn > Fe > Pb > (H) > Cu > Hg > Ag > Au
$$ - Upar wale bahut reactive (K, Na - paani se bhi react).
$$ - (H) ke UPAR wale metal hi dilute acid se H2 dete hain.
$$ - Neeche wale (Au, Ag) kam reactive - prakriti me FREE/native milte hain.
   @@ Yaad karne ki line: "Kal Na Ca Magar Aaj Zara Fir Pyaar (H) Karega
   @@ Hamesha Sona-Chandi" type mnemonics bana sakte ho.

<<<PAGEBREAK>>>

4. METAL aur NON-METAL KAISE REACT KARTE HAIN (IONIC BOND)
=========================================================
$$ Metal apne valence ELECTRON CHHOD-ta (cation banta), non-metal woh electron
$$ LE leta (anion banta). Opposite charge attract -> IONIC/ELECTROVALENT bond.

   Example - Sodium chloride (NaCl) banna:
   $$  Na -> Na+ + e-      (Na ne 1 electron chhoda)
   $$  Cl + e- -> Cl-      (Cl ne 1 electron liya)
   $$  Na+ + Cl- -> NaCl   (attraction se bond)
   Aur: Mg -> Mg2+ + 2e-, do Cl le ke MgCl2.

$$ IONIC COMPOUNDS KE PROPERTIES (exam favourite - list yaad rakho):
$$   (i)   Solid aur HARD (strong ionic attraction se).
$$   (ii)  HIGH melting & boiling point (bond todne ko zyada energy).
$$   (iii) Paani me SOLUBLE, par petrol/kerosene me insoluble.
$$   (iv)  Electricity conduct karte: MOLTEN (pighla) ya AQUEOUS (paani) state me,
$$         par THOS (solid) state me NAHI (kyunki ion move nahi kar paate).

5. OCCURRENCE & EXTRACTION OF METALS (METALLURGY)
=========================================================
@@ MINERAL = zameen me mila metal-wala natural padaarth.
@@ ORE = woh mineral jisme metal itna zyada ho ki nikalna faydemand ho.
@@ GANGUE = ore me mili mitti/impurity.

$$ Metal kaise nikaalein - REACTIVITY par depend karta:
$$   (A) KAM reactive (neeche - Au, Ag, Hg, Cu): bas HEAT karke.
$$       2HgS + 3O2 -> 2HgO + 2SO2 ; phir 2HgO -> 2Hg + O2 (sirf heating).
$$   (B) MIDDLE (Zn, Fe, Pb): pehle oxide banao, fir CARBON se reduce karo:
$$       - ROASTING (sulphide ore + zyada hawa -> oxide):
$$         2ZnS + 3O2 -> 2ZnO + 2SO2
$$       - CALCINATION (carbonate ore + kam hawa -> oxide):
$$         ZnCO3 -> ZnO + CO2
$$       - REDUCTION (oxide + carbon -> metal):
$$         ZnO + C -> Zn + CO
$$   (C) ZYADA reactive (upar - Na, Mg, Ca, Al, K): ELECTROLYSIS (electrolytic
$$       reduction). e.g. pighle NaCl ka electrolysis -> Na (cathode) + Cl2.

$$ THERMIT REACTION (bahut important - exam me pakka):
$$    Fe2O3 + 2Al -> 2Fe + Al2O3 + bahut heat
$$    - Al ne Fe2O3 ko reduce kiya (Al zyada reactive). Itni garmi ki Fe PIGHAL
$$      ke nikalta - isiliye RAILWAY PATRI (tracks) aur machine parts JODNE me use.

@@ REFINING (shudhi-karan) - ELECTROLYTIC REFINING:
@@   Impure metal = ANODE (+), pure metal ki patli sheet = CATHODE (-),
@@   metal-salt solution electrolyte. Current se pure metal cathode par jam jaata.

<<<PAGEBREAK>>>

6. CORROSION aur usse BACHAAV (ALLOYS)
=========================================================
$$ CORROSION = metal ka hawa/nami/acid se dheere-dheere kharaab hona.
$$   - Iron par RUST: reddish-brown (Fe2O3.xH2O). Rust ke liye HAWA + PAANI dono chahiye.
$$   - Silver par kaali parat (Ag2S), Copper par hari parat (basic copper carbonate).

$$ BACHAAV KE TARIKE (prevention):
$$   - Painting, oiling/greasing (hawa-paani rok-na).
$$   - GALVANISATION = iron par ZINC ki layer chadhana (sabse common).
$$   - Chrome plating, anodising, aur ALLOY banana (jaise stainless steel).

6.1 ALLOYS (MISHRA DHATU)
---------------------------------------------------------
$$ ALLOY = do ya zyada metal (ya metal + non-metal) ka homogeneous MIXTURE.
$$ Alloy banane se metal ki strength badhti, corrosion ghatta, properties improve.
$$   - Steel = Iron + Carbon (strong).
$$   - Stainless steel = Iron + Nickel + Chromium (rust nahi karta).
$$   - Brass (Pital) = Copper + Zinc.
$$   - Bronze (Kansa) = Copper + Tin.
$$   - Solder = Lead + Tin (wires jodne me, low melting point).
   @@ AMALGAM = woh alloy jisme MERCURY (Hg) ho. Pure iron bahut soft hota,
   @@ isliye usme thoda carbon mila ke steel banate (hard + useful).

<<<PAGEBREAK>>>

7. SOLVED EXAMPLES (HARDEST -> EASIEST)
=========================================================
$$ Ye type ke questions exam me pakka aate - steps khud likhke practice karo.

EXAMPLE 1 (Hardest): Zinc ke sulphide ore (ZnS) se shudh Zinc kaise nikaalenge?
   Saare steps + equations likho.
   Step 1 - ROASTING (sulphide -> oxide, zyada hawa me):
      2ZnS + 3O2 -> 2ZnO + 2SO2
   Step 2 - REDUCTION (oxide + carbon -> metal):
      ZnO + C -> Zn + CO
   Step 3 - REFINING: electrolytic refining se pure Zn.
   (Zn middle reactivity ka hai, isliye roasting + carbon reduction.)

EXAMPLE 2: Thermit reaction likho, type batao aur ek use + reason.
   Fe2O3 + 2Al -> 2Fe + Al2O3 + heat
   Type: Displacement + Redox (Al ne Fe2O3 reduce kiya, khud oxidise hua).
   Use: railway track/machine parts jodna. Reason: itni garmi nikalti ki
   Fe pighal ke nikalta (highly exothermic).

EXAMPLE 3: Ionic compound (NaCl) THOS me current conduct kyun nahi karta par
   pighla/paani me karta hai?
   Thos me ion fixed/jakde hote (move nahi kar sakte) -> no conduction.
   Pighalne/paani me ghulne par ion FREE ho ke move karte -> current conduct.

EXAMPLE 4: Reactivity series ke hisaab se batao - kya reaction hogi?
   (a) Fe + CuSO4   (b) Cu + FeSO4
   (a) HOGI: Fe, Cu se zyada reactive -> Fe + CuSO4 -> FeSO4 + Cu.
   (b) NAHI hogi: Cu, Fe se kam reactive - displace nahi kar sakta.

EXAMPLE 5: Copper dilute HCl me react nahi karta par Zinc karta - kyun?
   Reactivity series me Zn, hydrogen ke UPAR hai (acid se H2 deta), Cu hydrogen
   ke NEECHE hai (acid se H2 nahi de sakta). Zn + 2HCl -> ZnCl2 + H2.

EXAMPLE 6: Sodium ko kerosene me kyun rakhte hain? Paani ke saath reaction?
   Na itna reactive ki hawa/nami se turant react kar ke aag pakad leta, isliye
   kerosene me doob ke rakhte. 2Na + 2H2O -> 2NaOH + H2 + heat (tez, jal-uthta).

EXAMPLE 7 (Easiest): In properties se batao metal hai ya non-metal -
   "chamakdaar, taar me kheechne yogya, electricity conduct karta"
   Answer: METAL (lustrous + ductile + good conductor).

<<<PAGEBREAK>>>

8. QUICK Q&A - PADHNE KE BAAD KHUD CHECK KARO
=========================================================
$$ Pehle khud answer socho, fir niche milao. Ye board-style questions hain.

Q1. Malleability aur Ductility me farak?
A1. Malleability = sheet/chaadar me peet sakte. Ductility = taar (wire) me
    kheench sakte. Dono metals ki property hain.

Q2. Amphoteric oxide kya hai? 2 example.
A2. Jo oxide acid aur base DONO se react kare. e.g. Al2O3 aur ZnO.

Q3. Roasting aur Calcination me farak (with equation)?
A3. Roasting = SULPHIDE ore zyada hawa me garam -> oxide (2ZnS+3O2->2ZnO+2SO2).
    Calcination = CARBONATE ore kam hawa me garam -> oxide (ZnCO3->ZnO+CO2).

Q4. Thermit reaction ka use aur ek line me reason?
A4. Railway patri/machine parts jodne me; kyunki bahut heat nikalti aur Fe
    pighal ke nikalta (Fe2O3 + 2Al -> 2Fe + Al2O3 + heat).

Q5. Ionic compounds paani me ghulte par solid me current conduct nahi karte - kyun?
A5. Solid me ion fix hote (move nahi karte). Molten/aqueous me ion free move
    karte isliye conduct karte.

Q6. Aqua regia kya hai aur khaas baat?
A6. 3:1 conc. HCl : conc. HNO3 ka mixture. Gold/Platinum jaise inert metal bhi
    ghol deta.

Q7. Galvanisation kya hai?
A7. Iron par zinc ki parat chadhana taaki rust (corrosion) na lage.

Q8. Alloy kya hai? Stainless steel kisse banta?
A8. 2+ metal (ya metal+non-metal) ka homogeneous mixture. Stainless steel =
    Iron + Nickel + Chromium.

Q9. Sabse reactive aur sabse kam reactive metal (series ke according)?
A9. Sabse reactive = Potassium (K), sabse kam reactive = Gold (Au).

Q10. Mercury aur Iodine ki ek-ek unusual baat batao.
A10. Mercury = room temp par liquid metal. Iodine = non-metal hote hue bhi lustrous.

=========================================================
EXAM STRATEGY (1 minute revision):
$$  - 4 chemical reactions of metals (O2, water, acid, salt) + 1-1 example.
$$  - Reactivity series order ratlo - displacement/acid questions yahin se.
$$  - Ionic compound properties (4 points) likhna aana chahiye.
$$  - Roasting vs calcination + reduction + THERMIT - extraction me scoring.
$$  - Corrosion prevention + alloys (steel, brass, bronze) ke examples.
@@  - CORE BASICS page (ion, electron chhodna/lena, oxide nature) bhool jaao
@@    to wapas pehle padho - base strong rakho.
=========================================================
Generated by Kiro for Krishna1k - All the best!
"""


def to_markdown(content: str) -> str:
    """Convert the markup CONTENT into GitHub-friendly markdown."""
    out = ["# Metals and Non-metals",
           "### NCERT Class 10 Science - Chapter 3 (Hinglish Detailed Notes)",
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
    pdf_path = here / "Science_Class10_Ch3_Metals_NonMetals.pdf"
    md_path = here / "Science_Class10_Ch3_Metals_NonMetals.md"

    pdf_utils.text_to_pdf(
        CONTENT,
        pdf_path,
        title="Metals and Non-metals",
        subtitle="NCERT Class 10 Science - Ch 3 | Hinglish Detailed Notes",
    )
    md_path.write_text(to_markdown(CONTENT), encoding="utf-8")
    print(f"Wrote {md_path}")


if __name__ == "__main__":
    main()
