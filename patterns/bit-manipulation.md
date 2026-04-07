# Bit Manipulation

## What is Bit Manipulation?

Bit manipulation involves working directly with binary representation of numbers using bits (0 and 1).

---

## Why Use It?

- Faster operations
- Memory efficient
- Useful in subsets, XOR problems, masking

---

## Basic Operations

### AND (&)

```
a & b
```

- 1 if both bits are 1

---

### OR (|)

```
a | b
```

- 1 if at least one bit is 1

---

### XOR (^)

```
a ^ b
```

- 1 if bits are different

Important property:
```
a ^ a = 0
a ^ 0 = a
```

---

### NOT (~)

Flips bits

---

### Left Shift (<<)

```
a << 1 = a * 2
```

---

### Right Shift (>>)

```
a >> 1 = a // 2
```

---

## Important Tricks

---

### 1. Check if number is even

```
n & 1 == 0
```

---

### 2. Check if power of 2

```
n & (n - 1) == 0
```

---

### 3. Count set bits

```
while n:
    n = n & (n - 1)
    count += 1
```

---

### 4. Get ith bit

```
(n >> i) & 1
```

---

### 5. Set ith bit

```
n | (1 << i)
```

---

### 6. Remove ith bit

```
n & ~(1 << i)
```

---

## XOR Pattern (Very Important)

Used when:
- Find unique element
- Pairs cancel out

Example:
- Single Number problem

---

## Bitmasking

Represent subsets using bits

Example:
n = 3 → subsets = 2^3 = 8

```
for mask in range(1 << n):
    for i in range(n):
        if mask & (1 << i):
            include nums[i]
```

---

## Common Patterns

---

### 1. Single Number

Use XOR

---

### 2. Missing Number

XOR all numbers

---

### 3. Subsets using bitmask

---

### 4. Two unique numbers

Split using XOR bit

---

## Time Complexity

Usually O(n)

Bit operations are O(1)

---

## Common Mistakes

- Forgetting operator precedence
- Using wrong shift direction
- Not understanding XOR properties

---

## Must Solve Problems

- Single Number
- Missing Number
- Counting Bits
- Subsets (bitmask)

---

## Interview Strategy

1. Think in binary
2. Look for XOR cancellation
3. Use bitmask for subsets

---

## Summary

Bit manipulation:
- Gives optimal solutions
- Useful in XOR, subsets, masking
- Requires practice to master