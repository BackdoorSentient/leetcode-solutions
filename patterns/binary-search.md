# Binary Search Pattern

## 🧠 Core Idea
Divide search space in half repeatedly.

---

## 🔍 Why It Works
Each step removes half the possibilities → very fast

Time complexity:
O(log n)

---

## 🚀 When to Use
- Sorted arrays
- Monotonic functions
- "Find minimum/maximum valid answer"

---

## 🧩 Two Main Types

### 1. Classic Binary Search
Search element in sorted array

---

### 2. Binary Search on Answer (IMPORTANT)
Search in range of possible answers

Example:
- Koko Eating Bananas
- Capacity to ship packages

---

## ⚡ General Template
1. Define search space
2. Find mid
3. Check condition
4. Move left/right

---

## 🧠 Intuition
Binary search is not about array  
It is about **searching in a sorted/monotonic space**

---

## ⚠️ Common Mistakes
- Infinite loop (wrong condition)
- Overflow in mid calculation
- Wrong boundary updates
- Not understanding monotonic condition

---

## 🔄 Time & Space Complexity
- Time: O(log n)
- Space: O(1)

---

## 🧩 Example Problems
- Binary Search
- Search in Rotated Sorted Array
- Koko Eating Bananas

---

## 🧠 Key Insight
Binary search works on:
➡️ **Monotonic behavior (True/False zones)**