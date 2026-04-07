# Stack

## What is a Stack?

A Stack is a data structure that follows:

LIFO (Last In First Out)

---

## Core Idea

Last inserted element is removed first

---

## Basic Operations

```
stack = []

stack.append(x)   # push
stack.pop()       # pop
stack[-1]         # top element
```

---

## When to Use Stack

Use when:
- Reversing order
- Matching pairs
- Nested structures
- Backtracking-like behavior

---

## Common Patterns

---

### 1. Valid Parentheses

```
stack = []

for ch in s:
    if opening:
        stack.append(ch)
    else:
        if not stack or mismatch:
            return False
        stack.pop()

return not stack
```

---

### 2. Monotonic Stack

Used for:
- Next greater element
- Daily temperatures

---

### 3. Expression Evaluation

Used in calculators

---

### 4. Undo / Backtracking

Store previous states

---

## Stack vs Recursion

Recursion uses implicit stack

---

## Time Complexity

O(n)

---

## Space Complexity

O(n)

---

## Common Mistakes

- Popping from empty stack
- Not checking top before pop
- Confusing stack with queue

---

## Must Solve Problems

- Valid Parentheses
- Min Stack
- Next Greater Element
- Daily Temperatures

---

## Interview Strategy

1. Look for LIFO pattern
2. Use stack
3. Combine with monotonic logic if needed

---

## Summary

Stack:
- Simple but powerful
- Used in many patterns
- Foundation for advanced techniques