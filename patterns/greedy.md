# Greedy

## What is Greedy?

Greedy algorithm makes the best choice at each step hoping it leads to global optimal solution.

---

## Core Idea

Local optimal choice → Global optimal result

---

## When to Use Greedy

Use when:
- Problem asks for max/min
- Choices are independent
- No need to revisit decisions
- Problem has greedy property

---

## Key Insight

If a greedy choice works at one step and never needs correction → greedy is valid

---

## Important Patterns

---

### 1. Interval Scheduling

Sort by end time

```
intervals.sort(key=lambda x: x[1])
```

Pick earliest finishing

---

### 2. Jump Game

Track farthest reachable

---

### 3. Gas Station

Track total and current gas

---

### 4. Fractional Knapsack

Pick highest value/weight ratio

---

### 5. Activity Selection

Same as interval scheduling

---

## Greedy vs DP

| Greedy | DP |
|-------|----|
| Fast | Slower |
| Local decisions | Global decisions |
| Not always correct | Always correct |

---

## How to Prove Greedy Works

1. Greedy choice property
2. Optimal substructure

---

## Common Greedy Strategy

- Sort input
- Pick best option
- Move forward

---

## Time Complexity

Usually O(n log n) due to sorting

---

## Common Mistakes

- Using greedy when DP is needed
- Not proving correctness
- Wrong sorting criteria

---

## Must Solve Problems

- Jump Game
- Jump Game II
- Gas Station
- Merge Intervals
- Non-overlapping Intervals
- Candy

---

## Interview Strategy

1. Try greedy first
2. If fails → think DP
3. Justify greedy choice

---

## Summary

Greedy:
- Fast and efficient
- Works when local decisions are globally optimal
- Requires strong intuition