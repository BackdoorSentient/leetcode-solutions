# Math (Problem Solving)

## What is Math in DSA?

Math problems involve:
- Numbers
- Patterns
- Formulas
- Logical reasoning

---

## Core Idea

Use mathematical properties to:
- Reduce complexity
- Avoid brute force
- Derive direct formulas

---

## Common Areas

---

### 1. Number Properties

- Even / Odd
- Prime numbers
- Divisibility

---

### 2. GCD and LCM

```
gcd(a, b) = gcd(b, a % b)
```

Used in:
- Fractions
- Simplification

---

### 3. Modular Arithmetic

```
(a + b) % m = ((a % m) + (b % m)) % m
```

Used in:
- Large numbers
- Overflow handling

---

### 4. Prime Numbers

Check up to sqrt(n)

---

### 5. Combinatorics

- Permutations
- Combinations

---

### 6. Bit Math

- Power of 2
- Binary representation

---

## Important Patterns

---

### 1. Reverse Number

---

### 2. Palindrome Number

---

### 3. Power Problems

Fast exponentiation

```
def power(x, n):
    if n == 0:
        return 1
    half = power(x, n//2)
    if n % 2 == 0:
        return half * half
    return half * half * x
```

---

### 4. Factorial / Combinations

---

## Optimization Techniques

- Reduce loops using sqrt
- Use formulas instead of iteration
- Avoid overflow using modulo

---

## Time Complexity

Varies:
- O(1) for formulas
- O(sqrt(n)) for factors

---

## Common Mistakes

- Overflow issues
- Not handling negatives
- Ignoring edge cases
- Using brute force

---

## Must Solve Problems

- Palindrome Number
- Reverse Integer
- Power(x, n)
- Count Primes
- Happy Number

---

## Interview Strategy

1. Look for patterns
2. Try mathematical simplification
3. Avoid brute force

---

## Summary

Math:
- Reduces complexity
- Requires pattern recognition
- Often leads to optimal solutions