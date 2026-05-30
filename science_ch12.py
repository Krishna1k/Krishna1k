"""
science_ch12.py
---------------
Generates a detailed, simplified Hinglish study guide for
NCERT Class 10 Science, Chapter 12: "Magnetic Effects of Electric Current".

Outputs:
  - Science_Class10_Ch12_Magnetic_Effects_Current.pdf  (colour PDF)
  - Science_Class10_Ch12_Magnetic_Effects_Current.md   (markdown, red/green via emoji)

Markup conventions inside CONTENT (handled by pdf_utils):
  @@  -> RED   line  (CORE BASICS / extra ke liye)
  $$  -> GREEN line  (exam me baar-baar aane wale topics)
  <<<PAGEBREAK>>>     -> nayi page
"""

import re
from pathlib import Path

import pdf_utils


CONTENT = r"""MAGNETIC EFFECTS OF ELECTRIC CURRENT
NCERT Class 10 Science - Chapter 12 (Hinglish Detailed Notes)
=========================================================

@@ COLOUR CODE: RED = Core Basics / extra help (Class 7-8-9 wali cheezein jo yaad honi chahiye).
$$ COLOUR CODE: GREEN = Board exam me ye topics BAAR-BAAR aate hain - pakka yaad karo.
   Baaki normal black text = main chapter content (detail me, simple bhasha me).

<<<PAGEBREAK>>>

CORE BASICS - PEHLE YE PADHO (CLASS 7-8-9 KA FOUNDATION)
=========================================================
@@ Tune 7-8-9 nahi padhi - koi tension nahi. Ye page is chapter ki base hai.
@@ Ek baar achhe se padh le, fir chapter aasaani se samajh aayega.

@@ 1) MAGNET kya hai aur MAGNETIC POLES:
@@    - Magnet = woh cheez jo iron/steel ko apni taraf kheechti hai (attract).
@@    - Har magnet ke do sire (poles) hote: NORTH pole (N) aur SOUTH pole (S).
@@    - Magnet ko latkao to N pole hamesha UTTAR (North) disha me rukta -
@@      isiliye naam North pole pada.

@@ 2) LIKE aur UNLIKE POLES (attract / repel):
@@    - UNLIKE poles (N-S) ek dusre ko KHEECHTE hain (attract).
@@    - LIKE poles (N-N ya S-S) ek dusre ko DHAKELTE hain (repel).
@@    - Poles hamesha JODE (pair) me hote - magnet todo to dono tukde
@@      apne-apne N aur S bana lete (single pole nahi milta).

@@ 3) MAGNETIC FIELD (simple idea):
@@    - Magnet ke aas-paas ka woh region jaha uska asar (force) feel hota -
@@      use MAGNETIC FIELD kehte. Ye ek dishaa-wali (vector) cheez hai
@@      (magnitude + direction dono).

@@ 4) ELECTRIC CURRENT (Ch-11 se link):
@@    - Current = charge (electron) ka flow. Unit = AMPERE (A).
@@    - Conventional current ki direction = +ve se -ve terminal ki taraf
@@      (electron ulta chalte). Current chalega to circuit poora (closed) hona chahiye.

@@ 5) COIL aur SOLENOID:
@@    - COIL = taar (wire) ko ghuma ke banaya hua loop/lapet.
@@    - SOLENOID = bahut saare circular loops ka lamba bela (cylinder) jaisa coil.

@@ 6) AC vs DC (simple words):
@@    - DC (Direct Current) = ek hi disha me behta (cell/battery deta).
@@    - AC (Alternating Current) = disha baar-baar badalta rehta
@@      (India me 50 baar per second, yaani frequency 50 Hz).

@@ 7) CONDUCTOR kya hai:
@@    - Conductor = woh material jo current aasaani se paas hone de (copper, aluminium).
@@    - Current-carrying conductor = woh taar jisme current beh raha ho.

@@ 8) FIELD LINES ka idea:
@@    - Magnetic field ko dikhane ke liye hum kaal-pnik (imaginary) lines banate -
@@      inhe FIELD LINES (field rekha) kehte. Ye field ki direction batati hain.

@@ 9) RIGHT-HAND RULE ka idea (intro):
@@    - Current aur uske magnetic field ki direction yaad rakhne ke liye hum
@@      apne HAATH ko ek khaas tarike se pakad ke (rule) direction nikalte hain.
@@    - Is chapter me 3 rule aayenge: Right-hand THUMB rule, Fleming LEFT-hand
@@      rule, Fleming RIGHT-hand rule. Ghabrao mat - aage detail me hai.

<<<PAGEBREAK>>>

1. MAGNETIC FIELD aur FIELD LINES
=========================================================

1.1 MAGNETIC FIELD
---------------------------------------------------------
   - MAGNETIC FIELD = magnet ya current ke aas-paas ka region jaha magnetic
     force ka asar hota. Iski direction AUR magnitude dono hoti (vector quantity).
   - Field ki direction kisi point par = us point par rakhi compass needle
     ke North pole ke point karne ki disha.

1.2 MAGNETIC FIELD LINES (FIELD REKHA)
---------------------------------------------------------
$$ FIELD LINES = woh kaal-pnik (imaginary) lines jinke saath-saath compass
$$ needle ka N pole point karta - ye field ko draw karne ka tarika hai.

$$ FIELD LINES KI PROPERTIES (EXAM ME PAKKA - list yaad rakho):
$$   (i)   Magnet ke BAHAR field lines NORTH se SOUTH ki taraf jaati hain,
$$         aur magnet ke ANDAR South se North (isliye band loop banti).
$$   (ii)  Field lines hamesha BAND (closed) loops hoti hain.
$$   (iii) Do field lines kabhi ek dusre ko CUT (intersect) NAHI karti.
$$         (Kyunki ek point par field ki sirf EK hi direction ho sakti.)
$$   (iv)  Jaha lines PAAS-PAAS (dense) hoti waha field STRONG, jaha door-door
$$         (kam dense) waha field WEAK hoti hai.

   - BAR MAGNET ka field: lines ek pole (N) se nikalti, ghoom ke dusre pole (S)
     me jaati - sabse zyada bheed (crowd) poles ke paas (waha field strong).

<<<PAGEBREAK>>>

2. OERSTED KI KHOJ + STRAIGHT WIRE KA FIELD
=========================================================

2.1 OERSTED'S FINDING (current se magnetism)
---------------------------------------------------------
$$ OERSTED ne dekha: jab kisi taar me CURRENT behta hai to uske aas-paas
$$ MAGNETIC FIELD ban jaata hai.
$$   - Proof: current wale taar ke paas COMPASS needle rakho to woh GHOOM
$$     (deflect) jaati hai. Current band karo to needle wapas seedhi.
$$   - Current ULTA karo (direction badlo) to needle ULTI taraf ghoomti.
   - Matlab: electricity aur magnetism alag-alag nahi - jude hue hain.

2.2 STRAIGHT CURRENT-CARRYING CONDUCTOR KA FIELD
---------------------------------------------------------
   - Seedhe taar me current behne par uske charo taraf field banta hai jiski
     shape = CONCENTRIC CIRCLES (ek hi centre wale gol-gol ghere), taar centre me.
$$   - Taar ke PAAS circle chhote aur paas-paas (field STRONG); door jaate
$$     circle bade aur door-door (field WEAK).
$$   - CURRENT zyada karo to har point par field STRONG ho jaata.

$$ RIGHT-HAND THUMB RULE (direction nikalne ke liye - EXAM FAVOURITE):
$$   - Taar ko apne SEEDHE haath me is tarah pakdo ki ANGOOTHA (thumb) CURRENT
$$     ki direction me point kare.
$$   - Tab baaki MUDI hui ungliyaan (fingers) jis taraf taar ko ghere wo
$$     MAGNETIC FIELD (field lines) ki direction batati hain.
$$   - Ise "Maxwell's corkscrew rule" se bhi nikal sakte (corkscrew ghumao).

<<<PAGEBREAK>>>

3. CIRCULAR LOOP aur SOLENOID
=========================================================

3.1 CIRCULAR LOOP KA FIELD
---------------------------------------------------------
   - Circular loop ke har chhote hisse ke gird concentric circle banta;
     loop ke CENTRE par ye sab mil ke field LAGBHAG SEEDHI line jaisa banta
     (loop ke axis ke along).
   - Field BADHANE ke tarike:
       (a) CURRENT zyada karo.
       (b) Loop ka RADIUS chhota karo.
       (c) TURNS (n) badhao - n loops ka field = ek loop ka field x n
           (har turn ka field jud jaata).

3.2 SOLENOID KA FIELD
---------------------------------------------------------
$$ SOLENOID = bahut saare circular turns ka lamba coil (cylinder jaisa).
$$   - Solenoid ke ANDAR field UNIFORM hota (har jagah same strength + same
$$     direction) - lines lagbhag seedhi parallel.
$$   - Solenoid ka field bilkul BAR MAGNET jaisa dikhta: ek sira N pole,
$$     dusra sira S pole ban jaata.

$$ ELECTROMAGNET (vidyut chumbak):
$$   - Solenoid ke ANDAR SOFT IRON ki rod (core) daal do - ye bahut STRONG
$$     magnet ban jaata, ise ELECTROMAGNET kehte.
$$   - SOFT IRON use hota kyunki current band karte hi uska magnetism khatam
$$     ho jaata (temporary magnet) - chaalu/band kar sakte.
   - Use: cranes me bhaari iron utha-na, electric bell, etc.

<<<PAGEBREAK>>>

4. FORCE ON A CURRENT-CARRYING CONDUCTOR
=========================================================
$$ Jab current wale conductor ko MAGNETIC FIELD me rakhte hain to us par
$$ ek FORCE lagta hai (conductor dhakela/hilta hai).
   - Oersted me current ne magnet (compass) ko hilaya; yaha ulta - magnet
     current wale taar par force lagata. (Action-reaction jaisa idea.)

$$ FLEMING'S LEFT-HAND RULE (force/motion ki direction - EXAM FAVOURITE):
$$   - Baaye (LEFT) haath ke THUMB, FOREFINGER aur MIDDLE finger ko
$$     ek dusre ke perpendicular (90 degree) faila lo.
$$   - FOREFINGER (pehli ungli)  = magnetic FIELD ki direction.
$$   - MIDDLE finger (beech wali) = CURRENT ki direction.
$$   - THUMB (angootha)          = FORCE / MOTION ki direction.
$$   (Yaad: thumb=Thrust/force, Fore=Field, Centre/Middle=Current.)

$$ KHAAS BAAT:
$$   - Force SABSE ZYADA tab jab current, field ke PERPENDICULAR (90 degree) ho.
$$   - Agar current field ke PARALLEL ho to force ZERO (kuch nahi hota).
   - Force badhega agar current badhao ya field strong karo.

<<<PAGEBREAK>>>

5. ELECTRIC MOTOR (VIDYUT MOTOR)
=========================================================
$$ ELECTRIC MOTOR = woh device jo ELECTRICAL energy ko MECHANICAL energy
$$ (ghoomne/rotation) me badalti hai.

$$ PRINCIPLE (siddhant):
$$   - Magnetic field me rakhe CURRENT-CARRYING COIL par force lagta hai
$$     (Fleming's left-hand rule), jisse coil GHOOMTI hai.

$$ SIMPLE WORKING:
$$   - Ek rectangular coil ko magnet ke N aur S poles ke beech rakha jaata.
$$   - Coil ke do side me current ULTI-ULTI (opposite) direction me behta,
$$     isliye unpar force bhi opposite direction me - ek side UPAR, dusri NEECHE.
$$   - Is wajah se coil par ghoomne wala asar (torque) banta -> coil rotate.

$$ SPLIT-RING / COMMUTATOR KA ROLE (bahut important):
$$   - Har aadhe (half) rotation ke baad coil me current ki direction ULAT
$$     deta hai SPLIT-RING (commutator).
$$   - Isse force ki direction sahi rehti aur coil EK HI direction me lagataar
$$     ghoomti rehti hai (warna aadha ghoom ke ruk jaati).
   - USES: electric fan, washing machine, mixer/grinder, pump, fridge, MP3
     player, computer ki drive - sab me motor lagti hai.

<<<PAGEBREAK>>>

6. ELECTROMAGNETIC INDUCTION (FARADAY)
=========================================================
$$ ELECTROMAGNETIC INDUCTION = jab kisi coil ke paas MAGNETIC FIELD BADALTA
$$ (change hota) hai, to coil me CURRENT apne-aap paida (induce) ho jaata hai.
$$   - Ise EMF/current "induce" hona kehte; ye khoj FARADAY ne ki.

$$ CURRENT KAISE INDUCE KARE (3 tarike):
$$   - Magnet ko coil ke paas/door tezi se HILAO (move karo).
$$   - Coil ko magnet ke paas hilao.
$$   - Paas wali dusri coil me current ON/OFF/change karo (field badlega).
$$   Yaad: KUCH BHI MOVE/CHANGE ho ke field badle -> current induce.

$$ FLEMING'S RIGHT-HAND RULE (induced current ki direction - EXAM FAVOURITE):
$$   - Daaye (RIGHT) haath ke THUMB, FOREFINGER, MIDDLE finger 90 degree par.
$$   - FOREFINGER = magnetic FIELD ki direction.
$$   - THUMB      = conductor ki MOTION (movement) ki direction.
$$   - MIDDLE finger = INDUCED CURRENT ki direction.
   (Motor me LEFT-hand rule, generator/induction me RIGHT-hand rule - mat bhulna.)

<<<PAGEBREAK>>>

7. ELECTRIC GENERATOR (DYNAMO)
=========================================================
$$ ELECTRIC GENERATOR = woh device jo MECHANICAL energy (ghoomna) ko
$$ ELECTRICAL energy me badalti hai - bilkul motor ka ULTA kaam.

$$ PRINCIPLE: ELECTROMAGNETIC INDUCTION (coil magnet ke field me ghoomti to
$$ usme current induce ho jaata - Fleming's right-hand rule se direction).

$$ AC GENERATOR vs DC GENERATOR:
$$   - AC GENERATOR: coil ke sire do alag-alag SLIP RINGS se jude hote.
$$     Output current har aadhe ghoom me direction badalta -> ALTERNATING (AC).
$$   - DC GENERATOR: SLIP rings ki jagah SPLIT RING (commutator) lagate, jo
$$     direction ulatne se rok ke ek hi disha ka current deta -> DIRECT (DC).
$$   - Yaad: SLIP ring -> AC, SPLIT ring -> DC.

$$ AC vs DC (difference):
$$   - AC apni direction time-time par badalta (India me 50 Hz, har 1/100 s me
$$     direction change). DC ek hi disha me behta.
$$   - AC ko door tak bhejna (transmit) aasaan aur kam loss - isliye ghar tak
$$     AC aata. DC battery/cell se milta.

<<<PAGEBREAK>>>

8. DOMESTIC ELECTRIC CIRCUITS (GHAR KI WIRING)
=========================================================
$$ Ghar me 3 taar (wires) aate hain - har ek ka colour aur kaam yaad rakho:
$$   - LIVE wire  : RED (ya BROWN) - ye current laata hai (high potential).
$$   - NEUTRAL    : BLACK (ya BLUE) - current wapas le jaata (low potential).
$$   - EARTH wire : GREEN - safety ke liye, zameen (earth) se juda.
   - Ghar me supply lagbhag 220 V (AC) par aati hai.

$$ EARTH WIRE aur EARTHING (safety):
$$   - Earth wire metal wale appliance (iron press, fridge body) ki body se
$$     jodte hain aur ye zameen me jaata.
$$   - Agar galti se live wire body ko chhoo jaaye, to current sidha EARTH me
$$     chala jaata - insaan ko bijli ka jhatka (shock) nahi lagta. SAFETY.

$$ FUSE (safety device):
$$   - Fuse = patli taar (low melting point) jo circuit me series me lagti.
$$   - Bahut zyada current behne par fuse GARAM ho ke PIGHAL (melt) jaati aur
$$     circuit TOOT jaata - appliance aur aag se bachaav. (Live wire me lagti.)

$$ OVERLOADING vs SHORT CIRCUIT (causes + danger):
$$   - OVERLOADING = ek saath bahut saare appliance chalana (ya voltage badhna)
$$     -> circuit me current limit se zyada -> taar garam -> aag ka khatra.
$$   - SHORT CIRCUIT = LIVE aur NEUTRAL taar seedhe jud jaayein (insulation
$$     khraab ho ke) -> resistance lagbhag zero -> current bahut bada -> garmi,
$$     spark, aag. Dono case me FUSE pighal ke circuit bachata hai.

<<<PAGEBREAK>>>

9. SOLVED EXAMPLES (HARDEST -> EASIEST)
=========================================================
$$ Ye type ke questions exam me pakka aate - khud likh ke practice karo.

EXAMPLE 1 (Hardest): Electric motor ka working samjhao - commutator/split-ring
   ka role kya hai?
   - Magnet ke beech current-carrying coil rakhte; coil ke do side me current
     opposite direction me behta, isliye Fleming's LEFT-hand rule se ek side par
     UPAR aur dusri par NEECHE force -> coil ghoomti (rotate).
   - SPLIT-RING (commutator) har aadhe rotation par coil me current ki
     direction ULAT deta, jisse force ki direction theek rehti aur coil
     EK HI disha me lagataar ghoomti rehti hai.

EXAMPLE 2: Electromagnetic induction kya hai, current kaise induce karoge,
   aur direction kaunse rule se?
   - Coil ke paas magnetic field BADLO (magnet ko coil ke paas/door tezi se
     hilao, ya paas wali coil me current ON/OFF karo) -> coil me current induce.
   - Induced current ki DIRECTION nikalne ke liye FLEMING'S RIGHT-HAND RULE:
     forefinger=field, thumb=motion, middle finger=induced current.

EXAMPLE 3: Ek taar me current upar (north) ki taraf beh raha aur magnetic field
   andar (paper ke andar) hai. Fleming's left-hand rule se force ki direction?
   - Left hand: forefinger = field (paper ke andar), middle finger = current
     (upar). Tab THUMB jis taraf -> wahi FORCE ki direction.
   - (Rule lagao: forefinger andar, middle upar -> thumb left/right me aayega
     us geometry ke hisaab se. Hamesha 3 ungliyan 90 degree par rakho.)

EXAMPLE 4: Seedhe taar me current upar ki taraf beh raha hai. Uske aas-paas
   magnetic field ki direction kaise pata karoge?
   - RIGHT-HAND THUMB RULE: taar ko seedhe haath me pakdo, angootha current
     (upar) ki taraf -> mudi ungliyan jis taraf ghoomti, wahi field ki disha.
   - Field = taar ke charo taraf CONCENTRIC CIRCLES (ek taraf clockwise dikhega,
     niche se dekho to anticlockwise).

EXAMPLE 5: AC generator aur DC generator me kya farak hai?
   - AC generator me coil ke sire SLIP RINGS se jude -> output ki direction
     badalti rehti (AC milta).
   - DC generator me SPLIT RING (commutator) lagta -> direction nahi badalti,
     ek hi disha ka current (DC) milta. Yaad: slip->AC, split->DC.

EXAMPLE 6: Earth wire aur fuse kyun use karte? Short circuit aur overloading me
   farak?
   - EARTH WIRE: appliance ki body ko zameen se jodta; live wire body ko chhoo
     jaaye to current earth me jaata -> shock se bachaav.
   - FUSE: zyada current par pighal ke circuit todti -> aag/damage se bachaav.
   - SHORT CIRCUIT = live aur neutral seedhe jud jaana (current achanak bahut
     bada). OVERLOADING = ek saath bahut appliance/zyada load se current limit
     paar. Dono me taar garam, aag ka khatra; fuse circuit bachati.

EXAMPLE 7 (Easiest): Magnetic field lines ki 2 properties batao aur ye kyun
   ek dusre ko cut nahi karti?
   - Properties: (i) bahar N se S ki taraf, band loops banti; (ii) paas-paas
     ho to field strong, door-door ho to weak.
   - Cut isliye nahi karti kyunki agar do lines cut karein to us point par
     field ki DO direction ho jaayengi - jo possible nahi (ek point par field
     ki sirf ek hi direction hoti).

<<<PAGEBREAK>>>

10. QUICK Q&A - PADHNE KE BAAD KHUD CHECK KARO
=========================================================
$$ Pehle khud answer socho, fir niche milao. Ye board-style questions hain.

Q1. Magnetic field lines kya hain aur inki direction kaise tay hoti?
A1. Woh imaginary lines jinke saath compass ka N pole point karta. Direction =
    us point par field/compass-N ki disha (bahar N se S ki taraf).

Q2. Field lines ek dusre ko cut kyun nahi karti?
A2. Agar cut karein to us point par field ki do direction ho jaaye, jo galat
    hai - ek point par field ki sirf ek direction hoti.

Q3. Oersted ne kya khoja?
A3. Current-carrying taar ke aas-paas magnetic field banta hai (paas rakhi
    compass needle deflect ho jaati).

Q4. Right-hand thumb rule batao.
A4. Taar ko seedhe haath me pakdo, angootha current ki disha me; mudi ungliyan
    magnetic field (lines) ki direction dikhati hain.

Q5. Solenoid ke andar field kaisa hota aur electromagnet kya hai?
A5. Solenoid ke andar UNIFORM field (bar magnet jaisa). Andar SOFT IRON core
    daalo to strong temporary magnet = ELECTROMAGNET.

Q6. Fleming's left-hand rule aur right-hand rule me kaunsa kab?
A6. LEFT-hand = current wale conductor par force/motion (motor) ke liye.
    RIGHT-hand = induced current (generator/induction) ki direction ke liye.

Q7. Electric motor aur generator me energy conversion?
A7. Motor: electrical -> mechanical. Generator: mechanical -> electrical (ulta).

Q8. AC aur DC me ek mukhya farak?
A8. AC apni direction time-time par badalta (50 Hz India); DC ek hi disha me
    behta. Slip ring -> AC, split ring -> DC.

Q9. Ghar ke 3 taar aur unke colour?
A9. Live = red/brown, Neutral = black/blue, Earth = green (safety ke liye).

Q10. Fuse circuit me kaam kaise karta?
A10. Zyada current par fuse ki patli taar garam ho ke pighal jaati, circuit
     toot jaata - appliance aur aag se bachaav (live wire me series me lagti).

=========================================================
EXAM STRATEGY (1 minute revision):
$$  - Field line properties (4 points) + cut kyun nahi karti - pakka likhna aao.
$$  - 3 rule clear rakho: Right-hand THUMB (straight wire field), Fleming
$$    LEFT-hand (force/motor), Fleming RIGHT-hand (induced current/generator).
$$  - Solenoid uniform field + electromagnet (soft iron core) yaad rakho.
$$  - Electric motor working + commutator/split-ring ka role likhna aana chahiye.
$$  - Electromagnetic induction + AC vs DC generator (slip ring vs split ring).
$$  - Domestic circuit: live/neutral/earth colour, earthing, fuse, short
$$    circuit vs overloading - safety wale points scoring hain.
@@  - CORE BASICS page (magnet, poles, current, AC/DC, field line idea) bhool
@@    jaao to wapas pehle padho - base strong rakho.
=========================================================
Generated by Kiro for Krishna1k - All the best!
"""


def to_markdown(content: str) -> str:
    """Convert the markup CONTENT into GitHub-friendly markdown."""
    out = ["# Magnetic Effects of Electric Current",
           "### NCERT Class 10 Science - Chapter 12 (Hinglish Detailed Notes)",
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
    pdf_path = here / "Science_Class10_Ch12_Magnetic_Effects_Current.pdf"
    md_path = here / "Science_Class10_Ch12_Magnetic_Effects_Current.md"

    pdf_utils.text_to_pdf(
        CONTENT,
        pdf_path,
        title="Magnetic Effects of Electric Current",
        subtitle="NCERT Class 10 Science - Ch 12 | Hinglish Detailed Notes",
    )
    md_path.write_text(to_markdown(CONTENT), encoding="utf-8")
    print(f"Wrote {md_path}")


if __name__ == "__main__":
    main()
