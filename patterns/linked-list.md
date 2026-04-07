# Linked List

## What is a Linked List?

A Linked List is a sequence of nodes where:
- Each node contains value + pointer to next node

---

## Types of Linked Lists

- Singly Linked List
- Doubly Linked List
- Circular Linked List

---

## Core Idea

Nodes are connected via pointers instead of indices.

---

## Basic Structure

```
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

---

## Common Patterns

---

### 1. Traversal

```
curr = head

while curr:
    curr = curr.next
```

---

### 2. Reverse Linked List

```
prev = None
curr = head

while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt

return prev
```

---

### 3. Fast-Slow Pointer

Used for:
- Middle node
- Cycle detection

---

### 4. Merge Two Sorted Lists

```
dummy = ListNode()
curr = dummy

while l1 and l2:
    if l1.val < l2.val:
        curr.next = l1
        l1 = l1.next
    else:
        curr.next = l2
        l2 = l2.next
    curr = curr.next

curr.next = l1 or l2
return dummy.next
```

---

### 5. Remove Nth Node from End

Use two pointers

---

### 6. Detect Cycle

Use fast-slow pointers

---

## Key Techniques

---

### Dummy Node

Helps simplify edge cases

---

### Two Pointer Technique

Maintain gap between pointers

---

### In-place Modification

Change links without extra space

---

## Time Complexity

Usually O(n)

---

## Space Complexity

O(1)

---

## Common Mistakes

- Losing reference to next node
- Not handling edge cases (empty list, single node)
- Incorrect pointer updates

---

## Must Solve Problems

- Reverse Linked List
- Merge Two Sorted Lists
- Linked List Cycle
- Remove Nth Node From End
- Reorder List
- Linked List Cycle II

---

## Interview Strategy

1. Draw linked list
2. Track pointers carefully
3. Use dummy node if needed

---

## Summary

Linked List:
- Pointer-based structure
- Requires careful pointer handling
- Very common in interviews