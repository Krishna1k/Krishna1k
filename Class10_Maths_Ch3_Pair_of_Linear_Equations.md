# Class 10 NCERT Maths — Chapter 3: Pair of Linear Equations in Two Variables

> A simplified, detailed guide in Hinglish for students who missed Class 7-8-9.
> Based on the official NCERT (English Medium) textbook.

---

## SECTION 1: Foundation (Class 7-8-9 ka revision)

### 1.1 Equation kya hoti hai?

**Equation** = ek mathematical statement jisme `=` (equal sign) hota hai.

**Example:** `2x + 3 = 7` — ye ek equation hai.

### 1.2 Linear Equation in ONE Variable

Sirf ek variable (jaise x) ho aur uska power 1 ho.

**Form:** `ax + b = 0` (jahan a ≠ 0)

**Examples:** 
- `3x + 5 = 0` → solve karke x = -5/3 milta hai
- `2x - 8 = 0` → x = 4

Ek variable ki linear equation ka **sirf 1 solution** hota hai.

### 1.3 Linear Equation in TWO Variables — Asli baat

Ab do variables hain (x aur y), dono ka power 1.

**Form:** `ax + by + c = 0` (jahan a ≠ 0, b ≠ 0)

**Example:** `2x + 3y - 12 = 0`

⚠️ **Important:** Iska **infinite solutions** hote hain! Kyunki har x ke liye ek y mil sakta hai.

**Example check:** `x + y = 5`
- x = 1, y = 4 ✓
- x = 2, y = 3 ✓  
- x = 0, y = 5 ✓
- x = -1, y = 6 ✓
- ... aur bhi infinite

### 1.4 Cartesian Plane (Graph paper) — Basics

Graph paper pe **2 lines** hoti hain:
- **X-axis** (horizontal, leti hui)
- **Y-axis** (vertical, khadi)
- Dono ka meeting point = **Origin (0, 0)**

**Point likhne ka tareeka:** `(x, y)` — pehle x, phir y.

```
        Y-axis
          |
       4 -|     • (3, 4)
       3 -|
       2 -|
       1 -|
          |________________
   ---  0   1  2  3  4    X-axis
```

### 1.5 Linear equation ka graph kaisa dikhta hai?

Linear equation `ax + by + c = 0` ka graph hamesha ek **STRAIGHT LINE** hota hai. (Isliye iska naam "linear" hai!)

**How to plot karein?**
1. Equation se 2-3 (x, y) pairs nikaalo
2. Graph paper pe points lagao
3. Sab points ko join karo → seedhi line milegi

---

## SECTION 2: Pair of Linear Equations — Asli Chapter

### 2.1 Pair kya hoti hai?

**Pair of Linear Equations** = do linear equations ek saath, dono mein same variables.

**General form:**
```
a₁x + b₁y + c₁ = 0
a₂x + b₂y + c₂ = 0
```

**Example:**
```
2x + 3y = 12
x - y = 1
```

### 2.2 Solution kya hota hai?

**Solution** = wo (x, y) jo **dono equations ko satisfy** kare.

**Example:** `x = 3, y = 2` check karo upar wali equations mein:
- 2(3) + 3(2) = 6 + 6 = 12 ✓
- 3 - 2 = 1 ✓

So **(3, 2) solution hai**. ✅

### 2.3 Graphically — 3 cases possible hote hain

Jab tu dono equations ka graph banayega, **teen possibilities** hain:

#### Case 1: Lines INTERSECT (cut karein) → **UNIQUE solution**
- Dono lines ek point pe milengi
- Wo point hi solution hai
- System is **CONSISTENT**

#### Case 2: Lines PARALLEL (alag-alag) → **NO solution**
- Lines kabhi nahi milti
- Koi common point nahi
- System is **INCONSISTENT**

#### Case 3: Lines COINCIDENT (ek hi line hain) → **INFINITE solutions**
- Dono equations same line represent karti hain
- Har point common hai
- System is **CONSISTENT (Dependent)**

### 2.4 Conditions Without Drawing Graph (Important!)

Sirf coefficients dekh ke pata laga sakte hain ki kaunsi case hai:

| Condition | Geometrical Meaning | Solutions |
|---|---|---|
| `a₁/a₂ ≠ b₁/b₂` | Intersecting lines | Unique solution (Consistent) |
| `a₁/a₂ = b₁/b₂ ≠ c₁/c₂` | Parallel lines | No solution (Inconsistent) |
| `a₁/a₂ = b₁/b₂ = c₁/c₂` | Coincident lines | Infinite solutions (Consistent) |

**🔑 Yaad rakhne ka tareeka:**
- Sab ratios alag → 1 solution
- 2 ratios same, 1 alag → 0 solution
- Sab ratios same → infinite solutions

#### Example 1: `2x + 3y = 7` aur `4x + 6y = 14` ko check kar
- a₁/a₂ = 2/4 = 1/2
- b₁/b₂ = 3/6 = 1/2
- c₁/c₂ = 7/14 = 1/2 (NCERT mein c right side mein hota hai, sign ko denotation ke saath rakhna)

Sab ratios same → **Infinite solutions, coincident lines**

#### Example 2: `x + 2y = 4` aur `2x + 4y = 12`
- a₁/a₂ = 1/2
- b₁/b₂ = 2/4 = 1/2
- c₁/c₂ = 4/12 = 1/3

a₁/a₂ = b₁/b₂ ≠ c₁/c₂ → **No solution, parallel lines**

#### Example 3: `3x + 2y = 5` aur `2x - 3y = 7`
- a₁/a₂ = 3/2
- b₁/b₂ = 2/(-3) = -2/3

a₁/a₂ ≠ b₁/b₂ → **Unique solution, intersecting lines**

---

## SECTION 3: Algebraic Methods (Bina Graph ke Solve)

Graph banana lambi process hai. Algebraic methods se zyada accurate aur fast solve hota hai.

### 3.1 Method 1: SUBSTITUTION Method

**Idea:** Ek equation se ek variable ko doosre ke terms mein nikaalo, phir doosri equation mein daal do.

**Steps:**
1. Ek equation mein se ek variable (jaise y) ko doosre ke terms mein express karo
2. Doosri equation mein woh value daal do
3. Ab single variable ki equation hai — solve karo
4. Pehli equation mein wapas daal ke doosra variable nikaalo

#### Example 4: Solve karo
```
x + y = 14    ...(1)
x - y = 4     ...(2)
```

**Step 1:** Equation (1) se `y = 14 - x`

**Step 2:** Equation (2) mein daal:
```
x - (14 - x) = 4
x - 14 + x = 4
2x = 18
x = 9
```

**Step 3:** `y = 14 - 9 = 5`

**Solution: x = 9, y = 5** ✅

**Verify:** 9 + 5 = 14 ✓ and 9 - 5 = 4 ✓

#### Example 5: Solve karo
```
2x + 3y = 11   ...(1)
2x - 4y = -24  ...(2)
```

**Step 1:** Equation (1) se `2x = 11 - 3y` → `x = (11 - 3y)/2`

**Step 2:** Equation (2) mein daal:
```
2 × (11 - 3y)/2 - 4y = -24
(11 - 3y) - 4y = -24
11 - 7y = -24
-7y = -35
y = 5
```

**Step 3:** `x = (11 - 3(5))/2 = (11 - 15)/2 = -4/2 = -2`

**Solution: x = -2, y = 5** ✅

### 3.2 Method 2: ELIMINATION Method

**Idea:** Equations ko add/subtract karke ek variable ko **gayab** kar do.

**Steps:**
1. Dono equations ko aisa multiply karo ki ek variable ke coefficients same ho jayein
2. Add ya subtract karo to eliminate that variable
3. Single variable wali equation solve karo
4. Pehli mein daal ke doosra variable nikaalo

#### Example 6: Solve karo
```
2x + 3y = 8    ...(1)
4x + 6y = 7    ...(2)
```

**Step 1:** Equation (1) ko 2 se multiply karo:
```
4x + 6y = 16   ...(1')
4x + 6y = 7    ...(2)
```

**Step 2:** Subtract (1') - (2):
```
0 = 9
```

Ye possible nahi hai → **No solution!** (Lines parallel hain)

#### Example 7: Solve karo
```
3x + 4y = 10   ...(1)
2x - 2y = 2    ...(2)
```

**Step 1:** Equation (2) ko 2 se multiply karo to make y-coefficient = 4:
```
4x - 4y = 4    ...(2')
```

**Step 2:** Add (1) + (2'):
```
3x + 4y + 4x - 4y = 10 + 4
7x = 14
x = 2
```

**Step 3:** Equation (2) mein daal: `2(2) - 2y = 2` → `-2y = -2` → `y = 1`

**Solution: x = 2, y = 1** ✅

### 3.3 Konsa method use karein? 🤔

| Situation | Best Method |
|---|---|
| Ek variable ka coefficient already 1 ya -1 hai | **Substitution** |
| Coefficients bade-bade ya odd hain | **Elimination** |
| Equations same form mein hain (jaise 2x+3y, 4x-3y) | **Elimination** (y eliminate ho jayega) |

---

## SECTION 4: Word Problems (Real-life applications)

Yaha kahaani di hoti hai, equations banani hoti hain, phir solve karna hai.

#### Example 8: Age problem

"Father ki age, son ki age se 4 zyada hai. 5 saal pehle, father ki age son se 3 guna thi. Dono ki current ages nikaalo."

**Step 1:** Variables le:
- Son ki current age = x
- Father ki current age = y

**Step 2:** Equations banao:
- "Father age = son ki age se 4 zyada" → `y = x + 4` ... (1) (galat statement, let me re-check)
  
Actually problem ko thoda adjust karta hoon for clearer math:

"Father ki current age son se 30 zyada hai. 5 saal pehle father ki age son se 4 guna thi."

- `y = x + 30` ... (1)
- 5 saal pehle: father age = y - 5, son age = x - 5
- `y - 5 = 4(x - 5)` ... (2)

**Step 3:** Solve (substitution):
```
(x + 30) - 5 = 4(x - 5)
x + 25 = 4x - 20
45 = 3x
x = 15
y = 15 + 30 = 45
```

**Answer:** Son 15 saal ka, Father 45 saal ka. ✅

#### Example 9: Number problem

"Do numbers ka sum 25 hai aur unka difference 5 hai. Numbers nikaalo."

Let numbers be x and y (x > y).
- `x + y = 25` ...(1)
- `x - y = 5` ...(2)

Add (1) + (2): `2x = 30` → x = 15
Subtract: `2y = 20` → y = 10

**Answer:** 15 aur 10. ✅

---

## SECTION 5: Q&A TIME (Section ke baad ka test)

### Set A: Foundation Questions

**Q1.** Ye linear equations konsi hain (1 variable / 2 variables)?
- (a) `3x + 5 = 11`
- (b) `2x + 3y = 12`
- (c) `5y - 7 = 0`
- (d) `x - 4y + 1 = 0`

**Q2.** `x + y = 7` ke liye 3 solutions likho.

### Set B: Conditions for Solution

**Q3.** Bina solve kiye bata, ye system ka kya hoga (unique / no / infinite solution)?
- (a) `x + 2y = 5` aur `2x + 4y = 10`
- (b) `2x + y = 6` aur `4x + 2y = 7`
- (c) `3x - y = 4` aur `x + 2y = 1`

### Set C: Solving

**Q4.** Substitution method se solve kar:
```
x + 2y = 7
3x - y = 0
```

**Q5.** Elimination method se solve kar:
```
2x + 3y = 12
3x - 2y = 5
```

### Set D: Word Problem

**Q6.** Do numbers ka sum 50 hai aur ek number doosre se 10 zyada hai. Numbers nikaalo.

---

## SUMMARY (Yaad rakh)

1. **Linear equation in 2 variables:** `ax + by + c = 0` ka graph **straight line** hota hai.

2. **Pair of linear equations** ke teen cases:
   - Intersecting → unique solution (consistent)
   - Parallel → no solution (inconsistent)
   - Coincident → infinite solutions (dependent)

3. **Coefficient ratios se pata lagao:**
   | Ratio condition | Solutions |
   |---|---|
   | a₁/a₂ ≠ b₁/b₂ | Unique |
   | a₁/a₂ = b₁/b₂ ≠ c₁/c₂ | None |
   | a₁/a₂ = b₁/b₂ = c₁/c₂ | Infinite |

4. **Substitution method:** Ek variable ko doosre se replace karo.

5. **Elimination method:** Equations add/subtract karke ek variable gayab karo.

6. **Word problems:** Variables le → equations banao → solve karo → check karo.

---

Generated by Kiro for Krishna1k
