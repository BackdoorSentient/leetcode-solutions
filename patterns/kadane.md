# Kadane’s Algorithm (Maximum Subarray)

## What is Kadane’s Algorithm?

Kadane’s Algorithm is used to find the **maximum sum subarray** in an array in O(n) time.

---

## Core Idea

At each index:
- Either extend the current subarray
- Or start a new subarray

---

## Key Insight

If the current sum becomes negative, it will never help future sums → discard it.

---

## Algorithm

```
max_sum = nums[0]
curr_sum = 0

for num in nums:
    curr_sum = max(num, curr_sum + num)
    max_sum = max(max_sum, curr_sum)

return max_sum
```

---

## Intuition

Think:
- "Is it better to continue previous subarray or start fresh?"

---

## Why It Works

Negative sum reduces future sum → reset  
Positive sum helps → keep extending

---

## Step-by-Step Example

nums = [-2,1,-3,4,-1,2,1,-5,4]

```
curr_sum evolves:
-2 → 1 → -2 → 4 → 3 → 5 → 6 → 1 → 5

max_sum = 6
```

Subarray = [4, -1, 2, 1]

---

## Variations

---

### 1. Maximum Product Subarray

Track:
- max product
- min product (because negative flips)

---

### 2. Circular Subarray

Max of:
- normal Kadane
- total sum - min subarray

---

### 3. Maximum Sum with Constraints

Combine with prefix sum or sliding window

---

## Edge Cases

- All negative numbers → return max element
- Single element array

---

## Time Complexity

O(n)

---

## Space Complexity

O(1)

---

## Common Mistakes

- Initializing curr_sum = 0 incorrectly
- Not handling all negative case
- Confusing with prefix sum

---

## Must Solve Problems

- Maximum Subarray
- Maximum Product Subarray
- Maximum Sum Circular Subarray

---

## Interview Strategy

1. Recognize "maximum subarray" pattern
2. Apply Kadane directly
3. Modify for variations

---

## Summary

Kadane:
- Greedy + DP hybrid
- Tracks best subarray dynamically
- Very common interview problem