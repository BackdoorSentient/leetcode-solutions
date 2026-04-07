# Dynamic Programming

## What is Dynamic Programming?

Dynamic Programming (DP) is an optimization technique used when:
1. A problem can be broken into smaller subproblems
2. Subproblems repeat
3. We can store results to avoid recomputation

Instead of solving the same problem again and again, we store results and reuse them.

---

## Core Idea

Solve once → store → reuse

DP = Recursion + Memoization OR Tabulation

---

## When to Use DP (Pattern Recognition)

Use DP when you see:
- "Maximum / Minimum"
- "Count ways"
- "Can we reach / is it possible"
- Overlapping subproblems
- Choices at every step

---

## Types of DP

### 1. Top-Down (Memoization)

Use recursion + cache

```
def solve(i):
    if i in dp:
        return dp[i]
    dp[i] = ...
    return dp[i]
```

---

### 2. Bottom-Up (Tabulation)

Build from base case

```
dp[0] = base

for i in range(1, n):
    dp[i] = ...
```

---

## 5 Step DP Thinking Process

### Step 1: Define State

What uniquely identifies a subproblem?

Examples:
- dp[i] → answer till index i
- dp[i][j] → answer using i items and capacity j

---

### Step 2: State Transition

How to move from smaller problem to bigger?

Example:
dp[i] = max(dp[i-1], dp[i-2] + nums[i])

---

### Step 3: Base Case

Smallest valid answer

---

### Step 4: Order of Computation

- Forward
- Backward
- Grid traversal

---

### Step 5: Optimize Space (Optional)

Convert dp array → variables if possible

---

## Important DP Patterns

---

### 1. Linear DP

Used in arrays

Problems:
- Climbing Stairs
- House Robber
- Maximum Subarray

Example:

```
dp[i] = max(dp[i-1] + nums[i], nums[i])
```

---

### 2. Knapsack DP

Choice: take or not take

```
dp[i][w] = max(
    dp[i-1][w],
    dp[i-1][w-weight[i]] + value[i]
)
```

Problems:
- 0/1 Knapsack
- Partition Equal Subset Sum
- Target Sum

---

### 3. Subsequence DP

Used in strings

```
if s1[i] == s2[j]:
    dp[i][j] = 1 + dp[i-1][j-1]
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

Problems:
- Longest Common Subsequence
- Edit Distance

---

### 4. Kadane’s Algorithm

Max subarray

```
curr = max(num, curr + num)
max_sum = max(max_sum, curr)
```

---

### 5. DP on Grids

Move in matrix

```
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

Problems:
- Unique Paths
- Minimum Path Sum

---

### 6. DP with Bitmasking (Advanced)

Used when:
- n ≤ 20
- subsets

---

## Memoization vs Tabulation

| Feature | Memoization | Tabulation |
|--------|------------|-----------|
| Approach | Recursive | Iterative |
| Speed | Slightly slower | Faster |
| Stack | Uses recursion stack | No stack |
| Control | Easy | Requires ordering |

---

## Time Complexity

Usually:
O(n), O(n^2), O(n * target)

---

## Space Optimization

Example:

```
prev = 0
curr = 1

for i in range(n):
    prev, curr = curr, prev + curr
```

---

## Common Mistakes

- Wrong state definition
- Missing base case
- Wrong transition
- Not identifying overlapping subproblems
- Using DP when greedy works

---

## How to Identify DP Quickly

Ask:
- Are subproblems repeating?
- Can I cache results?
- Do I have choices at each step?

If YES → DP

---

## Must Solve Problems

Easy:
- Climbing Stairs
- Min Cost Climbing Stairs

Medium:
- House Robber
- Coin Change
- Longest Increasing Subsequence
- Longest Common Subsequence

Hard:
- Edit Distance
- Regular Expression Matching

---

## Interview Strategy

1. Start with recursion (brute force)
2. Add memoization
3. Convert to tabulation
4. Optimize space

---

## Summary

DP is about:
- Breaking problems
- Avoiding recomputation
- Building solutions step by step

If you master DP patterns, you unlock most medium and hard problems.