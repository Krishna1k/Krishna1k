"""
science_ch1.py
--------------
Generates a detailed, simplified Hinglish study guide for
NCERT Class 10 Science, Chapter 1: "Chemical Reactions and Equations".

Outputs:
  - Science_Class10_Ch1_Chemical_Reactions.pdf  (colour PDF)
  - Science_Class10_Ch1_Chemical_Reactions.md   (markdown, red=🔴 green=🟢)

Markup conventions inside CONTENT (handled by pdf_utils):
  @@  -> RED   line  (CORE BASICS / extra ke liye)
  $$  -> GREEN line  (exam me baar-baar aane wale topics)
  <<<PAGEBREAK>>>     -> nayi page
"""

import re
from pathlib import Path

import pdf_utils


CONTENT = r"""CHEMICAL REACTIONS AND EQUATIONS
NCERT Class 10 Science - Chapter 1 (Hinglish Detailed Notes)
=========================================================

@@ COLOUR CODE: RED = Core Basics / extra help (Class 7-8-9 wali cheezein jo yaad honi chahiye).
$$ COLOUR CODE: GREEN = Board exam me ye topics BAAR-BAAR aate hain - pakka yaad karo.
   Baaki normal black text = main chapter content (detail me, simple bhasha me).

<<<PAGEBREAK>>>

CORE BASICS - PEHLE YE PADHO (CLASS 7-8-9 KA FOUNDATION)
=========================================================
@@ Tune 7-8-9 nahi padhi, koi baat nahi. Ye page chapter samajhne ke liye
@@ zaroori base hai. Pure page ko ek baar achhe se padh le, fir aage badhna.

@@ 1) MATTER, ATOM, MOLECULE:
@@    - Matter = jis cheez me mass ho aur jagah ghere (jaise paani, hawa, lohaa).
@@    - Atom = element ka sabse chhota kann (jaise H, O, Na).
@@    - Molecule = do ya zyada atom jud ke bante hain (jaise H2O, O2).

@@ 2) ELEMENT, COMPOUND, MIXTURE:
@@    - Element = ek hi tarah ke atom (Iron = Fe, Oxygen = O2).
@@    - Compound = 2+ element fixed ratio me chemically jude (Water = H2O).
@@    - Mixture = bina chemical bond ke mila hua (namak + paani).

@@ 3) SYMBOL aur FORMULA:
@@    - Symbol = element ka short naam: Hydrogen=H, Oxygen=O, Sodium=Na,
@@      Carbon=C, Calcium=Ca, Iron=Fe, Copper=Cu, Zinc=Zn, Chlorine=Cl.
@@    - Formula = compound me kaunse atom kitne hain: H2O = 2 H + 1 O.

@@ 4) VALENCY (combining power) - formula banane ke liye:
@@    - H=1, O=2, Na=1, Cl=1, Ca=2, Mg=2, Al=3, C=4.
@@    - Criss-cross trick: Ca(valency 2) + Cl(valency 1) => CaCl2.
@@    - Common ions: SO4 (valency 2), NO3 (1), CO3 (2), OH (1).

@@ 5) SUBSCRIPT vs COEFFICIENT (bahut important - log yahin galti karte hain):
@@    - Subscript = chhota number niche (H2 ka '2'): batata hai 1 molecule me
@@      kitne atom. Ye kabhi mat badlo balance karte waqt.
@@    - Coefficient = aage bada number (2H2O ka '2'): batata hai kitne molecule.
@@      Balance karte waqt sirf YE number change karte hain.

@@ 6) DIATOMIC MOLECULES (apne aap me 2 atom): H2, O2, N2, Cl2, F2, Br2, I2.

@@ 7) STATE SYMBOLS (equation me likhte hain):
@@    (s)=solid, (l)=liquid, (g)=gas, (aq)=aqueous (paani me ghula hua).

@@ 8) PHYSICAL vs CHEMICAL CHANGE (Class 7):
@@    - Physical change = sirf roop badle, nayi cheez nahi bani, reversible.
@@      Jaise ice se paani, paani se bhaap.
@@    - Chemical change = NAYA padaarth banta hai, mostly irreversible.
@@      Jaise lohe par zang, doodh se dahi, paper jalna.

@@ 9) ACID, BASE, SALT (Class 7) - quick idea:
@@    - Acid = khatta (nimbu, sirka), HCl, H2SO4.
@@    - Base/Alkali = kadwa, saboon jaisa, NaOH, Ca(OH)2.
@@    - Acid + Base => Salt + Water (isko neutralisation bolte hain).

@@ 10) LAW OF CONSERVATION OF MASS (Class 9 - Lavoisier):
@@    - Reaction me mass na banta hai na nasht hota - reactant ka total mass
@@      = product ka total mass. ISI wajah se equation BALANCE karna padta hai.

<<<PAGEBREAK>>>

1. CHEMICAL REACTION KYA HAI?
=========================================================
Jab koi padaarth (ya padaarth) badal ke ek ya zyada NAYE padaarth bana de,
to use chemical reaction kehte hain. Purane padaarth = REACTANT, naye
padaarth = PRODUCT.

Example: Magnesium ribbon ko jalao to safed powder (Magnesium oxide) banta hai.
   Magnesium + Oxygen  ->  Magnesium oxide

$$ CHEMICAL REACTION HONE KE SIGNS (exam me "how do you know a reaction
$$ has occurred?" aksar puchte hain) - koi bhi ek-do dikhe to reaction hua:
$$    (i)   Colour change (rang badalna)
$$    (ii)  State change (solid/liquid/gas badalna)
$$    (iii) Temperature change (garmi nikle ya soshit ho)
$$    (iv)  Gas banna (bubbles/effervescence)
$$    (v)   Precipitate banna (paani me na ghulne wala thos)

   Daily life examples: doodh se dahi, lohe par zang, khana pachna (digestion),
   shwasan (respiration), saans se nikli CO2.

2. CHEMICAL EQUATION
=========================================================
Reaction ko shabdon ki jagah symbol/formula se likhna = chemical equation.

  Word equation:   Magnesium + Oxygen -> Magnesium oxide
  Symbol equation: Mg + O2 -> MgO   (abhi ye balanced nahi hai)

  - Reactant left side, Product right side, beech me arrow (->).
  - Arrow ka matlab "banata hai / yields", direction reaction ki taraf.

3. BALANCED CHEMICAL EQUATION
=========================================================
$$ Balancing har board exam me aata hai - 100% prepare karo.

Balanced equation = jisme dono taraf har element ke atom ki SANKHYA barabar ho.
Reason = Law of Conservation of Mass (mass na banti na nasht hoti).

Unbalanced:  Mg + O2 -> MgO
Balanced:    2Mg + O2 -> 2MgO   (dono taraf Mg=2, O=2)

$$ BALANCING KE STEPS (Hit and Trial Method):
   Step 1: Skeleton (kacchi) equation likho - sahi formula ke saath.
   Step 2: Har element ke atom dono side gino (table bana lo).
   Step 3: Sabse zyada atom wale compound se shuru karo, coefficient lagao.
   Step 4: Metal -> non-metal -> H -> O is order me balance karna easy padta hai.
   Step 5: Sirf COEFFICIENT badlo (aage ka number), SUBSCRIPT kabhi mat badlo.
   Step 6: Last me state symbols (s/l/g/aq) aur conditions likho.

   Example (step by step): Fe + H2O -> Fe3O4 + H2
     - Fe: right 3, left 1  => left me 3Fe
     - O: right 4, left 1   => left me 4H2O
     - ab H: left 4x2=8, right 2 => right me 4H2
     Final: 3Fe + 4H2O -> Fe3O4 + 4H2   (Fe=3, O=4, H=8 dono taraf) Done!

@@ EXTRA TIP: Polyatomic ion (jaise SO4, NO3) agar dono side same hai to use
@@ ek "unit" maan ke balance karo, atom-atom todne ki zaroorat nahi.

CONDITIONS aur EXTRA INFO equation me kaise likhein:
   - Heat ke liye arrow ke upar "Delta" ya "heat" likhte hain.
   - Catalyst, temperature, pressure bhi arrow ke upar.
   - Gas nikle to upar arrow (up), precipitate bane to niche arrow (down).
   Example: 2H2O --(electricity)--> 2H2(g) + O2(g)

<<<PAGEBREAK>>>

4. TYPES OF CHEMICAL REACTIONS
=========================================================
$$ Reaction types se direct questions + examples puchte hain. Har type ka
$$ kam se kam 1 example + 1 balanced equation yaad rakho.

4.1 COMBINATION REACTION (Sanyojan)
---------------------------------------------------------
$$ Do ya zyada reactant mil ke EK product banate hain. (A + B -> AB)

   Examples:
   $$ CaO + H2O -> Ca(OH)2    (Bujha hua chuna/slaked lime banta hai,
                                bahut garmi nikalti hai = exothermic)
      C + O2 -> CO2           (coal jalna)
      2H2 + O2 -> 2H2O        (paani banna)
      2Mg + O2 -> 2MgO

   @@ Note: CaO = Quick lime (bina bujha chuna). Isme paani daalo to
   @@ Ca(OH)2 (slaked lime) banta hai + heat - white-washing me use hota hai.

4.2 DECOMPOSITION REACTION (Viyojan)
---------------------------------------------------------
$$ Ek reactant tut ke do ya zyada product deta hai. (AB -> A + B)
$$ Combination ka ULTA. Energy chahiye hoti hai (heat/light/electricity).

   3 prakaar (source of energy ke hisaab se):
   $$ (a) THERMAL decomposition (heat se):
   $$     CaCO3 --(heat)--> CaO + CO2   (cement industry, very important)
   $$     2FeSO4 --(heat)--> Fe2O3 + SO2 + SO3
   $$        (green crystal -> brown; sulphur ki badboo)
   $$     2Pb(NO3)2 --(heat)--> 2PbO + 4NO2 + O2  (bhure/brown fumes - NO2)

   $$ (b) ELECTROLYTIC decomposition (electricity se):
   $$     2H2O --(electricity)--> 2H2 + O2   (water ka electrolysis)

   $$ (c) PHOTOLYTIC / photochemical (light/sunlight se):
   $$     2AgCl --(sunlight)--> 2Ag + Cl2   (white -> grey)
   $$     2AgBr --(sunlight)--> 2Ag + Br2   (photography me use)

   @@ Yaad rakho: zyada-tar decomposition reactions ENDOTHERMIC hoti hain
   @@ (energy lagti hai), jabki combination aksar EXOTHERMIC hoti hain.

4.3 DISPLACEMENT REACTION (Visthapan)
---------------------------------------------------------
$$ Zyada reactive element, kam reactive element ko uske compound se
$$ HATA (displace) deta hai. (A + BC -> AC + B)

   Examples:
   $$ Fe + CuSO4 -> FeSO4 + Cu
   $$    (CuSO4 ka neela rang halka hara ho jaata; Fe zyada reactive hai)
      Zn + CuSO4 -> ZnSO4 + Cu
      Zn + 2HCl -> ZnCl2 + H2    (gas ke bubble)

   @@ Reactivity series (zyada se kam reactive): K > Na > Ca > Mg > Al >
   @@ Zn > Fe > Pb > (H) > Cu > Ag > Au. Upar wala neeche wale ko displace karta.

4.4 DOUBLE DISPLACEMENT REACTION (Dohra Visthapan)
---------------------------------------------------------
$$ Do compounds apne ions/parts AAPAS ME exchange karte hain.
$$ (AB + CD -> AD + CB). Aksar precipitate (ppt) banta hai.

   Examples:
   $$ Na2SO4 + BaCl2 -> BaSO4(down) + 2NaCl
   $$    (BaSO4 = safed precipitate; ye PRECIPITATION reaction hai)
      AgNO3 + NaCl -> AgCl(down) + NaNO3   (white ppt)

   $$ NEUTRALISATION bhi double displacement hai:
   $$    NaOH + HCl -> NaCl + H2O   (acid + base -> salt + water)

4.5 OXIDATION, REDUCTION aur REDOX
---------------------------------------------------------
$$ OXIDATION = Oxygen GAIN ya Hydrogen LOSS (oxygen judna).
$$ REDUCTION = Oxygen LOSS ya Hydrogen GAIN (oxygen hatna).
$$ REDOX = jisme oxidation aur reduction DONO ek saath hote hain.

   Example:  CuO + H2 --(heat)--> Cu + H2O
   $$   - CuO ne oxygen khoya  => CuO ka REDUCTION (Cu bana)
   $$   - H2 ne oxygen paaya   => H2 ka OXIDATION (H2O bana)
        - Oxidising agent = CuO (jo oxygen deta), Reducing agent = H2.

   Aur example: ZnO + C -> Zn + CO   (C oxidise, ZnO reduce)
                MnO2 + 4HCl -> MnCl2 + Cl2 + 2H2O

   @@ Trick yaad rakho - "OIL RIG":
   @@ Oxidation Is Loss (of electrons), Reduction Is Gain (of electrons).
   @@ (Class 10 level par mostly oxygen/hydrogen wali definition kaafi hai.)

4.6 EXOTHERMIC aur ENDOTHERMIC REACTION
---------------------------------------------------------
$$ EXOTHERMIC = energy/heat NIKALTI hai (aas-paas garam ho jaata).
$$    - Respiration (shwasan): C6H12O6 + 6O2 -> 6CO2 + 6H2O + energy
$$    - Natural gas/coal jalna; CaO + H2O -> Ca(OH)2 + heat
$$    - Sadte hue vegetable matter se compost banna.
$$ ENDOTHERMIC = energy/heat SOSHIT hoti hai (aas-paas thanda).
$$    - Zyadatar decomposition reactions (CaCO3 ko todna, water electrolysis).

<<<PAGEBREAK>>>

5. OXIDATION KE DAILY-LIFE EFFECTS
=========================================================

5.1 CORROSION (Karan / Zang lagna)
---------------------------------------------------------
$$ Metal ka apni surface par hawa, nami (moisture), acid se dheere-dheere
$$ kharaab hona = corrosion.
   - Iron par RUST: reddish-brown (Fe2O3.xH2O). Rust ke liye HAWA + PAANI
     dono chahiye.
   $$ Silver par kaali parat (Ag2S - hydrogen sulphide se).
   $$ Copper par hari parat (basic copper carbonate).

   @@ ROKNE KE TARIKE (exam me "how to prevent corrosion" puchte hain):
   @@   Painting, oiling/greasing, galvanisation (zinc ki parat),
   @@   chrome plating, anodising, alloy banana (jaise stainless steel).
   - Galvanisation = iron par zinc ki layer chadhana - rust se bachata hai.

5.2 RANCIDITY (Baasipan)
---------------------------------------------------------
$$ Tel/ghee/fatty food ka hawa (oxygen) se oxidise ho ke badboo aur kharaab
$$ swaad dena = rancidity. (Chips/namkeen ke purane hone par smell badalna.)

   $$ ROKNE KE TARIKE:
   $$   - Antioxidants milana (oxidation rokte hain).
   $$   - Air-tight container me rakhna.
   $$   - Fridge me rakhna (thanda).
   $$   - Chips packet me NITROGEN gas bharna (oxygen hata ke).

<<<PAGEBREAK>>>

6. SOLVED EXAMPLES (HARDEST -> EASIEST)
=========================================================
$$ Ye type ke numerical/identify questions exam me pakka aate hain. Steps
$$ ko dhyan se follow karo - khud likh ke practice karo.

EXAMPLE 1 (Hardest): Balance karo aur type batao -
   Fe + H2O -> Fe3O4 + H2
   Step 1: Fe count - right 3 => 3Fe left.
   Step 2: O count - right 4 => 4H2O left.
   Step 3: H count - left 4x2=8 => right 4H2 (8 H).
   ANSWER: 3Fe + 4H2O -> Fe3O4 + 4H2  (check: Fe=3, O=4, H=8 both sides)
   Type: Displacement (Fe ne H ko paani se displace kiya).

EXAMPLE 2: Pb(NO3)2 ko garam karne par bhure dhuein (brown fumes) nikle.
   Equation likho, balance karo, type batao.
   Skeleton: Pb(NO3)2 --(heat)--> PbO + NO2 + O2
   Balance: 2Pb(NO3)2 --(heat)--> 2PbO + 4NO2 + O2
   (check: Pb=2, N=4, O: left 2x6=12; right 2+8+2=12)
   Type: Thermal Decomposition. Brown fumes = NO2.

EXAMPLE 3: In reaction me oxidise aur reduce kya hua?
   3MnO2 + 4Al -> 3Mn + 2Al2O3
   - Al ne oxygen paaya  => Al OXIDISED (reducing agent).
   - MnO2 ne oxygen khoya => MnO2 REDUCED (oxidising agent).
   Type: Redox + Displacement (Al ne Mn ko displace kiya).

EXAMPLE 4: Balance karo - KNO3 -> KNO2 + O2
   O check: left 3, right 2+2=4. LCM(3,4)... seedha:
   2KNO3 -> 2KNO2 + O2  (K=2, N=2, O: left 6; right 4+2=6)
   Type: Thermal Decomposition.

EXAMPLE 5: Na2SO4(aq) + BaCl2(aq) -> ?  Type aur product batao.
   Ions exchange: Na<->Ba, SO4<->Cl.
   Na2SO4 + BaCl2 -> BaSO4(down) + 2NaCl
   BaSO4 = safed precipitate. Type: Double displacement (precipitation).

EXAMPLE 6: Zinc ko tanu (dilute) HCl me daala - gas bubble nikle. Equation?
   Zn + 2HCl -> ZnCl2 + H2(up)
   Type: Displacement. Gas = Hydrogen (jalti tili "pop" awaaz karti).

EXAMPLE 7 (Easiest): Word equation ko balanced symbol equation me badlo -
   "Hydrogen + Chlorine -> Hydrogen chloride"
   H2 + Cl2 -> 2HCl   (H=2, Cl=2 both sides). Type: Combination.

<<<PAGEBREAK>>>

7. QUICK Q&A - PADHNE KE BAAD KHUD CHECK KARO
=========================================================
$$ Pehle khud answer socho, fir niche milao. Ye board-style questions hain.

Q1. Balanced chemical equation kyun zaroori hai?
A1. Kyunki Law of Conservation of Mass ke according reaction me mass na
    banti na nasht hoti; dono side atom barabar hone chahiye.

Q2. Combination aur Decomposition reaction me kya farak hai? (1 example each)
A2. Combination: 2+ cheez mil ke 1 banti (CaO + H2O -> Ca(OH)2).
    Decomposition: 1 cheez tut ke 2+ banti (CaCO3 --heat--> CaO + CO2).

Q3. Decomposition ke 3 types kaunse hain (energy ke hisaab se)?
A3. Thermal (heat), Electrolytic (electricity), Photolytic (light/sunlight).

Q4. CuO + H2 -> Cu + H2O me oxidise aur reduce kya hua?
A4. H2 oxidise hua (H2O bana), CuO reduce hua (Cu bana). Ye redox hai.

Q5. Silver chloride ko brown/dark bottle me kyun rakhte hain?
A5. Kyunki 2AgCl --sunlight--> 2Ag + Cl2 (photolytic decomposition) ho jaata,
    light se white AgCl grey ho jaata hai. Isliye light se bachate hain.

Q6. Rancidity ko rokne ke 2 tarike batao.
A6. Antioxidants milana; air-tight container/fridge; chips packet me
    nitrogen gas bharna (oxygen hatana).

Q7. Galvanisation kya hai?
A7. Iron par zinc ki parat chadhana taaki rust (corrosion) na lage.

Q8. Ek exothermic aur ek endothermic reaction ka example do.
A8. Exothermic: respiration / CaO + H2O. Endothermic: water ka electrolysis
    ya CaCO3 ka decomposition.

Q9. Reaction hua hai ya nahi - kaise pata chalega? (koi 3 sign)
A9. Colour change, gas/effervescence banna, temperature change, precipitate
    banna, ya state/smell change.

Q10. Fe + CuSO4 reaction kis type ka hai aur kya observe hota hai?
A10. Displacement. CuSO4 ka neela rang halka hara ho jaata aur laal-bhura
     copper jam jaata (Fe zyada reactive isliye Cu ko displace karta).

=========================================================
EXAM STRATEGY (1 minute revision):
$$  - Balancing + reaction type identify karna = sure-shot marks.
$$  - Har type ka 1 balanced example ratlo.
$$  - Corrosion prevention + rancidity prevention ke points likhna aata ho.
$$  - Decomposition ke colour change wale examples (FeSO4, Pb(NO3)2, AgCl) yaad.
@@  - CORE BASICS page bhool gaye to wapas pehle padho - base strong rakho.
=========================================================
Generated by Kiro for Krishna1k - All the best!
"""


def to_markdown(content: str) -> str:
    """Convert the markup CONTENT into GitHub-friendly markdown."""
    out = ["# Chemical Reactions and Equations",
           "### NCERT Class 10 Science - Chapter 1 (Hinglish Detailed Notes)",
           "",
           "> Colour key: 🔴 = Core Basics / extra help &nbsp;|&nbsp; "
           "🟢 = comes often in board exams",
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
            emoji = "🔴" if marker == "@@" else "🟢"
            out.append(f"{indent}{emoji}{rest}")
            continue
        if pdf_utils._is_header(line.strip()):
            out.append(f"\n## {line.strip().title()}\n")
            continue
        out.append(line)
    return "\n".join(out) + "\n"


def main():
    here = Path(__file__).parent
    pdf_path = here / "Science_Class10_Ch1_Chemical_Reactions.pdf"
    md_path = here / "Science_Class10_Ch1_Chemical_Reactions.md"

    pdf_utils.text_to_pdf(
        CONTENT,
        pdf_path,
        title="Chemical Reactions and Equations",
        subtitle="NCERT Class 10 Science - Ch 1 | Hinglish Detailed Notes",
    )
    md_path.write_text(to_markdown(CONTENT), encoding="utf-8")
    print(f"Wrote {md_path}")


if __name__ == "__main__":
    main()
