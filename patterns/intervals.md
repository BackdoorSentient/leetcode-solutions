# Intervals

## What are Intervals?

Intervals are ranges:
[start, end]

Used to represent time, segments, or ranges.

---

## Core Idea

Most interval problems involve:
- Sorting
- Merging
- Overlap detection

---

## When to Use

Use when:
- Given ranges
- Need to merge or schedule
- Overlap problems

---

## Key Pattern

### Step 1: Sort intervals

```
intervals.sort(key=lambda x: x[0])
```

---

## Important Patterns

---

### 1. Merge Intervals

```
intervals.sort()
merged = []

for interval in intervals:
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])
```

---

### 2. Non-overlapping Intervals

Remove minimum intervals

Greedy:
- Sort by end time

---

### 3. Insert Interval

Insert and merge

---

### 4. Meeting Rooms

Check overlap

---

### 5. Minimum Meeting Rooms

Use heap for tracking rooms

---

## Overlap Condition

Two intervals overlap if:

```
a.start <= b.end AND b.start <= a.end
```

---

## Time Complexity

Sorting dominates:
O(n log n)

---

## Common Mistakes

- Not sorting first
- Wrong overlap condition
- Modifying intervals incorrectly

---

## Must Solve Problems

- Merge Intervals
- Insert Interval
- Non-overlapping Intervals
- Meeting Rooms
- Meeting Rooms II

---

## Interview Strategy

1. Sort intervals
2. Check overlap
3. Merge or count

---

## Summary

Intervals:
- Sorting is key
- Greedy + merging patterns
- Very common in interviews