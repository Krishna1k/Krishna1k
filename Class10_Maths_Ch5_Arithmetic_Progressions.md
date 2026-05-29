# Class 10 NCERT Maths — Chapter 5: Arithmetic Progressions

> A simplified, detailed guide in Hinglish for students who missed Class 7-8-9.
> Based on the official NCERT (English Medium) textbook.

---

## SECTION 1: Foundation

### 1.1 Sequence kya hoti hai?

**Sequence** = numbers ki ek list jo kisi specific pattern follow karti hai.

**Examples:**
- 1, 3, 5, 7, 9, ... (odd numbers)
- 2, 4, 8, 16, 32, ... (powers of 2)
- 1, 4, 9, 16, 25, ... (squares)
- 5, 10, 15, 20, ... (multiples of 5)

Har number ko **term** kehte hain — first term, second term, etc.

### 1.2 Arithmetic Progression (AP) — The Definition

**AP** = wo sequence jisme har term, **previous term mein ek FIXED number add** karke milti hai.

Wo fixed number ko **common difference (d)** kehte hain.

**Examples of AP:**
- **2, 5, 8, 11, 14, ...** (d = 3)
- **10, 7, 4, 1, -2, ...** (d = -3)
- **5, 5, 5, 5, ...** (d = 0)
- **-1, 2, 5, 8, ...** (d = 3)

**Not AP:**
- 1, 4, 9, 16, ... (squares — difference badalti hai)
- 2, 4, 8, 16, ... (powers — multiplication, addition nahi)

### 1.3 AP ke Notations

| Notation | Matlab |
|---|---|
| `a` (or `a₁`) | First term |
| `d` | Common difference |
| `aₙ` | nth term (general term) |
| `n` | Number of terms |
| `Sₙ` | Sum of first n terms |
| `l` | Last term |

### 1.4 Common Difference d kaise nikaalein?

**Formula:** `d = aₙ - aₙ₋₁` (any term minus previous term)

**Example:** AP: 5, 9, 13, 17, ...
- d = 9 - 5 = 4
- d = 13 - 9 = 4 ✓
- d = 17 - 13 = 4 ✓

⚠️ Saare consecutive differences same hone chahiye, warna AP nahi hai.

### 1.5 General form of AP

```
a, a+d, a+2d, a+3d, a+4d, ...
```

So:
- 1st term = a
- 2nd term = a + d
- 3rd term = a + 2d
- 4th term = a + 3d
- nth term = a + (n-1)d

---

## SECTION 2: nth Term Formula

### 2.1 The Formula (Important!)

```
aₙ = a + (n-1)d
```

Yahan:
- aₙ = nth term (jo nikaalna hai)
- a = first term
- d = common difference
- n = term number

### 2.2 Examples

#### Example 1: AP: 2, 5, 8, 11, ... ka 20th term nikaal

a = 2, d = 3, n = 20

```
a₂₀ = a + (n-1)d
    = 2 + (20-1)(3)
    = 2 + 19 × 3
    = 2 + 57
    = 59
```

**Answer: 59** ✅

#### Example 2: AP ka 4th term 0 hai aur 11th term -7 hai. AP nikaalo.

a + 3d = 0 ...(1)
a + 10d = -7 ...(2)

(2) - (1): 7d = -7 → **d = -1**
From (1): a = -3d = 3 → **a = 3**

So AP: **3, 2, 1, 0, -1, -2, -3, -4, ...** ✅

#### Example 3: 100, 95, 90, ... ka kaunsa term -50 hai?

a = 100, d = -5, aₙ = -50

```
-50 = 100 + (n-1)(-5)
-50 - 100 = (n-1)(-5)
-150 = -5(n-1)
n - 1 = 30
n = 31
```

So **31st term -50 hai**. ✅

---

## SECTION 3: Sum of First n Terms (Sₙ)

### 3.1 The Formulas (Dono yaad rakh!)

**Formula 1 (when first term and d known):**
```
Sₙ = n/2 × [2a + (n-1)d]
```

**Formula 2 (when first and last term known):**
```
Sₙ = n/2 × (a + l)
```
jahan `l` = last term = aₙ.

⚠️ Yaad rakh: `aₙ = a + (n-1)d`, isliye dono formulas connected hain.

### 3.2 Examples

#### Example 4: 2, 5, 8, 11, ... ke first 20 terms ka sum nikaal

a = 2, d = 3, n = 20

```
S₂₀ = 20/2 × [2(2) + (20-1)(3)]
    = 10 × [4 + 57]
    = 10 × 61
    = 610
```

**Answer: 610** ✅

#### Example 5: 1+2+3+...+100 (first 100 natural numbers ka sum)

AP: 1, 2, 3, 4, ..., 100. So a=1, d=1, n=100, l=100.

```
S₁₀₀ = 100/2 × (1 + 100)
     = 50 × 101
     = 5050
```

**Answer: 5050** ✅ (Famous Gauss formula!)

#### Example 6: AP 2, 5, 8, ... ka kitne terms tak ka sum 155 hoga?

a=2, d=3, Sₙ=155
```
155 = n/2 [4 + 3(n-1)]
310 = n[3n + 1]
3n² + n - 310 = 0
```

Splitting: a×c = -930, sum = 1 → 31 × -30
```
3n² + 31n - 30n - 310 = 0
n(3n + 31) - 10(3n + 31) = 0
(3n + 31)(n - 10) = 0
```

n = 10 (positive only) → **10 terms**.

---

## SECTION 4: Word Problems

#### Example 7: Theatre seats

"Ek theatre ki first row mein 20 seats hain. Har next row mein 2 seats zyada hain. 30th row mein kitne seats?"

a = 20, d = 2, n = 30

```
a₃₀ = 20 + 29 × 2 = 20 + 58 = 78
```

**Answer: 78 seats** ✅

#### Example 8: Salary problem

"Ek aadmi ki starting salary ₹8000 hai. Har saal ₹500 ki increment milti hai. 10 saal ki total earnings nikaalo."

AP: 8000, 8500, 9000, ... (d = 500)

S₁₀ = 10/2 [2(8000) + 9(500)]
    = 5 [16000 + 4500]
    = 5 × 20500
    = **₹1,02,500** ✅

---

## SECTION 5: Q&A TIME

**Q1.** Inn sequences mein se kaunsi AP hai? Agar AP hai toh d bata.
- (a) 2, 4, 6, 8, ...
- (b) 1, 4, 9, 16, ...
- (c) -3, -1, 1, 3, ...
- (d) 1, 3, 9, 27, ...

**Q2.** AP: 7, 13, 19, 25, ... ka 50th term nikaal.

**Q3.** Agar AP ka 10th term 32 hai aur 20th term 72 hai, toh AP nikaal.

**Q4.** AP: 1, 4, 7, 10, ... ke first 25 terms ka sum nikaal.

**Q5.** Find n: AP 9, 17, 25, ... mein kaunsa term 105 hoga?

**Q6.** Word problem: "Ek admi 8 din mein, har din 5 km zyada distance cover karta hai. Pehle din 3 km cover ki. 8 dino mein total kitna km cover hua?"

---

## SUMMARY

1. **AP:** Sequence with constant common difference d.
2. **General form:** a, a+d, a+2d, a+3d, ...
3. **nth term formula:** `aₙ = a + (n-1)d`
4. **Sum formulas:**
   - `Sₙ = n/2 [2a + (n-1)d]` (use when d known)
   - `Sₙ = n/2 (a + l)` (use when last term l known)
5. **d nikaalna:** any term minus previous term.
6. **Word problems:** identify a, d, n; pick right formula.

---

Generated by Kiro for Krishna1k
