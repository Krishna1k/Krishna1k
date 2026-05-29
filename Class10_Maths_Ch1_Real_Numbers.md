# Class 10 NCERT Maths — Chapter 1: Real Numbers (Core-Basics Edition)

> Special edition for students who skipped Class 7-8-9.
> 🔴 **RED / 🔴-marked text = CORE BASIC (prerequisite)** — Class 7-8-9 ka jo tujhe pehle se aana chahiye tha. Inhe miss mat karna!
>
> *(In the PDF these appear in actual RED color. On GitHub, they're marked with 🔴.)*

---

# 🔴 PAGE 1 — CORE BASICS (MISS MAT KARNA)

> Ye saari cheezein Class 7-8-9 ki hain. Pura Chapter 1 inhi pe khada hai. Pehle ye samajh, phir aage badh.

🔴 **1) Factor kya hota hai?**
Factor = jo number kisi doosre number ko **poora** (bina remainder) divide kar de.
Example: 12 ke factors = 1, 2, 3, 4, 6, 12.

🔴 **2) Multiple kya hota hai?**
Multiple = number ki "table" ke numbers.
Example: 3 ke multiples = 3, 6, 9, 12, 15, ...
(Factor chhota hota hai, multiple bada.)

🔴 **3) Prime, Composite, aur 1**
- **Prime** = sirf 2 factors (1 aur khud): 2, 3, 5, 7, 11...
- **Composite** = 2 se zyada factors: 4, 6, 8, 9, 10...
- **1 na prime hai na composite** (sirf 1 factor hai).
- **2 ekloti even prime** number hai.

🔴 **4) Power / Exponent (chhota upar wala number)**
`2³` ka matlab 2 ko 3 baar multiply = 2×2×2 = 8.
Yahan 2 = base, 3 = power. `a²` = "a square", `a³` = "a cube".

🔴 **5) Square Root (√ — the root symbol)**
Square root = power ka **ulta**.
√9 = 3 (kyunki 3×3 = 9), √25 = 5 (kyunki 5×5 = 25).
Is guide mein hum `sqrt(n)` ya `√n` likhte hain (jaise √2).

🔴 **6) p/q mein q = 0 kyun nahi ho sakta?**
`p/q` ka matlab p ko q se **divide** karna. Kisi cheez ko **0 se divide karna allowed nahi** (5/0 ka koi answer hi nahi — undefined). Isliye rational number `p/q` mein hamesha **q ≠ 0**.

🔴 **7) HCF (Highest Common Factor)**
HCF = do numbers ka sabse **bada common factor**.
12 = {1,2,3,4,6,12}, 18 = {1,2,3,6,9,18} → common {1,2,3,6} → **HCF = 6**.

🔴 **8) LCM (Least Common Multiple)**
LCM = do numbers ka sabse **chhota common multiple**.
12 → 12,24,36,48...  18 → 18,36,54... → common chhota = **36 = LCM**.

🔴 **9) Number Types (recap)**
- Natural (N): 1,2,3,...  | Whole (W): 0,1,2,3,...
- Integers (Z): ...-2,-1,0,1,2...
- Rational (Q): p/q form (q≠0): 1/2, 0.25
- Irrational: p/q mein nahi aata: √2, π
- Real (R): rational + irrational dono.

🔴 **10) Terminating vs Non-terminating decimal**
- Terminating = khatam ho jaye: 0.5, 0.25
- Non-terminating repeating = pattern repeat: 0.333...
- Non-terminating non-repeating = na khatam na pattern: √2 = 1.41421356... (ye **irrational**)

---

# CHAPTER 1 — ASLI CONTENT

## Topic 1: Fundamental Theorem of Arithmetic

**Statement:** Har composite number ko prime numbers ke **product** (multiplication) ke roop mein likha ja sakta hai, aur ye tareeka **unique** hota hai (order chhod ke).

> 🔴 *[CORE]* "Product of primes" matlab prime numbers ko multiply karna. (Prime/factor wala RED page point 1 & 3 dekh.)

**Example 1:** 156 ka prime factorisation
```
156 / 2 = 78
 78 / 2 = 39
 39 / 3 = 13
 13 / 13 = 1
```
**156 = 2 × 2 × 3 × 13 = 2² × 3 × 13**

> 🔴 *[CORE]* `2²` ka matlab 2×2 (power wala RED page point 4).

**Example 2:** 3825 ka prime factorisation
```
3825 / 3 = 1275
1275 / 3 = 425
 425 / 5 = 85
  85 / 5 = 17
  17 / 17 = 1
```
**3825 = 3² × 5² × 17**

## Topic 2: HCF and LCM by Prime Factorisation

**Method:**
- HCF = common prime factors × **lowest** power
- LCM = all prime factors × **highest** power

> 🔴 *[CORE]* HCF/LCM ka basic matlab RED page (point 7 & 8). Pehle wo samajh.

**Example 3:** 96 aur 404 ka HCF aur LCM
```
96  = 2⁵ × 3
404 = 2² × 101

HCF = 2² = 4              (common prime 2, lowest power)
LCM = 2⁵ × 3 × 101 = 9696 (all primes, highest power)

Verify: HCF × LCM = 4 × 9696 = 38784 ; 96 × 404 = 38784 ✓
```

> 🔴 *[CORE]* Sirf 2 numbers ke liye: **HCF × LCM = product of the two numbers**. (3 numbers pe ye rule nahi chalta.)

## Topic 3: Irrational Numbers (√2 is irrational)

> 🔴 *[CORE]* √2 = "woh number jisko square karne pe 2 aaye". (Root symbol RED page point 5.)

**Theorem used:** Agar prime `p`, `a²` ko divide karta hai, toh `p`, `a` ko bhi divide karta hai.

**Proof: √2 is irrational (Proof by Contradiction)**

1. Maan le √2 rational hai. Toh √2 = p/q, where **q ≠ 0** aur HCF(p,q) = 1 (simplest form).
   > 🔴 *[CORE]* q ≠ 0 kyun? RED page point 6. HCF(p,q)=1 matlab simplest form.
2. Square dono side: `2 = p²/q²` → `2q² = p²` ...(i)
3. 2 divides p² → **2 divides p**.
4. So p = 2c.
5. (i) mein daal: `2q² = 4c²` → `q² = 2c²`
6. 2 divides q² → **2 divides q**.
7. Ab p aur q dono ko 2 divide karta hai, par HCF = 1 tha. **Contradiction!**

**Conclusion:** Assumption galat. **√2 irrational hai.** ∎

**Quick results (yaad rakh):**
- √p irrational hota hai jab p prime ho.
- Rational + Irrational = Irrational
- (non-zero) Rational × Irrational = Irrational

---

## Q&A TIME (khud try kar, phir bhej — main check karunga)

**Q1.** 140 ko prime factors ke product mein likho.
**Q2.** 26 aur 91 ka HCF aur LCM nikaal (prime factorisation se).
**Q3.** √5 ko irrational prove kar (√2 wala method copy kar).
**Q4.** 🔴 CORE CHECK: 1 prime hai ya composite? Kyun?
**Q5.** 🔴 CORE CHECK: 5/0 ka answer kya hai? p/q mein q ke baare mein kya rule hai?
**Q6.** 3 + 2√5 ko irrational dikhao.

---

## SUMMARY

1. **Fundamental Theorem:** har composite number = unique product of primes.
2. **HCF** = common primes × lowest power; **LCM** = all primes × highest power.
3. 2 numbers ke liye: **HCF × LCM = product of numbers**.
4. **√p irrational** hai jab p prime ho.
5. **Rational + Irrational = Irrational**.

> 🔴 **CORE BASICS (RED page) ek baar aur revise kar lena** — factor, multiple, prime, power, root, q≠0, HCF, LCM. Inke bina ye chapter adhoora rahega.

---

Generated by Kiro for Krishna1k
