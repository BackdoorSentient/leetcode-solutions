# Fast and Slow Pointers (Tortoise and Hare)

## What is Fast and Slow Pointer?

This technique uses two pointers moving at different speeds:
- Slow pointer → moves 1 step
- Fast pointer → moves 2 steps

Used to detect cycles and find middle elements efficiently.

---

## Core Idea

If there is a cycle:
- Fast pointer will eventually meet slow pointer

If no cycle:
- Fast pointer reaches end

---

## When to Use

Use when:
- Linked list problems
- Cycle detection
- Middle of list
- Repeated patterns

---

## Basic Template (Cycle Detection)

```
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        return True

return False
```

---

## Key Patterns

---

### 1. Detect Cycle in Linked List

Fast meets slow → cycle exists

---

### 2. Find Start of Cycle

After meeting point:

```
slow = head

while slow != fast:
    slow = slow.next
    fast = fast.next

return slow
```

---

### 3. Find Middle of Linked List

```
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

return slow
```

---

### 4. Check Palindrome Linked List

- Find middle
- Reverse second half
- Compare both halves

---

## Mathematical Insight (Important)

Distance relation:

Let:
- L = distance to cycle start
- C = cycle length

When fast meets slow:
fast has traveled 2x distance of slow

This property helps find cycle start

---

## Time Complexity

O(n)

---

## Space Complexity

O(1)

---

## Common Mistakes

- Not checking fast and fast.next
- Confusing meeting point with start of cycle
- Incorrect pointer updates

---

## Must Solve Problems

- Linked List Cycle
- Linked List Cycle II
- Middle of the Linked List
- Palindrome Linked List

---

## Interview Strategy

1. Ask: Is there a cycle?
2. Use fast-slow immediately
3. If cycle → find entry point

---

## Summary

Fast-slow pointers:
- Detect cycles efficiently
- Find middle in one pass
- Works in O(1) space