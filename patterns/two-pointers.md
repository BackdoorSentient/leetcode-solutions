# Two Pointers

## What is Two Pointers?

Two pointers use two indices to traverse data efficiently.

---

## Core Idea

Instead of nested loops:
- Use two pointers to reduce complexity

---

## Types of Two Pointers

---

### 1. Opposite Direction

```
left = 0
right = n - 1

while left < right:
```

Used in:
- Sorted arrays
- Palindrome problems

---

### 2. Same Direction

```
slow = 0

for fast in range(n):
```

Used in:
- Removing duplicates
- Partitioning

---

## Key Patterns

---

### 1. Pair Sum in Sorted Array

```
while left < right:
    if nums[left] + nums[right] == target:
        return True
    elif sum < target:
        left += 1
    else:
        right -= 1
```

---

### 2. Remove Duplicates

---

### 3. Container With Most Water

---

### 4. Partition Array

---

## When to Use

Use when:
- Sorted array
- Pair/triplet problems
- Palindrome checks
- Subarrays with conditions

---

## Time Complexity

O(n)

---

## Common Mistakes

- Using on unsorted data (when not allowed)
- Moving wrong pointer
- Missing edge cases

---

## Must Solve Problems

- Two Sum II
- Container With Most Water
- 3Sum
- Remove Duplicates from Sorted Array

---

## Interview Strategy

1. Check if sorted
2. Use two pointers
3. Decide movement logic

---

## Summary

Two Pointers:
- Eliminates nested loops
- Very efficient
- Core interview pattern