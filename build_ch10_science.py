"""
Build Class 10 Science Chapter 10 study PDF: "The Human Eye and the Colourful World"
Hinglish. Markup: @@ RED (core basics), $$ GREEN (exam favourite), ## header.
Run: python3 build_ch10_science.py
"""
from pdf_utils import build_pdf

CONTENT = r"""
==========================================

@@PART A - CORE BASICS (MISS MAT KARNA)
@@Ch9 + Class 8 ki yeh cheezein pehle pakki karo, warna Ch10 samajh nahi aayega.

## 1. Refraction aur Lens (Ch9 revision - bahut zaroori)

@@Refraction = light ka ek medium se doosre me mud-na (speed change).
@@Convex lens = beech mota, CONVERGING (kiranein milati) -> real image bana sakta.
@@Concave lens = beech patla, DIVERGING (kiranein failati) -> virtual chhota.
@@Power P = 1/f (metre); unit DIOPTRE (D). Convex +ve, concave -ve.

## 2. Image banna (Ch9 revision)

@@Lens screen par real, inverted image banata (jaise camera/aankh).
@@Focal length jitni chhoti -> power utni jyada (zyada mud-aata).

## 3. White light aur Colours (Class 8 base)

@@White light (suraj ki roshni) = saat (7) colours se bani.
@@VIBGYOR: Violet, Indigo, Blue, Green, Yellow, Orange, Red.
@@Prism = teen-konaa (triangular) kaanch jo light ko todta.
@@Transparent medium me alag colour alag speed se chalte.

## 4. Atmosphere aur kann (Class 7-8)

@@Atmosphere = Earth ke charo taraf hawa (gases + dust + paani ke kann).
@@Light chhote kanno se takrakar bikhar (scatter) sakti.
@@Chhoti wavelength (blue) zyada bikharti, badi (red) kam bikharti.

## 5. Wavelength ka idea

@@Light ek wave hai; har colour ki alag wavelength.
@@   Red ki sabse BADI wavelength, Violet ki sabse CHHOTI.
@@   Chhoti wavelength = zyada scatter (bikhrav).

@@-- END OF CORE BASICS (RED) PAGE --

<<<PAGEBREAK>>>

==========================================

## PART B - CHAPTER KA MAIN CONTENT
## Class 10 Science | Ch 10: The Human Eye and the Colourful World

$$[GREEN = board exam me baar-baar poocha jaata hai]

## 1. Human Eye ki Structure [VERY IMPORTANT - RATTA]

$$   CORNEA: aankh ke aage ka transparent parda; sabse zyada refraction yahin.
$$   IRIS: rangeen hissa; pupil ka size control karta.
$$   PUPIL: beech ka kaala chhed; kitni light andar aaye control (iris se).
$$   EYE LENS (crystalline): convex lens; fine focusing karta (image sharp).
$$   CILIARY MUSCLE: lens ki shape (focal length) badalta.
$$   RETINA: peeche ka parda (screen) jahan REAL, INVERTED image banti.
$$     Isme light-sensitive cells: RODS (kam roshni/dim) + CONES (rang + tej roshni).
$$   OPTIC NERVE: image ka signal brain tak le jaata.
$$Aankh ki image: retina par real aur inverted hoti (brain seedha samajhta).

## 2. Power of Accommodation [IMPORTANT]

$$Accommodation = aankh ke lens ka apni FOCAL LENGTH badal-ne ki capacity,
$$   taaki paas aur door dono cheez sharp dikhe.
$$   - Door dekhne par: ciliary muscle DHEELE -> lens patla -> focal length BADI.
$$   - Paas dekhne par: ciliary muscle TIGHT -> lens mota -> focal length CHHOTI.
$$Near point (least distance of distinct vision) = 25 cm (normal aankh).
$$Far point = infinity (normal aankh door tak dekh sakti).
$$Lens itna patla nahi ho sakta ki 25cm se paas focus kare -> isliye bahut paas
$$   ki cheez clear nahi dikhti.

## 3. Defects of Vision aur Sudhaar (Correction) [TOP EXAM AREA]

$$(A) MYOPIA (nikat-drishti / near-sightedness):
$$   - PAAS saaf dikhta, DOOR nahi.
$$   - Kaaran: image retina ke AAGE banti (eyeball lamba ya lens zyada convex).
$$   - Sudhaar: CONCAVE lens (diverging) - far point wapas infinity par.

$$(B) HYPERMETROPIA (door-drishti / far-sightedness):
$$   - DOOR saaf dikhta, PAAS nahi.
$$   - Kaaran: image retina ke PEECHE banti (eyeball chhota ya lens kam convex).
$$   - Sudhaar: CONVEX lens (converging) - near point 25cm par le aata.

$$(C) PRESBYOPIA:
$$   - Budhape me aankh ke muscle kamzor + lens lachila nahi -> paas+door dono
$$     me dikkat.
$$   - Sudhaar: BIFOCAL lens (upar concave for door, neeche convex for paas).
$$Cataract: lens dhundhla (cloudy) ho jaata -> surgery se theek (yeh accommodation
$$   defect nahi, alag).
$$Memory: "Myopia = Minus (concave) lens; Hypermetropia = + (convex) lens".

## 4. Refraction through Prism aur Dispersion [TOP EXAM AREA]

$$Prism light ko mod-ta (do baar refraction) aur DISPERSION karta:
$$DISPERSION = white light ka apne 7 colours (VIBGYOR) me toot jaana.
$$   Kaaran: har colour alag angle se mudta (Violet sabse zyada, Red sabse kam).
$$Spectrum = VIBGYOR ki rangeen patti.
$$Recombination: doosra ulta prism lagao -> 7 colour wapas white light ban jaate
$$   (Newton ka experiment).

## 5. Rainbow (Indradhanush) [IMPORTANT]

$$Rainbow = baarish ke baad aakash me VIBGYOR ka arc.
$$Kaise banta: hawa me paani ki boondein chhote PRISM jaise kaam karti ->
$$   sunlight me REFRACTION + DISPERSION + INTERNAL REFLECTION + REFRACTION ->
$$   7 colour alag dikhte. Suraj peeche, boondein saamne hone par dikhta.

## 6. Atmospheric Refraction [IMPORTANT]

$$Atmosphere me hawa ki layers ka temperature/density alag -> light mud-ti.
$$(A) Tare timtimate (twinkling) - star ki light layers se mud-mud ke aati,
$$   thodi-thodi badalti -> kabhi tej kabhi mand. (Planet nahi timtimate kyunki
$$   woss paas hain -> bade source.)
$$(B) Suraj sunrise/sunset par jaldi dikhna - actual horizon ke neeche hone par
$$   bhi atmospheric refraction se 2 min pehle dikh jaata.
$$(C) Sunrise/sunset par suraj OVAL/laal dikhna.

## 7. Scattering of Light (Tyndall + Sky colour) [TOP EXAM - VERY IMP]

$$Scattering = light ka chhote kanno se takrakar har disha me bikhar jaana.
$$TYNDALL EFFECT = colloid/dust me light ka path dikhna (jaise jungle me dhundh
$$   me sunlight ki kiran, ya smoke me torch beam).
$$Chhoti wavelength (BLUE) zyada scatter; badi (RED) kam scatter.

$$(A) Aakash NEELA kyun? - hawa ke molecules blue (chhoti wavelength) ko zyada
$$   scatter karte -> aankh tak chaaro taraf se blue aata -> sky blue dikhta.
$$(B) Sunrise/sunset par suraj LAAL kyun? - tab light ko zyada hawa paar karni
$$   padti -> blue raaste me hi scatter ho jaata -> sirf RED (kam scatter) bachta.
$$(C) Antariksh (space) me aasman KAALA - kyunki wahan hawa/molecules nahi ->
$$   scattering nahi.
$$(D) Khatre ka signal LAAL kyun? - red light kam scatter hoti -> door se bhi
$$   saaf dikhti -> isliye danger sign red.

## 8. Quick Revision - One Liners
   - Eye: cornea (max refraction), iris (pupil control), retina (real inverted
     image, rods+cones), accommodation = lens focal length change.
   - Near point 25cm, far point infinity.
   - Myopia -> concave lens; Hypermetropia -> convex; Presbyopia -> bifocal.
   - Dispersion: white -> VIBGYOR (violet max bend, red min).
   - Sky blue + sunset red = scattering (blue zyada, red kam scatter).

<<<PAGEBREAK>>>

==========================================

## PART C - SOLVED EXAMPLES (HARDEST -> EASIEST)

## Example 1 (HARDEST) - Defect identify + lens + kaaran

Q: Ek vyakti door ki cheez saaf nahi dekh paata par paas ki dekh leta. Kaunsa
   defect? Kaaran kya? Kaunsa lens? Image kahan banti?

   Solution:
   - Defect: MYOPIA (near-sightedness).
   - Kaaran: eyeball lamba ya lens zyada convex -> image retina ke AAGE banti.
   - Sudhaar: CONCAVE (diverging) lens - jo door ki kiranein thodi failakar
     image wapas retina par laata.

## Example 2 - Sky blue + sunset red dono ek saath

Q: Aakash din me neela par sunset par suraj laal kyun dikhta? Scattering se
   samjhao.

   Solution:
   - Blue ki wavelength chhoti -> hawa molecules zyada scatter karte -> din me
     chaaro taraf se blue aata -> sky blue.
   - Sunset par light ko zyada atmosphere paar karna padta -> blue raaste me
     scatter ho jaata, sirf RED (kam scatter) aankh tak pahunchta -> suraj laal.

## Example 3 - Dispersion + recombination

Q: Prism se white light ka kya hota? Wapas white kaise milegi?

   Solution:
   - White light prism se guzar kar 7 colours (VIBGYOR) me TOOT jaati
     (dispersion) - violet sabse zyada, red sabse kam mudta.
   - Ek doosra ulta (inverted) prism lagao -> saare colour milkar wapas WHITE
     light ban jaati (Newton).

## Example 4 - Accommodation

Q: Power of accommodation kya hai? Door aur paas dekhte waqt lens me kya change?

   Solution:
   - Accommodation = lens ka focal length badalne ki capacity.
   - Door: ciliary muscle dheele -> lens patla -> focal length badi.
   - Paas: ciliary muscle tight -> lens mota -> focal length chhoti.

## Example 5 (EASIEST) - Retina par image

Q: Aankh me image kahan banti aur kaisi (real/virtual)?

   Solution:
   - RETINA par; real aur inverted (ulti).

<<<PAGEBREAK>>>

==========================================

## PART D - SELF TEST (EASY -> HARD)

## EASY (1 mark)
   Q1. Retina ka kaam kya hai? Rods aur cones me antar.
   Q2. Normal aankh ka near point aur far point.
   Q3. Tyndall effect kya hai? 1 example.
   Q4. VIBGYOR me konsa colour sabse zyada/kam mudta.

## MEDIUM (2-3 marks)
   Q5. Power of accommodation samjhao (door vs paas).
   Q6. Myopia ka kaaran + sudhaar (lens).
   Q7. Hypermetropia ka kaaran + sudhaar (lens).
   Q8. Dispersion kya hai? Prism se kaise hoti.

## HARD (3-5 marks, board favourite)
   Q9. Aankh ki structure (5 bhaag + kaam).
   Q10. 3 vision defects (myopia/hypermetropia/presbyopia) + lens.
   Q11. Aakash neela + sunset laal scattering se explain.
   Q12. Atmospheric refraction: tare timtimana + suraj jaldi dikhna.

==========================================

## ANSWER HINTS (PART D)
   A1. Retina = screen (real inverted image); rods (dim light), cones (rang).
   A2. Near point 25 cm, far point infinity.
   A3. Colloid/dust me light path dikhna; jungle dhundh me sunlight kiran.
   A4. Violet sabse zyada, Red sabse kam.
   A5. Lens focal length change; door-patla(badi f), paas-mota(chhoti f).
   A6. Image retina ke aage; concave lens.
   A7. Image retina ke peeche; convex lens.
   A8. White light ka 7 colour me toot-na; prism alag-alag angle se modta.
   A9. Cornea, iris, pupil, lens, retina, optic nerve (+kaam).
   A10. Myopia-concave; hypermetropia-convex; presbyopia-bifocal.
   A11. Blue zyada scatter (sky blue); sunset blue scatter ho jaata, red bachta.
   A12. Layers se light mudti -> tare timtimate; suraj 2 min pehle dikhta.

==========================================
## "Padhai tabhi pakki jab khud likh ke test do." - All the best, Krishna!
## Generated by Kiro for Krishna1k
==========================================
"""

if __name__ == "__main__":
    build_pdf(CONTENT, "Science_Class10_Ch10_Human_Eye_Colourful_World.pdf",
              title="Class 10 Science - Chapter 10",
              subtitle="The Human Eye and the Colourful World (Hinglish Notes)")
