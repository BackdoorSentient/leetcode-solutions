# Trees

## What is a Tree?

A Tree is a hierarchical data structure with:
- Nodes
- Edges
- One root

---

## Key Properties

- No cycles
- Exactly one path between nodes
- n nodes → n-1 edges

---

## Types of Trees

- Binary Tree
- Binary Search Tree (BST)
- Balanced Tree
- Complete Tree

---

## Basic Structure

```
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---

## Tree Traversals

---

### 1. DFS Traversals

#### Inorder (Left → Root → Right)

```
def inorder(root):
    if not root:
        return
    inorder(root.left)
    process(root)
    inorder(root.right)
```

---

#### Preorder (Root → Left → Right)

---

#### Postorder (Left → Right → Root)

---

### 2. BFS (Level Order)

```
from collections import deque

queue = deque([root])

while queue:
    node = queue.popleft()

    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)
```

---

## Important Patterns

---

### 1. Depth Calculation

```
return 1 + max(left, right)
```

---

### 2. Diameter of Tree

Track longest path

---

### 3. Lowest Common Ancestor

---

### 4. Path Sum

Check root-to-leaf paths

---

### 5. Balanced Tree

Check height difference

---

## BST Properties

Left < Root < Right

Used for:
- Fast search
- Sorted traversal

---

## Time Complexity

O(n)

---

## Space Complexity

O(h) recursion stack

---

## Common Mistakes

- Not handling null nodes
- Confusing traversal order
- Incorrect recursion base case

---

## Must Solve Problems

- Maximum Depth of Binary Tree
- Invert Binary Tree
- Level Order Traversal
- Diameter of Binary Tree
- Lowest Common Ancestor

---

## Interview Strategy

1. Think recursively
2. Identify traversal type
3. Define return values clearly

---

## Summary

Trees:
- Recursive structure
- Core interview topic
- Requires strong recursion understanding