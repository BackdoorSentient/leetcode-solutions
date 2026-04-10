# Big O Notation (Complete Deep Dive)

## What is Big O?

Big O notation describes how an algorithm's **time or space grows** as input size `n` increases.

It focuses on:
- Growth rate
- Worst-case behavior
- Scalability

---

# 🔢 Mathematical Definition

We say:

```
f(n) = O(g(n))
```

if there exist constants `c > 0` and `n₀` such that:

```
f(n) ≤ c · g(n)   for all n ≥ n₀
```

---

## 🧠 Intuition

- `f(n)` → actual runtime of algorithm
- `g(n)` → simplified growth function
- `c` → constant multiplier
- `n₀` → threshold where behavior stabilizes

👉 Meaning:

After some point, `f(n)` will **never grow faster than g(n)** (up to a constant factor)

---

# 📈 Growth Rate Hierarchy

From fastest to slowest:

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
```

---

## 🔥 Why Growth Rate Matters

Example for n = 1,000,000:

| Complexity | Steps |
|----------|------|
| O(1) | 1 |
| O(log n) | ~20 |
| O(n) | 1,000,000 |
| O(n²) | 1,000,000,000,000 |

👉 Huge difference as n grows

---

# 🧮 Mathematical Derivations

---

## Logarithmic Growth

Repeated division:

```
n → n/2 → n/4 → n/8 → ... → 1
```

Solve:

```
n / 2^k = 1
⇒ n = 2^k
⇒ k = log₂(n)
```

---

## Triangular Sum

```
1 + 2 + 3 + ... + n = n(n+1)/2
```

⇒ O(n²)

---

## Geometric Series

```
1 + 2 + 4 + 8 + ... + n = 2n - 1
```

⇒ O(n)

---

# 🔍 Time Complexity Analysis

---

## 1. Single Loop

```
for i in range(n):
```

→ O(n)

---

## 2. Nested Loop

```
for i in range(n):
    for j in range(n):
```

→ O(n²)

---

## 3. Dependent Nested Loop

```
for i in range(n):
    for j in range(i):
```

Total:

```
1 + 2 + 3 + ... + n = n(n+1)/2
```

→ O(n²)

---

## 4. Logarithmic Loop

```
while n > 1:
    n = n // 2
```

→ O(log n)

---

## 5. Two Pointers

```
left = 0
right = n-1

while left < right:
    left += 1
    right -= 1
```

→ O(n)

(each element processed once)

---

## 6. Sliding Window

```
for right in range(n):
    while condition:
        left += 1
```

→ O(n)

(each index moves at most n times)

---

## 7. Recursion

Example:

```
T(n) = T(n-1) + O(1)
```

→ O(n)

---

### Divide and Conquer

```
T(n) = 2T(n/2) + O(n)
```

→ O(n log n)

---

## Master Theorem (Advanced)

For:

```
T(n) = aT(n/b) + O(n^d)
```

Cases:

- If d < log_b(a) → O(n^(log_b a))
- If d = log_b(a) → O(n^d log n)
- If d > log_b(a) → O(n^d)

---

# 🧠 Space Complexity (Deep Dive)

Measures **extra memory used by the algorithm**

---

## 🔑 Input vs Auxiliary Space

- Input space → given by problem (NOT counted)
- Auxiliary space → extra memory (counted)

Example:

```
arr = input (not counted)
new_arr = [0]*n (counted)
```

---

## 🧠 Recursion Stack Space

Each recursive call uses memory

```
def dfs(node):
    dfs(node.left)
```

If depth = n:

```
Space = O(n)
```

---

## ⚖️ In-place vs Extra Space

In-place:
```
nums.sort()
```
→ O(1) or O(log n)

Extra space:
```
sorted(nums)
```
→ O(n)

---

## ⚠️ Hidden Space Usage (VERY IMPORTANT)

| Structure | Space |
|----------|------|
| HashMap | O(n) |
| Set | O(n) |
| Stack | O(n) |
| Queue | O(n) |
| Heap | O(n) |

---

## 📦 Space Examples

---

### O(1)

```
x = 10
```

---

### O(n)

```
arr = [0] * n
```

---

### O(n²)

```
matrix = [[0]*n for _ in range(n)]
```

---

## 🔁 Recursion Space Example

```
def f(n):
    return f(n-1)
```

→ O(n) stack space

---

# ⚖️ Time vs Space Tradeoff

- Faster algorithms may use more memory
- Less memory may increase time

Example:
- HashMap → O(n) space but faster lookup

---

# 🚨 Important Rules

---

## 1. Drop Constants

```
O(2n) → O(n)
```

---

## 2. Drop Lower Order Terms

```
O(n² + n) → O(n²)
```

---

## 3. Consider Worst Case

Big O = worst-case complexity

---

# ❗ Common Mistakes

- Ignoring nested loops
- Confusing log n with n
- Ignoring recursion stack space
- Ignoring hashmap/extra structures
- Counting input as extra space

---

# 🧠 How to Think in Interviews

Ask:

1. How many times does loop run?
2. Is there nesting?
3. Is input shrinking (log)?
4. Are we using extra data structures?
5. Is recursion involved?

---

# 🔥 Pattern → Complexity Mapping

| Pattern | Time |
|--------|------|
| Sliding Window | O(n) |
| Two Pointers | O(n) |
| Binary Search | O(log n) |
| Prefix Sum | O(n) |
| HashMap | O(n) |
| DFS/BFS | O(V + E) |
| Heap | O(log n) |
| DP | O(n) to O(n²) |
| Backtracking | O(2ⁿ) |

---

# 🎯 Final Intuition

Big O is not about exact time — it's about:

- Growth
- Scalability
- Efficiency

---

## 🧾 Summary

- Big O = upper bound
- Includes BOTH time and space
- Focus on large input
- Ignore constants
- Compare growth rates
- Always mention space in interviews