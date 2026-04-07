# Graphs

## What is a Graph?

A graph is a collection of:
- Nodes (vertices)
- Edges (connections)

---

## Types of Graphs

- Directed / Undirected
- Weighted / Unweighted
- Cyclic / Acyclic
- Connected / Disconnected

---

## Graph Representation

---

### 1. Adjacency List (Most Common)

```
graph = {
    0: [1, 2],
    1: [2],
    2: [0]
}
```

---

### 2. Adjacency Matrix

```
matrix[i][j] = 1 if edge exists
```

---

## Core Traversals

---

### 1. DFS (Depth First Search)

```
def dfs(node):
    visited.add(node)

    for nei in graph[node]:
        if nei not in visited:
            dfs(nei)
```

---

### 2. BFS (Breadth First Search)

```
from collections import deque

queue = deque([start])
visited.add(start)

while queue:
    node = queue.popleft()

    for nei in graph[node]:
        if nei not in visited:
            visited.add(nei)
            queue.append(nei)
```

---

## Important Patterns

---

### 1. Connected Components

Count how many separate groups

---

### 2. Cycle Detection

- Undirected → use parent
- Directed → use recursion stack

---

### 3. Shortest Path

- Unweighted → BFS
- Weighted → Dijkstra

---

### 4. Topological Sort

Used in DAG

---

### 5. Grid as Graph

Treat matrix as graph

Used in:
- Number of Islands
- Rotting Oranges

---

## BFS vs DFS

| Feature | BFS | DFS |
|--------|-----|-----|
| Uses | Queue | Recursion/Stack |
| Finds shortest path | Yes | No |
| Memory | More | Less |

---

## Time Complexity

O(V + E)

---

## Common Mistakes

- Not marking visited
- Infinite loops
- Wrong graph representation
- Confusing BFS and DFS use cases

---

## Must Solve Problems

- Number of Islands
- Rotting Oranges
- Clone Graph
- Course Schedule
- Pacific Atlantic Water Flow

---

## Interview Strategy

1. Identify graph structure
2. Choose BFS or DFS
3. Track visited
4. Handle cycles carefully

---

## Summary

Graphs:
- Model relationships
- Use BFS/DFS for traversal
- Core topic for interviews