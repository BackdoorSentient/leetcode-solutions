# Prefix Sum Pattern

## 🧠 Core Idea
Precompute cumulative sums so that any subarray sum can be calculated in **O(1)** time.

Instead of recalculating sum for every range, you store running totals.

---

## 🔍 Why It Works
Brute force:
- For every subarray → calculate sum → O(n²)

Prefix Sum:
- Precompute once → O(n)
- Query any subarray → O(1)

---

## 🚀 When to Use
Look for:
- "Subarray sum"
- "Range sum queries"
- "Sum between indices L and R"
- Multiple sum queries on same array

---

## 🧩 Concept

Create a prefix array:

- `prefix[i] = sum of elements from index 0 to i`

---

## ⚡ Key Formula

To find sum of subarray from L to R:

- If L == 0 → directly `prefix[R]`
- Else → `prefix[R] - prefix[L - 1]`

---

## 🧠 Intuition
Instead of summing again:
- Remove unwanted part from total

Think:
"Total till R - total before L = sum of L to R"

---

## ⚡ Example

Array:
[2, 4, 1, 3]

Prefix:
[2, 6, 7, 10]

Find sum from index 1 to 3:
= 10 - 2 = 8

---

## 🧩 Advanced Use Case (IMPORTANT)

### Prefix Sum + HashMap

Used when:
- "Find subarray with given sum"

Idea:
- Store prefix sums in HashMap
- Check if `(current_sum - target)` exists

---

## 🧠 Thinking Process
Ask:
- Am I calculating sums repeatedly?
- Are there multiple range queries?

If yes → Prefix Sum

---

## ⚠️ Common Mistakes
- Off-by-one errors
- Wrong indexing (L-1 confusion)
- Not handling L = 0 case
- Forgetting to initialize prefix properly

---

## 🔄 Time & Space Complexity
- Preprocessing: O(n)
- Query: O(1)
- Space: O(n)

---

## 🧩 Example Problems
- Range Sum Query
- Subarray Sum Equals K
- Continuous Subarray Sum

---

## 🧠 Key Insight
Prefix sum is about:
➡️ **trading space for instant range queries**

It converts repeated work into one-time computation.