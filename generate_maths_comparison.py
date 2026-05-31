"""
Generate: CBSE (NCERT) vs NIOS - Class 10 Maths chapter comparison.

Outputs:
  - CBSE_vs_NIOS_Class10_Maths_Comparison.pdf   (colored; RED=exam-important,
                                                 GREEN=common in both boards)
  - CBSE_vs_NIOS_Class10_Maths_Comparison.md     (markdown; RED=red dot, GREEN=green dot)

Content is in Hinglish. Markup:
  "# h1", "## h2", "@@ red line", "$$ green line",
  "==========" rule, "<<<PAGEBREAK>>>" page break.
"""

from pathlib import Path
import pdf_utils

TITLE = "CBSE (NCERT) vs NIOS - Class 10 Maths"
SUBTITLE = "Chapter comparison | kya match | kya chhoot raha | exam-important (RED)"

CONTENT = r"""
# LEGEND - kaise padhein
@@RED  = Exam me IMPORTANT / zaroor aata hai (high weightage, must-do)
$$GREEN = CBSE aur NIOS DONO me COMMON hai (safe overlap - yahan strong raho)
   Black = normal jaankari
==========================================

# EK-LINE VERDICT
$$Agar NCERT/CBSE achhe se padh lo to NIOS Maths ka ~85% apne aap cover.
NIOS = 26 chapters (6 module) - zyada chapters, par har chapter halka.
CBSE = 14 chapters - kam chapters, par har chapter me zyada depth + tough Q.
@@Sirf 2 cheez EXTRA karni hai: Commercial Maths (NIOS-only) + NIOS exam pattern/TMA.

<<<PAGEBREAK>>>
# A) CHAPTER MATCHING  (CBSE chapter  ->  NIOS chapter)

## Number System + Algebra
$$Real Numbers           -> NIOS Ch1 Number Systems + Ch2 Exponents & Radicals
$$Polynomials            -> NIOS Ch3 Algebraic Expr & Polynomials + Ch4 Special Products/Factorization
$$Pair of Linear Eqns    -> NIOS Ch5 Linear Equations
$$Quadratic Equations    -> NIOS Ch6 Quadratic Equations
$$Arithmetic Progression -> NIOS Ch7 Arithmetic Progressions

## Geometry
$$Triangles              -> NIOS Ch11 Congruence + Ch14 Similarity of Triangles
$$Circles                -> NIOS Ch15 Circles + Ch16 Angles in Circle/Cyclic Quad + Ch17 Secants/Tangents
$$Coordinate Geometry    -> NIOS Ch19 Co-ordinate Geometry

## Trigonometry
$$Introduction to Trig   -> NIOS Ch22 Intro Trig + Ch23 Trig Ratios of Special Angles

## Mensuration
$$Areas Related to Circles -> NIOS Ch20 Perimeters & Area of Plane Figures
$$Surface Areas & Volumes  -> NIOS Ch21 Surface Area & Volume of Solid Figures

## Statistics & Probability
$$Statistics             -> NIOS Ch24 Data & Representation + Ch25 Measures of Central Tendency
$$Probability            -> NIOS Ch26 Introduction to Probability

@@NATIJA: CBSE ke 14 me se 13 chapters NIOS me MIL jaate hain.

<<<PAGEBREAK>>>
# B) KAUN KAUN MISS OUT HO RAHA HAI

## (i) NIOS me HAI par CBSE Class 10 me NAHI  (NIOS-only - ye EXTRA padho)
@@Ch8 Percentage & its Applications  (profit-loss, discount, SI & CI)  - EXAM me aata hai
@@Ch9 Instalment Buying  (kist / EMI)  - Commercial Maths, EXAM me aata hai
Ch2 Exponents & Radicals / Surds  (CBSE me Class 9 level)
Ch4 Special Products & Factorization  (CBSE me Class 8-9)
Ch10 Lines and Angles  (CBSE Class 9)
Ch11 Congruence of Triangles  (CBSE Class 9)
Ch12 Concurrent Lines  (CBSE Class 9)
Ch13 Quadrilaterals  (CBSE Class 9)
=> NIOS me kaafi Class-9 foundation + Commercial Maths extra juda hua hai.

## (ii) CBSE Class 10 me HAI par NIOS me NAHI / bahut halka  (CBSE-only)
@@Some Applications of Trigonometry = Heights & Distances  - CBSE me hai, NIOS me dedicated chapter nahi
Real Numbers ki depth: Fundamental Theorem of Arithmetic, irrational ke proof (CBSE zyada deep)
Polynomials: zeros aur coefficients ka relation (CBSE me zyada detail)

<<<PAGEBREAK>>>
# C) VOLUME / DEPTH  (kitna content)
NIOS : 26 chapters, 6 module. Zyada chapters par har chapter chhota,
       foundation-heavy aur questions SEEDHE (direct) hote hain.
CBSE : 14 chapters. Kam chapters par har chapter me zyada DEPTH,
       application aur HOTS / case-study questions.

## Marks ka weightage
@@NIOS Maths (211): 80 marks Theory (public exam) + 20 marks TMA.  Pass = 33%.
CBSE Maths: 80 marks Board theory + 20 internal.  Pass = 33%.

## CBSE unit-wise marks (80 ka paper) - priority ka idea
@@Algebra .................... 20 marks   (sabse zyada - TOP priority)
@@Geometry ................... 15 marks
@@Trigonometry ............... 12 marks
@@Statistics & Probability ... 11 marks
   Mensuration ............... 10 marks
   Number Systems ............ 06 marks
   Coordinate Geometry ....... 06 marks

<<<PAGEBREAK>>>
# D) RED = EXAM-IMPORTANT TOPICS (ye zaroor karo)

## Algebra (highest weightage)
@@Quadratic Equations: roots, discriminant, word problems
@@Arithmetic Progression: nth term (an) aur sum (Sn)
@@Pair of Linear Equations: substitution/elimination + word problems
@@Polynomials: zeros, sum aur product of zeros

## Commercial Maths (NIOS-only - na bhulna)
@@Simple Interest aur Compound Interest ke sums
@@Profit, Loss, Discount, Percentage
@@Instalment Buying (EMI / kist)

## Geometry
@@Circles: tangent properties + theorems (proof + numerical)
@@Triangles: similarity criteria + Basic Proportionality Theorem (Thales)

## Trigonometry
@@Trigonometric identities + ratios of 0/30/45/60/90
@@(CBSE) Heights & Distances ke application sums

## Mensuration / Stats / Probability
@@Surface Area & Volume: cylinder, cone, sphere + combinations
@@Statistics: mean / median / mode (grouped data)
@@Probability: single-event basic problems

<<<PAGEBREAK>>>
# E) FINAL PLAN  (NCERT base pe NIOS clear)
$$1. NCERT achhe se = NIOS ka ~85% done (aur strong tough base ban jaata hai)
@@2. Commercial Maths (Ch8, Ch9) NIOS book se alag se padho - MUST (NCERT me nahi)
   3. Heights & Distances ek halki nazar (CBSE me hai, NIOS me optional)
@@4. 3 NIOS sample paper + saari worksheets solve karo (pattern seedha hai)
@@5. TMA zaroor jama karo = 20% almost-free marks
$$NATIJA: NIOS Maths me sirf pass nahi - ACHHA score aayega.
==========================================
Sources: NCERT/CBSE Class 10 Maths (rationalised syllabus) + NIOS official
Secondary Mathematics (211) course material (26 chapters / 6 modules).
Hinglish notes - Kiro for Krishna1k.
"""


def to_markdown(content: str) -> str:
    out = ["# " + TITLE, "", "_" + SUBTITLE + "_", "",
           "> Legend: 🔴 = exam-important (must-do)  |  "
           "🟢 = common in both CBSE & NIOS", ""]
    for raw in content.splitlines():
        s = raw.rstrip()
        st = s.strip()
        if st == "<<<PAGEBREAK>>>":
            out.append("\n---\n")
        elif st.startswith("=========="):
            out.append("\n---\n")
        elif s.startswith("## "):
            out.append("### " + s[3:].strip())
        elif s.startswith("# "):
            out.append("## " + s[2:].strip())
        else:
            m_red = s.lstrip().startswith("@@")
            m_grn = s.lstrip().startswith("$$")
            if m_red:
                indent = s[: len(s) - len(s.lstrip())]
                out.append(indent + "- 🔴 " + s.lstrip()[2:].strip())
            elif m_grn:
                indent = s[: len(s) - len(s.lstrip())]
                out.append(indent + "- 🟢 " + s.lstrip()[2:].strip())
            elif st == "":
                out.append("")
            else:
                out.append(s)
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    here = Path(__file__).parent
    pdf_path = here / "CBSE_vs_NIOS_Class10_Maths_Comparison.pdf"
    md_path = here / "CBSE_vs_NIOS_Class10_Maths_Comparison.md"
    pdf_utils.build_pdf(CONTENT, pdf_path, title=TITLE, subtitle=SUBTITLE)
    md_path.write_text(to_markdown(CONTENT), encoding="utf-8")
    print(f"Wrote {md_path}")
