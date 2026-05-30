# Class 10 NCERT Maths — Chapter 2: Polynomials (Core-Basics Edition)

> Special edition for students who skipped Class 7-8-9.
> 🔴 **RED / 🔴-marked = CORE BASIC (prerequisite)** — Class 7-8-9 ka jo tujhe pehle se aana chahiye tha.
> 🟢 **GREEN / 🟢-marked = EXAM mein BAAR-BAAR aata hai** — zaroor yaad rakh.
>
> *(In the PDF: RED = core basics, GREEN = frequently-asked. On GitHub marked 🔴 / 🟢.)*

---

# 🔴 PAGE 1 — CORE BASICS (MISS MAT KARNA)

> Ye saari cheezein Class 7-8-9 ki hain. Pura Chapter 2 inhi pe khada hai.

🔴 **1) Variable aur Constant**
Variable = badalne wala (x, y) — unknown number. Constant = fixed number (5, -3, 1/2).

🔴 **2) Power / Exponent**
`x²` = x×x, `x³` = x×x×x. "x square", "x cube".

🔴 **3) Polynomial kya hai?**
Expression jisme variable ke power sirf **whole numbers** ho (0,1,2,3...) — negative/fraction power nahi.
- Hai: `2x+3`, `x²-5x+6`, `7`
- Nahi: `x⁻¹+2`, `√x+1` (galat power)

🔴 **4) Degree**
Polynomial ka sabse bada power. `2x+5` → degree 1, `x²-3x+1` → degree 2.

🔴 **5) Types (degree ke hisab se)**
- Degree 1 = **Linear**: `ax + b`
- Degree 2 = **Quadratic**: `ax² + bx + c`
- Degree 3 = **Cubic**: `ax³ + bx² + cx + d`
- (a hamesha ≠ 0)

🔴 **6) Coefficient**
Variable ke aage wala number. `3x² - 5x + 7` mein: a=3, b=-5, c=7. Inhi ko a,b,c bolenge.

🔴 **7) p(x) notation aur substitution**
`p(x)` = polynomial ka naam. `p(2)` = x ki jagah 2 daal do.
`p(x)=x²-4` → `p(2) = 2²-4 = 0`.

🔴 **8) Zero / Root of polynomial**
Woh x jiske liye `p(x)=0`. `p(x)=2x-6` → x=3 → zero = 3.
(Graph jahan x-axis ko cut kare, wahi zero.)

🔴 **9) Factorisation (splitting middle term) — recap**
`ax²+bx+c` ko `(..)(..)` mein todna. Middle term b ko 2 numbers p,q mein todo jahan `p+q = b` aur `p×q = a×c`.

🔴 **10) Graph basics**
X-axis = horizontal, Y-axis = vertical. Linear ka graph = seedhi line. Quadratic ka graph = "U"/ulta "U" (**parabola**). Graph jahan x-axis touch/cut kare = zero.

---

# CHAPTER 2 — ASLI CONTENT

## Topic 1: Geometrical Meaning of Zeroes

Polynomial ka graph x-axis ko jitni baar **cut** karta hai, utne uske **zeroes** hote hain.

- **Linear** (`ax+b`): seedhi line, 1 baar cut → **1 zero**
- **Quadratic** (`ax²+bx+c`): **parabola** (U shape)
  - 2 jagah cut → 2 zeroes
  - 1 jagah touch → 1 zero (repeated)
  - cut hi nahi → 0 real zeroes
- **Cubic**: zyada se zyada 3 baar → up to 3 zeroes

> 🔴 *[CORE]* "Cut karna" = graph aur x-axis ka milna. Wahi point zero hota hai.

## Topic 2: Zeroes aur Coefficients ka Rishta

> 🟢 **EXAM ALERT:** Ye relationship aur ispe based questions **har exam** mein aate hain. Formula ratta maar lo.

Quadratic `p(x) = ax² + bx + c` ke zeroes α aur β ho toh:

> 🟢 **Sum of zeroes:** α + β = **−b/a**
> 🟢 **Product of zeroes:** α × β = **c/a**

**Example:** `x² - 5x + 6` (a=1, b=-5, c=6)
- Sum = −b/a = 5 ; Product = c/a = 6
- (Zeroes 2 aur 3: 2+3=5 ✓, 2×3=6 ✓)

**Cubic** (`ax³+bx²+cx+d`) — sirf jaankari: sum = −b/a, sum of pairs = c/a, product = −d/a.

## Topic 3: Quadratic Polynomial Banana (sum & product se)

> 🟢 **EXAM ALERT:** "Sum aur product diya hai, polynomial banao" — baar-baar aata hai.

> 🟢 **Polynomial = x² − (sum)x + (product)**

**Example:** sum = 5, product = 6 → polynomial = `x² - 5x + 6`.

---

# 🧮 SOLVED EXAMPLES — Hardest → Easiest

> 🟢 Ye 8 examples poori tarah **solve karke** dikhaye hain. Upar hardest, neeche easiest.

### Solved Example 1 (HARDEST) — α²+β², 1/α+1/β 🟢
α, β zeroes hain `x² - 5x + 6` ke. α+β = 5, αβ = 6.
- (a) α² + β² = (α+β)² − 2αβ = 25 − 12 = **13**
- (b) 1/α + 1/β = (α+β)/(αβ) = **5/6**

### Solved Example 2 — Ek zero diya ho 🟢
`x² - 4x + k` ka ek zero 3 hai. k aur doosra zero?
```
p(3)=0 → 9 − 12 + k = 0 → k = 3
Product = c/a = k = 3 → 3 × (doosra) = 3 → doosra zero = 1
(Sum check: 3+1 = 4 = −b/a ✓)
```

### Solved Example 3 — Zeroes nikaal + verify rishta 🟢
`6x² - 7x - 3` ke zeroes + relationship verify.
```
a×c = -18, sum -7 → -9 aur +2
6x² - 9x + 2x - 3 = 3x(2x-3) + 1(2x-3) = (2x-3)(3x+1)
Zeroes: 3/2, -1/3
Sum = 3/2 - 1/3 = 7/6 = -b/a ✓
Product = (3/2)(-1/3) = -1/2 = c/a = -3/6 ✓
```

### Solved Example 4 — Polynomial banao (zeroes diye) 🟢
Zeroes 3 aur -2:
```
Sum = 1, Product = -6
Polynomial = x² - (1)x + (-6) = x² - x - 6
```

### Solved Example 5 — Polynomial banao (sum/product diye)
Sum = -3, Product = 2:
```
Polynomial = x² - (-3)x + 2 = x² + 3x + 2
```

### Solved Example 6 — Graph se zeroes count
- x-axis ko 2 jagah cut → 2 zeroes
- 1 jagah touch → 1 zero (repeated)
- chhuye hi nahi → 0 real zeroes
(Number of zeroes = cutting points.)

### Solved Example 7 — Verify rishta (simple)
`x² - 2x - 8`:
```
(x-4)(x+2) → zeroes 4, -2
Sum = 2 = -b/a ✓ ; Product = -8 = c/a ✓
```

### Solved Example 8 (EASIEST) — Linear zero & p(2)
- (a) `2x - 6` ka zero: 2x-6=0 → **x = 3**
- (b) `p(x)=x²-4` → p(2) = 2²-4 = **0** (2 ek zero hai)

---

## Q&A TIME (khud try kar, phir bhej — main check karunga)

**Q1.** `p(x) = 3x² + 5x - 2` ka degree aur type bata.
**Q2.** `p(x) = x² - 4` ke liye p(2) aur p(-2) nikaal.
**Q3.** `x² - 7x + 12` ke zeroes nikaal aur sum/product rishta verify kar.
**Q4.** Zeroes 5 aur -3 wala quadratic banao.
**Q5.** Sum = 4, Product = -5 wala quadratic banao.
**Q6.** α, β zeroes hain `x² - 6x + 8` ke. α² + β² nikaal.
**Q7.** 🔴 CORE CHECK: `x⁻¹ + 3` polynomial hai ya nahi? Kyun?
**Q8.** 🔴 CORE CHECK: `2x² + 3x - 1` mein a, b, c kya hain?

---

## SUMMARY

1. **Zeroes** = jahan p(x)=0 (graph x-axis ko cut kare).
2. **Number of zeroes** = cutting points (linear 1, quadratic up to 2, cubic up to 3).
3. Quadratic `ax²+bx+c`: **Sum = −b/a**, **Product = c/a**.
4. **Polynomial banao:** `x² − (sum)x + (product)`.
5. **Identity:** α² + β² = (α+β)² − 2αβ.

> 🔴 CORE BASICS (RED page) revise karna — polynomial, degree, coefficient (a,b,c), zero, p(x), parabola.

---

Generated by Kiro for Krishna1k
