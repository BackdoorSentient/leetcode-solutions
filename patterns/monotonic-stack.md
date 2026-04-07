# Monotonic Stack

## What is a Monotonic Stack?

A Monotonic Stack maintains elements in increasing or decreasing order.

---

## Core Idea

Remove elements that are no longer useful for future computations.

---

## When to Use

Use when:
- Need next greater/smaller element
- Span problems
- Histogram problems

---

## Types

---

### 1. Increasing Stack

Small → Large

---

### 2. Decreasing Stack

Large → Small

---

## Template

```
stack = []

for i in range(len(nums)):
    while stack and nums[stack[-1]] < nums[i]:
        stack.pop()

    stack.append(i)
```

---

## Key Patterns

---

### 1. Next Greater Element

```
res = [-1] * n
stack = []

for i in range(n):
    while stack and nums[stack[-1]] < nums[i]:
        idx = stack.pop()
        res[idx] = nums[i]

    stack.append(i)
```

---

### 2. Previous Smaller Element

Traverse normally

---

### 3. Daily Temperatures

Find next greater temperature

---

### 4. Largest Rectangle in Histogram

Key idea:
- For each bar, find left and right boundaries

---

## Important Insight

Each element is:
- Pushed once
- Popped once

---

## Time Complexity

O(n)

---

## Common Mistakes

- Using values instead of indices
- Wrong comparison sign
- Not handling leftover stack

---

## Must Solve Problems

- Next Greater Element I
- Daily Temperatures
- Largest Rectangle in Histogram
- Online Stock Span

---

## Interview Strategy

1. Identify "next greater/smaller"
2. Use stack
3. Maintain monotonic order

---

## Summary

Monotonic Stack:
- Efficient for range queries
- Eliminates unnecessary elements
- Very common pattern