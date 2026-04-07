# Prefix Sum

## What is Prefix Sum?

Prefix Sum stores cumulative sum up to each index.

```
prefix[i] = nums[0] + nums[1] + ... + nums[i]
```

---

## Core Idea

Precompute sums to answer range queries in O(1)

---

## Why Use Prefix Sum?

Without prefix sum:
- Range sum = O(n)

With prefix sum:
- Range sum = O(1)

---

## Build Prefix Array

```
prefix = [0] * (n + 1)

for i in range(n):
    prefix[i+1] = prefix[i] + nums[i]
```

---

## Range Sum Query

```
sum(l, r) = prefix[r+1] - prefix[l]
```

---

## Important Patterns

---

### 1. Subarray Sum Equals K

Use prefix sum + hashmap

```
mp = {0:1}
prefix = 0

for num in nums:
    prefix += num
    count += mp.get(prefix - k, 0)
    mp[prefix] = mp.get(prefix, 0) + 1
```

---

### 2. Subarray Sums Divisible by K

Use modulo

```
prefix % k
```

---

### 3. Contiguous Array

Convert:
0 → -1

Then find equal 0s and 1s

---

### 4. Binary Subarrays With Sum

Same as subarray sum equals k

---

## Prefix Sum Variants

---

### 1. 2D Prefix Sum

```
prefix[i][j] = matrix sum from (0,0) to (i,j)
```

---

### 2. Prefix XOR

Used in bit problems

---

## Time Complexity

Build: O(n)  
Query: O(1)

---

## Space Complexity

O(n)

---

## Common Mistakes

- Off-by-one errors
- Not initializing mp = {0:1}
- Wrong modulo handling

---

## When to Use Prefix Sum

- Subarray sum problems
- Range queries
- Cumulative frequency

---

## Must Solve Problems

- Subarray Sum Equals K
- Subarray Sums Divisible by K
- Contiguous Array
- Binary Subarrays With Sum

---

## Interview Strategy

1. Think: cumulative sum
2. Use hashmap for counting
3. Handle prefix differences

---

## Summary

Prefix Sum:
- Converts O(n²) → O(n)
- Powerful with hashmap
- Core pattern for subarrays