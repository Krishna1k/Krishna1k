"""
science_ch4.py
--------------
Generates a detailed, simplified Hinglish study guide for
NCERT Class 10 Science, Chapter 4: "Carbon and its Compounds".

Outputs:
  - Science_Class10_Ch4_Carbon_Compounds.pdf  (colour PDF)
  - Science_Class10_Ch4_Carbon_Compounds.md   (markdown, red/green via emoji)

Markup conventions inside CONTENT (handled by pdf_utils):
  @@  -> RED   line  (CORE BASICS / extra ke liye)
  $$  -> GREEN line  (exam me baar-baar aane wale topics)
  <<<PAGEBREAK>>>     -> nayi page
"""

import re
from pathlib import Path

import pdf_utils


CONTENT = r"""CARBON AND ITS COMPOUNDS
NCERT Class 10 Science - Chapter 4 (Hinglish Detailed Notes)
=========================================================

@@ COLOUR CODE: RED = Core Basics / extra help (Class 7-8-9 wali cheezein jo yaad honi chahiye).
$$ COLOUR CODE: GREEN = Board exam me ye topics BAAR-BAAR aate hain - pakka yaad karo.
   Baaki normal black text = main chapter content (detail me, simple bhasha me).

<<<PAGEBREAK>>>

CORE BASICS - PEHLE YE PADHO (CLASS 7-8-9 KA FOUNDATION)
=========================================================
@@ Tune 7-8-9 nahi padhi - koi tension nahi. Ye page is chapter ki base hai.
@@ Ek baar achhe se padh le, fir poora chapter aasaani se samajh aayega.

@@ 1) IONIC vs COVALENT BOND (recap):
@@    - IONIC bond = ek atom electron CHHOD-ta, dusra LE leta (metal + non-metal).
@@      Opposite charge ke ion attract karte. e.g. NaCl.
@@    - COVALENT bond = dono atom electron SHARE karte (non-metal + non-metal).
@@      e.g. H2O, CH4. Is chapter me mostly COVALENT bond hi chalega.

@@ 2) CARBON KI VALENCY = 4 (sabse important base):
@@    - Carbon ka atomic number 6, electronic config = 2,4 (K shell 2, L shell 4).
@@    - Outer shell me 4 electron -> octet (8) pura karne ko 4 aur chahiye.
@@    - Isliye carbon ki valency 4 hai = TETRAVALENT (4 bond bana sakta).

@@ 3) ELEMENT, COMPOUND, MOLECULE:
@@    - ELEMENT = ek hi type ke atom (C, H, O).
@@    - COMPOUND = 2+ element chemically jude fixed ratio me (H2O, CO2).
@@    - MOLECULE = 2+ atom jude hue, padaarth ka chhota unit (O2, CH4).

@@ 4) HYDROCARBON kya hai:
@@    - Sirf CARBON aur HYDROGEN se bana compound = hydrocarbon (CH4, C2H6).
@@    - Petrol, diesel, CNG, LPG sab hydrocarbon hi hain (fuel).

@@ 5) SINGLE / DOUBLE / TRIPLE BOND ka matlab:
@@    - SINGLE bond = 1 electron pair share (C-C). DOUBLE = 2 pair (C=C).
@@      TRIPLE = 3 pair share (C tripletie C). Zyada bond = zyada reactive.

@@ 6) STRUCTURAL FORMULA idea:
@@    - Sirf C aur H ki ginti (CH4) = molecular formula.
@@    - Har bond ko line (-) se dikhana = STRUCTURAL formula (atom kaise jude).

@@ 7) COMBUSTION / OXIDATION ka matlab:
@@    - COMBUSTION = oxygen me jalna, heat + light deta (CH4 + O2 -> CO2 + H2O).
@@    - OXIDATION = oxygen add hona ya hydrogen hatna (alcohol -> acid banna).

@@ 8) ACID / ALCOHOL ka intuition:
@@    - ALCOHOL = jisme -OH group ho (sharab/spirit jaisa), e.g. C2H5OH.
@@    - ACID = khatta, litmus blue ko red kare; carboxylic acid me -COOH hota.

@@ 9) ISOMER ka matlab (intro):
@@    - Same molecular formula par alag STRUCTURE wale compounds = isomers.
@@      e.g. C4H10 ke do roop (seedhi chain aur branched chain).

@@ 10) CATALYST kya hai:
@@    - Woh padaarth jo reaction ki SPEED badha de par khud kharch na ho.
@@      e.g. hydrogenation me Nickel (Ni) catalyst.

<<<PAGEBREAK>>>

1. COVALENT BONDING - CARBON ELECTRON SHARE KYUN KARTA HAI
=========================================================
$$ Carbon ke outer shell me 4 electron hain. Octet (8) pura karne ke liye:
$$   - 4 electron CHHOD-na padega -> bahut energy chahiye (mushkil).
$$   - 4 electron LE-na padega -> 4 extra electron ko sambhalna mushkil.
$$ Isliye carbon na deta na leta - balki electron SHARE karta = COVALENT BOND.
$$ Electron share karne se dono atom apna octet pura kar lete hain.

1.1 COVALENT BOND ke examples (shared pairs)
---------------------------------------------------------
$$   - H2  : H-H        (1 pair share = single bond)
$$   - O2  : O=O        (2 pair share = double bond)
$$   - N2  : N triple N (3 pair share = triple bond)
$$   - H2O : H-O-H      (oxygen 2 H ke saath share karta)
$$   - NH3 : N ke saath 3 H (nitrogen ke 3 bond)
$$   - CH4 : C ke 4 bond, 4 H ke saath (methane)

1.2 COVALENT COMPOUNDS ke PROPERTIES (exam favourite list)
---------------------------------------------------------
$$   (i)   LOW melting point aur boiling point (weak inter-molecular force).
$$   (ii)  Mostly POOR conductor of electricity (koi free ion/electron nahi).
$$   (iii) Generally paani me kam ghulte, organic solvent me ghulte hain.
   @@ Reason: covalent molecule neutral hote, charge-wale ion nahi bante,
   @@ isliye current conduct nahi karte (ionic compounds ke ulta).

<<<PAGEBREAK>>>

2. VERSATILITY OF CARBON (itne saare compounds kyun?)
=========================================================
$$ Carbon ke LAKHON (millions) compounds hain. 3 main reason:
$$   (1) CATENATION = carbon ka khud-ke-saath lambi chain/ring banane ka gun.
$$       C-C-C-C... seedhi, branched ya ring me jud sakta (sabse zyada carbon me).
$$   (2) TETRAVALENCY = carbon ke 4 bond -> 4 alag atom ke saath jud sakta
$$       (H, O, N, S, halogen) -> bahut variety ke compounds.
$$   (3) CHHOTA SIZE = nucleus shared electron ko strongly pakadta -> bahut
$$       STRONG aur stable bond -> compounds tikau (stable) hote hain.
   @@ Isi wajah se carbon "living world" ka base hai (DNA, protein, etc).

<<<PAGEBREAK>>>

3. ALLOTROPES OF CARBON (ek hi element, alag roop)
=========================================================
   ALLOTROPE = same element ke alag-alag physical roop (alag structure).

3.1 DIAMOND
---------------------------------------------------------
   - Har carbon, 4 dusre carbon se juda -> rigid 3D structure.
   - Sabse HARD natural padaarth, high melting point.
   - Electricity conduct NAHI karta (koi free electron nahi).
   - Use: cutting/drilling tools, jewellery.

3.2 GRAPHITE
---------------------------------------------------------
   - Har carbon sirf 3 carbon se juda -> layers (parat) banti hain.
   - Layers ek dusre par slide karti -> SMOOTH/slippery (lubricant).
   - Electricity CONDUCT karta (har carbon ka 1 free electron hota).
   - Use: pencil "lead", electrode, lubricant.
   @@ Yaad rakho: diamond hard par insulator; graphite soft par conductor.

3.3 FULLERENE (C60)
---------------------------------------------------------
   - Carbon atoms football (buckyball) jaise gol structure me - C60 famous.
   - Naya allotrope, research/nanotech me use.

<<<PAGEBREAK>>>

4. SATURATED vs UNSATURATED HYDROCARBONS
=========================================================
$$ SATURATED = carbon ke beech sirf SINGLE bond (C-C). Inhe ALKANE kehte.
$$    - General formula: CnH2n+2  (e.g. CH4, C2H6, C3H8).
$$ UNSATURATED = beech me DOUBLE ya TRIPLE bond ho.
$$    - DOUBLE bond (C=C) wale = ALKENE,  formula CnH2n  (e.g. C2H4 ethene).
$$    - TRIPLE bond wale = ALKYNE,        formula CnH2n-2 (e.g. C2H2 ethyne).
$$ Unsaturated zyada REACTIVE hote (addition reaction dete hain).

4.1 CHAINS aur RINGS
---------------------------------------------------------
   - STRAIGHT chain: carbon ek line me jude (n-butane).
   - BRANCHED chain: beech wale carbon se shaakha nikle (isobutane).
   - RING (cyclic): carbon gol ring me jude.
     e.g. CYCLOHEXANE (C6H12 ring), BENZENE (C6H6 ring with alternate bonds).

<<<PAGEBREAK>>>

5. HOMOLOGOUS SERIES
=========================================================
$$ DEFINITION: Same general formula aur same functional group wale compounds ki
$$ series, jisme har agla member pichhle se ek -CH2- unit zyada ho.
$$ CHARACTERISTICS (exam me likhna aata chahiye):
$$   (i)   Sabhi members ka SAME general formula (e.g. alkane CnH2n+2).
$$   (ii)  Do lagatar members me -CH2- (yaani 14 u mass) ka farak.
$$   (iii) Same FUNCTIONAL GROUP -> milti-julti chemical properties.
$$   (iv)  Molecular mass badhne ke saath physical properties (M.P/B.P) GRADUAL
$$         (dheere-dheere) change hoti hain.
   Example (Alkane series): CH4 -> C2H6 -> C3H8 -> C4H10 (har baar +CH2).

<<<PAGEBREAK>>>

6. FUNCTIONAL GROUPS
=========================================================
$$ FUNCTIONAL GROUP = woh atom/group jo compound ko uski khaas property deta hai
$$ (hydrogen ya carbon ki jagah lagta hai). Yaad rakho:
$$   - HALOGEN  ( -Cl, -Br )         -> haloalkane (e.g. chloromethane CH3Cl).
$$   - ALCOHOL  ( -OH )              -> e.g. ethanol C2H5OH.
$$   - ALDEHYDE ( -CHO )            -> e.g. ethanal CH3CHO.
$$   - KETONE   ( -CO- beech me )    -> e.g. propanone CH3COCH3.
$$   - CARBOXYLIC ACID ( -COOH )    -> e.g. ethanoic acid CH3COOH.

<<<PAGEBREAK>>>

7. IUPAC NOMENCLATURE (naam rakhne ke rules)
=========================================================
$$ Naam = PREFIX + ROOT (carbon count) + SUFFIX (functional group).
$$ ROOT (carbon ki ginti): 1=Meth, 2=Eth, 3=Prop, 4=But, 5=Pent.
$$ SUFFIX/ending family ke hisaab se:
$$   - Alkane (single bond)        -> "-ane"   (methane CH4)
$$   - Alkene (double bond)        -> "-ene"   (ethene C2H4)
$$   - Alkyne (triple bond)        -> "-yne"   (ethyne C2H2)
$$   - Alcohol ( -OH )             -> "-ol"    (methanol CH3OH)
$$   - Aldehyde ( -CHO )           -> "-al"    (methanal HCHO)
$$   - Carboxylic acid ( -COOH )   -> "-oic acid" (methanoic acid HCOOH)
$$   - Ketone ( -CO- )             -> "-one"   (propanone CH3COCH3)
$$ Example 1-carbon family: methane / methanol / methanal / methanoic acid.
   @@ Trick: pehle carbon gino (root), fir functional group dekh ke suffix lagao.

<<<PAGEBREAK>>>

8. CHEMICAL PROPERTIES OF CARBON COMPOUNDS
=========================================================
$$ 4 important reactions exam me baar-baar: COMBUSTION, OXIDATION, ADDITION, SUBSTITUTION.

8.1 COMBUSTION (jalna)
---------------------------------------------------------
$$ Carbon compound O2 me jal kar CO2 + H2O + heat + light deta.
$$    CH4 + 2O2 -> CO2 + 2H2O + heat
$$    C2H5OH + 3O2 -> 2CO2 + 3H2O + heat
$$ - SATURATED hydrocarbon -> saaf NEELI (blue) flame (poora oxygen mile to).
$$ - UNSATURATED / kam oxygen -> kaali dhuaan wali PEELI (yellow) sooty flame.
   @@ Gas stove ki blue flame = clean burning; bartan kaala ho to oxygen kam.

8.2 OXIDATION
---------------------------------------------------------
$$ Alcohol ko OXIDISE karne par CARBOXYLIC ACID banta:
$$    C2H5OH --[alkaline KMnO4 + heat]--> CH3COOH
$$ - OXIDISING AGENT = alkaline KMnO4 ya acidified K2Cr2O7.
$$ - Ye agent oxygen dete hain, isliye "oxidising agent" kehte.

8.3 ADDITION REACTION (sirf UNSATURATED par)
---------------------------------------------------------
$$ Unsaturated hydrocarbon + H2 --[Ni/Pd catalyst]--> saturated hydrocarbon.
$$    (HYDROGENATION) e.g. ethene + H2 -> ethane.
$$ USE: vegetable oil (unsaturated, liquid) + H2 (Ni) -> VANASPATI GHEE (saturated, solid).
   @@ Isliye ise "hardening of oils" kehte hain - oil thos ban jaata.

8.4 SUBSTITUTION REACTION (sirf SATURATED par)
---------------------------------------------------------
$$ Saturated hydrocarbon ke H ki jagah dusra atom aa jaaye (sunlight me):
$$    CH4 + Cl2 --[sunlight]--> CH3Cl + HCl
$$ - Ek-ek karke H ki jagah Cl lagta jaata (chlorination).

<<<PAGEBREAK>>>

9. ETHANOL  (C2H5OH)
=========================================================
$$ PROPERTIES: rang-heen liquid, room temp par liquid, paani me poori tarah ghulta.
$$ Ye hi "alcohol" hai jo sharab (alcoholic drinks) me hota.

$$ 9.1 SODIUM ke saath reaction:
$$    2C2H5OH + 2Na -> 2C2H5ONa + H2 (gas)
$$    (sodium ethoxide + hydrogen gas nikalti) - alcohol ka test.

$$ 9.2 DEHYDRATION (paani hatna) - ethene banana:
$$    C2H5OH --[conc. H2SO4, 443K]--> C2H4 (ethene) + H2O
$$    conc. H2SO4 yahan dehydrating agent hai.

   USES: alcoholic drinks, solvent, medicines/tincture, fuel.
   @@ DENATURED ALCOHOL = ethanol me zaharili cheez (methanol) mila dete taaki
   @@ peene laayak na rahe (industry use ke liye, tax bachane).
   @@ HARMFUL EFFECTS: jyada peena liver kharab karta, judgement/health bigaadta,
   @@ pure methanol to andhapan/maut tak kar sakta - bahut khatarnaak.

<<<PAGEBREAK>>>

10. ETHANOIC ACID  (CH3COOH) - ACETIC ACID
=========================================================
$$ Sirka (VINEGAR) = ethanoic acid ka 5-8% paani wala ghol.
$$ GLACIAL ACETIC ACID = pure (almost 100%) ethanoic acid; thandi me jam jaata (ice jaisa).

$$ 10.1 NaOH (base) ke saath - neutralisation:
$$    CH3COOH + NaOH -> CH3COONa + H2O   (salt + water)

$$ 10.2 CARBONATE / BICARBONATE ke saath (CO2 nikalti - bubbles):
$$    2CH3COOH + Na2CO3 -> 2CH3COONa + H2O + CO2
$$    CH3COOH + NaHCO3 -> CH3COONa + H2O + CO2
$$    (Ye fizz/CO2 wala test acid pehchanne me kaam aata.)

$$ 10.3 ESTERIFICATION (sweet smell - exam favourite):
$$    CH3COOH + C2H5OH --[conc. H2SO4]--> CH3COOC2H5 + H2O
$$    (ester = ethyl ethanoate; meetha/fruity smell - perfume aur flavour me use.)

$$ 10.4 SAPONIFICATION (ester + base -> soap):
$$    Ester + NaOH -> alcohol + sodium salt of acid (SOAP).
$$    Ye reaction soap banane ka base hai.

<<<PAGEBREAK>>>

11. SOAPS & DETERGENTS
=========================================================
$$ SOAP MOLECULE ke 2 part hote:
$$   - HYDROPHILIC head (-COONa) = paani-pasand (ionic, water me ghulta).
$$   - HYDROPHOBIC tail (lambi carbon chain) = paani-se-door, oil/grease pasand.

$$ 11.1 MICELLE banna:
$$   Paani me soap ke molecule cluster banate -> tails andar (oil ki taraf),
$$   heads bahar (paani ki taraf). Is gol cluster ko MICELLE kehte.

$$ 11.2 CLEANSING ACTION (kaise saaf karta):
$$   Tail kapde ki GANDAGI/oil ko pakadta, head paani ki taraf rehta. Micelle
$$   me phans ke gandagi paani me ghul/uthkar nikal jaati -> kapda saaf.

$$ 11.3 HARD WATER ka problem (soap):
$$   Hard water me Ca/Mg salts hote. Soap inse react kar ke insoluble SCUM
$$   (chipchipa jhaag-rahit kachra) bana deta -> jhaag nahi banta, saboon barbaad.

$$ 11.4 DETERGENTS ka faida:
$$   Detergent hard water me bhi kaam karte (Ca/Mg ke saath scum nahi bante),
$$   isliye hard water me bhi achha jhaag/safai dete.
   @@ Soap = natural (vegetable/animal fat se); Detergent = synthetic.

<<<PAGEBREAK>>>

12. SOLVED EXAMPLES (HARDEST -> EASIEST)
=========================================================
$$ Ye type ke questions exam me pakka aate - steps khud likhke practice karo.

EXAMPLE 1 (Hardest): Esterification aur Saponification ki poori equation likho.
   ESTERIFICATION (acid + alcohol -> ester):
      CH3COOH + C2H5OH --[conc. H2SO4]--> CH3COOC2H5 + H2O
      (ethyl ethanoate ester banta - meetha smell.)
   SAPONIFICATION (ester ka base se ulta-toot-na -> soap):
      CH3COOC2H5 + NaOH -> CH3COONa + C2H5OH
      (CH3COONa = soap/sodium salt, alcohol wapas milta.)

EXAMPLE 2: C4H10 ke structural isomers banao/pehchaano.
   Molecular formula same (C4H10) par 2 structure:
   (a) n-BUTANE  : C-C-C-C  (seedhi straight chain).
   (b) ISO-BUTANE: beech wale carbon se ek CH3 branch (branched chain).
   Dono isomers hain - same formula, alag structure, alag properties.

EXAMPLE 3: Ethanol aur Ethanoic acid me farak kaise pehchaane (tests)?
   (i) LITMUS test: ethanoic acid blue litmus ko RED kar deta; ethanol nahi (neutral).
   (ii) NaHCO3 test: ethanoic acid + NaHCO3 -> CO2 ki FIZZ (bubbles); ethanol me
        koi fizz nahi. (Isse pakka pehchaan ho jaata.)

EXAMPLE 4: In reactions ka TYPE batao (combustion/oxidation/addition/substitution):
   (a) CH4 + 2O2 -> CO2 + 2H2O           => COMBUSTION
   (b) C2H4 + H2 --Ni--> C2H6            => ADDITION (hydrogenation)
   (c) CH4 + Cl2 --sunlight--> CH3Cl+HCl => SUBSTITUTION
   (d) C2H5OH --KMnO4--> CH3COOH         => OXIDATION

EXAMPLE 5: Vegetable oil ka hydrogenation - equation + use.
   Vegetable oil (unsaturated) + H2 --[Ni catalyst]--> Vanaspati ghee (saturated).
   Use: liquid oil ko thos ghee me badalne ke liye (hardening of oils).

EXAMPLE 6: Carbon itne saare compounds kyun banata hai?
   (i) CATENATION - carbon khud se lambi chain/ring banata.
   (ii) TETRAVALENCY - 4 bond, alag-alag atom ke saath jud sakta.
   (iii) Chhota size -> strong stable bond. Inhi se lakhon compounds.

EXAMPLE 7 (Easiest): Methane ke baad alkane series ka agla member + general formula?
   General formula alkane = CnH2n+2.  CH4 ke baad agla = C2H6 (ethane).
   (Har agla member +CH2 zyada hota - homologous series.)

<<<PAGEBREAK>>>

13. QUICK Q&A - PADHNE KE BAAD KHUD CHECK KARO
=========================================================
$$ Pehle khud answer socho, fir niche milao. Ye board-style questions hain.

Q1. Carbon ionic bond kyun nahi banata, covalent kyun?
A1. 4 electron dena/lena bahut mushkil (energy zyada), isliye carbon electron
    SHARE karta (covalent) aur octet pura karta.

Q2. Catenation kya hai?
A2. Carbon ka khud-ke-saath lambi chain/ring/branch banane ka gun - isi se
    bahut saare compounds bante.

Q3. Saturated aur unsaturated hydrocarbon me farak?
A3. Saturated = sirf single bond (alkane, CnH2n+2). Unsaturated = double/triple
    bond (alkene CnH2n / alkyne CnH2n-2), zyada reactive.

Q4. Homologous series ki koi 2 characteristics likho.
A4. (i) Same general formula + same functional group. (ii) Do members me -CH2-
    (14 u) ka farak aur gradual property change.

Q5. Saaf neeli flame aur peeli sooty flame me kya batati hai?
A5. Neeli flame = poora oxygen, clean combustion (saturated). Peeli/sooty =
    oxygen kam ya unsaturated - kaala dhua/carbon nikalta.

Q6. Ethanol ko sodium ke saath react karaao - product?
A6. 2C2H5OH + 2Na -> 2C2H5ONa + H2. Hydrogen gas nikalti (sodium ethoxide banta).

Q7. Esterification reaction me catalyst aur khaas pehchaan?
A7. Catalyst = conc. H2SO4. Pehchaan = ester ka meetha/fruity smell (perfume me use).

Q8. Soap hard water me theek se kaam kyun nahi karta?
A8. Hard water ke Ca/Mg salts soap se react kar insoluble SCUM banate -> jhaag
    nahi banta. Detergent hard water me bhi chalta.

Q9. Micelle kya hai?
A9. Paani me soap molecules ka gol cluster - tail andar (oil ki taraf), head
    bahar (paani ki taraf). Yahi gandagi ko ghol kar nikalta.

Q10. Glacial acetic acid kya hai?
A10. Pure (almost 100%) ethanoic acid - thandi me ice jaisa jam jaata isliye
     "glacial" kehte hain.

=========================================================
EXAM STRATEGY (1 minute revision):
$$  - Covalent bonding + catenation/tetravalency reasons - 3-3 line ratlo.
$$  - 4 reactions (combustion, oxidation, addition, substitution) + 1-1 equation.
$$  - Ethanol (Na, dehydration) aur Ethanoic acid (NaOH, carbonate, ester) ki reactions.
$$  - Homologous series + functional groups + IUPAC suffix table.
$$  - Soap micelle + cleansing action + hard water ka problem.
@@  - CORE BASICS page (valency 4, covalent vs ionic, isomer) bhool jaao to
@@    wapas pehle padho - base strong rakho.
=========================================================
Generated by Kiro for Krishna1k - All the best!
"""


def to_markdown(content: str) -> str:
    """Convert the markup CONTENT into GitHub-friendly markdown."""
    out = ["# Carbon and its Compounds",
           "### NCERT Class 10 Science - Chapter 4 (Hinglish Detailed Notes)",
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
    pdf_path = here / "Science_Class10_Ch4_Carbon_Compounds.pdf"
    md_path = here / "Science_Class10_Ch4_Carbon_Compounds.md"

    pdf_utils.text_to_pdf(
        CONTENT,
        pdf_path,
        title="Carbon and its Compounds",
        subtitle="NCERT Class 10 Science - Ch 4 | Hinglish Detailed Notes",
    )
    md_path.write_text(to_markdown(CONTENT), encoding="utf-8")
    print(f"Wrote {md_path}")


if __name__ == "__main__":
    main()
