"""
Build the Class 10 Science Chapter 2 study PDF:
    "Acids, Bases and Salts"

Content in Hinglish. Uses pdf_utils markup:
    @@ -> RED  (Core Basics / prerequisite, Class 7-8-9)
    $$ -> GREEN (board exam me baar-baar aata hai)
    ## -> bold header
Run:  python3 build_ch2_science.py
"""

from pdf_utils import build_pdf

CONTENT = r"""
==========================================

@@PART A - CORE BASICS (MISS MAT KARNA)
@@Class 7-8-9 ki yeh cheezein pehle pakki karo, warna Ch2 samajh nahi aayega.
@@(Yeh pura RED page hai - revision ke time sabse pehle ise dekho.)

## 1. Acid aur Base - Class 7 wali pehchaan

@@Acid = khatte (sour) swaad wale padarth. Jaise: nimbu, imli, sirka (vinegar),
@@   dahi. "Acid" Latin shabd 'acidus' = khatta se aaya hai.
@@Base = kadwe (bitter) swaad wale aur chhoone par CHIKNE (soapy) lagte hain.
@@   Jaise: baking soda, sabun, chuna paani.
@@Indicator = woh padarth jo acid/base me rang badal kar batata hai.
@@   Natural indicator: Litmus (lichen se banta), Haldi, China rose (gudhal).

## 2. Litmus ka rule (sabse base concept)

@@Litmus do colour me aata: BLUE litmus aur RED litmus.
@@   Acid -> BLUE litmus ko RED kar deta hai.
@@   Base -> RED litmus ko BLUE kar deta hai.
@@Yaad rakho: "Acid me Blue Roye (B->R), Base me Red Blue ho jaaye (R->B)".
@@Neutral (jaise distilled water) kisi litmus ka rang nahi badalta.

## 3. Atom, Ion, Molecule (Class 8-9 base)

@@Atom = sabse chhota kann. Ion = charge wala atom/group.
@@   Cation = +ve charge (electron khoya). Anion = -ve charge (electron mila).
@@   H+ (hydrogen ion), OH- (hydroxide ion), Cl-, Na+, SO4 2-, CO3 2-.
@@Molecule = atoms ka group jud kar bana. HCl, H2O, NaOH.
@@Compound = do ya zyada alag elements chemically jude.

## 4. Common Formula yaad rakho (ratta zone)

@@Acids: HCl (hydrochloric), H2SO4 (sulphuric), HNO3 (nitric),
@@   H2CO3 (carbonic), CH3COOH (acetic - sirke me).
@@Bases: NaOH (sodium hydroxide), KOH (potassium hydroxide),
@@   Ca(OH)2 (calcium hydroxide - chuna), NH4OH (ammonium hydroxide).
@@Salts: NaCl (common salt), Na2CO3 (washing soda), NaHCO3 (baking soda),
@@   CaCO3 (limestone/marble), CuSO4 (copper sulphate).

## 5. Reaction ki bhasha (Class 9 revision)

@@Reactant (arrow ke baayi taraf) ----> Product (arrow ke daayi taraf).
@@States: (s)=solid, (l)=liquid, (g)=gas, (aq)=aqueous (paani me ghula).
@@Equation hamesha BALANCE honi chahiye (dono taraf atom barabar).
@@Effervescence = bubbles/jhaag nikalna (gas banne ki nishani).

## 6. Concentrated vs Dilute aur ek SAFETY rule

@@Concentrated = paani kam, acid/base zyada (strong/khatarnak).
@@Dilute = paani zyada daal kar patla kiya hua.
@@SAFETY (bahut important): "Acid ko paani me daalo, paani ko acid me NAHI".
@@   Kyunki paani+acid milte waqt bahut garmi nikalti, acid me paani daalo to
@@   chhinta ud kar jala sakta hai.

@@-- END OF CORE BASICS (RED) PAGE --

<<<PAGEBREAK>>>

==========================================

## PART B - CHAPTER KA MAIN CONTENT
## Class 10 Science | Ch 2: Acids, Bases and Salts

$$[GREEN = board exam me baar-baar poocha jaata hai]

## 1. Indicators (Suchak) - poora list

Indicator acid/base ki maujoodgi batata hai (rang/smell badal kar).
$$Types:
$$   (1) Natural: Litmus (purple/blue/red), Haldi (turmeric), China rose.
$$   (2) Synthetic: Methyl orange, Phenolphthalein.
$$   (3) Olfactory indicator: SMELL se batata (jaise pyaaz, vanilla, laung).
$$       Base me inki smell chali jaati, acid me bani rehti.

$$Indicator colour table (RATTA - exam me direct aata):
   Indicator        | Acid me        | Base me
   -----------------|----------------|----------------
$$   Blue litmus      | Red ho jaata   | Blue hi rehta
$$   Red litmus       | Red hi rehta   | Blue ho jaata
$$   Methyl orange    | Red / Pink     | Yellow
$$   Phenolphthalein  | Colourless     | Pink
$$   Haldi (turmeric) | Yellow hi      | Reddish-brown

## 2. Acids/Bases ke Chemical Properties [TOP EXAM AREA]

## (A) Metal ke saath reaction

$$Acid + Metal ----> Salt + Hydrogen gas (H2)
$$   2HCl + Zn ----> ZnCl2 + H2 (gas)
$$Test of H2 gas: jalti hui teeli (candle) paas le jaao to "POP" sound aati.
$$Base + Metal (kuch active metals) ----> Salt + Hydrogen gas
$$   2NaOH + Zn ----> Na2ZnO2 (sodium zincate) + H2

## (B) Metal carbonate / bicarbonate ke saath

$$Acid + Metal Carbonate ----> Salt + CO2 + H2O
$$Acid + Metal Bicarbonate ----> Salt + CO2 + H2O
$$   2HCl + Na2CO3 ----> 2NaCl + H2O + CO2
$$   HCl + NaHCO3 ----> NaCl + H2O + CO2
$$CO2 test: CO2 ko chuna paani (lime water) me se nikalo to woh DOODHIYA
$$   (milky) ho jaata. Ca(OH)2 + CO2 ----> CaCO3 (white) + H2O.
$$   Zyada CO2 daalo to milkiness gayab (CaCO3 + CO2 + H2O -> Ca(HCO3)2).

## (C) Acid + Base = NEUTRALISATION [VERY IMPORTANT]

$$Acid + Base ----> Salt + Water  (yeh NEUTRALISATION reaction hai)
$$   NaOH + HCl ----> NaCl + H2O
$$Iska asli khel: H+ (acid se) + OH- (base se) ----> H2O.

## (D) Metal oxide aur Non-metal oxide

$$Acid + Metal oxide ----> Salt + Water (Metal oxides BASIC hote hain)
$$   2HCl + CuO ----> CuCl2 (blue-green) + H2O
$$Base + Non-metal oxide ----> Salt + Water (Non-metal oxides ACIDIC hote hain)
$$   2NaOH + CO2 ----> Na2CO3 + H2O
$$Conclusion: Metal oxide = basic ; Non-metal oxide = acidic.

## 3. Acid/Base me aisa kya common hai? [VERY IMPORTANT]

$$Saare acids me H+ (hydrogen) ion COMMON hota hai.
$$Saare bases me OH- (hydroxide) ion COMMON hota hai.
$$Acid paani me ghulkar H+ (asal me H3O+, hydronium) deta hai.
$$   HCl + H2O ----> H3O+ + Cl-
$$IMPORTANT: Acid sirf PAANI ki maujoodgi me hi H+ deta hai (ionise hota).
$$   Isiliye DRY HCl gas, dry blue litmus ka rang NAHI badalti.
$$Base jo paani me ghulta hai use ALKALI kehte hain (NaOH, KOH).

## 4. Acid/Base ko paani me ghol-na (Dilution)

$$Acid ya base ko paani me ghol-ne par H+/OH- ki concentration GHAT-ti hai.
$$Yeh process EXOTHERMIC hai (garmi nikalti).
$$SAFETY: "Hamesha acid ko paani me daalo (slowly + stir), ulta KABHI nahi" -
$$   warna achaanak bahut garmi se chhinta ud sakta hai (acid splash).

## 5. Strength: pH Scale [SABSE IMPORTANT TOPIC]

$$pH = "potenz of Hydrogen" - H+ ion ki concentration naapne ka scale.
$$Scale 0 se 14 tak:
$$   pH = 7  -> Neutral (jaise pure/distilled water)
$$   pH < 7  -> Acidic (jitna kam, utna strong acid). 0 = strongest acid.
$$   pH > 7  -> Basic / Alkaline (jitna zyada, utna strong base). 14 = strongest base.
$$Universal indicator: alag-alag pH par alag rang deta (poora range).

$$Strong vs Weak:
$$   Strong acid (HCl, H2SO4, HNO3) -> paani me PURA ionise (zyada H+).
$$   Weak acid (CH3COOH, H2CO3) -> THODA ionise (kam H+).
$$   Strong base (NaOH, KOH) ; Weak base (NH4OH, Mg(OH)2).

$$pH daily life me (board favourite):
$$   Body/blood pH ~ 7.4 (bahut narrow range me rehna chahiye).
$$   Acid rain pH < 5.6 -> nadiyon ka pH girta -> jal-jeevan ko nuksaan.
$$   Mitti (soil) ka pH theek hona zaroori - acidic mitti me chuna daalte.
$$   Pet (stomach) me HCl -> jyada ho to acidity -> ANTACID (base jaise
$$      Milk of Magnesia / Mg(OH)2) lete hain neutralise karne ko.
$$   Daant (teeth): muh ka pH 5.5 se neeche jaaye to enamel ghisne lagta;
$$      bacteria sugar se acid banate -> isliye base wala toothpaste use karo.
$$   Bee/cheenti ka doonk -> methanoic (formic) acid -> baking soda (base) lagao.
$$   Nettle plant doonk -> formic acid -> dock plant patta (base) ragdo.

## 6. SALTS [BADA AUR SCORING TOPIC]

Salt = acid aur base ke neutralisation se banta padarth.

$$pH of salts (kis acid+base se bana, us par depend):
$$   Strong acid + Strong base -> NEUTRAL salt (pH = 7). Eg: NaCl.
$$   Strong acid + Weak base   -> ACIDIC salt (pH < 7). Eg: NH4Cl.
$$   Weak acid + Strong base   -> BASIC salt (pH > 7). Eg: Na2CO3, CH3COONa.

## 7. Important Salts (har ek board me aata) [VERY IMPORTANT]

$$(A) Common Salt - NaCl
$$   Samudra ke paani + rock salt se. Yeh kayi cheezon ka "raw material" hai.

$$(B) Sodium Hydroxide - NaOH (CHLOR-ALKALI process)
$$   NaCl ke paani (brine) me bijli (electrolysis) chalate hain:
$$   2NaCl + 2H2O --electricity--> 2NaOH + Cl2 (gas) + H2 (gas)
$$   3 product 3 jagah use: NaOH (soap), Cl2 (bleaching/PVC), H2 (fuel).
$$   Cathode par H2, Anode par Cl2, solution me NaOH banta.

$$(C) Bleaching Powder - CaOCl2 (Calcium oxychloride)
$$   Slaked lime par Cl2 gas paas karke banta:
$$   Ca(OH)2 + Cl2 ----> CaOCl2 + H2O
$$   Use: kapde/paani bleach + disinfect, peene ke paani ko saaf karna.

$$(D) Baking Soda - NaHCO3 (Sodium hydrogen carbonate / bicarbonate)
$$   Banta: NaCl + H2O + CO2 + NH3 ----> NH4Cl + NaHCO3
$$   Garam karne par: 2NaHCO3 --heat--> Na2CO3 + H2O + CO2
$$   Use: baking (cake fulaata - CO2 nikalta), antacid (pet ki acidity),
$$      soda-acid fire extinguisher, baking powder ka hissa.
$$   Baking powder = baking soda + ek mild edible acid (jaise tartaric acid).
$$      Tartaric acid CO2 ke saath bani Na2CO3 ko neutralise karta (kadwa nahi lagta).

$$(E) Washing Soda - Na2CO3.10H2O (sodium carbonate decahydrate)
$$   Baking soda se: Na2CO3 + 10H2O ----> Na2CO3.10H2O (recrystallise karke).
$$   Use: ghar ki safai, kaanch/sabun banana, paani ki "permanent hardness" hatana.

## 8. Water of Crystallisation aur Plaster of Paris [IMPORTANT]

$$Water of crystallisation = salt ke crystal me FIXED maatra me juda paani.
$$   Eg: CuSO4.5H2O (blue vitriol) me 5 water; Na2CO3.10H2O me 10; CaSO4.2H2O (gypsum).
$$   Blue CuSO4.5H2O ko garam karo -> safed ho jaata (paani udd jaata),
$$      phir paani daalo -> wapas neela (water of crystallisation wapas).

$$Plaster of Paris (POP) = CaSO4.(1/2)H2O (calcium sulphate hemihydrate).
$$   Gypsum (CaSO4.2H2O) ko 373K (100 C) tak garam karke banta:
$$   CaSO4.2H2O --heat 373K--> CaSO4.(1/2)H2O + (3/2)H2O
$$   POP + paani -> wapas gypsum ban kar SAKHT (set) ho jaata (hardening).
$$   Use: tooti haddi ka plaster (doctor), murti/khilone, deewar smooth karna.
$$   NOTE: POP ko nami se door (airtight) rakho, warna set ho jaayega.

## 9. Quick Revision - One Liners

   - Acid: H+ deta, blue litmus red, pH < 7.
   - Base/Alkali: OH- deta, red litmus blue, pH > 7.
   - Neutralisation: Acid + Base -> Salt + Water.
   - Acid + metal -> salt + H2 (pop test).
   - Acid + carbonate -> salt + CO2 + water (lime water milky).

<<<PAGEBREAK>>>

==========================================

## PART C - SOLVED EXAMPLES (HARDEST -> EASIEST)
## Step-by-step. Pehle mushkil, taaki baad me sab aasaan lage.

## Example 1 (HARDEST) - Chlor-alkali + saare products ka use

Q: NaCl ke jaleeya (aqueous) ghol me bijli chalane par kya banta hai? Equation,
   electrode par kahan kya, aur teeno products ke use likho.

   Solution:
   Reaction: 2NaCl + 2H2O --electricity--> 2NaOH + Cl2 + H2
   - Anode (+) par: Cl2 gas nikalti.
   - Cathode (-) par: H2 gas nikalti.
   - Solution me: NaOH (sodium hydroxide) bachta.
   Uses: NaOH -> soap/detergent, paper. Cl2 -> water treatment, PVC, bleaching
         powder. H2 -> fuel, margarine, ammonia banana.
   Iska naam Chlor-alkali process (Chlor = Cl2, alkali = NaOH).

## Example 2 - Water of crystallisation wala observation

Q: Blue CuSO4 crystal ko garam karne par kya hota? Wapas paani daalo to?

   Solution:
   - Garam karne par paani (water of crystallisation) udd jaata -> crystal SAFED.
     CuSO4.5H2O --heat--> CuSO4 (white) + 5H2O
   - Thande hone par paani ki kuch boondein daalo -> wapas NEELA ho jaata,
     kyunki water of crystallisation wapas jud jaata.
   Seekh: rang neela isi 5 water of crystallisation ki wajah se hai.

## Example 3 - POP banana + ek hi cheez do roop

Q: Plaster of Paris kaise banta? Formula? POP set kyun ho jaata hai?

   Solution:
   - Gypsum (CaSO4.2H2O) ko ~373K tak garam karo:
     CaSO4.2H2O --heat--> CaSO4.(1/2)H2O + (3/2)H2O   [yeh POP hai]
   - POP me paani milao to wapas gypsum (CaSO4.2H2O) ban jaata aur sakht
     (hard) ho jaata -> isliye haddi/murti ke liye use hota.

## Example 4 - Antacid kaam kaise karta (neutralisation)

Q: Pet me acidity (jyada HCl) hone par antacid kaise rahat deta hai?

   Solution:
   - Antacid ek MILD base hota (jaise Milk of Magnesia = Mg(OH)2).
   - Base, extra HCl ko neutralise kar deta -> Salt + Water banta -> jalan kam.
     Mg(OH)2 + 2HCl ----> MgCl2 + 2H2O
   - Yeh neutralisation reaction ka daily-life example hai.

## Example 5 (EASIEST) - Litmus + ek simple equation

Q: (a) HCl blue litmus ka rang kya karega? (b) Zn + HCl ka product?

   Solution:
   (a) HCl ek acid hai -> Blue litmus ko RED kar dega.
   (b) Zn + 2HCl ----> ZnCl2 + H2 (gas). Gas jalane par "pop" sound deti.

<<<PAGEBREAK>>>

==========================================

## PART D - SELF TEST (EASY -> HARD)
## Khud likho, phir niche answer hint se check karo. Active recall = best memory.

## EASY (1 mark)

   Q1. Acid aur base ko litmus se kaise pehchaante hain?
   Q2. pH = 7, pH < 7, pH > 7 ka matlab batao.
   Q3. Neutralisation reaction ki definition + general equation.
   Q4. Baking soda aur washing soda ke chemical formula likho.

## MEDIUM (2-3 marks)

   Q5. Acid ke metal carbonate ke saath reaction ka general + 1 example.
       CO2 ko kaise test karoge?
   Q6. Olfactory indicator kya hai? 2 example.
   Q7. "Acid ko paani me daalo, paani ko acid me nahi" - kyun? Samjhao.
   Q8. Strong acid aur weak acid me 1 difference + 1-1 example.

## HARD (3-5 marks, board favourite)

   Q9. Chlor-alkali process: equation, electrode products aur teeno ka use.
   Q10. Plaster of Paris: formula, banane ki vidhi (equation), 2 use, ek
        savdhani (storage).
   Q11. pH ka daily life me mahatva: (a) dant (b) pet (c) acid rain
        (d) cheenti/bee doonk - har ek explain karo.
   Q12. Water of crystallisation kya hai? CuSO4.5H2O ko garam karne aur phir
        paani daalne par kya hota - equation sahit.

==========================================

## ANSWER HINTS (PART D)

   A1. Acid: blue litmus -> red. Base: red litmus -> blue.
   A2. 7 = neutral; <7 = acidic; >7 = basic/alkaline.
   A3. Acid + Base -> Salt + Water (eg NaOH + HCl -> NaCl + H2O).
   A4. Baking soda = NaHCO3 ; Washing soda = Na2CO3.10H2O.
   A5. Acid + carbonate -> salt + CO2 + H2O (2HCl+Na2CO3->2NaCl+H2O+CO2);
       CO2 lime water ko doodhiya kar deta.
   A6. Smell se acid/base batane wala (pyaaz, vanilla, laung).
   A7. Dilution exothermic hai; acid me paani daalo to garmi+chhinta -> jal sakte.
   A8. Strong (HCl) pura ionise; Weak (CH3COOH) thoda ionise.
   A9. 2NaCl+2H2O--elec-->2NaOH+Cl2+H2; anode Cl2, cathode H2, soln NaOH;
       uses soap/bleach/fuel.
   A10. CaSO4.(1/2)H2O; gypsum 373K garam; haddi plaster + murti; nami se door.
   A11. Dant: pH<5.5 enamel ghise; Pet: HCl jyada=acidity, antacid; acid rain
        pH<5.6 jal-jeevan nuksaan; doonk formic acid, base(baking soda) lagao.
   A12. Crystal me juda fixed paani; CuSO4.5H2O garam->white(+5H2O), paani
        daalo->wapas blue.

==========================================
## "Padhai tabhi pakki jab khud likh ke test do." - All the best, Krishna!
## Generated by Kiro for Krishna1k
==========================================
"""

if __name__ == "__main__":
    build_pdf(
        CONTENT,
        "Science_Class10_Ch2_Acids_Bases_Salts.pdf",
        title="Class 10 Science - Chapter 2",
        subtitle="Acids, Bases and Salts (Hinglish Notes)",
    )
