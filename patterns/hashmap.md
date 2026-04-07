# HashMap Pattern

## 🧠 Core Idea
A HashMap (dictionary) stores data as **key → value** pairs and gives **O(1)** average time for insert, delete, and lookup.

Instead of re-computing or re-checking values, you **store information while iterating** and reuse it instantly.

---

## 🔍 Why It Works
Hashing converts a key into an index in memory.

This allows:
- Direct access instead of scanning the whole array
- Turning **O(n²)** problems into **O(n)**

---

## 🚀 When to Use
Use HashMap when you see:
- "Find two elements..."
- "Check if something exists"
- "Count frequency"
- "Track previous values"

---

## 🧩 Common Use Cases

### 1. Lookup Optimization
Store values so you don’t re-scan.

### 2. Frequency Counting
Count occurrences of elements.

### 3. Complement Problems
Example: Two Sum → check `target - num`

### 4. Mapping Relationships
Example: character → value mapping

---

## ⚡ Thinking Process
Ask:
- Can I store something to avoid repeating work?
- Can I check existence in O(1)?

If yes → HashMap

---

## ⚠️ Common Mistakes
- Inserting before checking (wrong for Two Sum)
- Overwriting keys unintentionally
- Not handling duplicates
- Assuming order (HashMap is unordered)

---

## 🔄 Time & Space Complexity
- Time: O(n)
- Space: O(n)

Tradeoff: You use extra memory to gain speed.

---

## 🧩 Example Problems
- Two Sum
- Roman to Integer
- Valid Anagram
- Contains Duplicate

---

## 🧠 Key Insight
HashMap is about **memory vs speed tradeoff**.

You store information → reduce time complexity.