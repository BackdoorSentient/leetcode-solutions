# Monotonic Queue

## What is a Monotonic Queue?

A Monotonic Queue is a deque (double-ended queue) that maintains elements in a specific order:
- Increasing (small → large)
- Decreasing (large → small)

---

## Core Idea

Maintain only **useful elements** while removing useless ones.

---

## When to Use

Use when:
- Sliding window problems
- Need min/max in window
- Efficiently maintain order

---

## Why Not Use Heap?

Heap:
- O(log n) per operation

Monotonic Queue:
- O(1) amortized

---

## Key Operations

We maintain a deque of indices.

---

### 1. Push Element

For decreasing queue (max):

```
while dq and nums[dq[-1]] < nums[i]:
    dq.pop()

dq.append(i)
```

---

### 2. Remove Out of Window

```
if dq[0] == i - k:
    dq.popleft()
```

---

### 3. Get Answer

```
nums[dq[0]]  # max element
```

---

## Sliding Window Maximum Template

```
from collections import deque

dq = deque()
result = []

for i in range(len(nums)):
    while dq and nums[dq[-1]] < nums[i]:
        dq.pop()

    dq.append(i)

    if dq[0] == i - k:
        dq.popleft()

    if i >= k - 1:
        result.append(nums[dq[0]])
```

---

## Types

---

### 1. Decreasing Queue

- Front = maximum

---

### 2. Increasing Queue

- Front = minimum

---

## Time Complexity

O(n)

Each element:
- Added once
- Removed once

---

## Common Mistakes

- Not removing out-of-window elements
- Using values instead of indices
- Wrong comparison (< vs >)

---

## Must Solve Problems

- Sliding Window Maximum
- Shortest Subarray with Sum at Least K
- Constrained Subsequence Sum

---

## Interview Strategy

1. Identify sliding window + max/min
2. Use deque
3. Maintain monotonic property

---

## Summary

Monotonic Queue:
- Optimized sliding window technique
- Maintains order efficiently
- Better than heap for window problems