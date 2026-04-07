# String

## What is String in DSA?

A String is a sequence of characters.

Most string problems involve:
- Pattern matching
- Substrings
- Frequency counting
- Transformations

---

## Core Idea

Treat strings like arrays + apply patterns like:
- Sliding window
- Two pointers
- Hashing

---

## Common Operations

```
s.lower()
s.upper()
s.split()
s[::-1]   # reverse
```

---

## Key Patterns

---

### 1. Two Pointers

Used for:
- Palindrome check

```
left, right = 0, len(s)-1

while left < right:
    if s[left] != s[right]:
        return False
    left += 1
    right -= 1
```

---

### 2. Sliding Window

Used for:
- Substrings

Example:
- Longest substring without repeating characters

---

### 3. Hash Map / Frequency Count

```
mp = {}

for ch in s:
    mp[ch] = mp.get(ch, 0) + 1
```

---

### 4. Anagram Pattern

Sort or use frequency

---

### 5. Expand Around Center

Used in:
- Longest Palindromic Substring

---

## Important Concepts

---

### Substring vs Subsequence

- Substring → continuous
- Subsequence → not necessarily continuous

---

### Immutable Strings

Strings cannot be modified directly

---

## Time Complexity

Usually O(n)

---

## Common Mistakes

- Confusing substring vs subsequence
- Not handling edge cases (empty string)
- Inefficient string concatenation

---

## Must Solve Problems

- Valid Palindrome
- Longest Substring Without Repeating Characters
- Group Anagrams
- Longest Palindromic Substring
- Palindromic Substrings

---

## Interview Strategy

1. Identify pattern (window / hashmap / two pointers)
2. Avoid brute force
3. Use efficient operations

---

## Summary

String:
- Combines multiple patterns
- Very common in interviews
- Requires pattern recognition