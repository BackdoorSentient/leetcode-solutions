# Heap (Priority Queue)

## What is a Heap?

A Heap is a data structure that always gives:
- Smallest element (Min Heap)
- Largest element (Max Heap)

---

## Core Idea

Maintain order so that top element is always optimal.

---

## Python Heap

Python has **min heap** by default:

```
import heapq

heap = []
heapq.heappush(heap, x)
heapq.heappop(heap)
```

---

## Max Heap Trick

```
heapq.heappush(heap, -x)
```

---

## When to Use Heap

Use when:
- You need top K elements
- Repeated min/max extraction
- Streaming data
- Scheduling problems

---

## Common Patterns

---

### 1. Top K Elements

```
heap = []

for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > k:
        heapq.heappop(heap)
```

---

### 2. Kth Largest Element

Keep heap of size k

---

### 3. Merge K Sorted Lists

Use heap to pick smallest

---

### 4. Sliding Window Maximum

Use heap or deque

---

### 5. Median from Data Stream

Two heaps:
- Max heap (left)
- Min heap (right)

---

## Heap vs Sorting

| Heap | Sorting |
|------|--------|
| O(n log k) | O(n log n) |
| Efficient for top K | Full ordering |

---

## Time Complexity

| Operation | Time |
|----------|------|
| Push | O(log n) |
| Pop | O(log n) |
| Peek | O(1) |

---

## Common Mistakes

- Forgetting heap is min heap
- Not maintaining size k
- Incorrect push/pop order

---

## Must Solve Problems

- Kth Largest Element
- Top K Frequent Elements
- K Closest Points to Origin
- Merge K Sorted Lists
- Median from Data Stream

---

## Interview Strategy

1. Ask: do I need smallest/largest repeatedly?
2. Use heap
3. Limit heap size if needed

---

## Summary

Heap:
- Efficient priority structure
- Best for top K and streaming problems