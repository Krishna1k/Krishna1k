"""
Build Class 10 Science Chapter 12 study PDF: "Magnetic Effects of Electric Current"
Hinglish. Markup: @@ RED (core basics), $$ GREEN (exam favourite), ## header.
Run: python3 build_ch12_science.py
"""
from pdf_utils import build_pdf

CONTENT = r"""
==========================================

@@PART A - CORE BASICS (MISS MAT KARNA)
@@Ch11 + Class 6-8 ki yeh cheezein pehle pakki karo.

## 1. Magnet ka basic (Class 6)

@@Magnet ke do pole: North (N) aur South (S).
@@Same pole REPEL (door bhagaate), opposite pole ATTRACT (paas khinchte).
@@   "Like poles repel, unlike poles attract."
@@Magnet ke around ek area hota jaha uska asar hota = MAGNETIC FIELD.
@@Compass needle (chumbak ki sui) hamesha North-South dikhati.

## 2. Current aur Circuit (Ch11 revision)

@@Current = charge ka flow (ampere). Conventional current +ve se -ve.
@@Conductor (taar) me current behne par uske around kuch hota -> isi chapter ka
@@   main idea (magnetic effect).
@@Solenoid = taar ko spring/coil jaise lapet kar banaya gaya.

## 3. Direction batane ke tareeke

@@3D direction: (dot . ) = current/field BAAHAR aapki taraf;
@@   (cross x) = ANDAR (paper ke andar) jaa rahi.
@@Perpendicular = 90 degree par. Right angle = 90 degree.

## 4. Maths/Geometry basics

@@Circle ke concentric (ek hi center wale) circles ka idea.
@@Direction (left/right/up/down) clearly samajhna - Fleming rules ke liye.

## 5. AC vs DC (idea)

@@DC (Direct current) = ek hi disha me (cell/battery se).
@@AC (Alternating current) = disha badalti rehti (ghar ka supply, India me 50 Hz
@@   matlab 1 second me 50 baar direction badalti -> 100 baar polarity change).

@@-- END OF CORE BASICS (RED) PAGE --

<<<PAGEBREAK>>>

==========================================

## PART B - CHAPTER KA MAIN CONTENT
## Class 10 Science | Ch 12: Magnetic Effects of Electric Current

$$[GREEN = board exam me baar-baar poocha jaata hai]

## 1. Magnetic Field aur Field Lines [IMPORTANT]

$$Oersted ne dekha: current wale taar ke paas compass sui ghoom jaati ->
$$   matlab current MAGNETIC FIELD banati hai.
$$Magnetic field = woh area jaha magnet/current ka magnetic asar hota.
$$   Field ek VECTOR hai (magnitude + direction dono).
$$Magnetic field LINES ki properties:
$$   - Bahar N se S ki taraf, magnet ke andar S se N (closed loops).
$$   - Kabhi ek doosre ko CROSS nahi karti (kyunki ek point par 2 direction
$$     possible nahi).
$$   - Paas-paas lines = strong field; door-door = weak field.

## 2. Field due to Current in a Straight Conductor [IMPORTANT]

$$Seedhe taar ke around magnetic field = concentric (ek center wale) CIRCLES.
$$   Current jyada -> field strong; taar se door -> field weak.
$$RIGHT HAND THUMB RULE: right haath ka angootha CURRENT ki direction me;
$$   ungliyon ka curl (mudna) = magnetic field ki direction.

## 3. Field due to Solenoid + Electromagnet [VERY IMPORTANT]

$$Solenoid (coil) me current -> field bilkul BAR MAGNET jaisa.
$$   - Ek sira N pole, doosra S pole. Andar field uniform (parallel lines).
$$ELECTROMAGNET = solenoid ke andar soft iron core daal do -> strong temporary
$$   magnet. Current band -> magnetism khatam (isliye "temporary").
$$   (Soft iron core use hota kyunki jaldi magnetise + jaldi demagnetise hota.)

## 4. Force on Current-Carrying Conductor [TOP EXAM AREA]

$$Magnetic field me rakhe current wale taar par FORCE lagta (push).
$$   Force max jab current field ke PERPENDICULAR (90 par) ho.
$$FLEMING'S LEFT HAND RULE (force/motion ke liye):
$$   Left haath - 3 ungli 90 par phailao:
$$   - First finger (tarjani) = Field (B)
$$   - Centre finger (madhya) = Current (I)
$$   - Thumb (angootha) = Force/motion (F)
$$Memory: "FBI" - thumb=Force, first=B(field), centre=I(current).
$$Yeh ELECTRIC MOTOR ka base hai.

## 5. Electric Motor [TOP EXAM AREA]

$$Electric motor = electrical energy ko MECHANICAL (ghoomne wali) energy me badle.
$$Working: magnetic field me coil me current -> dono side opposite force (Fleming
$$   left hand) -> coil GHOOMTI.
$$SPLIT RING / COMMUTATOR = har aadhe chakkar me current ki direction PALAT-ta
$$   -> coil ek hi disha me ghoomti rehti.
$$Brushes = current ko coil tak pahunchate. Use: fan, mixer, pump, washing machine.

## 6. Electromagnetic Induction (EMI) [TOP EXAM AREA]

$$Faraday: badalti (changing) magnetic field se coil me current PAIDA hoti
$$   (bina battery) -> ELECTROMAGNETIC INDUCTION.
$$   - Magnet ko coil ke paas hilao (ya coil ko) -> galvanometer me current dikhta.
$$   - Jitni tezi se movement, utni jyada current.
$$FLEMING'S RIGHT HAND RULE (induced current ke liye):
$$   Right haath - thumb=motion, first=field, centre=induced current.
$$Memory: motor=LEFT (force), generator/induction=RIGHT.

## 7. Electric Generator (Dynamo) [VERY IMPORTANT]

$$Generator = MECHANICAL energy ko ELECTRICAL energy me badle (motor ka ulta).
$$Working: coil ko magnetic field me ghumao -> EMI se current paida.
$$AC generator: SLIP RINGS use -> alternating current (AC) deta.
$$DC generator: SPLIT RING (commutator) use -> ek direction current (DC).
$$Ghar ka supply AC hota (India 220V, 50 Hz).

## 8. Domestic Electric Circuit + Safety [IMPORTANT]

$$Ghar me 3 taar aate:
$$   - LIVE (red/brown) - +ve, current laata.
$$   - NEUTRAL (black/blue) - current wapas le jaata.
$$   - EARTH (green) - safety, leakage current ko zameen me bhej deta.
$$Earthing: metal body ko earth wire se jodte -> agar live taar body ko chhoo
$$   jaaye to current zameen me chala jaaye, insaan ko shock na lage.
$$Short circuit: live aur neutral seedha touch -> achaanak bahut current -> fuse
$$   pighal kar circuit tod deta.
$$Overloading: ek hi socket par bahut appliances -> jyada current -> aag ka khatra.
$$FUSE live wire me lagta (kam m.p. taar) - safety device.

## 9. Quick Revision - One Liners
   - Current -> magnetic field (Oersted). Field lines cross nahi karti.
   - Right hand thumb rule (field around wire); solenoid = bar magnet.
   - Fleming LEFT hand = force (MOTOR). Fleming RIGHT hand = induced current
     (GENERATOR/EMI).
   - Motor: electrical->mechanical (split ring). Generator: mechanical->electrical.
   - Ghar: live/neutral/earth; earthing+fuse = safety; short circuit + overload
     khatarnak.

<<<PAGEBREAK>>>

==========================================

## PART C - SOLVED EXAMPLES (HARDEST -> EASIEST)

## Example 1 (HARDEST) - Motor vs Generator + kaunsa Fleming rule

Q: Electric motor aur generator me kya antar? Dono me kaunsa Fleming rule lagta
   aur energy conversion kya?

   Solution:
   - MOTOR: electrical -> mechanical energy. Field me current wali coil par force
     lagta -> coil ghoomti. Fleming LEFT hand rule. Split ring/commutator use.
   - GENERATOR: mechanical -> electrical energy. Coil ghumane par EMI se current.
     Fleming RIGHT hand rule. AC me slip ring, DC me split ring.
   Yaad: motor=LEFT, generator=RIGHT.

## Example 2 - Fleming left hand apply karna

Q: Ek taar me current paper ke andar (x) ja rahi, magnetic field neeche se upar.
   Force ki direction?

   Solution:
   - Fleming left hand: first finger (field) upar, centre finger (current) andar,
     thumb (force) jis taraf aaye = force direction. Yahan thumb ek side
     (left/right) point karega - i.e. force taar ke perpendicular (horizontal).
   - (Concept: F field aur current dono ke perpendicular hota.)

## Example 3 - Electromagnetic induction

Q: Bina battery ke coil me current kaise paida kar sakte? Kis cheez par depend?

   Solution:
   - Magnet ko coil ke paas/door hilao (ya coil ko hilao) -> magnetic field
     change -> EMI se induced current. Galvanometer ye dikha deta.
   - Depend: movement ki speed (jitni tez, utni jyada current) + coil ke turns.

## Example 4 - Field lines property

Q: Do magnetic field lines kabhi cross kyun nahi karti?

   Solution:
   - Agar cross karein to us point par field ki 2 alag directions hongi, jo
     impossible hai (ek point par sirf ek direction). Isliye cross nahi karti.

## Example 5 (EASIEST) - Earth wire ka kaam

Q: Ghar me earth (green) wire ka kya kaam hai?

   Solution:
   - Safety. Leakage/extra current ko zameen me bhej deta -> shock se bachata.

<<<PAGEBREAK>>>

==========================================

## PART D - SELF TEST (EASY -> HARD)

## EASY (1 mark)
   Q1. Magnetic field lines ki 2 properties.
   Q2. Right hand thumb rule kya batata hai?
   Q3. Electromagnet me soft iron core kyun?
   Q4. AC aur DC me 1 antar.

## MEDIUM (2-3 marks)
   Q5. Fleming left hand rule + kis device me use.
   Q6. Solenoid ka field bar magnet jaisa - samjhao.
   Q7. Domestic circuit ke 3 taar + kaam.
   Q8. Short circuit aur overloading me antar.

## HARD (3-5 marks, board favourite)
   Q9. Electric motor ki working + split ring ka kaam.
   Q10. Electromagnetic induction + Faraday experiment + Fleming right hand.
   Q11. Generator working (AC vs DC, slip ring vs split ring).
   Q12. Earthing kya hai aur insaan ko shock se kaise bachata + fuse ka role.

==========================================

## ANSWER HINTS (PART D)
   A1. N se S bahar (closed loops); cross nahi karti; paas=strong field.
   A2. Current wale seedhe taar ke around field ki direction.
   A3. Jaldi magnetise + demagnetise hota (temporary strong magnet).
   A4. DC ek disha; AC disha badalti (ghar 50 Hz).
   A5. First=field, centre=current, thumb=force; MOTOR me use.
   A6. Ek sira N, doosra S, andar uniform field - bar magnet jaisa.
   A7. Live (current laata), neutral (wapas), earth (safety).
   A8. Short: live-neutral touch, achaanak current; overload: bahut appliance.
   A9. Field me current coil par force (Fleming left) -> ghoomti; split ring
       current direction palat kar ek disha me ghumata.
   A10. Changing field se induced current; magnet-coil hilao; Fleming right hand.
   A11. Coil ghumao -> EMI; AC slip ring, DC split ring.
   A12. Metal body earth se jodna; leakage current zameen me; fuse zyada current
        par pighal kar bachata.

==========================================
## "Padhai tabhi pakki jab khud likh ke test do." - All the best, Krishna!
## Generated by Kiro for Krishna1k
==========================================
"""

if __name__ == "__main__":
    build_pdf(CONTENT, "Science_Class10_Ch12_Magnetic_Effects.pdf",
              title="Class 10 Science - Chapter 12",
              subtitle="Magnetic Effects of Electric Current (Hinglish Notes)")
