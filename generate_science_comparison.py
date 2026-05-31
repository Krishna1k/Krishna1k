"""
Generate: CBSE (NCERT) vs NIOS - Class 10 SCIENCE chapter comparison (in-depth).

Outputs:
  - CBSE_vs_NIOS_Class10_Science_Comparison.pdf   (colored)
  - CBSE_vs_NIOS_Class10_Science_Comparison.md     (markdown, red/green emoji)

RED (@@)  = exam-important / high weightage (must-do)
GREEN ($$) = topic common in BOTH CBSE and NIOS (safe overlap)
Hinglish content. Data: NCERT/CBSE Class 10 Science (rationalised 2023-24)
+ NIOS official Secondary Science & Technology (212), 32 lessons.
"""

from pathlib import Path
import pdf_utils

TITLE = "CBSE (NCERT) vs NIOS - Class 10 SCIENCE"
SUBTITLE = "In-depth | kya match | kya chhoot raha | exam-important (RED)"

CONTENT = r"""
# LEGEND - kaise padhein
@@RED  = Exam me IMPORTANT / high weightage (zaroor karo)
$$GREEN = CBSE aur NIOS DONO me COMMON topic (safe overlap)
   Black = normal jaankari / sub-topic
==========================================

# BADA PICTURE (sabse pehle samjho)
$$CBSE Class 10 Science achhe se padha = NIOS ka Class-10 core poora cover ho jaata hai.
@@NIOS "Science & Technology (212)" asal me Class 9 + Class 10 ka COMBINED course hai - poore 32 chapters.
CBSE Class 10 Science = sirf 13 chapters, par har chapter me ZYADA depth, numericals aur diagrams.
@@Isliye NIOS me bahut saara Class-9 wala content EXTRA aata hai (Motion, Force, Gravitation, Sound,
   Matter, Atomic Structure, Cell, Tissues) - wo alag se padhna padega.
@@CBSE ne jo HATA diya (Periodic Classification, Evolution) wo NIOS me ABHI BHI hai - dobara padho.
NIOS 212 me PRACTICAL bhi hota hai (Theory + Practical + TMA). CBSE me bhi internal practical.

<<<PAGEBREAK>>>
# A) CHEMISTRY  (CBSE -> NIOS mapping + sub-topics)

$$Chemical Reactions & Equations  ->  NIOS Ch4 Chemical Reaction and Equations
   sub: balancing, combination/decomposition/displacement/double-displacement, redox,
   corrosion, rancidity
$$Acids, Bases & Salts  ->  NIOS Ch8 Acids, Bases and Salts
   sub: pH scale, indicators, neutralisation, salts - NaCl, baking soda, washing soda,
   bleaching powder, Plaster of Paris
$$Metals & Non-metals  ->  NIOS Ch27 Metals and Non-metals
   sub: reactivity series, ionic bond, extraction & refining, corrosion, alloys
$$Carbon & its Compounds  ->  NIOS Ch28 Carbon and Its Compounds
   sub: covalent bond, homologous series, nomenclature, ethanol & ethanoic acid,
   soaps & detergents (micelles)

## Chemistry me NIOS-only (CBSE Class 10 me NAHI / Class 9 level)
@@Ch6 Periodic Classification of Elements  - CBSE ne HATA diya, par NIOS me aata hai
Ch2 Matter in Our Surroundings   (CBSE Class 9)
Ch3 Atom and Molecules           (CBSE Class 9)
Ch5 Atomic Structure             (CBSE Class 9)
@@Ch7 Chemical Bonding            (NIOS me alag chapter, exam me important)

<<<PAGEBREAK>>>
# B) BIOLOGY  (CBSE -> NIOS mapping + sub-topics)

$$Life Processes  ->  NIOS Ch22 Life Processes-1 (Nutrition, Transport, Respiration, Excretion)
   sub: autotrophic/heterotrophic nutrition, photosynthesis, human digestion,
   respiration, blood circulation (heart), excretion (nephron)
$$Control & Coordination  ->  NIOS Ch23 Life Processes-2 (Control & Coordination)
   sub: neuron, reflex arc, brain parts, hormones (endocrine), plant tropisms
$$How do Organisms Reproduce  ->  NIOS Ch24 Life Processes-3 (Reproduction)
   sub: asexual modes, sexual reproduction, human reproductive system, flower
$$Heredity  ->  NIOS Ch25 Heredity
   sub: Mendel laws, monohybrid/dihybrid, sex determination

## Biology me NIOS-only (CBSE me nahi / Class 9 level)
@@Ch20 History of Life on Earth  - isme Evolution-type content (CBSE ne Evolution hata diya)
Ch19 Classification of Living Organisms   (CBSE Class 9)
Ch21 Building Blocks of Life - Cell and Tissues   (CBSE Class 9)

<<<PAGEBREAK>>>
# C) PHYSICS  (CBSE -> NIOS mapping + sub-topics)

$$Light - Reflection & Refraction  ->  NIOS Ch15 Light Energy (partial)
   sub: mirror formula, lens formula, magnification, refraction, refractive index
$$The Human Eye & Colourful World  ->  NIOS Ch15 Light Energy (partial)
   sub: eye defects (myopia/hypermetropia) + correction, prism, dispersion, scattering
$$Electricity  ->  NIOS Ch16 Electrical Energy
   sub: Ohm's law, resistance, series/parallel, heating effect, power (P=VI)
$$Magnetic Effects of Current  ->  NIOS Ch17 Magnetic Effect of Electric Current
   sub: magnetic field, Fleming rules, motor, electromagnetic induction, generator

## Physics me NIOS-only (CBSE Class 10 me NAHI - Class 9 level, par NIOS me poora aata hai)
@@Ch9 Motion and its Description   (graphs, equations of motion)
@@Ch10 Force and Motion           (Newton's laws, momentum)
@@Ch11 Gravitation                (g, weight, free fall)
@@Ch13 Work and Energy            (KE, PE, power)
Ch14 Thermal Energy               (heat, temperature)
@@Ch18 Sound and Communication    (sound waves, reflection, applications)
Note: NIOS me Light "ek hi" chapter (Ch15) me hai, par CBSE me 2 alag chapters me
zyada depth + numericals milte hain.

<<<PAGEBREAK>>>
# D) ENVIRONMENT + EXTRA APPLIED (CBSE -> NIOS)
$$Our Environment  ->  NIOS Ch29 Natural Environment + Ch30 Human Impact on Environment
   sub: ecosystem, food chain/web, trophic levels, ozone layer, waste management

## NIOS-only applied chapters (CBSE me nahi / trim ho gaye)
@@Ch12 Sources of Energy   (CBSE me tha, rationalise me hata - NIOS me aata hai)
Ch26 Air and Water
Ch31 Food Production       (agriculture, crop, food preservation)
Ch32 Health and Hygiene    (diseases, immunity, nutrition)
Ch1 Measurement in Science and Technology   (units, SI, instruments)
Note: CBSE ne "Sustainable Management of Natural Resources" hata diya;
NIOS me environment/resource content kaafi detail me hai.

<<<PAGEBREAK>>>
# E) VOLUME / DEPTH  (kitna aur kitna gehra)
NIOS 212 : 32 chapters (Class 9 + 10 combined). BREADTH zyada, depth medium,
           bhasha simple, theory-heavy + practical. Questions zyadatar seedhe.
CBSE     : 13 chapters (sirf Class 10). Breadth kam, par har chapter DEEP -
           numericals, ray-diagrams, application aur HOTS/case-study.
@@Numericals: CBSE me ZYADA (Physics - mirror/lens formula, Ohm's law, power;
   Chemistry - balancing, mole). NIOS me kam aur direct.

## CBSE Science marks weightage (Theory 80)
@@Chemistry (Chemical Substances) ...... 25 marks
@@Biology (World of Living) ............ 25 marks
@@Physics - Effects of Current ......... 13 marks
@@Physics - Natural Phenomena (Light/Eye) 12 marks
   Environment (Natural Resources) ..... 05 marks

## Exam pattern
@@NIOS Science (212): Theory 80 + Practical 20 + TMA (internal). Pass = 33%.
CBSE Science: Theory 80 + Internal/Practical 20. Pass = 33%.
NIOS me Lab Manual / Practical zaroori hai - usko bhi taiyaar karna.

<<<PAGEBREAK>>>
# F) RED - EXAM-IMPORTANT TOPICS (dono boards me)

## Chemistry
@@Balancing equations + reaction types (combination, decomposition, displacement, redox)
@@Acids/Bases: pH, indicators, important salts (washing/baking soda, bleaching powder, POP)
@@Metals: reactivity series, extraction, electrolytic refining, corrosion
@@Carbon: homologous series, ethanol & ethanoic acid, soaps vs detergents
@@(NIOS) Periodic Classification: Mendeleev vs Modern table, periodic trends

## Biology
@@Life Processes: photosynthesis, human digestive/respiratory/circulatory/excretory system
@@Control & Coordination: neuron, reflex arc, hormones, plant tropisms
@@Reproduction: asexual types, human reproductive system, flower structure
@@Heredity: Mendel's laws, monohybrid cross, sex determination

## Physics
@@Light: mirror & lens formula, ray diagrams, refraction, power of lens (numericals)
@@Human Eye: myopia/hypermetropia + correction, dispersion, scattering (blue sky)
@@Electricity: Ohm's law, series vs parallel, heating effect, power (numericals)
@@Magnetism: Fleming's rules, electromagnetic induction, motor & generator
@@(NIOS) Motion graphs + 3 equations of motion, Newton's laws, gravitation (g), work-energy

## Environment
@@Ecosystem, food chain/web, trophic levels, 10% energy law
@@Ozone depletion, biodegradable vs non-biodegradable waste

<<<PAGEBREAK>>>
# G) AGAR CBSE SE NIOS JA RAHE HO - YE EXTRA PADHO
@@1. Physics (Class 9 wala): Motion, Force & Laws, Gravitation, Work & Energy, Sound
@@2. Chemistry (Class 9 wala): Matter, Atoms & Molecules, Atomic Structure, Chemical Bonding
@@3. Periodic Classification of Elements (CBSE-removed, NIOS me aata hai)
@@4. Biology (Class 9 wala): Cell & Tissues, Classification of Living Organisms
   5. Applied: Sources of Energy, Air & Water, Food Production, Health & Hygiene
@@6. NIOS Practical / Lab Manual taiyaar karo (theory ke alawa alag se)

# H) FINAL PLAN
$$1. CBSE Class 10 Science achhe se = NIOS ka Class-10 core done + strong deep base.
@@2. Upar (G) wale NIOS-only Class-9 chapters padho - yahi sabse bada gap hai.
@@3. Periodic Classification dobara padho.
@@4. Practical + Lab Manual + TMA jama karo (free + zaroori marks).
@@5. 3 NIOS sample paper + saari worksheets solve karo (pattern seedha hota hai).
$$NATIJA: NIOS Science me sirf pass nahi - ACHHA score aayega.
==========================================
Sources: NCERT/CBSE Class 10 Science (rationalised 2023-24, 13 chapters) +
NIOS official Secondary Science & Technology (212), 32 lessons.
Hinglish notes - Kiro for Krishna1k.
"""


if __name__ == "__main__":
    here = Path(__file__).parent
    pdf_path = here / "CBSE_vs_NIOS_Class10_Science_Comparison.pdf"
    md_path = here / "CBSE_vs_NIOS_Class10_Science_Comparison.md"
    pdf_utils.build_pdf(CONTENT, pdf_path, title=TITLE, subtitle=SUBTITLE)
    md_path.write_text(
        pdf_utils.to_markdown(CONTENT, TITLE, SUBTITLE), encoding="utf-8"
    )
    print(f"Wrote {md_path}")
