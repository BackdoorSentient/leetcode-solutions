# Binary Search

## What is Binary Search?

Binary Search is used to find elements in a sorted space by repeatedly dividing the search range in half.

---

## Core Idea

Eliminate half of the search space every step

---

## When to Use Binary Search

Use when:
- Array is sorted
- You need O(log n)
- You are searching for answer in a range

---

## Types of Binary Search

---

### 1. Classic Binary Search

```
while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

---

### 2. Lower Bound

First occurrence

---

### 3. Upper Bound

Last occurrence

---

### 3. Binary Search on Answer (IMPORTANT)

Search in possible answers, not array

Used in:
- Koko Eating Bananas
- Capacity to Ship Packages

---

## Binary Search on Answer Pattern

```
def can(mid):
    return True/False

left, right = range

while left < right:
    mid = (left + right) // 2

    if can(mid):
        right = mid
    else:
        left = mid + 1
```

---

## Key Concepts

---

### 1. Monotonic Function

Condition changes only once

Example:
TTTTFFFF or FFFFTTTT

---

### 2. Search Space

Can be:
- indices
- values
- answer range

---

### 3. Mid Calculation

```
mid = left + (right - left) // 2
```

Avoid overflow

---

## Variations

---

### 1. Search in Rotated Array

Check sorted half

---

### 2. Find Minimum in Rotated Array

---

### 3. Peak Element

Compare neighbors

---

### 4. First and Last Position

Two binary searches

---

## Time Complexity

O(log n)

---

## Common Mistakes

- Infinite loop (wrong condition)
- Wrong mid update
- Using <= vs <
- Not identifying monotonic behavior

---

## Must Solve Problems

- Binary Search
- Search Insert Position
- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array
- Koko Eating Bananas
- Find Peak Element
- First and Last Position

---

## Interview Strategy

1. Identify sorted / monotonic behavior
2. Decide search space
3. Write template
4. Adjust conditions carefully

---

## Summary

Binary Search:
- Reduces search space
- Works on sorted or monotonic problems
- Very important for interviews