# Hash Map (Hash Table)

## What is a Hash Map?

A Hash Map stores data in **key → value pairs** and provides **O(1) average time** for insert, delete, and lookup.

---

## Core Idea

Use a hash function to map keys to indices for fast access.

---

## When to Use Hash Map

Use when:
- You need fast lookup
- Checking existence
- Counting frequency
- Mapping relationships

---

## Basic Operations

```
mp = {}

mp[key] = value      # insert/update
value = mp[key]      # access
del mp[key]          # delete
key in mp            # check existence
```

---

## Common Patterns

---

### 1. Frequency Counting

```
for num in nums:
    mp[num] = mp.get(num, 0) + 1
```

Used in:
- Top K Frequent Elements
- Valid Anagram

---

### 2. Two Sum Pattern

Store complement

```
for i, num in enumerate(nums):
    diff = target - num
    if diff in mp:
        return [mp[diff], i]
    mp[num] = i
```

---

### 3. Prefix Sum + Hash Map

Store prefix sums

```
mp = {0: 1}
prefix = 0

for num in nums:
    prefix += num
    count += mp.get(prefix - k, 0)
    mp[prefix] = mp.get(prefix, 0) + 1
```

---

### 4. Grouping

```
mp = {}

for word in strs:
    key = sorted(word)
    mp[key].append(word)
```

Used in:
- Group Anagrams

---

### 5. First Occurrence Tracking

Store index of first appearance

---

## Collision Handling (Concept)

- Two keys can map to same index
- Handled via chaining or open addressing

(Not required for interviews but good to know)

---

## Time Complexity

| Operation | Time |
|----------|------|
| Insert | O(1) |
| Search | O(1) |
| Delete | O(1) |

Worst case: O(n)

---

## Space Complexity

O(n)

---

## Common Mistakes

- Forgetting default values
- Using list instead of tuple/string as key
- Not handling missing keys
- Mutating keys (invalid)

---

## Must Solve Problems

- Two Sum
- Valid Anagram
- Group Anagrams
- Subarray Sum Equals K
- Top K Frequent Elements

---

## Interview Strategy

1. Think: can I trade space for speed?
2. Use hashmap for lookup
3. Combine with prefix sum if needed

---

## Summary

Hash Map:
- Fast lookup structure
- Used in almost every problem
- Core tool for optimization