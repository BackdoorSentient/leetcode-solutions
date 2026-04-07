# Sliding Window

## What is Sliding Window?

Sliding Window is used to process a **subarray or substring of size k or variable size** efficiently.

---

## Core Idea

Instead of recomputing every window:
- Expand window (right pointer)
- Shrink window (left pointer)

---

## Types of Sliding Window

---

### 1. Fixed Size Window

Window size = k

```
window_sum += nums[i]

if i >= k:
    window_sum -= nums[i-k]
```

---

### 2. Variable Size Window

Adjust size dynamically

```
while condition invalid:
    shrink window
```

---

## General Template

```
left = 0

for right in range(n):
    add nums[right]

    while condition not satisfied:
        remove nums[left]
        left += 1

    update answer
```

---

## Key Patterns

---

### 1. Longest Substring Without Repeating Characters

Use set/map

---

### 2. Minimum Window Substring

Shrink window when valid

---

### 3. Max Consecutive Ones

Flip limited zeros

---

### 4. Subarrays with K Constraint

Combine with prefix sum or hashmap

---

## When to Use

Use when:
- Subarray / substring problems
- Continuous segment
- "Longest", "smallest", "count"

---

## Time Complexity

O(n)

Each element:
- Visited at most twice

---

## Common Mistakes

- Not shrinking window properly
- Wrong condition check
- Infinite loop in while
- Not updating answer correctly

---

## Must Solve Problems

- Maximum Average Subarray I
- Minimum Size Subarray Sum
- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Max Consecutive Ones III

---

## Interview Strategy

1. Identify window
2. Expand right
3. Shrink left when needed
4. Track result

---

## Summary

Sliding Window:
- Optimizes subarray problems
- Converts O(n²) → O(n)
- One of the most important patterns