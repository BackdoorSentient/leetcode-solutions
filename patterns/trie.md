# Trie (Prefix Tree)

## What is a Trie?

A Trie is a tree-like data structure used to store strings efficiently.

Each node represents a character.

---

## Core Idea

Store words character by character so that:
- Common prefixes are shared
- Searching becomes fast

---

## Structure

```
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
```

---

## Basic Operations

---

### 1. Insert

```
def insert(word):
    node = root
    for ch in word:
        if ch not in node.children:
            node.children[ch] = TrieNode()
        node = node.children[ch]
    node.isEnd = True
```

---

### 2. Search

```
def search(word):
    node = root
    for ch in word:
        if ch not in node.children:
            return False
        node = node.children[ch]
    return node.isEnd
```

---

### 3. StartsWith (Prefix)

```
def startsWith(prefix):
    node = root
    for ch in prefix:
        if ch not in node.children:
            return False
        node = node.children[ch]
    return True
```

---

## When to Use

Use when:
- Prefix-based search
- Dictionary problems
- Auto-complete
- Word search problems

---

## Advantages

- Fast prefix queries
- Efficient for large word sets

---

## Disadvantages

- High memory usage
- Not efficient for small datasets

---

## Time Complexity

- Insert: O(n)
- Search: O(n)

n = length of word

---

## Important Patterns

---

### 1. Word Search (Backtracking + Trie)

---

### 2. Replace Words

---

### 3. Auto-complete

---

### 4. Longest Word with Prefix

---

## Common Mistakes

- Forgetting isEnd flag
- Not handling empty strings
- Memory inefficiency

---

## Must Solve Problems

- Implement Trie
- Word Search II
- Replace Words
- Longest Word in Dictionary

---

## Interview Strategy

1. Think prefix
2. Use Trie
3. Combine with DFS if needed

---

## Summary

Trie:
- Best for prefix problems
- Combines tree + string logic
- Powerful but memory heavy