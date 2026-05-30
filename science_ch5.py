"""
science_ch5.py
--------------
Generates a detailed, simplified Hinglish study guide for
NCERT Class 10 Science, Chapter 5: "Life Processes".

Outputs:
  - Science_Class10_Ch5_Life_Processes.pdf  (colour PDF)
  - Science_Class10_Ch5_Life_Processes.md   (markdown, red/green via emoji)

Markup conventions inside CONTENT (handled by pdf_utils):
  @@  -> RED   line  (CORE BASICS / extra ke liye)
  $$  -> GREEN line  (exam me baar-baar aane wale topics)
  <<<PAGEBREAK>>>     -> nayi page
"""

import re
from pathlib import Path

import pdf_utils


CONTENT = r"""LIFE PROCESSES
NCERT Class 10 Science - Chapter 5 (Hinglish Detailed Notes)
=========================================================

@@ COLOUR CODE: RED = Core Basics / extra help (Class 7-8-9 wali cheezein jo yaad honi chahiye).
$$ COLOUR CODE: GREEN = Board exam me ye topics BAAR-BAAR aate hain - pakka yaad karo.
   Baaki normal black text = main chapter content (detail me, simple bhasha me).

<<<PAGEBREAK>>>

CORE BASICS - PEHLE YE PADHO (CLASS 7-8-9 KA FOUNDATION)
=========================================================
@@ Tune 7-8-9 nahi padhi - koi tension nahi. Ye page is chapter ki base hai.
@@ Ek baar achhe se padh le, fir chapter aasaani se samajh aayega.

@@ 1) CELL (KOSHIKA) - jeevan ki sabse chhoti ikai (unit):
@@    - Saare jeev cell se bane hote. Cell ke andar chhote-chhote parts =
@@      ORGANELLES (jaise factory ke alag-alag machine).
@@    - MITOCHONDRIA = "powerhouse of cell" - yahin respiration se ENERGY (ATP) banti.
@@    - CHLOROPLAST = sirf POUDHE (plant) ke cell me - isme CHLOROPHYLL (hara rang)
@@      hota jo sunlight pakad ke photosynthesis karta.

@@ 2) DIFFUSION = molecules ka ZYADA concentration se KAM concentration ki taraf
@@    apne aap failna (jaise itar ki khushboo poore kamre me). Gas exchange isi se.

@@ 3) OSMOSIS = paani (solvent) ka semi-permeable membrane ke aar-paar, kam ghol
@@    se zyada ghole (concentrated) ki taraf jaana. (Diffusion ka special case - paani ka.)

@@ 4) AUTOTROPH vs HETEROTROPH:
@@    - AUTOTROPH = khud apna khana banaye (poudhe - photosynthesis se). "Auto" = khud.
@@    - HETEROTROPH = doosron par nirbhar, khud nahi bana sakte (jaanwar, fungi, hum).

@@ 5) ENZYME = ek biological CATALYST (protein) jo body me reactions ko tez karta -
@@    jaise khane ko todna (digestion). Har enzyme ka apna khaas kaam hota.

@@ 6) GLAND (GRANTHI) = woh ang jo koi useful ras (juice/hormone/enzyme) banata aur
@@    chhodta. e.g. salivary gland (laar), liver, pancreas.

@@ 7) TISSUE -> ORGAN -> ORGAN SYSTEM:
@@    - Ek jaise cells milke TISSUE, alag tissue milke ORGAN (jaise dil, kidney),
@@      kayi organ milke ORGAN SYSTEM (jaise digestive system) banate.

@@ 8) RESPIRATION vs BREATHING (farak yaad rakho - exam favourite):
@@    - BREATHING = bas saans andar-bahar lena (O2 lena, CO2 chhodna) - physical kriya.
@@    - RESPIRATION = cell ke andar glucose ko todke ENERGY nikalna - chemical kriya.

@@ 9) BLOOD aur OXYGEN TRANSPORT (intro):
@@    - BLOOD = laal taral jo poore body me oxygen, khana aur waste le jaata.
@@    - HAEMOGLOBIN (RBC me laal pigment) oxygen ko pakad ke cells tak pahunchata.

@@ 10) DIFFUSION BADE JEEVO KE LIYE KAAFI NAHI:
@@    - Chhote jeev (Amoeba) me har cell hawa/paani ke direct sampark me - diffusion se kaam chal jaata.
@@    - Bade jeev (hum) me andar ke cells tak diffusion bahut SLOW pad jaata, isiliye
@@      special transport system (blood, heart, xylem/phloem) chahiye.

<<<PAGEBREAK>>>

1. LIFE PROCESSES KYA HAIN
=========================================================
   Woh saare kaam (processes) jo ek jeev ko ZINDA (alive) rakhne ke liye zaroori
   hain, unhe LIFE PROCESSES kehte. Ye background me chalte rehte hain.

$$ 4 MAIN LIFE PROCESSES (yaad rakho - N-R-T-E):
$$   (1) NUTRITION    - khana lena aur energy/material ke liye use karna.
$$   (2) RESPIRATION  - khane (glucose) ko todke energy (ATP) nikalna.
$$   (3) TRANSPORTATION - cheezein (O2, khana, waste) ek jagah se doosri pahunchana.
$$   (4) EXCRETION    - body ka harmful waste bahar nikalna.

   @@ Kyun zaroori? Body ki tooti-phooti repair, growth, energy aur control ke liye
   @@ in processes ka chalna laazmi hai - warna jeev zinda nahi rah sakta.

<<<PAGEBREAK>>>

2. NUTRITION (POSHAN)
=========================================================
   Khana lene aur use karne ka tarika. Do main type:

2.1 NUTRITION KE TYPE
---------------------------------------------------------
$$ AUTOTROPHIC NUTRITION = khud apna khana banana (poudhe, kuch bacteria) -
$$    CO2 + H2O se sunlight + chlorophyll ki madad se (photosynthesis).
$$ HETEROTROPHIC NUTRITION = doosre se khana lena. Iske 3 type:
$$    (a) SAPROPHYTIC - mare/sadte padaarth se khana (fungi, mushroom, bread mould).
$$    (b) PARASITIC   - kisi zinda host par/andar reh ke khana (Cuscuta, kide, leech).
$$    (c) HOLOZOIC    - poora khana andar le ke fir digest karna (Amoeba, insaan, kutta).

<<<PAGEBREAK>>>

2.2 PHOTOSYNTHESIS (POUDHO KA KHANA BANANA)
---------------------------------------------------------
$$ Wo process jisme green plant sunlight + chlorophyll se CO2 aur H2O ko glucose
$$ (khana) me badalte aur O2 chhodte.

$$ EQUATION (pakka yaad - exam me direct aata):
$$    6CO2 + 6H2O --(sunlight, chlorophyll)--> C6H12O6 + 6O2

$$ PHOTOSYNTHESIS KE 3 MAIN EVENTS (steps):
$$    (1) Chlorophyll dwara SUNLIGHT (light energy) ko ABSORB (pakadna) karna.
$$    (2) Light energy ko CHEMICAL energy me badalna AUR paani (H2O) ko todna
$$        (splitting) -> Hydrogen + Oxygen me.
$$    (3) CO2 ka REDUCTION (kami) hoke CARBOHYDRATE (glucose) banna.
   @@ Ye 3 events ek saath ek hi jagah hone zaroori nahi - alag-alag bhi ho sakte.

   ROLE OF STOMATA (PATTI ke chhote chhid):
$$    - STOMATA = patti par chhote chhid (pores) jinse gaseous exchange (CO2 andar,
$$      O2 bahar) hota aur transpiration me paani vaashp banke nikalta.
$$    - Har stoma ke do GUARD CELLS hote: paani bharke phoolte -> stoma KHULTA;
$$      paani nikalke sikudte -> stoma BAND ho jaata.
   @@ Jab paani bachana ho (zyada garmi) to plant stomata band karke loss rokta.

<<<PAGEBREAK>>>

2.3 NUTRITION IN AMOEBA aur PARAMECIUM (single-cell jeev)
---------------------------------------------------------
   AMOEBA (holozoic - PHAGOCYTOSIS se):
   - Amoeba apni body se ungli-jaisa PSEUDOPODIA (jhoothe pair) banake khana
     gher leta. Khana ek FOOD VACUOLE me band ho jaata.
   - Vacuole ke andar enzyme khane ko digest karte; bina-pacha waste bahar nikal jaata.

   PARAMECIUM:
   - Iski body par chhote baal-jaise CILIA hote jo hilke khane ko ek fix mouth-jaisi
     jagah tak dhakelte. Cilia ki madad se khana andar jaata.

<<<PAGEBREAK>>>

2.4 HUMAN DIGESTIVE SYSTEM (INSAAN KA PACHAN TANTRA)
---------------------------------------------------------
$$ Path: MOUTH -> OESOPHAGUS -> STOMACH -> SMALL INTESTINE -> LARGE INTESTINE -> ANUS.

$$ MOUTH (MUH):
$$   - Teeth (daant) khane ko chhota-chhota chabate.
$$   - SALIVA (laar) me enzyme SALIVARY AMYLASE (PTYALIN) - STARCH ko sugar me todta.

$$ OESOPHAGUS (KHANA-NALI):
$$   - PERISTALSIS = nali ki deewar ke sikudne-failne wale movement se khana
$$     dheere-dheere neeche stomach ki taraf dhakelta.

$$ STOMACH (AAMASHAY):
$$   - HCl (hydrochloric acid) - germ/bacteria maarta AUR medium ACIDIC banata
$$     taaki enzyme kaam kar sakein.
$$   - PEPSIN enzyme - PROTEIN ko todta (acidic medium me active).
$$   - MUCUS (lesa) - stomach ki deewar ko acid se BACHATA.

$$ SMALL INTESTINE (CHHOTI AANT) - digestion yahin POORI hoti:
$$   - BILE (liver/jigar se, gall bladder me store) - FAT ko chhote tukdo me todta
$$     (EMULSIFICATION) aur medium ko ALKALINE banata.
$$   - PANCREATIC JUICE (pancreas se): TRYPSIN (protein), LIPASE (fat),
$$     AMYLASE (starch/carbohydrate) ko todte.
$$   - ABSORPTION: andar ungli-jaisi VILLI (finger-like) hoti jo surface badhake
$$     pacha hua khana khoon (blood) me absorb karti.

$$ LARGE INTESTINE (BADI AANT):
$$   - Bache khane se PAANI absorb karti; bacha waste solid hoke nikalne ko taiyaar.
$$ ANUS: bina-pacha waste (mal) body se bahar (egestion).

<<<PAGEBREAK>>>

3. RESPIRATION (SHWASAN)
=========================================================
   Glucose ko todke ENERGY (ATP) nikalne ka process. Do type:

3.1 AEROBIC vs ANAEROBIC + GLUCOSE KE 3 RASTE
---------------------------------------------------------
$$ Pehla step sabme same: GLUCOSE -> PYRUVATE (CYTOPLASM me, oxygen ki zaroorat nahi).
$$ Uske baad pyruvate ka 3 alag-alag raasta:

$$ (1) AEROBIC (oxygen ke SAATH) - MITOCHONDRIA me:
$$     Pyruvate -> CO2 + H2O + BAHUT ZYADA energy (ATP).
$$ (2) ANAEROBIC, YEAST me (oxygen ke BINA) - FERMENTATION:
$$     Pyruvate -> ETHANOL + CO2 + thodi energy. (Sharab/double-roti banane me.)
$$ (3) ANAEROBIC, hamari MUSCLES me (oxygen ki KAMI par - tez bhaagte waqt):
$$     Pyruvate -> LACTIC ACID + thodi energy. (Isi se muscle me CRAMP/dard hota.)

$$ Yaad: Aerobic se sabse ZYADA energy milti (poora glucose toot-ta).
   @@ ATP = body ka "energy currency" - jab chahiye toot ke energy de deta.

<<<PAGEBREAK>>>

3.2 HUMAN RESPIRATORY SYSTEM (SHWASAN TANTRA)
---------------------------------------------------------
$$ Hawa ka path: NOSTRILS (naak) -> TRACHEA (wind-pipe) -> BRONCHI -> BRONCHIOLES
$$    -> ALVEOLI (chhote thaili-jaise baloon).
$$ ALVEOLI = yahin gas exchange hota. Iski deewar patli + bahut saari hoke BADA
$$    SURFACE AREA banati taaki O2-CO2 ka exchange tezi se ho.

   BREATHING MECHANISM:
   - DIAPHRAGM (chest ke neeche muscle sheet) niche jaati + pasli upar -> chest
     bada hota -> hawa ANDAR (inhale). Ulta hone par hawa BAHAR (exhale).

$$ HAEMOGLOBIN (RBC me) O2 ko pakadke poore body ke cells tak le jaata.
$$    (CO2 zyadatar plasma/paani me ghulke wapas lungs tak aata.)

   @@ AQUATIC vs TERRESTRIAL breathing rate:
   @@   - Paani me ghuli O2 hawa se BAHUT KAM hoti, isliye machhli (fish) ko tezi se
   @@     (zyada baar) saans lena padta - breathing rate ZYADA.
   @@   - Zameen ke jeev ko hawa me kaafi O2 milti - breathing rate KAM.

<<<PAGEBREAK>>>

4. TRANSPORTATION (PARIVAHAN)
=========================================================

4.1 HUMAN CIRCULATORY SYSTEM (KHOON KA PARIVAHAN)
---------------------------------------------------------
$$ HEART (DIL) ke 4 CHAMBERS:
$$    - Upar 2 = ATRIA (Right Atrium + Left Atrium) - blood RECEIVE karte.
$$    - Niche 2 = VENTRICLES (Right + Left) - blood PUMP karte (motti deewar).

$$ PATH OF BLOOD (simple):
$$    Body se deoxygenated blood -> Right Atrium -> Right Ventricle -> LUNGS
$$    (yahan O2 milta) -> Left Atrium -> Left Ventricle -> poore body me.

$$ DOUBLE CIRCULATION = blood ek pure chakkar me DO baar dil se guzarta:
$$    (i) Pulmonary - dil se lungs aur wapas. (ii) Systemic - dil se body aur wapas.
$$ KYUN ZAROORI: isse oxygenated aur deoxygenated blood MIX nahi hote ->
$$    body ko poori O2 milti -> high energy, warm-blooded (garam-khoon) jeevo ke
$$    liye zaroori (temperature maintain karne ko zyada energy chahiye).

   ARTERIES vs VEINS vs CAPILLARIES:
$$   - ARTERY: dil se body ki taraf blood le jaaye; motti elastic deewar, valve nahi
$$     (lungs ki pulmonary artery ko chhodke saari oxygenated blood le jaati).
$$   - VEIN: body se dil ki taraf blood laaye; patli deewar, VALVE hote (ulta na bahe).
$$   - CAPILLARY: sabse patli (1-cell motti) naliyan - yahin cells se exchange hota.

   - BLOOD: plasma (taral) + RBC (O2) + WBC (bachav) + PLATELETS (chot par khoon
     jamake bleeding rokte).
   - LYMPH: ek halka rang-heen taral jo extra fluid aur fat ko wapas blood me laata.
$$  - BLOOD PRESSURE = arteries ki deewar par blood ka dabaav. Normal ~120/80.
$$    Zyada (high BP) = hypertension - dangerous ho sakta.

<<<PAGEBREAK>>>

4.2 TRANSPORTATION IN PLANTS (POUDHO ME PARIVAHAN)
---------------------------------------------------------
$$ Do transport tissue: XYLEM aur PHLOEM.

$$ XYLEM:
$$   - PAANI + MINERALS ko jadon (roots) se patti ki taraf UPAR le jaata (ek direction).
$$   - TRANSPIRATION PULL: patti se paani vaashp banke udta -> neeche se paani
$$     kheenchta (jaise straw se kheechna). Din me ye main force hoti.

$$ PHLOEM:
$$   - Photosynthesis se bana KHANA (mostly SUCROSE) ko poore plant me pahunchata =
$$     TRANSLOCATION.
$$   - ENERGY (ATP) use karke hota; aur DONO direction me ho sakta (upar aur neeche)
$$     kyunki khana jad, fal, beej har jagah chahiye.

<<<PAGEBREAK>>>

5. EXCRETION (UTSARJAN)
=========================================================
   Body ka harmful nitrogen-wala waste (jaise urea) bahar nikalna.

5.1 HUMAN EXCRETORY SYSTEM
---------------------------------------------------------
$$ Parts: 2 KIDNEYS -> URETER -> URINARY BLADDER -> URETHRA.
$$ NEPHRON = kidney ki FILTERING UNIT (har kidney me lakhon nephron).

$$ URINE FORMATION (2 main steps):
$$   (1) FILTRATION: blood high pressure par nephron ke filter (glomerulus) se
$$       chhanta - paani, glucose, salt, urea sab nikal jaate.
$$   (2) SELECTIVE REABSORPTION: useful cheezein (glucose, kaafi paani, kuch salt)
$$       wapas blood me absorb ho jaati; bacha urea + extra paani = URINE.
   - Urine ureter se bladder me jama hota, fir urethra se bahar.

$$ ARTIFICIAL KIDNEY = DIALYSIS: jab kidney fail ho jaaye to machine se blood ka
$$    waste (urea) saaf kiya jaata (kidney ka kaam machine karti).

5.2 EXCRETION IN PLANTS (POUDHO ME)
---------------------------------------------------------
   - Gaseous waste (O2, CO2) STOMATA se nikal jaata.
   - Kuch waste purani PATTI ya BARK (chhaal) me store hoke jhad jaata.
   - RESIN aur GUM (gondh) ke roop me store.
   - Kuch waste jad ke aas-paas MITTI (soil) me chhod dete.

<<<PAGEBREAK>>>

6. SOLVED EXAMPLES (HARDEST -> EASIEST)
=========================================================
$$ Ye type ke questions exam me pakka aate - steps khud likhke practice karo.

EXAMPLE 1 (Hardest): Double circulation samjhao - heart ke chambers, blood ka
   path aur kyun zaroori hai?
   - Heart ke 4 chamber: 2 atria (upar, receive) + 2 ventricles (neeche, pump).
   - Path: body (deoxygenated) -> Right Atrium -> Right Ventricle -> lungs (O2 milta)
     -> Left Atrium -> Left Ventricle -> poore body.
   - Blood ek chakkar me 2 baar dil se guzarta (pulmonary + systemic) = double circulation.
   - Zaroori: oxygenated + deoxygenated blood mix nahi hote -> poori O2 supply ->
     warm-blooded jeevo ki high energy zarurat poori hoti.

EXAMPLE 2: Glucose ke breakdown ke 3 raaste - end-product aur jagah (site) batao.
   - Common: Glucose -> Pyruvate (cytoplasm me).
   - (a) Aerobic (mitochondria): Pyruvate -> CO2 + H2O + bahut ATP.
   - (b) Anaerobic, yeast: Pyruvate -> Ethanol + CO2 (fermentation).
   - (c) Anaerobic, muscles: Pyruvate -> Lactic acid (cramp ka kaaran).

EXAMPLE 3: Photosynthesis ka equation, 3 events aur stomata ka role likho.
   - 6CO2 + 6H2O --(sunlight, chlorophyll)--> C6H12O6 + 6O2
   - Events: (1) chlorophyll light absorb kare (2) light energy -> chemical energy +
     paani toote (H aur O) (3) CO2 reduce hoke carbohydrate bane.
   - Stomata: gas exchange (CO2 in, O2 out); guard cells paani se phoolke kholte/bandh karte.

EXAMPLE 4: Kaun-sa enzyme kahaan, kis khane par kaam karta? (table)
   - Saliva (mouth)        : Salivary amylase/ptyalin -> Starch.
   - Stomach               : Pepsin (acidic) -> Protein.
   - Small intestine       : Trypsin -> Protein; Lipase -> Fat; Amylase -> Starch.
   - (Bile fat ko emulsify karta - enzyme nahi, par fat todne me madad.)

EXAMPLE 5: Xylem aur Phloem me 3 farak likho.
   - Xylem: paani + minerals; sirf UPAR (one-way); energy nahi lagti (transpiration pull).
   - Phloem: bana khana (sucrose); DONO direction; ATP energy use hoti (translocation).

EXAMPLE 6: Nephron me urine kaise banta - steps?
   - (1) Filtration: glomerulus me high pressure par blood chhanta (paani, glucose,
     salt, urea nikalte).
   - (2) Selective reabsorption: glucose, zyada paani, kuch salt wapas blood me.
   - Bacha urea + paani = urine -> ureter -> bladder -> urethra se bahar.

EXAMPLE 7 (Easiest): Autotrophic aur Heterotrophic nutrition me farak + example.
   - Autotrophic: khud khana banaye (photosynthesis). e.g. green plants.
   - Heterotrophic: doosron se khana le. e.g. insaan, kutta, fungi.

<<<PAGEBREAK>>>

7. QUICK Q&A - PADHNE KE BAAD KHUD CHECK KARO
=========================================================
$$ Pehle khud answer socho, fir niche milao. Ye board-style questions hain.

Q1. Respiration aur Breathing me farak?
A1. Breathing = bas hawa andar-bahar lena (physical). Respiration = cell me glucose
    todke energy nikalna (chemical, mitochondria me).

Q2. Photosynthesis ke liye kya-kya chahiye?
A2. CO2, H2O, sunlight aur chlorophyll. Product: glucose (C6H12O6) + O2.

Q3. Stomata ka kaam aur band/khulna kaun control karta?
A3. Gaseous exchange aur transpiration. GUARD CELLS paani bharke phoolne par khulta,
    sikudne par band ho jaata.

Q4. HCl stomach me kyun banta hai?
A4. Germs maarne aur medium acidic banane ke liye taaki pepsin (protein-enzyme)
    kaam kar sake.

Q5. Villi kya hai aur kyun zaroori?
A5. Chhoti aant me ungli-jaisi structure jo surface area badhake pacha hua khana
    blood me absorb karti.

Q6. Anaerobic respiration ke products kahaan kya hote?
A6. Yeast me ethanol + CO2; hamari muscles me lactic acid (cramp).

Q7. Alveoli ki khaasiyat kya hai?
A7. Patli deewar + bahut saari -> bada surface area, isliye O2-CO2 exchange tezi se hota.

Q8. Double circulation me blood kitni baar dil se guzarta aur kyun acha hai?
A8. Ek chakkar me 2 baar. Oxygenated/deoxygenated blood mix nahi hote -> efficient
    O2 supply.

Q9. Xylem aur Phloem me se kaun energy use karta?
A9. Phloem (translocation me ATP lagti). Xylem mostly transpiration pull (energy nahi).

Q10. Dialysis kya hai?
A10. Kidney fail hone par machine (artificial kidney) se blood ka urea/waste saaf
    karna.

<<<PAGEBREAK>>>

=========================================================
EXAM STRATEGY (1 minute revision):
$$  - Photosynthesis equation + 3 events + stomata/guard cell - pakka aata.
$$  - Human digestive system path + enzyme table (amylase/pepsin/trypsin/lipase).
$$  - Respiration ke 3 raaste (aerobic, yeast, muscle) end-product ke saath.
$$  - Heart 4 chambers + blood path + DOUBLE CIRCULATION kyun zaroori.
$$  - Xylem vs Phloem differences + nephron/urine formation (2 steps).
@@  - CORE BASICS page (cell, diffusion, osmosis, autotroph/heterotroph) bhool
@@    jaao to wapas pehle padho - base strong rakho.
=========================================================
Generated by Kiro for Krishna1k - All the best!
"""


def to_markdown(content: str) -> str:
    """Convert the markup CONTENT into GitHub-friendly markdown."""
    out = ["# Life Processes",
           "### NCERT Class 10 Science - Chapter 5 (Hinglish Detailed Notes)",
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
    pdf_path = here / "Science_Class10_Ch5_Life_Processes.pdf"
    md_path = here / "Science_Class10_Ch5_Life_Processes.md"

    pdf_utils.text_to_pdf(
        CONTENT,
        pdf_path,
        title="Life Processes",
        subtitle="NCERT Class 10 Science - Ch 5 | Hinglish Detailed Notes",
    )
    md_path.write_text(to_markdown(CONTENT), encoding="utf-8")
    print(f"Wrote {md_path}")


if __name__ == "__main__":
    main()
