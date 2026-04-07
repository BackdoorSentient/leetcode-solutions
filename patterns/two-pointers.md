# Two Pointers Pattern

## 🧠 Core Idea
Use two indices instead of nested loops to reduce time complexity.

---

## 🔍 Why It Works
Nested loops → O(n²)  
Two pointers → O(n)

You reduce unnecessary comparisons.

---

## 🚀 When to Use
- Sorted arrays
- Pair problems
- Palindrome checking
- Removing duplicates

---

## 🧩 Types

### 1. Opposite Direction
- Left at start
- Right at end

Used in:
- Pair sum
- Palindrome

---

### 2. Same Direction (Fast & Slow)
- Fast pointer moves ahead
- Slow pointer tracks result

Used in:
- Remove duplicates
- Linked list cycles

---

## ⚡ General Strategy
- Compare values
- Move pointers based on condition

---

## 🧠 Intuition
Instead of checking all pairs:
→ Use structure (sorted array) to eliminate possibilities

---

## ⚠️ Common Mistakes
- Using on unsorted array (when not allowed)
- Moving wrong pointer
- Infinite loops (wrong condition)

---

## 🔄 Time & Space Complexity
- Time: O(n)
- Space: O(1)

---

## 🧩 Example Problems
- Valid Palindrome
- Two Sum II (sorted)
- Remove Duplicates

---

## 🧠 Key Insight
Two pointers = **smart traversal using structure**