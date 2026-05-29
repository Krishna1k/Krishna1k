# Class 10 NCERT Maths — Chapter 4: Quadratic Equations

> A simplified, detailed guide in Hinglish for students who missed Class 7-8-9.
> Based on the official NCERT (English Medium) textbook.

---

## SECTION 1: Foundation

### 1.1 Polynomial revision (Chapter 2 se)

Yaad hai? Polynomial = expression jisme variable ke power whole numbers hote hain.
- Linear polynomial: `ax + b` (degree 1)
- **Quadratic polynomial: `ax² + bx + c` (degree 2)** ← Ye chapter isi pe hai
- Cubic polynomial: `ax³ + bx² + cx + d` (degree 3)

### 1.2 Equation vs Expression

- **Expression:** `2x² + 3x - 5` (sirf likha hua)
- **Equation:** `2x² + 3x - 5 = 0` (`=` sign hai)

### 1.3 Quadratic Equation kya hai?

**Definition:** Wo equation jiska standard form ho:
```
ax² + bx + c = 0
```
jahan **a, b, c real numbers hain aur a ≠ 0**.

⚠️ **Important:** `a ≠ 0` warna ye linear equation ban jayegi.

**Examples (Quadratic):**
- `x² - 5x + 6 = 0` (a=1, b=-5, c=6)
- `2x² + 7x = 0` (a=2, b=7, c=0)
- `3x² - 12 = 0` (a=3, b=0, c=-12)

**Not Quadratic:**
- `2x + 5 = 0` (no x² term)
- `x³ + 2x + 1 = 0` (degree 3)
- `x² + 1/x = 5` (1/x = x⁻¹, fraction power)

### 1.4 Roots (Solutions) of a Quadratic Equation

**Root** = wo value of `x` jiske liye equation satisfy ho (LHS = RHS = 0).

Quadratic equation ke **2 roots** hote hain (zyada se zyada).

**Example:** `x² - 5x + 6 = 0`
- Check x = 2: (2)² - 5(2) + 6 = 4 - 10 + 6 = 0 ✓
- Check x = 3: (3)² - 5(3) + 6 = 9 - 15 + 6 = 0 ✓

So roots are **2 aur 3**.

---

## SECTION 2: Solving by FACTORISATION (Splitting Middle Term)

### 2.1 Idea

Quadratic ko `(x - p)(x - q) = 0` form mein todo. Phir:
- Either `x - p = 0` → x = p
- Or `x - q = 0` → x = q

**Logic:** Agar do cheezon ka product 0 hai, toh kam-se-kam ek toh 0 hi hogi.

### 2.2 Splitting Middle Term Method

**Formula:** `ax² + bx + c = 0` mein:
- Middle coefficient `b` ko aise 2 numbers mein todo (say p, q)
- ki **p + q = b** AND **p × q = a × c**

#### Example 1: `x² + 7x + 12 = 0` solve kar

Yahan a=1, b=7, c=12, so a×c = 12.

Find p, q such that:
- p + q = 7
- p × q = 12

**Try:** 3 aur 4 → 3+4=7 ✓, 3×4=12 ✓

```
x² + 7x + 12 = 0
x² + 3x + 4x + 12 = 0
x(x + 3) + 4(x + 3) = 0
(x + 3)(x + 4) = 0
```

So **x = -3 or x = -4**.

#### Example 2: `2x² - 5x + 3 = 0` solve kar

a=2, b=-5, c=3, so a×c = 6.

Find p, q:
- p + q = -5
- p × q = 6

**Try:** -2 aur -3 → -2+(-3) = -5 ✓, (-2)×(-3) = 6 ✓

```
2x² - 5x + 3 = 0
2x² - 2x - 3x + 3 = 0
2x(x - 1) - 3(x - 1) = 0
(x - 1)(2x - 3) = 0
```

So **x = 1 or x = 3/2**.

#### Example 3: `6x² - x - 2 = 0` solve kar

a=6, b=-1, c=-2, so a×c = -12.

Find p, q:
- p + q = -1
- p × q = -12

**Try:** -4 aur 3 → -4+3 = -1 ✓, (-4)×3 = -12 ✓

```
6x² - x - 2 = 0
6x² - 4x + 3x - 2 = 0
2x(3x - 2) + 1(3x - 2) = 0
(3x - 2)(2x + 1) = 0
```

So **x = 2/3 or x = -1/2**.

---

## SECTION 3: Solving by QUADRATIC FORMULA

### 3.1 Magic Formula (Yaad rakh!)

Agar `ax² + bx + c = 0` ho, toh:

```
       -b ± √(b² - 4ac)
x  =  ──────────────────
              2a
```

Ye formula har quadratic equation pe kaam karta hai — chahe factorisation kitni bhi mushkil ho.

### 3.2 Discriminant — D ka kamaal

```
D = b² - 4ac
```

D ki value se pata chal jaata hai roots kaise honge:

| D ki value | Roots |
|---|---|
| **D > 0** | Two **distinct real** roots |
| **D = 0** | Two **equal real** roots (i.e., one repeated root) |
| **D < 0** | **No real** roots (imaginary) |

### 3.3 Examples

#### Example 4: `2x² - 7x + 3 = 0` formula se solve kar

a=2, b=-7, c=3

**D = b² - 4ac = (-7)² - 4(2)(3) = 49 - 24 = 25** (>0, distinct real roots)

```
x = (7 ± √25) / 4
x = (7 ± 5) / 4
```

So **x = (7+5)/4 = 3 or x = (7-5)/4 = 1/2**.

#### Example 5: `x² - 6x + 9 = 0`

a=1, b=-6, c=9

**D = 36 - 36 = 0** (equal roots)

```
x = (6 ± 0) / 2 = 3
```

So **x = 3, 3** (repeated root).

#### Example 6: `x² + x + 1 = 0`

a=1, b=1, c=1

**D = 1 - 4 = -3** (< 0)

So **No real roots**.

---

## SECTION 4: Word Problems

#### Example 7: Number problem

"Ek number aur uska reciprocal ka sum 10/3 hai. Number nikaalo."

Let number = x. Reciprocal = 1/x.

```
x + 1/x = 10/3
```

Multiply by 3x:
```
3x² + 3 = 10x
3x² - 10x + 3 = 0
```

Splitting middle term: a×c = 9, p+q = -10
- p = -9, q = -1 → -9 + (-1) = -10 ✓, (-9)(-1) = 9 ✓

```
3x² - 9x - x + 3 = 0
3x(x - 3) - 1(x - 3) = 0
(x - 3)(3x - 1) = 0
```

**x = 3 or x = 1/3**

(Both work — reciprocals of each other)

#### Example 8: Speed problem

"Ek train 360 km ki distance fixed speed se cover karti hai. Agar speed 5 km/h zyada hoti, toh time 1 hour kam lagta. Original speed nikaalo."

Let original speed = x km/h.
- Original time = 360/x
- New speed = (x+5), new time = 360/(x+5)

Equation: `360/x - 360/(x+5) = 1`

Multiply by x(x+5):
```
360(x+5) - 360x = x(x+5)
1800 = x² + 5x
x² + 5x - 1800 = 0
```

Splitting: a×c = -1800, p+q = 5
- 45 × (-40) = -1800, 45 + (-40) = 5 ✓

```
x² + 45x - 40x - 1800 = 0
x(x + 45) - 40(x + 45) = 0
(x + 45)(x - 40) = 0
```

x = -45 (rejected, speed +ve hoti hai) or **x = 40 km/h**.

---

## SECTION 5: Q&A TIME

**Q1.** Inn mein se konsi quadratic equation hai?
- (a) `x² + 5 = 0`
- (b) `2x + 3 = 0`
- (c) `x³ - 1 = 0`
- (d) `5x² - 7x + 1 = 0`

**Q2.** `x² - 3x - 10 = 0` ko factorisation se solve kar.

**Q3.** `2x² + x - 6 = 0` ko quadratic formula se solve kar.

**Q4.** Inn equations ka discriminant nikaal aur roots ka nature bata:
- (a) `x² + 4x + 4 = 0`
- (b) `2x² - 3x + 5 = 0`
- (c) `x² - 5x + 4 = 0`

**Q5.** Word problem: "Do consecutive odd positive integers ka product 143 hai. Numbers nikaalo."

---

## SUMMARY

1. **Quadratic equation:** `ax² + bx + c = 0` (a ≠ 0)
2. **Roots:** Maximum 2 hote hain
3. **Methods to solve:**
   - **Factorisation** (splitting middle term)
   - **Quadratic formula:** `x = (-b ± √D) / 2a`
4. **Discriminant D = b² - 4ac:**
   - D > 0 → distinct real roots
   - D = 0 → equal roots
   - D < 0 → no real roots
5. **Word problems:** Variable le → equation banao → solve → reject impossible solutions

---

Generated by Kiro for Krishna1k
