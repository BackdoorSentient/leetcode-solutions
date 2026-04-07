# Simulation

## What is Simulation?

Simulation means directly **imitating the process described in the problem** step by step.

You don’t optimize immediately — you **follow the rules exactly as given**.

---

## Core Idea

Understand the process → implement it exactly

---

## When to Use

Use when:
- Problem describes a process step-by-step
- No clear pattern like DP/greedy
- You need to "simulate" actions

---

## Examples

- Robot movement
- Game rules
- Matrix transformations
- String processing

---

## Approach

1. Understand rules clearly
2. Translate rules into code
3. Track state changes
4. Repeat until done

---

## Common Patterns

---

### 1. Grid Simulation

Move in directions:

```
dirs = [(1,0), (-1,0), (0,1), (0,-1)]
```

Used in:
- Robot Return to Origin
- Rotting Oranges

---

### 2. State Tracking

Maintain variables:

```
x, y = 0, 0
```

---

### 3. Step-by-Step Execution

```
for move in moves:
    if move == 'U':
        y += 1
```

---

### 4. Queue-Based Simulation

Used when events spread over time

---

## Time Complexity

Usually O(n) or O(n * m)

---

## Common Mistakes

- Misunderstanding rules
- Missing edge cases
- Not updating state correctly
- Overcomplicating simple simulation

---

## Optimization

- Only optimize if constraints are large
- Use better data structures if needed

---

## Must Solve Problems

- Robot Return to Origin
- Rotting Oranges
- Spiral Matrix
- Game of Life

---

## Interview Strategy

1. Don’t overthink
2. Follow problem exactly
3. Code cleanly

---

## Summary

Simulation:
- Direct implementation approach
- Focus on correctness
- Often easier than it looks