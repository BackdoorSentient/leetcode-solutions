# Sliding Window Pattern

## 🧠 Core Idea
Instead of recalculating values for every subarray, maintain a **window** that moves across the array.

Reuse previous computations by:
- Adding new element
- Removing old element

---

## 🔍 Why It Works
Brute force checks all subarrays → O(n²)

Sliding window avoids rework → O(n)

---

## 🚀 When to Use
Look for:
- Subarray / substring
- "Maximum / Minimum"
- "Longest / Shortest"
- Contiguous elements

---

## 🧩 Types of Sliding Window

### 1. Fixed Size Window
Window size = constant

Example:
- Maximum average subarray of size k

---

### 2. Variable Size Window
Window expands and shrinks based on condition

Example:
- Longest substring without repeating characters

---

## ⚡ General Template

### Fixed Window
1. Build first window
2. Slide:
   - Add next element
   - Remove previous element

---

### Variable Window
1. Expand window (right++)
2. While condition breaks → shrink (left++)
3. Update result

---

## 🧠 Intuition
Think like:
"Can I reuse previous work instead of recalculating?"

---

## ⚠️ Common Mistakes
- Forgetting to shrink window
- Wrong condition for shrinking
- Updating result at wrong time
- Not handling edge cases (empty, k > n)

---

## 🔄 Time & Space Complexity
- Time: O(n)
- Space: O(1) or O(k)

---

## 🧩 Example Problems
- Maximum Average Subarray
- Longest Substring Without Repeating Characters
- Minimum Window Substring

---

## 🧠 Key Insight
Sliding window is about:
➡️ **Avoiding repeated work on overlapping subarrays**