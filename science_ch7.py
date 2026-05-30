"""
science_ch7.py
--------------
Generates a detailed, simplified Hinglish study guide for
NCERT Class 10 Science, Chapter 7: "How do Organisms Reproduce?".

Outputs:
  - Science_Class10_Ch7_How_Organisms_Reproduce.pdf  (colour PDF)
  - Science_Class10_Ch7_How_Organisms_Reproduce.md   (markdown, red/green via emoji)

Markup conventions inside CONTENT (handled by pdf_utils):
  @@  -> RED   line  (CORE BASICS / extra ke liye)
  $$  -> GREEN line  (exam me baar-baar aane wale topics)
  <<<PAGEBREAK>>>     -> nayi page
"""

import re
from pathlib import Path

import pdf_utils


CONTENT = r"""HOW DO ORGANISMS REPRODUCE?
NCERT Class 10 Science - Chapter 7 (Hinglish Detailed Notes)
=========================================================

@@ COLOUR CODE: RED = Core Basics / extra help (Class 7-8-9 wali cheezein + zaroori base).
$$ COLOUR CODE: GREEN = Board exam me ye topics BAAR-BAAR aate hain - pakka yaad karo.
   Baaki normal black text = main chapter content (detail me, simple bhasha me).

<<<PAGEBREAK>>>

CORE BASICS - PEHLE YE PADHO (CLASS 7-8-9 KA FOUNDATION)
=========================================================
@@ Tune 7-8-9 nahi padhi - koi tension nahi. Ye page is chapter ki base hai.
@@ Ek baar achhe se padh le, fir chapter aasaani se samajh aayega.

@@ 1) CELL (koshika) kya hai (Class 8):
@@    - Body ki sabse chhoti living unit = CELL. Saare jeev cells se bante.
@@    - Reproduction bhi cell level par hota (cell divide ho ke nayi cell banti).

@@ 2) DNA aur CHROMOSOME (intro - Class 9/10):
@@    - DNA = ek lamba chemical (Deoxyribose Nucleic Acid) jo saari "information"
@@      rakhta - jeev kaisa dikhega aur kaam karega.
@@    - Cell ke nucleus me DNA dhaage jaise CHROMOSOME me packed hota hai.

@@ 3) GENE (intro):
@@    - GENE = DNA ka chhota tukda jo ek khaas feature (rang, height) control karta.
@@    - Bachhe ko ye genes maa-baap se milte hain (heredity / vanshanugat).

@@ 4) GAMETE (yaun koshika):
@@    - Reproduction ke liye banne wali special cell = GAMETE.
@@    - Inme normal body cell ki AADHI (half) chromosome hoti hain.

@@ 5) FERTILISATION aur ZYGOTE:
@@    - Male gamete + Female gamete ka jud-na = FERTILISATION.
@@    - Jud-ne se bani nayi single cell = ZYGOTE (yahi se naya jeev banta).

@@ 6) VARIATION:
@@    - Ek hi species ke jeevon me chhote-chhote farak = VARIATION.
@@    - Sexual reproduction se variation aati (do parents ka DNA milta).

@@ 7) MITOSIS vs MEIOSIS (bahut simple idea - cell division):
@@    - Cell ka divide ho ke nayi cell banana = CELL DIVISION.
@@    - MITOSIS: 1 cell -> 2 same cell (body badhne aur repair ke liye).
@@    - MEIOSIS: special division jisme chromosome AADHE ho jaate -> GAMETE bante.

@@ 8) MALE vs FEMALE GAMETE:
@@    - MALE gamete = chhota, move kar sakta (jaise sperm, pollen).
@@    - FEMALE gamete = bada, food store wala, sthir (jaise egg/ovum, ovule).

@@ 9) SPECIES kya hai:
@@    - Aise jeev jo aapas me reproduce kar ke fertile bachhe de sakein = ek SPECIES.
@@    - Reproduction species ko generation to generation aage chalata hai.

<<<PAGEBREAK>>>

1. REPRODUCTION KYUN - DNA COPYING AUR VARIATION
=========================================================
   Reproduction = jeevon dwara apne jaise naye jeev (offspring) banana.
$$ - Reproduction se individual amar nahi hota, par SPECIES bachi rehti hai
$$   (generation to generation chalti rehti).

1.1 DNA COPYING - ASLI KHEL
---------------------------------------------------------
$$ - Reproduction ki basic ghatna = DNA ka COPY banna (DNA copying).
$$ - Cell DNA copy kar ke do DNA set banata, fir cell divide ho ke 2 cell banti.
   - DNA hi decide karta offspring kaisa banega (body design ki "blueprint").
@@ - DNA copy 100% perfect nahi hota - thodi galtiyan/farak reh jaate -> VARIATION.

1.2 VARIATION KYUN ZAROORI (EVOLUTION SE LINK)
---------------------------------------------------------
$$ - Variation = species me chhote farak. Ye EVOLUTION ka raw material hai.
$$ - Agar environment badle (garmi, thand, naya disease), to jin individuals me
$$   us situation ko jhelne wali variation hogi, woh BACH jaate (survive).
   - Isliye variation species ko badalte environment me survive karne me madad karti.
@@ - Asexual me variation bahut kam (offspring lagbhag identical), sexual me zyada.

<<<PAGEBREAK>>>

2. ASEXUAL REPRODUCTION (EK PARENT, NO GAMETES)
=========================================================
$$ ASEXUAL = sirf EK parent se reproduction, gametes nahi bante, fertilisation nahi.
$$ Offspring parent ke lagbhag IDENTICAL (clone jaise). Ab modes dekho:

2.1 FISSION (CELL KA BAT-NA) - SINGLE-CELLED JEEV
---------------------------------------------------------
$$ - BINARY FISSION: 1 cell -> 2 cell (do barabar tukde).
$$     * Amoeba: kisi bhi plane (direction) me bat jaata.
$$     * Leishmania (kala-azar wala): DEFINITE/fixed plane me bat-ta.
$$ - MULTIPLE FISSION: 1 cell -> ek saath BAHUT saari cells.
$$     * Plasmodium (malaria parasite) multiple fission karta.

2.2 BUDDING (KALI/BUD NIKALNA)
---------------------------------------------------------
$$ - Parent body par ek chhota bud (ubhaar) nikalta, badh ke alag ho jaata.
$$     * Hydra aur Yeast budding ke example.

2.3 FRAGMENTATION (TUKDO ME TUT-NA)
---------------------------------------------------------
$$ - Body kai tukdo me toot ke, har tukda naya jeev ban jaata.
$$     * Spirogyra (paani me dhaage jaisi algae) fragmentation karti.

2.4 REGENERATION (KHOYA HUA PART WAPAS BANANA)
---------------------------------------------------------
$$ - Kuch simple jeev kat jaane par har tukde se poora jeev bana lete.
$$     * Planaria aur Hydra regeneration kar sakte.
@@ - DHYAAN: Regeneration = reproduction NAHI. Ye specialised cells se hota; normal
@@   condition me ye jeev iss tarah multiply nahi karte (ye chot ka response hai).

2.5 SPORE FORMATION (SPORES SE)
---------------------------------------------------------
$$ - Kuch jeev SPORANGIA (thaili) me bahut saare SPORES banate.
$$     * Rhizopus (bread mould): upar uthi sticks par sporangia, unme spores.
$$ - Spore hawa me ud ke nami/surface par girte aur naye jeev me badh jaate.
@@ - Spores ki moti covering unhe sookhe/kharab haalat me bacha ke rakhti.

2.6 VEGETATIVE PROPAGATION (PAUDHON ME - BINA SEED)
---------------------------------------------------------
$$ - Plant ke vegetative part (root, stem, leaf) se naya plant ban-na.
$$ NATURAL tarike:
$$   - Potato (aalu) ki AANKHEN (eyes) se naye plant.
$$   - Onion (pyaaz) jaise bulb se.
$$   - Bryophyllum ke PATTE ke kinaaron par leaf buds -> gir ke naye plant.
$$ ARTIFICIAL (insaan dwara) tarike:
$$   - CUTTING: stem ka tukda laga dena (rose/gulab).
$$   - LAYERING: tehni ko jhuka ke mitti me daba dena (jasmine/chameli).
$$   - GRAFTING: do plant ke parts jod dena (mango/aam ki achhi variety).
$$   - TISSUE CULTURE: lab me cells/tissue se naye plantlets ugana.
$$ FAYDE (advantages):
$$   - Tezi se (faster) plant milta; offspring parent ke bilkul IDENTICAL.
$$   - Jin plants me seed nahi bante (banana/kela, rose, jasmine) unhe bhi uga sakte.
@@   - Tissue culture se kam jagah me bahut saare disease-free plant banate.

<<<PAGEBREAK>>>

3. SEXUAL REPRODUCTION - VARIATION KI IMPORTANCE
=========================================================
$$ SEXUAL = DO parents (male + female), dono ke gametes jud-te (fertilisation).
$$ Dono ka DNA milne se offspring me NAYI combination -> zyada VARIATION.
   - Isliye sexual reproduction evolution ke liye zyada faydemand.
@@ - Gametes meiosis se bante (chromosome aadhe) taaki fertilisation ke baad
@@   offspring me chromosome ki sankhya constant rahe - na double ho.

3.1 PHOOL WAALE PAUDHON ME (FLOWERING PLANTS)
---------------------------------------------------------
$$ FLOWER ke 4 parts (bahar se andar):
$$   - SEPALS (baahri hare patte) - kali ko protect karte.
$$   - PETALS (rangeen pankhudiyan) - insects ko aakarshit (attract) karte.
$$   - STAMEN = MALE part = ANTHER + FILAMENT. Anther me POLLEN grains bante.
$$   - CARPEL/PISTIL = FEMALE part = STIGMA + STYLE + OVARY. Ovary me OVULE.
$$ - UNISEXUAL flower: sirf stamen YA sirf carpel (papaya, watermelon).
$$ - BISEXUAL flower: stamen AUR carpel dono (hibiscus/gudhal, mustard/sarson).

   POLLINATION (pollen ka stigma tak pahunchna):
$$   - SELF-pollination: usi (ya same plant ke) phool ke stigma par pollen.
$$   - CROSS-pollination: doosre phool par (hawa, paani, insects se) - variation zyada.

   FERTILISATION (plant me):
$$   - Pollen stigma par girta -> POLLEN TUBE banata jo style se ho ke OVULE tak jaata.
$$   - Male gamete, ovule me female gamete se judta = fertilisation -> ZYGOTE.
$$ FERTILISATION ke baad kya banta (yaad rakho):
$$   - ZYGOTE  ka EMBRYO ban-ta.
$$   - OVULE   ka SEED (beej) ban-ta.
$$   - OVARY   ka FRUIT (phal) ban-ta.
$$   - Baaki parts (petals, stamen, stigma) aksar sookh ke gir jaate.
   GERMINATION:
$$   - Anukool condition (paani, hawa, temperature) milne par SEED se naya plant
$$     nikalna = GERMINATION.

<<<PAGEBREAK>>>

4. HUMAN REPRODUCTION (MANAV PRAJANAN)
=========================================================
@@ Insaano me reproduction sirf sexual hota; puberty ke baad body iske layak banti.

4.1 MALE REPRODUCTIVE SYSTEM
---------------------------------------------------------
$$ - TESTES (2): SPERM (male gamete) aur hormone TESTOSTERONE banate.
$$     * Testes body ke BAHAR SCROTUM me hote - kyunki sperm banne ke liye body
$$       se thoda KAM (cooler) temperature chahiye.
$$ - VAS DEFERENS: sperm ko aage le jaane wali nali.
$$ - SEMINAL VESICLE + PROSTATE GLAND: fluid daalte; fluid + sperm = SEMEN.
$$ - URETHRA: semen (aur urine) ko bahar le jaane ka common rasta.

4.2 FEMALE REPRODUCTIVE SYSTEM
---------------------------------------------------------
$$ - OVARIES (2): EGG/OVUM (female gamete) aur hormone OESTROGEN & PROGESTERONE banate.
$$ - FALLOPIAN TUBE (OVIDUCT): egg ko le jaati; YAHI par FERTILISATION hota.
$$ - UTERUS (garbhashay/womb): yahan embryo implant ho ke develop karta.
$$ - VAGINA: sperm ke andar aane ka aur baby ke janam ka rasta.

4.3 PUBERTY (SECONDARY SEXUAL CHARACTERS)
---------------------------------------------------------
$$ - Puberty = 10-12 saal ke aas-paas body me reproduction layak badlaav.
$$ - LADKO me: aawaaz bhaari, chehre/body par baal, muscles badhte.
$$ - LADKIYON me: breast develop, periods (menstruation) shuru, body shape badle.

4.4 FERTILISATION SE BIRTH TAK
---------------------------------------------------------
$$ - Sperm + Egg fallopian tube me jud-te -> ZYGOTE.
$$ - Zygote divide karta -> uterus ki deewar me jam jaata = IMPLANTATION (embryo).
$$ - PLACENTA: embryo aur maa ke beech ka connection (special disc/tissue).
$$     * Iske through embryo ko maa se OXYGEN + NUTRIENTS milte aur embryo ka
$$       WASTE maa ke khoon me jaata.
$$ - GESTATION (pregnancy) ~9 mahine; fir uterus muscles ke sankuchan se BIRTH.

4.5 MENSTRUATION (MAAHVAARI)
---------------------------------------------------------
$$ - Har ~28 din me ek egg release hota; uterus ki andar wali lining (khoon +
$$   tissue) embryo ke liye moti ho jaati.
$$ - Agar egg FERTILISE NAHI hota -> ye lining toot ke khoon ke saath bahar nikalti
$$   = MENSTRUATION (period), ~2-8 din chalta. Fir cycle dohra-ta hai.
@@ - Pehli baar period aana puberty ka sign hai; ye ek normal healthy process hai.

<<<PAGEBREAK>>>

5. REPRODUCTIVE HEALTH
=========================================================

5.1 CONTRACEPTION (GARBH-NIRODH) - FAMILY PLANNING
---------------------------------------------------------
$$ Pregnancy ko rokne ke tarike (4 type):
$$   - BARRIER: sperm-egg ko milne se rok-na. e.g. CONDOM (STD se bhi bachata).
$$   - HORMONAL: ORAL PILLS - hormone balance badal ke egg release rok-ti.
$$   - IUCD: COPPER-T - uterus ke andar lagaya jaane wala device.
$$   - SURGICAL: VASECTOMY (male - vas deferens block) ya TUBECTOMY (female -
$$     fallopian tube block).
$$ - FAMILY PLANNING: chhota/healthy parivaar, maa ki sehat, population control.

5.2 SEXUALLY TRANSMITTED DISEASES (STDs)
---------------------------------------------------------
$$ - Sexual contact se failne wali bimariyan:
$$     * BACTERIAL: gonorrhoea, syphilis.
$$     * VIRAL: HIV-AIDS, warts (genital warts).
$$ - CONDOM in diseases ko failne se rokne me madad karta.

5.3 SEX DETERMINATION (BACHHE KA LING KAISE TAY HOTA)
---------------------------------------------------------
$$ - Insaano me 23 jode chromosome; 1 jodi = SEX CHROMOSOME.
$$   - FEMALE = XX, MALE = XY.
$$ - Maa hamesha X deti. Pita X de to bachhi (XX), Y de to ladka (XY).
$$ - Matlab: bachhe ka LING PITA ke sperm se decide hota (maa ki galti nahi).

5.4 SAMAJIK PEHLU (SOCIAL) - BAHUT ZAROORI
---------------------------------------------------------
$$ - Janam se pehle ling pata karna (prenatal sex determination) aur FEMALE
$$   FOETICIDE (kanya bhrun hatya) - dono GAIR-KAANUNI (ILLEGAL) hain.
@@ - Girta hua sex ratio (ladkiyan kam) samaj ke liye nuksaandeh - ladka-ladki barabar.

<<<PAGEBREAK>>>

6. SOLVED EXAMPLES (HARDEST -> EASIEST)
=========================================================
$$ Ye type ke questions exam me pakka aate - khud likh ke practice karo.

EXAMPLE 1 (Hardest): Flowering plant me fertilisation samjhao aur batao har part
   kya ban-ta hai.
   - Pollen stigma par girta -> pollen tube banata -> style se ho ke ovary ke
     ovule tak pahunchta. Male gamete + female gamete (ovule me) = fertilisation.
   - Banta hai: ZYGOTE se EMBRYO, OVULE se SEED, OVARY se FRUIT.
   - Sahi condition par seed germinate ho ke naya plant deta.

EXAMPLE 2: Human female reproductive path aur PLACENTA ka role likho.
   - Ovary se egg -> fallopian tube (yahi fertilisation) -> zygote uterus me
     implant -> embryo develop.
   - PLACENTA maa aur embryo ko jodta: embryo ko oxygen+nutrients deta aur uska
     waste maa ke khoon me bhejta. ~9 mahine baad birth.

EXAMPLE 3: Sahi jodi milao - asexual mode aur organism.
   - Binary fission -> Amoeba/Leishmania
   - Multiple fission -> Plasmodium
   - Budding -> Hydra, Yeast
   - Fragmentation -> Spirogyra
   - Regeneration -> Planaria
   - Spore formation -> Rhizopus

EXAMPLE 4: Variation kyun useful? Sexual vs Asexual reproduction.
   - Variation se badalte environment me kuch individuals survive kar lete ->
     species bachi rehti (evolution ka base).
   - Asexual: 1 parent, no gametes, fast, offspring identical, variation kam.
   - Sexual: 2 parents, gametes + fertilisation, DNA milta, variation zyada.

EXAMPLE 5: Contraception methods ko classify karo (type ke hisaab se).
   - Barrier -> Condom
   - Hormonal -> Oral pills
   - IUCD -> Copper-T (uterus me)
   - Surgical -> Vasectomy (male) / Tubectomy (female)

EXAMPLE 6: Sex determination cross banao aur dikhao pita ling decide karta.
   - Maa: XX (sirf X deti). Pita: XY (X ya Y deta).
   - X (maa) ke saath X (pita) = XX = LADKI
   - X (maa) ke saath Y (pita) = XY = LADKA
   - Y sirf pita deta -> isliye bachhe ka ling PITA par depend karta.

EXAMPLE 7 (Easiest): Male aur female gamete ke naam aur kahan bante?
   - Male gamete = SPERM (testes me banta).
   - Female gamete = EGG/OVUM (ovary me banta).

<<<PAGEBREAK>>>

7. QUICK Q&A - PADHNE KE BAAD KHUD CHECK KARO
=========================================================
$$ Pehle khud answer socho, fir niche milao. Ye board-style questions hain.

Q1. Reproduction me DNA copying kyun zaroori hai?
A1. DNA me body ki saari information hoti; copy ho ke offspring ko milti taaki
    woh parent jaisa bane. Copy me chhoti galti se variation aati.

Q2. Binary aur Multiple fission me farak (example sahit)?
A2. Binary: 1 cell -> 2 cell (Amoeba). Multiple: 1 cell -> bahut cells ek saath
    (Plasmodium).

Q3. Regeneration reproduction kyun nahi maana jaata?
A3. Ye specialised cells se chot ka response hai; normal me ye jeev iss tarah
    naye jeev nahi banate. (Planaria/Hydra example.)

Q4. Vegetative propagation ke 2 fayde?
A4. (i) Tez aur identical plant milte; (ii) jin plants me seed nahi bante
    (banana, rose) unhe bhi uga sakte.

Q5. Stamen aur Carpel ke parts batao.
A5. Stamen (male) = Anther + Filament. Carpel/Pistil (female) = Stigma + Style
    + Ovary.

Q6. Fertilisation ke baad ovule, ovary aur zygote ka kya banta?
A6. Ovule se Seed, Ovary se Fruit, Zygote se Embryo.

Q7. Testes scrotum me (body ke bahar) kyun hote?
A7. Sperm banne ke liye body se thoda kam (cooler) temperature chahiye hota.

Q8. Placenta ka kaam kya hai?
A8. Maa aur embryo ko jodta - embryo ko oxygen+nutrients deta aur uska waste
    maa ke khoon me bhejta.

Q9. Menstruation kyun hota hai?
A9. Egg fertilise na ho to uterus ki moti lining toot ke khoon ke saath bahar
    nikalti - ~28 din ke cycle me.

Q10. Bachhe ka ling kaun decide karta aur kaise?
A10. Pita. X sperm se ladki (XX), Y sperm se ladka (XY). Maa hamesha X deti.

=========================================================
EXAM STRATEGY (1 minute revision):
$$  - Asexual modes + 1-1 example (fission/budding/fragmentation/spore/regeneration).
$$  - Vegetative propagation (natural + artificial) ke 2 fayde.
$$  - Flower parts + plant fertilisation (ovule->seed, ovary->fruit, zygote->embryo).
$$  - Human male/female organs + unke kaam; PLACENTA + MENSTRUATION pakka.
$$  - Contraception 4 type + Sex determination (XX/XY, pita decide karta).
@@  - CORE BASICS page (cell, DNA, gene, gamete, fertilisation) bhool jaao to
@@    wapas pehle padho - base strong rakho.
=========================================================
Generated by Kiro for Krishna1k - All the best!
"""


def to_markdown(content: str) -> str:
    """Convert the markup CONTENT into GitHub-friendly markdown."""
    out = ["# How do Organisms Reproduce?",
           "### NCERT Class 10 Science - Chapter 7 (Hinglish Detailed Notes)",
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
    pdf_path = here / "Science_Class10_Ch7_How_Organisms_Reproduce.pdf"
    md_path = here / "Science_Class10_Ch7_How_Organisms_Reproduce.md"

    pdf_utils.text_to_pdf(
        CONTENT,
        pdf_path,
        title="How do Organisms Reproduce?",
        subtitle="NCERT Class 10 Science - Ch 7 | Hinglish Detailed Notes",
    )
    md_path.write_text(to_markdown(CONTENT), encoding="utf-8")
    print(f"Wrote {md_path}")


if __name__ == "__main__":
    main()
