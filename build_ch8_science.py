"""
Build Class 10 Science Chapter 8 study PDF: "Heredity"
Hinglish. Markup: @@ RED (core basics), $$ GREEN (exam favourite), ## header.
Run: python3 build_ch8_science.py
"""
from pdf_utils import build_pdf

CONTENT = r"""
==========================================

@@PART A - CORE BASICS (MISS MAT KARNA)
@@Ch7 + Class 9 ki yeh cheezein pehle pakki karo, warna Ch8 samajh nahi aayega.

## 1. Cell, Nucleus, DNA, Chromosome, Gene

@@Cell ke nucleus me CHROMOSOME hote (dhaage jaise).
@@Chromosome DNA + protein ka bana. DNA me jeev ki saari instructions.
@@GENE = DNA ka chhota tukda jo ek trait (lakshan) ko control karta.
@@   Jaise: height ka gene, aankh ke rang ka gene.
@@Human me 23 jodi (=46) chromosome hote (har parent se 23-23).

## 2. Trait, Gamete, Fertilisation (Ch7 link)

@@Trait (lakshan) = jeev ki koi pehchaan (height, rang, beej ka aakar).
@@Gamete = reproductive cell (sperm/egg) - isme aadhe (23) chromosome.
@@Fertilisation: sperm(23) + egg(23) -> zygote(46). Isi se bachche ko
@@   dono parents ke gene milte hain.

## 3. Variation aur Heredity ka idea

@@Heredity (anuvanshikta) = parents se bachchon me traits ka transfer.
@@Variation = ek species ke jeevon me antar.
@@Bachcha parents jaisa hota PAR bilkul same nahi (variation ki wajah se).

## 4. Dominant/Recessive ka simple idea

@@Har trait ke liye 2 gene copy (ek ma se, ek pita se).
@@Agar 2 alag copy ho to jo DIKHTA hai = DOMINANT (haavi),
@@   jo chhup jaata = RECESSIVE (dabba hua).

## 5. Probability (Maths link)

@@Probability = kisi cheez ke hone ki sambhavna (0 se 1, ya % me).
@@   Sikka uchaalo -> head ya tail, dono ka chance 1/2 (50%).
@@Genetics me ratio nikalne ke liye yahi probability kaam aati.

@@-- END OF CORE BASICS (RED) PAGE --

<<<PAGEBREAK>>>

==========================================

## PART B - CHAPTER KA MAIN CONTENT
## Class 10 Science | Ch 8: Heredity

$$[GREEN = board exam me baar-baar poocha jaata hai]

## 1. Heredity aur Mendel

$$Heredity = ek generation se agli me traits (lakshan) ka jaana.
$$Gregor MENDEL ("Father of Genetics") ne MATAR (pea plant, Pisum sativum) par
$$   experiment kiye -> heredity ke niyam diye.
$$Matar kyun chuna? - jaldi badhta, alag-alag clear traits (lamba/bauna,
$$   peela/hara beej), self+cross pollination dono possible.

## 2. Key Terms [VERY IMPORTANT - RATTA]

$$   Gene        : trait control karne wala DNA ka tukda.
$$   Allele      : ek gene ke alag roop (jaise T = lamba, t = bauna).
$$   Dominant    : jo trait dikhta hai (capital letter, T).
$$   Recessive   : jo dab jaata, sirf akela hone par dikhta (small letter, t).
$$   Genotype    : gene ka combination (TT, Tt, tt).
$$   Phenotype   : jo bahar dikhta (lamba ya bauna).
$$   Homozygous  : dono allele same (TT ya tt) - "pure".
$$   Heterozygous: dono allele alag (Tt) - "hybrid".
$$   F1 generation: pehli santaan (parents = P). F2 = F1 ka aapas me cross.

## 3. Monohybrid Cross (ek trait) [TOP EXAM AREA]

$$Mendel ne pure lamba (TT) x pure bauna (tt) cross kiya:
$$   P:    TT  x  tt
$$   F1:   sab Tt  -> SAARE LAMBE (dominant T dikha; t chhup gaya).
$$Phir F1 (Tt) x F1 (Tt) cross kiya:
$$   Punnett square:
$$           T        t
$$      T |  TT  |   Tt
$$      t |  Tt  |   tt
$$   F2 genotype: 1 TT : 2 Tt : 1 tt.
$$   F2 phenotype: 3 LAMBE : 1 BAUNA  (RATIO 3:1).
$$Conclusion: recessive trait (bauna) F1 me gayab hokar F2 me wapas aaya ->
$$   gene jodon (pairs) me hote, alag-alag santaan me baant-te.

## 4. Dihybrid Cross (do trait ek saath) [VERY IMPORTANT]

$$Mendel ne 2 traits ek saath dekhe: beej ka rang (Yellow Y / green y) aur
$$   aakar (Round R / wrinkled r).
$$   P:   RRYY (round-yellow) x rryy (wrinkled-green)
$$   F1:  sab RrYy -> round-yellow (dono dominant dikhe).
$$   F2 phenotype ratio = 9 : 3 : 3 : 1
$$      (9 round-yellow : 3 round-green : 3 wrinkled-yellow : 1 wrinkled-green).
$$Important: F2 me NAYE combinations (round-green, wrinkled-yellow) bhi aaye ->
$$   matlab do traits SWATANTRA roop se (independently) inherit hote hain.

## 5. Mendel ke Niyam (Laws) [IMPORTANT]

$$(1) Law of Dominance: do alag allele me se ek (dominant) hi dikhta hai.
$$(2) Law of Segregation: gamete bante waqt allele ka jodi alag (segregate) ho
$$   jaata - har gamete me ek hi allele jaata.
$$(3) Law of Independent Assortment: alag-alag traits ke gene ek doosre se
$$   swatantra roop se inherit hote (dihybrid cross se pata chala).

## 6. Sex Determination in Humans [TOP EXAM AREA]

$$Human me 23 jodi chromosome - 22 jodi AUTOSOMES + 1 jodi SEX CHROMOSOME.
$$   Female: XX.   Male: XY.
$$Mother hamesha X deti (egg me sirf X).
$$Father X ya Y de sakta (sperm me X ya Y).
$$   Agar father ka X mila -> XX -> LADKI.
$$   Agar father ka Y mila -> XY -> LADKA.
$$IMPORTANT CONCLUSION: bachche ka ling (gender) FATHER (ke sperm) par
$$   depend karta, mother par NAHI. (Yeh samaj ka galat-fehmi todta - exam fav.)

## 7. Acquired vs Inherited traits

$$Inherited trait: gene se mila, agli generation me jaata (aankh ka rang).
$$Acquired trait: jeevan me khud se aaya (jaise weightlifting se muscle, kata
$$   hua haath) - yeh DNA/gene me nahi jaata, isliye agli generation me NAHI jaata.
$$   (Eg: chuhe ki poonch kaat-te raho, bachche ki poonch normal hi rahegi.)

## 8. Quick Revision - One Liners
   - Mendel = father of genetics; matar par experiment.
   - Monohybrid F2 = 3:1; Dihybrid F2 = 9:3:3:1.
   - Genotype (TT/Tt/tt) gene; Phenotype (dikhne wala).
   - Female XX, Male XY; bachche ka gender FATHER decide karta.
   - Acquired trait agli generation me nahi jaata.

<<<PAGEBREAK>>>

==========================================

## PART C - SOLVED EXAMPLES (HARDEST -> EASIEST)

## Example 1 (HARDEST) - Monohybrid cross poora + ratio

Q: Pure lamba (TT) ko pure bauna (tt) se cross karo. F1 aur F2 ka genotype +
   phenotype ratio nikaalo. Recessive trait F2 me wapas kyun aaya?

   Solution:
   - P: TT x tt -> F1: sab Tt (saare LAMBE; T dominant).
   - F1 x F1 (Tt x Tt) Punnett:
        T t / T t -> TT, Tt, Tt, tt.
   - F2 genotype = 1 TT : 2 Tt : 1 tt.
   - F2 phenotype = 3 lamba : 1 bauna (3:1).
   - Bauna (tt) F1 me chhup gaya tha (t recessive), F2 me jab dono t mile (tt)
     to wapas dikha -> gene jodon me hote aur alag-alag baant-te.

## Example 2 - Dihybrid F2 ratio + nayi combination

Q: RRYY x rryy cross me F1 aur F2 phenotype ratio? Naye combinations kya batate?

   Solution:
   - F1: sab RrYy (round-yellow).
   - F2 phenotype = 9 round-yellow : 3 round-green : 3 wrinkled-yellow :
     1 wrinkled-green (9:3:3:1).
   - Naye combinations (round-green, wrinkled-yellow) batate ki do traits
     SWATANTRA roop se inherit hote (Law of Independent Assortment).

## Example 3 - Sex determination

Q: Bachche ka ling (gender) kaun determine karta - ma ya papa? Samjhao.

   Solution:
   - Mother sirf X deti (XX). Father X ya Y deta (XY).
   - Father ka X -> XX (ladki); father ka Y -> XY (ladka).
   - Isliye bachche ka gender FATHER ke sperm par depend karta, mother par nahi.

## Example 4 - Acquired vs inherited

Q: Agar koi insaan jeevan bhar gym karke muscle banaye, kya woh muscle uske
   bachche me aayega? Kyun?

   Solution:
   - Nahi. Yeh ACQUIRED trait hai (jeevan me khud banaya), gene/DNA me change
     nahi hua. Sirf inherited (gene wale) traits hi agli generation me jaate.

## Example 5 (EASIEST) - Genotype vs Phenotype

Q: Genotype aur phenotype me antar batao.

   Solution:
   - Genotype = gene combination (TT, Tt, tt).
   - Phenotype = jo bahar dikhta (lamba ya bauna).

<<<PAGEBREAK>>>

==========================================

## PART D - SELF TEST (EASY -> HARD)

## EASY (1 mark)
   Q1. Heredity aur gene ka matlab.
   Q2. Dominant aur recessive trait me antar.
   Q3. Human me kitne chromosome? Sex chromosome female/male me kya?
   Q4. Mendel ne kaun se plant par kaam kiya aur kyun?

## MEDIUM (2-3 marks)
   Q5. Genotype, phenotype, homozygous, heterozygous samjhao.
   Q6. Monohybrid cross F2 ratio (Punnett square sahit).
   Q7. Acquired aur inherited trait me antar + example.
   Q8. Mendel ke 3 niyam (laws) likho.

## HARD (3-5 marks, board favourite)
   Q9. Monohybrid cross: P se F2 tak + 3:1 ratio + recessive wapas kyun.
   Q10. Dihybrid cross F2 = 9:3:3:1 + independent assortment samjhao.
   Q11. Sex determination in humans poora (XX/XY, father decide).
   Q12. Mendel ne kaise prove kiya ki traits gene (pairs) ke roop me inherit hote.

==========================================

## ANSWER HINTS (PART D)
   A1. Heredity = parents se traits ka transfer; Gene = trait wala DNA tukda.
   A2. Dominant dikhta (T); recessive dab jaata, akela hone par dikhta (t).
   A3. 23 jodi (46); female XX, male XY.
   A4. Matar (pea); jaldi badhta, clear traits, self+cross pollination.
   A5. Genotype (gene), phenotype (dikhne wala), homozygous (TT/tt), hetero (Tt).
   A6. Tt x Tt -> 1TT:2Tt:1tt -> phenotype 3:1.
   A7. Inherited gene se (agli gen me jaata); acquired khud banaya (nahi jaata).
   A8. Dominance, Segregation, Independent assortment.
   A9. TT x tt -> F1 Tt (lamba) -> F2 3 lamba:1 bauna; recessive tt me wapas.
   A10. RRYY x rryy -> F1 RrYy -> F2 9:3:3:1; naye combinations = independent.
   A11. Mother X, father X/Y; X->ladki, Y->ladka; father decide karta.
   A12. Recessive trait F1 me gायab F2 me wapas -> gene pairs me, segregate hote.

==========================================
## "Padhai tabhi pakki jab khud likh ke test do." - All the best, Krishna!
## Generated by Kiro for Krishna1k
==========================================
"""

if __name__ == "__main__":
    build_pdf(CONTENT, "Science_Class10_Ch8_Heredity.pdf",
              title="Class 10 Science - Chapter 8",
              subtitle="Heredity (Hinglish Notes)")
