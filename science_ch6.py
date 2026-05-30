"""
science_ch6.py
--------------
Generates a detailed, simplified Hinglish study guide for
NCERT Class 10 Science, Chapter 6: "Control and Coordination".

Outputs:
  - Science_Class10_Ch6_Control_Coordination.pdf  (colour PDF)
  - Science_Class10_Ch6_Control_Coordination.md   (markdown, red/green via emoji)

Markup conventions inside CONTENT (handled by pdf_utils):
  @@  -> RED   line  (CORE BASICS / extra ke liye)
  $$  -> GREEN line  (exam me baar-baar aane wale topics)
  <<<PAGEBREAK>>>     -> nayi page
"""

import re
from pathlib import Path

import pdf_utils


CONTENT = r"""CONTROL AND COORDINATION
NCERT Class 10 Science - Chapter 6 (Hinglish Detailed Notes)
=========================================================

@@ COLOUR CODE: RED = Core Basics / extra help (Class 7-8-9 wali cheezein + base concepts).
$$ COLOUR CODE: GREEN = Board exam me ye topics BAAR-BAAR aate hain - pakka yaad karo.
   Baaki normal black text = main chapter content (detail me, simple bhasha me).

<<<PAGEBREAK>>>

CORE BASICS - PEHLE YE PADHO (CLASS 7-8-9 KA FOUNDATION)
=========================================================
@@ Tune 7-8-9 nahi padhi - koi tension nahi. Ye page is chapter ki base hai.
@@ Ek baar achhe se padh le, fir chapter aasaani se samajh aayega.

@@ 1) CELL kya hai:
@@    - Body ki sabse chhoti unit (building block). Sab kaam cells me hote hain.

@@ 2) TISSUE kya hai:
@@    - Ek jaise cells ka group jo milke ek kaam karta (e.g. nervous tissue,
@@      muscle tissue).

@@ 3) STIMULUS aur RESPONSE:
@@    - STIMULUS = bahar/andar se aaya koi change (light, garmi, awaaz, chubhan).
@@    - RESPONSE = us stimulus pe body ka reaction (haath hatana, aankh band).

@@ 4) GLAND kya hai:
@@    - Body ka woh ang jo koi useful chemical (juice/hormone) banata aur chhodta.

@@ 5) HORMONE kya hai (intro):
@@    - Chemical messenger jo gland banata; blood ke through travel karke door ke
@@      ang ko message deta (dheema par lambe samay ka control).

@@ 6) NEURON / NERVE kya hai (intro):
@@    - NEURON = nervous system ka cell (message le jaane wali "taar").
@@    - NERVE = bahut saare neuron fibre ka bundle (cable jaisa).

@@ 7) VOLUNTARY vs INVOLUNTARY action:
@@    - VOLUNTARY = jo hum soch ke, marzi se karte (likhna, chalna).
@@    - INVOLUNTARY = jo apne aap, bina soche hote (dil dhadakna, saans lena).

@@ 8) ENDOCRINE vs EXOCRINE gland (simple):
@@    - ENDOCRINE = DUCT nahi (ductless); hormone seedha BLOOD me chhodti.
@@    - EXOCRINE = DUCT (naali) ke through chhodti (jaise pasina, laar, paachak ras).

@@ 9) CONTROL dono me alag tarike se:
@@    - JANWAR (animals) = NERVOUS system + HORMONE (chemical) dono se control.
@@    - POUDHE (plants) = nervous system NAHI - sirf CHEMICAL/HORMONE se control.

<<<PAGEBREAK>>>

1. ANIMALS - NERVOUS SYSTEM
=========================================================
Janwar bahar ke changes (stimulus) ko sense karte aur turant response dete -
ye kaam NERVOUS SYSTEM karta hai (fast, electrical control).

1.1 NEURON - STRUCTURE AND FUNCTION
---------------------------------------------------------
$$ NEURON = nervous system ki structural + functional unit (sabse chhoti ikai).
$$ Parts (order me yaad rakho):
$$   - DENDRITE = jhaadi-numa sire; information/stimulus RECEIVE karte (input).
$$   - CELL BODY (cyton) = nucleus yahan; signal aage process hota.
$$   - AXON = lamba taar; message ko door LE JAATA (carry away).
$$   - NERVE ENDING / SYNAPSE = axon ke ant me gap (agle neuron/cell se jodta).

$$ INFORMATION KAISE TRAVEL KARTI (important):
$$   - Dendrite par stimulus -> ELECTRICAL impulse banta -> cell body -> axon ke
$$     end tak electrical signal jaata.
$$   - SYNAPSE (gap) ko electrical signal seedha cross nahi kar sakta - yahan
$$     CHEMICAL (neurotransmitter) release hota jo gap paar karke agle cell ke
$$     dendrite par naya electrical impulse bana deta.
$$   - Matlab: neuron ke ANDAR electrical, synapse par CHEMICAL transmission.

$$ NEURON KE TYPES (3):
$$   - SENSORY neuron = receptor se message CNS (brain/spinal cord) tak laata.
$$   - MOTOR neuron = CNS se message effector (muscle/gland) tak le jaata.
$$   - RELAY (inter) neuron = CNS ke andar sensory aur motor ko jodta.

<<<PAGEBREAK>>>

1.2 REFLEX ACTION AND REFLEX ARC
---------------------------------------------------------
$$ REFLEX ACTION = stimulus pe turant, apne aap (bina soche) hone wali response.
$$   Example: garam tawe/cheez ko chhute hi haath jhatke se hat jaata.

$$ REFLEX ARC = woh raasta jisse reflex signal jaata (brain ka wait nahi karta):
$$   RECEPTOR (skin) -> SENSORY neuron -> SPINAL CORD (relay neuron) ->
$$   MOTOR neuron -> EFFECTOR (muscle) -> action (haath hatna).

$$ REFLEX ARC kyun evolve hua / kyun zaroori:
$$   - Thinking (brain) ka process slow hai. Khatre me (garmi/chubhan) itni der
$$     me to nuksaan ho jaata.
$$   - Isliye signal ka shortcut SPINAL CORD se ban gaya -> response BAHUT FAST.
   @@ Brain ko baad me pata chalta ki "garam tha" - par haath pehle hi hat chuka.

1.3 HUMAN BRAIN
---------------------------------------------------------
Brain = sabse bada control centre. Spinal cord ke saath milke CENTRAL NERVOUS
SYSTEM (CNS) banata. Brain ke 3 main parts:

$$ (A) FOREBRAIN - sabse bada hissa (CEREBRUM):
$$     - Sochna, samajhna, yaad-dasht, intelligence (thinking).
$$     - VOLUNTARY actions ka control (marzi se hilna-dulna).
$$     - Senses ka centre - sunna, dekhna, sungh-na, swaad, chhuna.

$$ (B) MIDBRAIN:
$$     - Aankh/kaan ke kuch reflex; aage-peeche ke hisson ko jodta.

$$ (C) HINDBRAIN - 3 parts:
$$     - CEREBELLUM = posture aur BALANCE; movement ki PRECISION (seedha chalna,
$$       cycle chalana, pencil uthana - sab smooth + accurate banata).
$$     - MEDULLA OBLONGATA = INVOLUNTARY actions: heartbeat, saans (breathing),
$$       blood pressure (BP), ulti (vomiting), khaansi.
$$     - PONS = saans (respiration) control me madad; brain-cerebellum ke beech bridge.

$$ BRAIN KI PROTECTION (suraksha):
$$   - SKULL (cranium) = hard haddi ka box.
$$   - MENINGES = brain ke upar 3 jhilli (membrane) ki parat.
$$   - CEREBROSPINAL FLUID (CSF) = liquid cushion jo jhatke (shock) se bachata.

1.4 NERVOUS TISSUE SE ACTION KAISE HOTA
---------------------------------------------------------
- Jab muscle tak message pahunchta to MUSCLE CELLS apne andar ke khaas PROTEIN
  use karke apna SHAPE/length badalte (contract karte) -> body part hilta.

@@ NERVOUS SYSTEM KI LIMITATIONS (isliye hormone bhi chahiye):
@@   - Electrical impulse sirf unhi cells tak jaata jo nervous tissue se JUDE hain
@@     (har cell tak nahi pahunch sakta).
@@   - Ek baar signal bhejne ke baad cell ko "reset" hone me time lagta - to har
@@     jagah, continuous control mushkil.
@@   - Isliye body ek dusra (dheema par har cell tak pahunchne wala) system bhi
@@     use karti = CHEMICAL/HORMONAL communication.

<<<PAGEBREAK>>>

2. PLANTS - COORDINATION (NERVOUS SYSTEM NAHI)
=========================================================
Poudho me na brain, na nerves. Phir bhi stimulus pe response dete - SIRF
chemical (hormone) ke through. Plant ke movement 2 type ke:

$$ (a) GROWTH-DEPENDENT = TROPIC movement (badhne ke kaaran, slow, directional).
$$ (b) IMMEDIATE / NON-GROWTH = NASTIC movement (turant, bina growth ke).

2.1 TROPIC (DIRECTIONAL) MOVEMENTS
---------------------------------------------------------
$$ TROPISM = stimulus ki DIRECTION ke according plant part ka mudna/badhna.
$$   - PHOTOTROPISM = light ke according (shoot/tana light ki taraf = +ve).
$$   - GEOTROPISM (GRAVITROPISM) = gravity ke according: JADD (root) neeche ki
$$     taraf = +ve; TANA (shoot) upar ki taraf = -ve geotropism.
$$   - HYDROTROPISM = paani ke according (jadd paani ki taraf badhti).
$$   - CHEMOTROPISM = chemical ke according (e.g. POLLEN TUBE ka ovule ki taraf badhna).
$$   - THIGMOTROPISM = touch/support ke according (TENDRIL support se lipat jaati).

2.2 NASTIC MOVEMENT (NON-DIRECTIONAL)
---------------------------------------------------------
$$ Stimulus ki DIRECTION se matlab nahi; movement growth ke BINA, turant hoti.
$$ Example: TOUCH-ME-NOT (Mimosa pudica / chhui-mui) - chhute hi patte mud/band.
$$   - Kaaran: cells ke andar PAANI ki matra badal jaati (cell ka shape change),
$$     growth ki wajah se NAHI. Isliye thodi der me wapas khul bhi jaate.

2.3 PLANT HORMONES (PHYTOHORMONES)
---------------------------------------------------------
$$ Poudho ke chemical messengers jo growth/response control karte. 4 main:
$$   - AUXIN = cell ELONGATION (lambai badhana); PHOTOTROPISM isi se hota.
$$   - GIBBERELLIN = tana (stem) ki growth badhana.
$$   - CYTOKININ = cell DIVISION badhana; fruits aur seeds me zyada.
$$   - ABSCISIC ACID (ABA) = INHIBITOR (rokne wala) - growth ghatata, patte
$$     murjhana (wilting), STOMATA band karna.

<<<PAGEBREAK>>>

3. ANIMALS - HORMONES (ENDOCRINE SYSTEM)
=========================================================
$$ ENDOCRINE GLAND = DUCTLESS gland; hormone seedha BLOOD me chhodti, blood use
$$ poori body me pahuncha deta (target organ par asar).

3.1 MAIN GLANDS, HORMONES, FUNCTION, DEFICIENCY
---------------------------------------------------------
$$ ADRENALINE - gland: ADRENAL gland.
$$   Kaam: dar/emergency me "FIGHT-or-FLIGHT" - heartbeat tez, saans tez, blood
$$   muscles ki taraf - body ko ladne/bhaagne ke liye ready karta.

$$ THYROXINE - gland: THYROID.
$$   Kaam: metabolism (carbs, fat, protein) control. Banane ko IODINE chahiye.
$$   Kami (deficiency): GOITRE (gala phoolna) - isliye iodised namak khaate.

$$ GROWTH HORMONE - gland: PITUITARY (master gland).
$$   Kaam: body ki growth (lambai). Bachpan me KAM -> DWARFISM (baune rah jaana),
$$   ZYADA -> GIGANTISM (zaroorat se zyada lamba).

$$ INSULIN - gland: PANCREAS.
$$   Kaam: blood me SUGAR (glucose) level control karna.
$$   Kami: DIABETES (blood sugar high ho jaata).

$$ TESTOSTERONE - gland: TESTES (male).
$$   Kaam: ladko me puberty ke male changes (aawaz bhaari, baal aana).

$$ OESTROGEN - gland: OVARY (female).
$$   Kaam: ladkiyo me puberty ke female changes ka control.

3.2 FEEDBACK MECHANISM
---------------------------------------------------------
$$ Hormone ki MATRA (amount) body khud control karti = FEEDBACK mechanism.
$$ Example (insulin): khaana khaate hi blood SUGAR badhta -> pancreas zyada
$$   INSULIN chhodta -> sugar normal -> ab insulin ka secretion apne aap kam.
$$ Matlab: hormone "kab aur kitna" banega - ye blood me uske target level se tay
$$ hota (na zyada, na kam).

<<<PAGEBREAK>>>

4. SOLVED EXAMPLES (HARDEST -> EASIEST)
=========================================================
$$ Ye type ke questions exam me pakka aate - steps khud likhke practice karo.

EXAMPLE 1 (Hardest): Reflex arc ka poora pathway likho/describe karo aur batao
   ye brain wale raaste se FAST kyun hai.
   Pathway: RECEPTOR (skin) -> SENSORY neuron -> SPINAL CORD (relay neuron) ->
   MOTOR neuron -> EFFECTOR (muscle) -> haath hatna.
   Fast kyun: signal agar brain tak jaake "sochne" me time leta to der ho jaati;
   reflex arc me spinal cord turant motor neuron ko order de deta - response
   jhatpat. (Brain ko baad me pata chalta hai.)

EXAMPLE 2: Brain ke parts aur kaun kya control karta - table banao.
   Forebrain (Cerebrum) : sochna, yaad, intelligence, voluntary action, senses.
   Midbrain             : aankh/kaan ke reflex, beech ka link.
   Cerebellum           : posture, balance, movement ki precision.
   Medulla oblongata    : heartbeat, saans, BP, vomiting (involuntary).
   Pons                 : saans control + bridge.

EXAMPLE 3: Gland - Hormone - Function - Deficiency match karo.
   Thyroid    -> Thyroxine      -> metabolism control -> kami: GOITRE.
   Pituitary  -> Growth hormone -> growth -> kami: dwarfism, zyada: gigantism.
   Pancreas   -> Insulin        -> blood sugar control -> kami: diabetes.
   Adrenal    -> Adrenaline     -> fight-or-flight (emergency hormone).

EXAMPLE 4: Phototropism ko AUXIN ke through samjhao.
   Tana light ki taraf mudta. Light wali side me auxin KAM, shade (andheri) side
   me auxin ZYADA jama. Auxin cell ko lamba (elongate) karta, isliye shade side
   zyada badhti -> tana light ki taraf jhuk jaata. (Positive phototropism.)

EXAMPLE 5: Tropic aur Nastic movement me farak, ek-ek example.
   Tropic = direction ke according, GROWTH se, slow (e.g. phototropism - tana
   light ki taraf). Nastic = direction se matlab nahi, growth ke BINA, turant
   (e.g. touch-me-not ke patte chhute hi band).

EXAMPLE 6: Neuron ke parts aur impulse kaise travel karta (synapse sahit)?
   Parts: dendrite (receive) -> cell body -> axon (carry away) -> synapse.
   Travel: neuron ke andar ELECTRICAL impulse; synapse (gap) par CHEMICAL release
   ho ke gap paar karta aur agle neuron me naya electrical impulse banata.

EXAMPLE 7 (Easiest): Iodised (iodine wala) namak khaane ki salah kyun di jaati?
   Thyroid ko THYROXINE banane ke liye IODINE chahiye. Iodine ki kami se GOITRE
   (gala phoolna) ho jaata - isliye iodised namak recommend karte.

<<<PAGEBREAK>>>

5. QUICK Q&A - PADHNE KE BAAD KHUD CHECK KARO
=========================================================
$$ Pehle khud answer socho, fir niche milao. Ye board-style questions hain.

Q1. Neuron ki kya kya parts hain?
A1. Dendrite (receive), cell body (cyton), axon (carry away), nerve ending/
    synapse. Information dendrite se le ke axon end tak jaati.

Q2. Reflex action kya hai? Ek example.
A2. Bina soche, turant hone wali response. Example: garam cheez chhute hi haath
    hatna.

Q3. Synapse kya hai aur yahan signal kaise paar hota?
A3. Do neuron ke beech ka GAP. Yahan chemical (neurotransmitter) release ho ke
    gap paar karta aur agle neuron me electrical impulse bana deta.

Q4. Medulla oblongata kaunse kaam control karta?
A4. Involuntary - heartbeat, saans, blood pressure, vomiting.

Q5. Cerebellum ka kaam?
A5. Posture, balance aur body movements ki precision (smooth, controlled chalna).

Q6. Brain ki teen suraksha (protection) batao.
A6. Skull (cranium), meninges (3 jhilli), aur cerebrospinal fluid (CSF cushion).

Q7. Geotropism me root aur shoot kaisa behave karte?
A7. Root gravity ki taraf (neeche) = +ve geotropism; shoot gravity ke ulta
    (upar) = -ve geotropism.

Q8. Auxin kya kaam karta?
A8. Cell ki lambai (elongation) badhata aur phototropism me madad karta.

Q9. Insulin kya karta aur kami se kya hota?
A9. Blood me sugar (glucose) control karta. Kami se DIABETES (sugar high).

Q10. Endocrine aur exocrine gland me farak?
A10. Endocrine = ductless, hormone seedha blood me (e.g. thyroid). Exocrine =
     duct se chhodti (e.g. laar, pasina, paachak ras).

=========================================================
EXAM STRATEGY (1 minute revision):
$$  - Neuron ke parts + synapse par chemical transmission - diagram aana chahiye.
$$  - Reflex arc ka pura pathway (receptor -> ... -> effector) ratlo.
$$  - Brain parts + kaun kya control - cerebrum/cerebellum/medulla pakka.
$$  - Tropic movements 5 (photo/geo/hydro/chemo/thigmo) + nastic ka example.
$$  - Phytohormones 4 (auxin, gibberellin, cytokinin, ABA) ka kaam.
$$  - Endocrine gland + hormone + function + DEFICIENCY (thyroxine/goitre,
$$    insulin/diabetes, growth hormone) + feedback mechanism.
@@  - CORE BASICS page (cell, stimulus-response, gland, hormone, voluntary vs
@@    involuntary) bhool jaao to wapas pehle padho - base strong rakho.
=========================================================
Generated by Kiro for Krishna1k - All the best!
"""


def to_markdown(content: str) -> str:
    """Convert the markup CONTENT into GitHub-friendly markdown."""
    out = ["# Control and Coordination",
           "### NCERT Class 10 Science - Chapter 6 (Hinglish Detailed Notes)",
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
    pdf_path = here / "Science_Class10_Ch6_Control_Coordination.pdf"
    md_path = here / "Science_Class10_Ch6_Control_Coordination.md"

    pdf_utils.text_to_pdf(
        CONTENT,
        pdf_path,
        title="Control and Coordination",
        subtitle="NCERT Class 10 Science - Ch 6 | Hinglish Detailed Notes",
    )
    md_path.write_text(to_markdown(CONTENT), encoding="utf-8")
    print(f"Wrote {md_path}")


if __name__ == "__main__":
    main()
