"""
science_ch11.py
---------------
Generates a detailed, simplified Hinglish study guide for
NCERT Class 10 Science, Chapter 11: "Electricity".

Outputs:
  - Science_Class10_Ch11_Electricity.pdf  (colour PDF)
  - Science_Class10_Ch11_Electricity.md   (markdown, red/green via emoji)

Markup conventions inside CONTENT (handled by pdf_utils):
  @@  -> RED   line  (CORE BASICS / extra ke liye)
  $$  -> GREEN line  (exam me baar-baar aane wale topics)
  <<<PAGEBREAK>>>     -> nayi page
"""

import re
from pathlib import Path

import pdf_utils


CONTENT = r"""ELECTRICITY
NCERT Class 10 Science - Chapter 11 (Hinglish Detailed Notes)
=========================================================

@@ COLOUR CODE: RED = Core Basics / extra help (Class 7-8-9 wali cheezein jo yaad honi chahiye).
$$ COLOUR CODE: GREEN = Board exam me ye topics BAAR-BAAR aate hain - pakka yaad karo.
   Baaki normal black text = main chapter content (detail me, simple bhasha me).

<<<PAGEBREAK>>>

CORE BASICS - PEHLE YE PADHO (CLASS 7-8-9 KA FOUNDATION)
=========================================================
@@ Tune 7-8-9 nahi padhi - koi tension nahi. Ye page is chapter ki base hai.
@@ Numerical-heavy chapter hai, isliye base + formula rearrange karna pakka aana chahiye.

@@ 1) ELECTRIC CHARGE kya hai?
@@    - Har cheez atom se bani; atom me electron (-ve) aur proton (+ve) hote.
@@    - ELECTRON ke paas chhota -ve charge hota. Charge ka SI unit = COULOMB (C).
@@    - 1 electron ka charge = 1.6 x 10^-19 C (yaani 1 C me ~6.25 x 10^18 electron).
@@    - Charge ka behna (flow) hi CURRENT kehlata hai.

@@ 2) CONDUCTOR vs INSULATOR:
@@    - CONDUCTOR = current paas hone de (metal: Cu, Al; free electron hote).
@@    - INSULATOR = current na de (rubber, plastic, wood, glass).

@@ 3) CELL aur BATTERY:
@@    - CELL = ek device jo chemical energy ko electric energy me badle; do
@@      terminal hote - bada/lamba = +ve, chhota = -ve.
@@    - BATTERY = do ya zyada cell ka combination (zyada voltage ke liye).

@@ 4) CIRCUIT kya hai?
@@    - CIRCUIT = ek BAND (closed) raasta jisme current ghoom ke wapas aaye.
@@    - Switch ON = circuit closed (current chale); switch OFF = open (na chale).

@@ 5) COMMON CIRCUIT SYMBOLS (yaad rakho - diagram me kaam aayenge):
@@    - Cell        -> ek lamba patli line (+) aur ek chhoti moti line (-).
@@    - Battery     -> do ya zyada cell side by side.
@@    - Bulb        -> circle ke andar cross (X) ya loop (filament).
@@    - Switch/Key  -> ek gap with ek chhoti line (open/close).
@@    - Wire/Conductor -> seedhi line.
@@    - Resistor    -> ek rectangle (box) ya zig-zag line.
@@    - Ammeter     -> circle ke andar letter A.
@@    - Voltmeter   -> circle ke andar letter V.

@@ 6) CURRENT aur VOLTAGE simple words me:
@@    - CURRENT (I) = wire me charge kitni tezi se beh raha (paani ke flow jaisa).
@@    - VOLTAGE/POTENTIAL DIFFERENCE (V) = charge ko dhakelne wala "push"
@@      (paani ke pipe me pressure jaisa). Cell ye push deti hai.

@@ 7) SERIES vs PARALLEL (intro):
@@    - SERIES = sab components ek hi line/raaste me ek ke baad ek jude.
@@    - PARALLEL = components alag-alag branch me jude (ek hi do point ke beech).

@@ 8) UNITS TABLE (is chapter ke main units):
@@    - Current (I)            -> AMPERE (A)
@@    - Charge (Q)             -> COULOMB (C)
@@    - Potential diff (V)     -> VOLT (V)
@@    - Resistance (R)         -> OHM (ohm)
@@    - Resistivity (rho)      -> ohm*m (ohm metre)
@@    - Power (P)              -> WATT (W)
@@    - Energy                 -> JOULE (J) ya kWh (kilowatt-hour)

@@ 9) FORMULA REARRANGE karna (basic algebra - bahut zaroori):
@@    - Agar V = I R hai to: I = V / R  aur  R = V / I.
@@    - Yaani jis cheez ko nikalna ho, use akela karo, baaki cheezein dusri taraf.
@@    - Triangle trick: V upar, (I R) niche -> ungli se dhako jo chahiye.
@@    - Units bhi saath le ke chalo (V = volt, A = ampere, ohm = ohm).

<<<PAGEBREAK>>>

1. ELECTRIC CURRENT (VIDYUT DHARA)
=========================================================
$$ DEFINITION: Electric current = kisi conductor ke cross-section se per second
$$ behne wale charge ki maatra. Yaani current = charge / time.

$$ FORMULA:   I = Q / t
$$   - I = current (ampere, A), Q = charge (coulomb, C), t = time (second, s).
$$   - Isse: Q = I x t  aur  t = Q / I.

$$ UNIT: AMPERE (A).  1 A = 1 C / s
$$   - Matlab agar 1 second me 1 coulomb charge beh raha to current = 1 ampere.
   - Chhoti current ke liye: 1 mA (milliampere) = 10^-3 A,
     1 microampere = 10^-6 A.

$$ CURRENT KI DIRECTION (exam favourite):
$$   - CONVENTIONAL current ki direction = +ve charge ke behne ki direction
$$     (yaani +ve terminal se -ve terminal taraf bahar circuit me).
$$   - ELECTRON asal me -ve terminal se +ve terminal jaate (ulti direction).
$$   - To conventional current, electron flow ke ULT (opposite) maana jaata.

$$ MAAPNA (measure): current AMMETER se naapte.
$$   - Ammeter ko hamesha SERIES me jodte (jis component me current naapni ho).
$$   - Ideal ammeter ka resistance ZERO (taaki current par asar na pade).

<<<PAGEBREAK>>>

2. ELECTRIC POTENTIAL & POTENTIAL DIFFERENCE
=========================================================
$$ POTENTIAL DIFFERENCE (V) = do point ke beech unit charge ko le jaane me
$$ kiya gaya KAAM (work). Yahi charge ko circuit me dhakelta hai.

$$ FORMULA:   V = W / Q
$$   - V = potential difference (volt, V), W = work/energy (joule, J),
$$     Q = charge (coulomb, C).
$$   - Isse: W = V x Q  aur  Q = W / V.

$$ UNIT: VOLT (V).  1 V = 1 J / C
$$   - Matlab 1 coulomb charge ko le jaane me 1 joule kaam lage to V = 1 volt.

$$ MAAPNA (measure): potential difference VOLTMETER se naapte.
$$   - Voltmeter ko hamesha PARALLEL me jodte (jin do point ke beech V naapni ho).
$$   - Ideal voltmeter ka resistance INFINITE (bahut bada) hota.

   @@ Yaad rakhne ki trick:
   @@   - Ammeter -> A -> "A" se "series" (current naapta, series me).
   @@   - Voltmeter -> Parallel me (potential difference naapta).

<<<PAGEBREAK>>>

3. CIRCUIT DIAGRAM & SYMBOLS
=========================================================
   - Circuit diagram = circuit ko symbols se draw karna (asli device ke bajaye).
   - Faayda: samajhna aur banana aasaan, sabhi same symbol use karte.

   COMMON SYMBOLS (revision):
   - Cell / Battery, Bulb, Switch (key), Wire, Resistor (box/zig-zag),
     Ammeter (A in circle, series), Voltmeter (V in circle, parallel),
     Variable resistor / Rheostat (resistor with arrow).

   - Ek simple circuit: Cell -> switch -> bulb/resistor -> wapas cell.
     Ammeter series me, voltmeter resistor ke parallel me.

<<<PAGEBREAK>>>

4. OHM'S LAW (BAHUT IMPORTANT)
=========================================================
$$ OHM'S LAW: Constant temperature par, ek conductor me behne wali current (I)
$$ uske beech ke potential difference (V) ke DIRECTLY PROPORTIONAL hoti hai.
$$   V proportional to I   =>   V = I R

$$ FORMULA:   V = I R
$$   - V = potential difference (V), I = current (A), R = resistance (ohm).
$$   - Isse:  I = V / R   aur   R = V / I.

$$ V-I GRAPH:
$$   - V ko y-axis, I ko x-axis par lo -> graph ek SEEDHI LINE (straight line)
$$     origin se hoti hui aati hai.
$$   - Line ka SLOPE = V / I = R (resistance). Zyada slope -> zyada resistance.

$$ RESISTANCE (R):
$$   - R = V / I. Ye conductor ka current ke flow ke against "rukaawat" (opposition).
$$   - UNIT: OHM (likhte: ohm). 1 ohm = 1 volt / 1 ampere.
$$   - 1 ohm = jab 1 V lagane par 1 A current behti.

   @@ Note: jo conductor Ohm's law follow kare = OHMIC (e.g. metal wire).
   @@ Jo na follow kare (graph straight line na ho) = NON-OHMIC (e.g. bulb, diode).

<<<PAGEBREAK>>>

5. RESISTANCE & FACTORS (RESISTIVITY)
=========================================================
$$ Conductor ka resistance (R) in cheezon par depend karta hai:
$$   (i)   LENGTH (L): R, length ke DIRECTLY proportional. Lamba taar -> zyada R.
$$   (ii)  AREA (A): R, cross-section area ke INVERSELY proportional.
$$         Mota taar (zyada area) -> kam R.
$$   (iii) MATERIAL: har material ka apna RESISTIVITY (rho) hota.
$$   (iv)  TEMPERATURE: temperature badhne par (metal me) R badh jaata.

$$ FORMULA:   R = rho * L / A
$$   - rho (rho) = resistivity, L = length (m), A = area (m^2).
$$   - Isse:  rho = R * A / L.

$$ RESISTIVITY (rho):
$$   - DEFINITION: rho = us material ke 1 m lambe aur 1 m^2 area wale tukde ka
$$     resistance. Ye material ki apni property hai (size par depend nahi karti).
$$   - UNIT: ohm*m (ohm metre).

$$ CONDUCTOR vs INSULATOR by resistivity:
$$   - CONDUCTOR (metal): bahut KAM resistivity (10^-8 ohm*m range).
$$   - INSULATOR (rubber, glass): bahut ZYADA resistivity (10^12 ohm*m range).
$$   - ALLOY (nichrome, manganin): conductor se zyada resistivity + heat me
$$     jaldi oxidise nahi hote -> isiliye heating elements me use hote.

   @@ Note: silver sabse achha conductor (sabse kam resistivity), uske baad copper.
   @@ Ghar ki wiring me COPPER / ALUMINIUM use hota (kam resistivity, saste).

<<<PAGEBREAK>>>

6. RESISTORS IN SERIES
=========================================================
$$ SERIES me resistors ek ke baad ek (single line) jude hote.
$$ KEY POINTS:
$$   - Har resistor me SAME current (I) behti.
$$   - Total voltage = har resistor ke voltage ka JOD (sum):
$$     V = V1 + V2 + V3.
$$   - EQUIVALENT (total) RESISTANCE:  Rs = R1 + R2 + R3
$$   - Series me total resistance hamesha sabse BADE resistor se bhi ZYADA hoti.

   @@ Drawback: ek component fuse/kharab ho to poora circuit band (purani jhaalar
   @@ ki tarah - ek bulb gaya to sab band). Isliye ghar me series use nahi karte.

7. RESISTORS IN PARALLEL
=========================================================
$$ PARALLEL me sab resistors ek hi do point ke beech alag-alag branch me jude.
$$ KEY POINTS:
$$   - Har resistor par SAME voltage (V) lagta.
$$   - Total current = har branch ki current ka JOD: I = I1 + I2 + I3.
$$   - EQUIVALENT RESISTANCE:  1 / Rp = 1/R1 + 1/R2 + 1/R3
$$   - Parallel me total resistance hamesha sabse CHHOTE resistor se bhi KAM hoti.

$$ GHAR KE APPLIANCES PARALLEL ME KYUN? (exam me pakka aata)
$$   (i)   Har appliance ko same full voltage (220 V) milta.
$$   (ii)  Ek band ho to baaki chalte rehte (independent on/off).
$$   (iii) Har device apni zaroorat ki current le sakta (total R kam -> zyada current).

<<<PAGEBREAK>>>

8. HEATING EFFECT OF CURRENT (JOULE'S LAW)
=========================================================
$$ Jab current resistor se behti to resistance ki wajah se HEAT paida hoti -
$$ isko current ka HEATING EFFECT kehte.

$$ JOULE'S LAW OF HEATING:  H = I^2 * R * t
$$   - H = heat (joule, J), I = current (A), R = resistance (ohm), t = time (s).
$$   - Heat directly proportional to: I ke square, R, aur time t.

   Why heat? Current behne wale electron, conductor ke ions se takraate, jisse
   energy heat ke roop me release hoti.

$$ APPLICATIONS (heating effect ka use):
$$   - ELECTRIC HEATER / IRON / TOASTER / GEYSER: nichrome alloy ka coil
$$     (high resistivity + high melting point) garam ho jaata.
$$   - ELECTRIC BULB: tungsten FILAMENT (bahut high melting point ~3380 C)
$$     garam ho ke chamakta (roshni deta).
$$   - ELECTRIC FUSE (safety device): niche detail me.

$$ ELECTRIC FUSE (bahut important):
$$   - Ek patla taar (tin + lead alloy) jiska melting point KAM hota.
$$   - Circuit ke SERIES me lagaya jaata.
$$   - Jab current safe limit se zyada ho jaye (short circuit / overload), fuse
$$     wire H = I^2 R t se garam ho ke PIGHAL jaata -> circuit TOOT jaata.
$$   - Isse appliance aur aag se bachaav hota. Yahi fuse ka kaam hai.

<<<PAGEBREAK>>>

9. ELECTRIC POWER (VIDYUT SHAKTI)
=========================================================
$$ ELECTRIC POWER (P) = per second me use/kharch hone wali electric energy (rate).

$$ FORMULAE (teeno yaad rakho):
$$   P = V I        (power = voltage x current)
$$   P = I^2 * R    (V = IR daal ke)
$$   P = V^2 / R    (I = V/R daal ke)
$$   - P = power (watt, W), V = volt, I = ampere, R = ohm.

$$ UNIT: WATT (W).  1 W = 1 V x 1 A = 1 J/s.
$$   - Bada unit: 1 kilowatt (kW) = 1000 W.

$$ ELECTRIC ENERGY:  E = P x t  (power x time).
$$   - SI unit = JOULE (J). Par bijli ka bill JOULE me nahi, bada unit chahiye.

$$ COMMERCIAL UNIT OF ENERGY = KILOWATT-HOUR (kWh) - "1 UNIT" of electricity.
$$   - 1 kWh = 1 kW ka appliance 1 ghante (hour) chalane par use hui energy.
$$   - CONVERSION:  1 kWh = 1000 W x 3600 s = 3.6 x 10^6 J.

$$ ELECTRICITY BILL - UNITS KAISE NIKALE:
$$   - Units (kWh) = Power(kW) x time(hours used).
$$   - Total units x rate-per-unit = bill amount.
$$   - Tip: Watt ko 1000 se divide karke kW banao; minutes ko 60 se divide
$$     karke hours banao.

<<<PAGEBREAK>>>

10. SOLVED EXAMPLES (HARDEST -> EASIEST)
=========================================================
$$ Ye type ke numericals exam me pakka aate - steps + UNITS khud likhke practice karo.

EXAMPLE 1 (Hardest): Combination - 6 ohm aur 3 ohm PARALLEL me hain, aur ye
   combination 4 ohm ke saath SERIES me. Source = 12 V. Equivalent R aur total
   current nikaalo.
   Step 1 - Parallel part (6 aur 3):
      1/Rp = 1/6 + 1/3 = 1/6 + 2/6 = 3/6 = 1/2  ->  Rp = 2 ohm.
   Step 2 - Ab Rp (2 ohm) series me 4 ohm ke saath:
      R(total) = 2 + 4 = 6 ohm.
   Step 3 - Total current (Ohm's law):
      I = V / R = 12 / 6 = 2 A.
   ANSWER: Equivalent R = 6 ohm, total current = 2 A.

EXAMPLE 2: Parallel - 4 ohm aur 6 ohm parallel me 12 V se jude. Rp aur har branch
   ki current nikaalo.
   Step 1 - Equivalent:
      1/Rp = 1/4 + 1/6 = 3/12 + 2/12 = 5/12  ->  Rp = 12/5 = 2.4 ohm.
   Step 2 - Parallel me har branch par same V = 12 V:
      I1 = V/R1 = 12/4 = 3 A
      I2 = V/R2 = 12/6 = 2 A
   Step 3 - Check total: I = I1 + I2 = 3 + 2 = 5 A (= 12/2.4, sahi).
   ANSWER: Rp = 2.4 ohm, I1 = 3 A, I2 = 2 A.

EXAMPLE 3: Power & bill - ek 1000 W (1 kW) heater roz 2 ghante, 30 din chalta.
   Rate = Rs 5 per unit. Mahine ka bill nikaalo.
   Step 1 - Power = 1000 W = 1 kW.
   Step 2 - Time = 2 h/day x 30 = 60 hours.
   Step 3 - Energy = P x t = 1 kW x 60 h = 60 kWh (= 60 units).
   Step 4 - Bill = 60 x 5 = Rs 300.
   ANSWER: 60 units, bill = Rs 300.

EXAMPLE 4: Joule heating - ek 5 ohm resistor me 2 A current 5 minute behti.
   Kitni heat (H) paida hui?
   Step 1 - t ko second me: 5 min = 5 x 60 = 300 s.
   Step 2 - H = I^2 * R * t = (2)^2 x 5 x 300 = 4 x 5 x 300 = 6000 J.
   ANSWER: H = 6000 J (= 6 kJ).

EXAMPLE 5: Ohm's law - ek bulb par 220 V lagne par 0.5 A current behti.
   Resistance nikaalo.
   R = V / I = 220 / 0.5 = 440 ohm.
   ANSWER: R = 440 ohm.

EXAMPLE 6: R = rho*L/A - agar ek taar ki LENGTH double kar di jaye (area same),
   to resistance par kya asar? Aur agar AREA double ho (length same) to?
   - R proportional to L: length double -> R bhi DOUBLE (2 guna).
   - R proportional to 1/A: area double -> R HALF (aadha) ho jaata.
   ANSWER: length double => R x2 ; area double => R /2.

EXAMPLE 7 (Easiest): I = Q/t - ek conductor se 60 C charge 2 minute me behta.
   Current nikaalo.
   Step 1 - t = 2 min = 120 s.
   Step 2 - I = Q / t = 60 / 120 = 0.5 A.
   ANSWER: I = 0.5 A.

<<<PAGEBREAK>>>

11. QUICK Q&A - PADHNE KE BAAD KHUD CHECK KARO
=========================================================
$$ Pehle khud answer socho, fir niche milao. Ye board-style questions hain.

Q1. Electric current kya hai aur uska SI unit?
A1. Per second behne wala charge; I = Q/t. SI unit = ampere (A), 1 A = 1 C/s.

Q2. Ammeter aur Voltmeter circuit me kaise jodte hain?
A2. Ammeter SERIES me (current naapne), Voltmeter PARALLEL me (potential
    difference naapne). Ideal ammeter R = 0, ideal voltmeter R = infinite.

Q3. Ohm's law likho aur V-I graph kaisa hota?
A3. Constant temp par V proportional to I, yaani V = IR. V-I graph origin se
    nikalti SEEDHI LINE; slope = R.

Q4. Resistance kin cheezon par depend karta? Formula?
A4. Length (proportional L), area (proportional 1/A), material (rho), temperature.
    R = rho*L/A. Resistivity ka unit = ohm*m.

Q5. Series me equivalent resistance aur ek nuksan?
A5. Rs = R1 + R2 + R3. Nuksan: ek component kharab to poora circuit band.

Q6. Parallel ka formula aur ghar me parallel kyun?
A6. 1/Rp = 1/R1 + 1/R2 + ... Ghar me: har appliance ko full voltage milta aur
    ek band ho to baaki chalte.

Q7. Joule's law of heating likho aur ek application.
A7. H = I^2 * R * t. Application: electric heater/iron/bulb filament/fuse.

Q8. Electric fuse kaise kaam karta?
A8. Kam melting point ka patla taar series me; zyada current par H = I^2 R t se
    pighal ke circuit tod deta (overload/short circuit se bachaav).

Q9. Electric power ke teeno formula aur unit?
A9. P = VI = I^2 R = V^2 / R. Unit = watt (W); 1 W = 1 J/s.

Q10. 1 unit bijli = kitna? (kWh aur joule me)
A10. 1 unit = 1 kWh = 1000 W x 3600 s = 3.6 x 10^6 J.

=========================================================
EXAM STRATEGY (1 minute revision):
$$  - Ohm's law V = IR + V-I straight line graph (slope = R) - pakka aata.
$$  - R = rho*L/A + 4 factors (length, area, material, temperature).
$$  - Series Rs = R1+R2+R3 ; Parallel 1/Rp = 1/R1+1/R2+... (signs/steps yaad).
$$  - Joule's law H = I^2 R t + fuse working - scoring topic.
$$  - Power P = VI = I^2 R = V^2/R aur 1 kWh = 3.6 x 10^6 J + bill nikaalna.
$$  - Numericals me UNITS likhna mat bhoolo (marks katte hain warna).
@@  - CORE BASICS page (charge, circuit, symbols, formula rearrange) bhool jaao
@@    to wapas pehle padho - base strong rakho.
=========================================================
Generated by Kiro for Krishna1k - All the best!
"""


def to_markdown(content: str) -> str:
    """Convert the markup CONTENT into GitHub-friendly markdown."""
    out = ["# Electricity",
           "### NCERT Class 10 Science - Chapter 11 (Hinglish Detailed Notes)",
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
    pdf_path = here / "Science_Class10_Ch11_Electricity.pdf"
    md_path = here / "Science_Class10_Ch11_Electricity.md"

    pdf_utils.text_to_pdf(
        CONTENT,
        pdf_path,
        title="Electricity",
        subtitle="NCERT Class 10 Science - Ch 11 | Hinglish Detailed Notes",
    )
    md_path.write_text(to_markdown(CONTENT), encoding="utf-8")
    print(f"Wrote {md_path}")


if __name__ == "__main__":
    main()
