# Backtracking

## What is Backtracking?

Backtracking is a technique used to solve problems by:
- Trying all possible choices
- Reverting (undoing) a choice if it leads to a wrong solution

It is basically **DFS + decision tree exploration**.

---

## Core Idea

Choose → Explore → Undo (Backtrack)

---

## When to Use Backtracking

Use when:
- You need all possible combinations / permutations
- Problem asks for "generate all"
- Constraints are small (n ≤ 15 usually)
- You need to explore every path

---

## Backtracking Template

```
def backtrack(path, choices):
    if goal reached:
        result.append(path.copy())
        return

    for choice in choices:
        make choice
        backtrack(updated_path, updated_choices)
        undo choice
```

---

## Key Concepts

### 1. Decision Tree

Each recursive call represents a node  
Each choice is a branch

---

### 2. State

What defines your recursion?

Examples:
- index
- current path
- remaining target

---

### 3. Base Case

When to stop recursion?

Example:
- path length == k
- target == 0

---

## Important Patterns

---

### 1. Subsets

Include / Exclude pattern

```
def dfs(i):
    if i == len(nums):
        result.append(path.copy())
        return

    path.append(nums[i])
    dfs(i+1)

    path.pop()
    dfs(i+1)
```

---

### 2. Permutations

Use visited array

```
for i in range(n):
    if used[i]:
        continue

    used[i] = True
    path.append(nums[i])

    dfs()

    path.pop()
    used[i] = False
```

---

### 3. Combination Sum

Target reduces

```
if target == 0:
    result.append(path.copy())
    return

for i in range(start, len(nums)):
    if nums[i] > target:
        continue

    path.append(nums[i])
    dfs(i, target - nums[i])
    path.pop()
```

---

### 4. Palindrome Partitioning

Split string at every index

---

### 5. N-Queens

Constraint-based backtracking

---

## Pruning (Very Important)

Avoid useless paths

Examples:
- if target < 0 → stop
- if duplicate → skip
- if invalid state → skip

---

## Time Complexity

Usually exponential:
- O(2^n)
- O(n!)

---

## Common Mistakes

- Forgetting to backtrack (pop / undo)
- Not copying path
- Missing pruning
- Wrong base case

---

## Optimization Tips

- Sort input for pruning
- Use sets to avoid duplicates
- Stop early when condition fails

---

## Must Solve Problems

- Subsets
- Subsets II
- Permutations
- Combination Sum
- Combination Sum II
- Palindrome Partitioning
- N-Queens

---

## Interview Strategy

1. Draw decision tree
2. Identify state
3. Write template
4. Add pruning

---

## Summary

Backtracking is:
- Controlled brute force
- DFS on decision tree
- Powerful for combinations and constraints