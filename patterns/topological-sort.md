# Topological Sort

## What is Topological Sort?

Topological Sort is a linear ordering of nodes such that:

For every directed edge u → v, u comes before v

---

## Key Requirement

Graph must be:
- Directed
- Acyclic (DAG)

---

## When to Use

Use when:
- Dependencies exist
- Order matters
- Tasks must be completed in sequence

---

## Two Approaches

---

### 1. BFS (Kahn’s Algorithm)

---

#### Steps:

1. Compute indegree of each node
2. Add nodes with indegree 0 to queue
3. Process queue:
   - Remove node
   - Reduce indegree of neighbors
   - Add new 0 indegree nodes

---

#### Code Template

```
from collections import deque

indegree = [0] * n
graph = {i: [] for i in range(n)}

# build graph

queue = deque()

for i in range(n):
    if indegree[i] == 0:
        queue.append(i)

result = []

while queue:
    node = queue.popleft()
    result.append(node)

    for nei in graph[node]:
        indegree[nei] -= 1
        if indegree[nei] == 0:
            queue.append(nei)
```

---

### 2. DFS Approach

---

#### Idea:

- Use recursion
- Track visited and recursion stack
- Add nodes post-order

---

## Cycle Detection

If:
- Result size != number of nodes → cycle exists

---

## Applications

- Course Schedule
- Task scheduling
- Dependency resolution
- Build systems

---

## Time Complexity

O(V + E)

---

## Common Mistakes

- Not calculating indegree correctly
- Forgetting cycle detection
- Using on undirected graph

---

## Must Solve Problems

- Course Schedule
- Course Schedule II
- Alien Dictionary
- Minimum Height Trees

---

## Interview Strategy

1. Identify dependency graph
2. Use BFS (Kahn’s) or DFS
3. Check for cycles

---

## Summary

Topological Sort:
- Orders tasks with dependencies
- Works only on DAG
- Critical for graph problems