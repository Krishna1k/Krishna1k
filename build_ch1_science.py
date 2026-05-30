"""
Build the Class 10 Science Chapter 1 study PDF:
    "Chemical Reactions and Equations"

Content in Hinglish. Uses pdf_utils markup:
    @@ -> RED  (Core Basics / prerequisite, Class 7-8-9)
    $$ -> GREEN (board exam me baar-baar aata hai)
    ## -> bold header
Run:  python3 build_ch1_science.py
"""

from pdf_utils import build_pdf

CONTENT = r"""
==========================================

@@PART A - CORE BASICS (MISS MAT KARNA)
@@Class 7-8-9 ki yeh cheezein pehle pakki karo, warna Ch1 samajh nahi aayega.
@@(Yeh pura RED page hai - revision ke time sabse pehle ise dekho.)

## 1. Atom, Element, Molecule, Compound

@@Atom = matter ka sabse chhota kann jo reaction me hissa leta hai.
@@Element = ek hi type ke atoms se bani cheez. Jaise: Hydrogen (H), Oxygen (O),
@@   Iron (Fe), Sodium (Na), Carbon (C).
@@Molecule = do ya zyada atoms jud kar bante hain. Jaise: O2, H2, N2.
@@Compound = do ya zyada ALAG elements chemically jud kar bante hain.
@@   Jaise: H2O (paani), CO2, NaCl (namak).
@@Yaad rakho: Mixture me cheezein sirf mili hoti hain (alag ki ja sakti),
@@   compound me chemically judi hoti hain (aasani se alag nahi hoti).

## 2. Symbols aur Common Valency (Ratta zaroori)

@@Symbol = element ka short naam. H, O, C, N, Na, Cl, Ca, Mg, Al, Zn, Cu, Fe, Ag.
@@Valency = combine karne ki capacity (kitne haath se dosti karta hai).
@@   H = 1, O = 2, Na = 1, Cl = 1, Ca = 2, Mg = 2, Al = 3, Zn = 2.
@@Common ions: OH- (hydroxide), CO3 2- (carbonate), SO4 2- (sulphate),
@@   NO3 - (nitrate), HCO3 - (bicarbonate).
@@Trick (formula banane ka): valency ko CROSS karke neeche likho.
@@   Na(1) aur SO4(2) -> Na2SO4.  Al(3) aur O(2) -> Al2O3.

## 3. Chemical Formula kaise banti hai

@@Formula batata hai kaunse atoms kitne hain. H2O = 2 Hydrogen + 1 Oxygen.
@@Subscript (chhota neeche number) = us atom ki ginti. H2 me '2' subscript hai.
@@Agar koi number nahi likha to samjho '1' hai (jaise H2O me O = 1).

## 4. Physical Change vs Chemical Change (Bahut important base)

@@Physical change: sirf roop/shape badalta hai, NAYA padarth nahi banta,
@@   aur wapas laaya ja sakta hai. Jaise: ice -> water, paper faadna.
@@Chemical change: NAYA padarth banta hai, aasani se wapas nahi hota.
@@   Jaise: lakdi jalna, doodh ka dahi banna, loha rust hona.
@@Chemical change ke ishaare (signs): gas nikalna, rang badalna, temperature
@@   change, smell change, precipitate (theek neeche baithne wala thos) banna.

## 5. Reactant aur Product (Reaction ki bhasha)

@@Reactant = jo cheezein react karti hain (ARROW ke BAAYI taraf - left).
@@Product = jo cheezein banti hain (ARROW ke DAAYI taraf - right).
@@   Reactants  ---->  Products
@@States ke short form: (s)=solid, (l)=liquid, (g)=gas, (aq)=aqueous
@@   (paani me ghula hua). Inko likhna marks dilata hai.

## 6. Law of Conservation of Mass (Class 9 - Ch1 ki jaan)

@@"Reaction me na to mass banta hai na nasht hota hai."
@@Matlab: reactant ka total mass = product ka total mass.
@@Isi wajah se equation BALANCE karni padti hai (dono taraf har atom barabar).

@@-- END OF CORE BASICS (RED) PAGE --

<<<PAGEBREAK>>>

==========================================

## PART B - CHAPTER KA MAIN CONTENT
## Class 10 Science | Ch 1: Chemical Reactions and Equations

$$[GREEN = board exam me baar-baar poocha jaata hai]

## 1. Chemical Reaction kya hai?

Jab ek ya zyada padarth (reactants) milkar naya padarth (product) banate hain,
to use chemical reaction kehte hain.

$$Chemical reaction ho rahi hai - yeh pehchanne ke 5 signs:
$$   (1) Rang (colour) badalna
$$   (2) State badalna (solid/liquid/gas)
$$   (3) Temperature badalna (garam ya thanda hona)
$$   (4) Gas (bubbles) nikalna
$$   (5) Precipitate (avshep) banna
Memory hook: "Rang-State-Temp-Gas-Precipitate" = "Reaction ka RSTGP signal".

## 2. Chemical Equation

Reaction ko symbols/formula me likhna = chemical equation.
   Example (shabdo me): Magnesium + Oxygen ----> Magnesium oxide
   Symbol equation:     2Mg + O2 ----> 2MgO

$$Balanced Equation: jisme arrow ke dono taraf har element ke atoms barabar hon.
$$Yeh Law of Conservation of Mass ki wajah se zaroori hai (mass na bane na mite).

## 3. Equation BALANCE karna (Step-by-step) [VERY IMPORTANT]

$$Steps (Hit & Trial method):
   Step 1: Skeletal (kaccha) equation likho - reactant ----> product.
   Step 2: Har element ke atoms dono taraf gino.
   Step 3: Sabse zyada atom wale compound se shuru karo, coefficient (bada
           number aage) laga kar barabar karo. Subscript KABHI mat badlo.
   Step 4: H aur O ko aam taur par last me balance karo.
   Step 5: Aakhir me states (s, l, g, aq) likho.

Example: Fe + H2O ----> Fe3O4 + H2
   Balanced:  3Fe + 4H2O ----> Fe3O4 + 4H2
$$Yaad rakho: SIRF coefficient badal sakte ho (aage wala number),
$$   subscript (formula ke andar ka number) kabhi nahi.

## 4. Types of Chemical Reactions (Pura chapter ka dil) [TOP EXAM AREA]

$$Paanch (5) main types - "CD-DD-Redox" yaad rakho:
$$   Combination, Decomposition, Displacement, Double Displacement, Redox.

## (A) Combination Reaction

Do ya zyada reactant milkar EK product banate hain.
   General: A + B ----> AB
$$   CaO + H2O ----> Ca(OH)2  (Quick lime + paani = slaked lime, garmi nikalti)
   2H2 + O2 ----> 2H2O
   C + O2 ----> CO2
$$Yeh ek EXOTHERMIC reaction ka classic example hai (garmi release hoti hai).

## (B) Decomposition Reaction (Combination ka ulta)

EK reactant tootkar do ya zyada product deta hai.  AB ----> A + B
$$Teen prakar (energy ke source se):
$$   (1) Thermal (garmi se):  CaCO3 --heat--> CaO + CO2
$$       (limestone se quick lime - cement industry me use hota hai)
$$   (2) Electrolytic (bijli se): 2H2O --electricity--> 2H2 + O2
$$   (3) Photolytic (light se): 2AgCl --sunlight--> 2Ag + Cl2
$$       (AgCl safed se grey ho jaata - photography me use)
$$Decomposition ko "ulta combination" bolte hain. Yeh aksar ENDOTHERMIC hoti hai
$$   (energy SOKHTI hai - heat/light/electricity chahiye).

## (C) Displacement Reaction

Zyada reactive element, kam reactive element ko uski jagah se hata deta hai.
   General: A + BC ----> AC + B   (A zyada reactive hai)
$$   Fe + CuSO4 ----> FeSO4 + Cu  (loha, copper ko hata deta - neela halka hota)
$$   Zn + CuSO4 ----> ZnSO4 + Cu
   Reactivity yaad: K > Na > Ca > Mg > Al > Zn > Fe > Pb > (H) > Cu > Ag > Au
$$Memory: "Kya Naani Ka Magaz Aluminium Zinc Faad Lega? Hydrogen Copper Silver Gold"

## (D) Double Displacement Reaction

Do compounds ke ions AAPAS me jagah badal lete hain.
   General: AB + CD ----> AD + CB
$$   Na2SO4 + BaCl2 ----> BaSO4 (white ppt) + 2NaCl
$$   Yahan jo solid neeche baithta hai use PRECIPITATE (avshep) kehte hain.
$$Precipitation reaction = jis double displacement me insoluble solid bane.

## (E) Oxidation, Reduction aur Redox [VERY VERY IMPORTANT]

$$Oxidation = Oxygen ka JUDNA ya Hydrogen ka NIKALNA.
$$Reduction = Oxygen ka NIKALNA ya Hydrogen ka JUDNA.
$$Memory hook "OIL RIG": Oxidation Is Loss (of electrons),
$$   Reduction Is Gain (of electrons).
$$Doosra hook: "LEO ke GER" - Lose Electron = Oxidation, Gain Electron = Reduction.
$$Redox reaction = jisme oxidation aur reduction DONO ek saath hote hain.
$$   CuO + H2 ----> Cu + H2O
$$   (CuO ka O nikla = reduced ; H2 me O juda = oxidised)
$$   ZnO + C ----> Zn + CO  (ZnO reduced, C oxidised)
Oxidising agent = doosre ko oxidise kare (khud reduce ho).
Reducing agent  = doosre ko reduce kare (khud oxidise ho).

## 5. Exothermic aur Endothermic Reactions

$$Exothermic = HEAT BAHAR nikalti (release). "Exo = Exit = bahar".
$$   Examples: jalna (combustion), respiration (saans), CaO + H2O,
$$   doodh/khana sadna, cement set hona.
$$   Respiration ko exothermic reaction kyun kehte? -> Glucose tootkar energy deta:
$$   C6H12O6 + 6O2 ----> 6CO2 + 6H2O + Energy
$$Endothermic = HEAT ANDAR sokhti (absorb). Garmi do tabhi chalti hai.
$$   Examples: decomposition of CaCO3, photosynthesis.

## 6. Oxidation ke Daily-Life Effects (Bahut scoring) [GREEN]

$$(A) CORROSION (ksharan):
$$   Metal ka apni surface par air/moisture se dheere-dheere kharab hona.
$$   Iron par bhura-laal RUST (Fe2O3.xH2O) jamta hai.
$$   Rusting ke liye DONO chahiye: Oxygen (air) + Moisture (paani/nami).
$$   Bachne ke tareeke: painting, oiling/greasing, galvanisation (Zn coating),
$$      chrome plating, alloy banana (jaise stainless steel).
$$   Silver kala padta (Ag2S), Copper par hara (basic copper carbonate).

$$(B) RANCIDITY (vikritgandhita):
$$   Tel/ghee waale khane oxidise hokar kharab smell/taste dete hain.
$$   Rokne ke tareeke:
$$      - Antioxidants daalna (jaise BHA, BHT)
$$      - Air-tight container me rakhna
$$      - Nitrogen gas bhar dena (chips ke packet me - oxygen hata diya jaata)
$$      - Fridge me rakhna (cold), light se door rakhna.
Memory: "Rancidity = tel-ghee ka oxidation se sadna; Nitrogen pack se rokte."

## 7. Quick Revision Table - Reaction Types

   Type            | Pehchaan                  | Example
   ----------------|---------------------------|------------------------
   Combination     | A + B -> AB (jud jaaye)   | CaO + H2O -> Ca(OH)2
   Decomposition   | AB -> A + B (toot jaaye)  | CaCO3 -> CaO + CO2
   Displacement    | A + BC -> AC + B          | Fe + CuSO4 -> FeSO4 + Cu
   Double Displ.   | AB + CD -> AD + CB         | Na2SO4 + BaCl2 -> BaSO4..
   Redox           | Oxidation + Reduction     | CuO + H2 -> Cu + H2O

<<<PAGEBREAK>>>

==========================================

## PART C - SOLVED EXAMPLES (HARDEST -> EASIEST)
## Step-by-step. Pehle mushkil, taaki baad me sab aasaan lage.

## Example 1 (HARDEST) - Balancing + type + observation (full board style)

Q: Jab ferrous sulphate (FeSO4) crystals ko garam karte hain to:
   (a) equation likho aur balance karo (b) reaction type (c) observation.

   Solution:
   (a) 2FeSO4 --heat--> Fe2O3 + SO2 + SO3
       Balance check: Fe: 2=2, S: 2=2 (SO2+SO3), O: 8 = 3+2+3 = 8. Balanced.
   (b) Type: Decomposition (thermal) - ek reactant tootkar teen product.
   (c) Observation: Green crystals (FeSO4.7H2O) ka rang badal kar bhura ho jaata,
       aur gandhi (burnt sulphur) smell wali gas nikalti hai.

## Example 2 - Identify oxidised & reduced (Redox)

Q: MnO2 + 4HCl ----> MnCl2 + 2H2O + Cl2. Kaun oxidise, kaun reduce hua?

   Solution:
   - MnO2 ka oxygen nikal gaya (MnCl2 bana) -> MnO2 REDUCED hua.
   - HCl ka hydrogen nikal kar Cl2 bana (oxygen juda nahi, par H hata) -> HCl OXIDISED.
   - Oxidising agent = MnO2 ; Reducing agent = HCl.

## Example 3 - Double displacement + precipitate

Q: Lead nitrate + Potassium iodide ka reaction likho aur ppt ka rang batao.

   Solution:
   Pb(NO3)2 + 2KI ----> PbI2 (yellow ppt) + 2KNO3
   Type: Double displacement (precipitation reaction).
   Observation: Peela (yellow) PbI2 precipitate banta hai.

## Example 4 - Why is respiration exothermic?

Q: Respiration ko exothermic reaction kyun kehte hain?

   Solution:
   Glucose, oxygen ke saath tootkar CO2 + paani banata hai aur ENERGY release
   karta hai. Yeh energy hamare body ko garam aur active rakhti hai. Energy
   bahar aati hai isliye exothermic.
   C6H12O6 + 6O2 ----> 6CO2 + 6H2O + Energy

## Example 5 (EASIEST) - Balance this simple equation

Q: H2 + O2 ----> H2O ko balance karo.

   Solution:
   O dono taraf barabar karo: right me O ke liye 2 chahiye -> 2H2O.
   Ab H: right me 4 hai -> left me 2H2.
   Balanced:  2H2 + O2 ----> 2H2O

<<<PAGEBREAK>>>

==========================================

## PART D - SELF TEST (EASY -> HARD)
## Khud likho, phir niche answer hint se check karo. Yeh "test" tumhe yaad
## rakhne me sabse zyada help karega (active recall).

## EASY (1 mark)

   Q1. Combination reaction ki definition + 1 example likho.
   Q2. (s), (l), (g), (aq) ka matlab batao.
   Q3. Rust ka chemical naam/formula kya hai?
   Q4. Decomposition reaction kya hai? Ek line.

## MEDIUM (2-3 marks)

   Q5. In equations ko balance karo:
        (a) Na + O2 ----> Na2O
        (b) Al + Cl2 ----> AlCl3
        (c) Pb(NO3)2 ----> PbO + NO2 + O2
   Q6. Exothermic aur Endothermic me 2 differences + 1-1 example.
   Q7. Rancidity kya hai? Rokne ke 3 tareeke likho.
   Q8. Displacement aur Double displacement me antar (example sahit).

## HARD (3-5 marks, board favourite)

   Q9. 2FeSO4 -> Fe2O3 + SO2 + SO3 : reaction type + observation + balance check.
   Q10. CuO + H2 -> Cu + H2O me oxidation aur reduction dono dikhao
        (kaun oxidised, kaun reduced, oxidising/reducing agent).
   Q11. Corrosion kya hai? Iron rusting ke liye kya-kya zaroori? Bachne ke 3 upaay.
   Q12. White silver chloride ko dhoop me rakhne par kya hota hai? Equation +
        reaction type batao. (Photography se connection bhi.)

==========================================

## ANSWER HINTS (PART D)

   A1. Do/zyada reactant milke ek product. Eg: CaO + H2O -> Ca(OH)2.
   A2. s=solid, l=liquid, g=gas, aq=aqueous (paani me ghula).
   A3. Fe2O3.xH2O (hydrated iron oxide), bhura-laal.
   A4. Ek padarth tootkar 2+ padarth dene wali reaction.
   A5. (a) 4Na + O2 -> 2Na2O  (b) 2Al + 3Cl2 -> 2AlCl3
       (c) 2Pb(NO3)2 -> 2PbO + 4NO2 + O2
   A6. Exo = heat nikle (combustion); Endo = heat soke (photosynthesis).
   A7. Tel/ghee ka oxidation se kharab hona; antioxidant, airtight, N2 packing.
   A8. Displacement: A+BC->AC+B (Fe+CuSO4). Double: AB+CD->AD+CB (Na2SO4+BaCl2).
   A9. Thermal decomposition; green->brown, smelly SO2/SO3 gas; (atoms balanced).
   A10. CuO reduced (O gaya), H2 oxidised (O juda); ox.agent CuO, red.agent H2.
   A11. Metal ka air+moisture se kharab hona; iron rust ke liye O2 + paani;
        painting/oiling/galvanisation se bachao.
   A12. 2AgCl --sunlight--> 2Ag + Cl2 ; photolytic decomposition; safed se grey.

==========================================
## "Padhai tabhi pakki jab khud likh ke test do." - All the best, Krishna!
## Generated by Kiro for Krishna1k
==========================================
"""

if __name__ == "__main__":
    build_pdf(
        CONTENT,
        "Science_Class10_Ch1_Chemical_Reactions.pdf",
        title="Class 10 Science - Chapter 1",
        subtitle="Chemical Reactions and Equations (Hinglish Notes)",
    )
