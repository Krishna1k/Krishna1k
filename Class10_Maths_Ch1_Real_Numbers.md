# Class 10 NCERT Maths — Chapter 1: Real Numbers

> A simplified, detailed guide in Hinglish for students who missed Class 7-8-9.
> Based on the official NCERT (English Medium) textbook.

---

## PART 1: Foundation (Jo Class 7-8-9 mein padhana tha)

### 1. Numbers ke Types — Ek Family Tree

Sochh sabhi numbers ek bada family hai. Is family mein alag-alag log hain:

```
                    Real Numbers (R)
                    /              \
            Rational (Q)        Irrational (P)
            /        \              |
      Integers (Z)  Fractions    sqrt(2), sqrt(3), pi
        /    \      (1/2, 3/4)
   Whole(W)  Negative
    /    \   (-1,-2,-3)
  Zero  Natural (N)
        (1,2,3,4...)
```

**Definitions easy bhasha mein:**

| Type | Matlab | Examples |
|---|---|---|
| Natural Numbers (N) | Counting numbers | 1, 2, 3, 4, 5... |
| Whole Numbers (W) | Natural + 0 | 0, 1, 2, 3... |
| Integers (Z) | Whole + negative | ..., -3, -2, -1, 0, 1, 2, 3... |
| Rational Numbers (Q) | p/q form mein likh sake (q != 0) | 1/2, -3/4, 5, 0.25 |
| Irrational Numbers | p/q form mein NAHI likh sake | sqrt(2), sqrt(3), pi |
| Real Numbers (R) | Rational + Irrational sab | Sab kuch jo number line pe hai |

### 2. Rational vs Irrational — Kaise Pehchanen?

**Rational number** ki decimal expansion 2 type ki hoti hai:
- **Terminating** (khatam ho jaye): 0.5, 0.25, 0.125
- **Non-terminating but Repeating** (pattern repeat hota hai): 0.333..., 0.142857142857...

**Irrational number** ki decimal expansion:
- **Non-terminating AND Non-repeating**: sqrt(2) = 1.41421356...

### 3. Prime Numbers vs Composite Numbers

**Prime Number:** Wo number jo sirf 1 aur apne aap se divide hota hai.
- Examples: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29...
- 1 prime nahi hai!
- 2 ekloti even prime hai (Baaki sab prime odd hain)

**Composite Number:** Jo prime nahi hai (1 ke alawa). Iske 2 se zyada factors hote hain.
- Examples: 4, 6, 8, 9, 10, 12, 14, 15...

**Example:**
- 7 ke factors: 1, 7 → sirf 2 factors → Prime
- 12 ke factors: 1, 2, 3, 4, 6, 12 → 6 factors → Composite

### 4. HCF aur LCM — Bachpan se yaad rakh

**HCF (Highest Common Factor)** = GCD = sabse bada number jo dono ko divide kare.
**LCM (Least Common Multiple)** = sabse chhota number jo dono se divide ho.

**Example:** 12 aur 18 ka HCF aur LCM nikaal:
- 12 = 1, 2, 3, 4, 6, 12
- 18 = 1, 2, 3, 6, 9, 18
- Common: 1, 2, 3, 6 → HCF = 6
- Multiples of 12: 12, 24, 36, 48...
- Multiples of 18: 18, 36, 54...
- Common smallest: LCM = 36

**Magic Formula:** HCF x LCM = Product of two numbers
Check: 6 x 36 = 216, aur 12 x 18 = 216. Match!

---

## PART 2: Asli Chapter 1 Content (NCERT)

### Topic 1: The Fundamental Theorem of Arithmetic

**Statement:**
> "Every composite number can be expressed (factorised) as a product of primes, and this factorisation is unique, apart from the order in which the prime factors occur."

**Aasaan bhasha mein:** Koi bhi composite number ko prime numbers ke multiplication se likh sakte hain, aur ye tareeka unique (sirf ek hi tarah ka) hota hai.

**Example 1:** 156 ka prime factorisation kar
```
156 / 2 = 78
 78 / 2 = 39
 39 / 3 = 13
 13 / 13 = 1
```
So, **156 = 2 x 2 x 3 x 13 = 2^2 x 3 x 13**

**Example 2:** 3825 ka prime factorisation
```
3825 / 3 = 1275
1275 / 3 = 425
 425 / 5 = 85
  85 / 5 = 17
  17 / 17 = 1
```
So, **3825 = 3^2 x 5^2 x 17**

**Example 3:** 7 x 11 x 13 + 13 — kya ye composite hai?
```
= 13 x (7 x 11 + 1)
= 13 x (77 + 1)
= 13 x 78
```
Haan, ye composite hai kyunki iske factors 1, 13, 78 ke alawa aur bhi hain.

### Topic 2: HCF and LCM using Prime Factorisation

**Method:**
- HCF = Common prime factors ka product (lowest power)
- LCM = Sab prime factors ka product (highest power)

**Example 4:** 96 aur 404 ka HCF aur LCM nikaal

Step 1: Prime factorisation kar
- 96 = 2^5 x 3
- 404 = 2^2 x 101

Step 2: HCF nikaal (common primes, lowest power)
- Common: 2 (lowest power = 2^2)
- HCF = 2^2 = 4

Step 3: LCM nikaal (all primes, highest power)
- LCM = 2^5 x 3 x 101 = 32 x 3 x 101 = 9696

Verify: HCF x LCM = 4 x 9696 = 38784. And 96 x 404 = 38784. Match!

**Example 5:** 6, 72, 120 — teen numbers ka HCF aur LCM
- 6 = 2 x 3
- 72 = 2^3 x 3^2
- 120 = 2^3 x 3 x 5

HCF (common, lowest power): 2^1 x 3^1 = 6
LCM (all, highest power): 2^3 x 3^2 x 5 = 8 x 9 x 5 = 360

### Topic 3: Revisiting Irrational Numbers

**Theorem:** Let p be a prime number. If p divides a^2, then p divides a (where a is a positive integer).

**Famous Proof: sqrt(2) is irrational** (Ye exam mein aata hai!)

Proof by contradiction:

Step 1: Maan le sqrt(2) rational hai. Toh sqrt(2) = p/q (where p, q integers, q != 0, HCF(p,q) = 1, simplest form).

Step 2: Dono sides square karo:
   2 = p^2 / q^2
   2q^2 = p^2     ...(i)

Step 3: Iska matlab 2 divides p^2. Toh theorem se, 2 divides p.

Step 4: Toh p = 2c (kisi integer c ke liye).

Step 5: Equation (i) mein daal:
   2q^2 = (2c)^2 = 4c^2
   q^2 = 2c^2

Step 6: Iska matlab 2 divides q^2, toh 2 divides q.

Step 7: Ab problem! Humne kaha tha HCF(p, q) = 1, par dono ko 2 divide kar raha hai. Ye contradiction hai.

**Conclusion:** Hamari assumption galat thi. Toh **sqrt(2) irrational hai**. (Proved)

**Example 6:** Prove that sqrt(3) is irrational
1. Maan le sqrt(3) = p/q (HCF = 1)
2. 3q^2 = p^2 → 3 divides p^2 → 3 divides p
3. p = 3c → 3q^2 = 9c^2 → q^2 = 3c^2 → 3 divides q
4. Contradiction (HCF = 1 ko hum break kar diye)
5. So sqrt(3) is irrational.

**Example 7:** Prove that 5 - sqrt(3) is irrational
1. Maan le 5 - sqrt(3) rational hai, kaho r.
2. Toh sqrt(3) = 5 - r.
3. 5 - r rational hai (rational - rational = rational).
4. Par sqrt(3) irrational hai (humne abhi prove kiya).
5. Contradiction! So 5 - sqrt(3) is irrational.

**Example 8:** Prove that 3 x sqrt(2) is irrational
1. Maan le 3 x sqrt(2) rational hai, kaho r = p/q.
2. Toh sqrt(2) = p/(3q), jo rational hai.
3. Par sqrt(2) irrational hai.
4. Contradiction! So 3 x sqrt(2) is irrational.

**Useful rules to remember:**
- Rational + Irrational = Irrational
- Non-zero Rational x Irrational = Irrational
- Irrational + Irrational = ? (could be either, e.g., sqrt(2) + (-sqrt(2)) = 0 rational)

---

## PART 3: Practice Problems (Tu solve kar)

Q1. Express 140 as a product of its prime factors.
Q2. Find the HCF and LCM of 26 and 91 by prime factorisation.
Q3. Prove that sqrt(5) is irrational.
Q4. Show that 3 + 2 x sqrt(5) is irrational.
Q5. Find LCM and HCF of 17, 23, 29.

---

## SUMMARY (Yaad rakh)

1. Fundamental Theorem of Arithmetic: Har composite number = unique product of primes.
2. HCF x LCM = Product of two numbers (sirf 2 numbers ke liye).
3. HCF = common primes x lowest powers
4. LCM = all primes x highest powers
5. sqrt(p) irrational hai jab p prime ho.
6. Rational + Irrational = Irrational
7. Non-zero rational x Irrational = Irrational

---

Generated by Kiro for Krishna1k
