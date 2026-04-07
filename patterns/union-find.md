# Union Find (Disjoint Set)

## What is Union Find?

Union Find is used to:
- Track connected components
- Detect cycles in graphs

---

## Core Idea

Each element belongs to a set

Operations:
- Find → which set?
- Union → merge sets

---

## Structure

```
parent = [i for i in range(n)]
rank = [0] * n
```

---

## Find Operation (Path Compression)

```
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
```

---

## Union Operation (Union by Rank)

```
def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rootX == rootY:
        return False

    if rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    elif rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    else:
        parent[rootY] = rootX
        rank[rootX] += 1

    return True
```

---

## Optimizations

---

### 1. Path Compression

Flattens tree

---

### 2. Union by Rank

Keeps tree shallow

---

## When to Use

Use when:
- Connected components
- Cycle detection
- Graph grouping

---

## Applications

- Kruskal’s Algorithm
- Number of Islands
- Redundant Connection
- Accounts Merge

---

## Time Complexity

Almost O(1)

Amortized: O(α(n)) (very small)

---

## Common Mistakes

- Not using path compression
- Wrong union logic
- Forgetting to check cycles

---

## Must Solve Problems

- Number of Connected Components
- Redundant Connection
- Accounts Merge
- Kruskal’s Algorithm

---

## Interview Strategy

1. Identify connectivity problem
2. Use Union Find
3. Optimize with path compression

---

## Summary

Union Find:
- Best for connectivity
- Very fast
- Essential graph technique