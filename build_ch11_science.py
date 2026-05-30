"""
Build Class 10 Science Chapter 11 study PDF: "Electricity"
Hinglish. Markup: @@ RED (core basics), $$ GREEN (exam favourite), ## header.
Run: python3 build_ch11_science.py
"""
from pdf_utils import build_pdf

CONTENT = r"""
==========================================

@@PART A - CORE BASICS (MISS MAT KARNA)
@@Class 7-8 ki yeh cheezein pehle pakki karo, warna Ch11 samajh nahi aayega.

## 1. Charge aur Current ka idea (Class 8)

@@Electric charge = matter ka woh property jisse bijli ka asar hota.
@@   Charge ka unit = COULOMB (C). Electron par -ve charge.
@@Electric current = charge ka flow (behaav). Unit = AMPERE (A).
@@Conductor = bijli pass kare (metal, copper). Insulator = na kare (rubber, plastic).

## 2. Circuit ka idea (Class 7-8)

@@Circuit = closed (band) loop jisme current behti.
@@Cell/Battery = current ka source (energy deti). Switch = on/off.
@@Open circuit = toota (current nahi); Closed = jud-a (current behti).
@@Current cell ke +ve se -ve terminal ki taraf behti (conventional).

## 3. Symbols (RATTA - circuit diagram ke liye)

@@Cell: lambi line (+), chhoti moti line (-). Battery: 2+ cells.
@@Resistor: zigzag ya rectangle box. Bulb: cross wala circle.
@@Ammeter (A): current naapta (series me). Voltmeter (V): voltage (parallel me).

## 4. Maths basics (numericals ke liye)

@@Formula me units sahi rakho (V volt, I ampere, R ohm).
@@Cross-multiply, fraction jodna (1/R1 + 1/R2), reciprocal lena aana chahiye.
@@Powers of 10: kilo = 1000, milli = 1/1000.

## 5. Energy aur Power (Class 8 idea)

@@Energy = kaam karne ki capacity (unit Joule J).
@@Power = energy use hone ki RATE (per second). Unit Watt (W). 1W = 1J/s.

@@-- END OF CORE BASICS (RED) PAGE --

<<<PAGEBREAK>>>

==========================================

## PART B - CHAPTER KA MAIN CONTENT
## Class 10 Science | Ch 11: Electricity

$$[GREEN = board exam me baar-baar poocha jaata hai]

## 1. Electric Current aur Potential Difference [IMPORTANT]

$$Electric current (I) = charge flow ki rate.  I = Q / t
$$   Q = charge (coulomb), t = time (second). Unit: 1 ampere = 1 C/s.
$$1 electron charge = 1.6 x 10^-19 C. (1 coulomb = ~6.25 x 10^18 electrons.)
$$Potential difference (V) = do point ke beech charge ko move karne me kiya
$$   gaya kaam per unit charge.  V = W / Q. Unit = VOLT (V). 1V = 1 J/C.
$$Voltmeter parallel me, Ammeter series me lagta.

## 2. Ohm's Law [TOP EXAM AREA]

$$Ohm's Law: constant temperature par conductor me current (I) uske do siron ke
$$   beech voltage (V) ke SEEDHE proportional hoti.
$$   V = I R   (R = resistance, constant).
$$Resistance (R) = current ke behaav ka virodh (opposition). Unit = OHM (symbol).
$$V vs I graph = SEEDHI line (straight line through origin) -> slope = R.

## 3. Resistance kis par depend karta [VERY IMPORTANT]

$$R depend karta:
$$   (1) Length (L) par: R seedha proportional (lamba taar -> R jyada).
$$   (2) Area (A) par: R ulta proportional (mota taar -> R kam).
$$   (3) Material par: resistivity (rho) - har material ka apna.
$$   (4) Temperature: badhne par R aam taur par badhta.
$$Formula:  R = rho * L / A   (rho = resistivity, unit ohm-metre).
$$Resistivity: conductor (metal) bahut kam; insulator bahut zyada.
$$   Alloys (nichrome, manganin) ki resistivity zyada + temperature se kam asar
$$   -> isliye heating element (heater/iron) me nichrome use hota.

## 4. Series Combination [TOP EXAM AREA]

$$Series = resistors ek ke baad ek (single path).
$$   - Current (I) SAME har resistor me.
$$   - Voltage baant-ta: V = V1 + V2 + V3.
$$   - Total resistance:  Rs = R1 + R2 + R3  (badhta jaata, sabse jyada).
$$Nuksaan: ek component fail -> poora circuit band (jaise purani LED jhaalar).

## 5. Parallel Combination [TOP EXAM AREA]

$$Parallel = resistors alag-alag branch me (multiple path).
$$   - Voltage (V) SAME har resistor par.
$$   - Current baant-ta: I = I1 + I2 + I3.
$$   - Total resistance:  1/Rp = 1/R1 + 1/R2 + 1/R3 (ghat-ta, sabse kam).
$$Faayda (ghar me parallel kyun):
$$   - Har appliance ko poora 220V milta.
$$   - Ek band ho to baaki chalte rehte.
$$   - Har device ka apna switch + alag current.

## 6. Heating Effect of Current (Joule's Law) [TOP EXAM - NUMERICALS]

$$Current behne par resistor me HEAT paida hoti (Joule heating).
$$   H = I^2 R t   (Joule's law of heating).
$$   H = heat (J), I = current, R = resistance, t = time.
$$Heat current ke SQUARE par depend -> current double, heat 4 guna.
$$Uses: electric heater, iron, geyser, toaster, electric bulb (filament tungsten
$$   - high melting point), FUSE.
$$FUSE = patli taar (kam melting point) jo zyada current par PIGHAL kar circuit
$$   tod deti -> appliance ko aag/damage se bachati. (Safety device.)

## 7. Electric Power [TOP EXAM - NUMERICALS]

$$Power P = energy per unit time.
$$   P = V I = I^2 R = V^2 / R   (teeno form yaad rakho).
$$Unit: WATT (W). 1 W = 1 volt x 1 ampere. 1 kW = 1000 W.
$$Commercial unit of energy = kilowatt-hour (kWh) = "1 UNIT" bijli ka.
$$   1 kWh = 1000 W x 3600 s = 3.6 x 10^6 J.
$$Bill: Energy (kWh) = Power(kW) x time(hours). Cost = units x rate.

## 8. Quick Revision - Formula Sheet [RATTA]
   - I = Q/t ; V = W/Q ; Ohm: V = IR.
   - R = rho L / A (lamba->R jyada, mota->R kam).
   - Series: Rs = R1+R2+... (current same); Parallel: 1/Rp = 1/R1+... (V same).
   - Heat: H = I^2 R t. Power: P = VI = I^2R = V^2/R.
   - 1 unit = 1 kWh = 3.6 x 10^6 J. Fuse = safety (kam m.p. taar).

<<<PAGEBREAK>>>

==========================================

## PART C - SOLVED EXAMPLES (HARDEST -> EASIEST)

## Example 1 (HARDEST) - Series + Parallel mix + power + bill

Q: 6 ohm aur 3 ohm parallel me jude, phir 220V supply se. (a) Total R (b) Total
   current (c) Power (d) 5 ghante me kitne unit + Rs.8/unit par cost?

   Solution:
   (a) Parallel: 1/Rp = 1/6 + 1/3 = 1/6 + 2/6 = 3/6 = 1/2 -> Rp = 2 ohm.
   (b) I = V/R = 220/2 = 110 A.
   (c) P = VI = 220 x 110 = 24200 W = 24.2 kW.
   (d) Energy = 24.2 kW x 5 h = 121 kWh (units). Cost = 121 x 8 = Rs. 968.

## Example 2 - Heating effect numerical

Q: 5 ohm resistor me 2 A current 3 minute behti. Kitni heat paida hogi?

   Solution:
   - H = I^2 R t. t = 3 min = 180 s.
   - H = (2)^2 x 5 x 180 = 4 x 5 x 180 = 3600 J.

## Example 3 - Resistance of wire (rho L/A)

Q: Ek taar ko kheech kar dugna (double) lamba kar diya (volume same). Naya
   resistance purane ka kitna guna?

   Solution:
   - Length double -> L' = 2L. Volume same -> area aadha -> A' = A/2.
   - R = rho L/A -> R' = rho (2L)/(A/2) = 4 rho L/A = 4R.
   - Naya resistance = 4 GUNA (kyunki R length^2 ke proportional jab volume same).

## Example 4 - Ohm's law basic numerical

Q: 12 V battery se 4 ohm resistor juda. Current nikaalo.

   Solution:
   - V = IR -> I = V/R = 12/4 = 3 A.

## Example 5 (EASIEST) - Power formula

Q: 220 V par 2 A leta appliance ka power?

   Solution:
   - P = VI = 220 x 2 = 440 W.

<<<PAGEBREAK>>>

==========================================

## PART D - SELF TEST (EASY -> HARD)

## EASY (1 mark)
   Q1. Electric current ka formula + unit.
   Q2. Ohm's law likho.
   Q3. Fuse ka kaam kya hai?
   Q4. 1 unit (kWh) kitne joule ke barabar?

## MEDIUM (2-3 marks)
   Q5. Resistance kis-kis par depend karta (formula sahit).
   Q6. Series aur parallel ka total R formula + ek-ek antar.
   Q7. Ghar me parallel connection kyun use hota (2 reason).
   Q8. Power ke teeno formula likho + unit.

## HARD (3-5 marks, board favourite)
   Q9. 6 ohm + 3 ohm parallel, 220V: total R, current, power, 5h ka cost (Rs.8).
   Q10. Heating effect: 5 ohm, 2A, 3 min -> heat. Joule's law samjhao.
   Q11. Taar dugna lamba (volume same) -> resistance kitna guna?
   Q12. Heating element me nichrome (alloy) kyun use hota - 2 reason.

==========================================

## ANSWER HINTS (PART D)
   A1. I = Q/t ; unit ampere (A).
   A2. V = IR (constant temp par I, V ke proportional).
   A3. Zyada current par pighal kar circuit tod deti (safety).
   A4. 1 kWh = 3.6 x 10^6 J.
   A5. Length (seedha), area (ulta), material (rho), temp; R = rho L/A.
   A6. Series Rs=R1+R2 (current same); Parallel 1/Rp=1/R1+1/R2 (V same).
   A7. Har appliance poora 220V; ek band ho to baaki chale.
   A8. P = VI = I^2 R = V^2/R ; unit watt.
   A9. Rp=2 ohm, I=110A, P=24.2kW, units=121, cost=Rs.968.
   A10. H=I^2Rt=(4)(5)(180)=3600 J; heat current^2 par depend.
   A11. 4 guna (L double, area aadha).
   A12. High resistivity + temp se kam asar (jyada garmi deta, oxidise nahi).

==========================================
## "Padhai tabhi pakki jab khud likh ke test do." - All the best, Krishna!
## Generated by Kiro for Krishna1k
==========================================
"""

if __name__ == "__main__":
    build_pdf(CONTENT, "Science_Class10_Ch11_Electricity.pdf",
              title="Class 10 Science - Chapter 11",
              subtitle="Electricity (Hinglish Notes)")
