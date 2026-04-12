# Problem: 141. Linked List Cycle
# Link: https://leetcode.com/problems/linked-list-cycle/description/
# Difficulty: Easy
# Pattern: Fast & Slow Pointers
# Topic: Linked List

# Intuition:
# Use two pointers (slow and fast). Slow moves one step at a time,
# while fast moves two steps. If a cycle exists, fast will eventually
# meet slow inside the loop. If no cycle exists, fast will reach the end.

# Approach:
# Initialize both slow and fast pointers at the head.
# Traverse the list while fast and fast.next exist.
# Move slow by one step and fast by two steps.
# If at any point slow equals fast, a cycle is detected → return True.
# If the loop ends, no cycle exists → return False.

# Time Complexity:
# O(n) — Each node is visited at most once.

# Space Complexity:
# O(1) — No extra space is used.

from typing import Optional
from listnode import ListNode

def build_linked_list(arr):
    dummy = ListNode()
    current = dummy
    nodes = []

    for num in arr:
        node = ListNode(num)
        nodes.append(node)
        current.next = node
        current = current.next

    return dummy.next, nodes  # return nodes to help create cycle

class Solution:
    def hasCycle(self,head:Optional[ListNode]):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                return True
            
        return False
    
sol=Solution()

# Correct list creation
head, nodes = build_linked_list([3, 2, 0, -4])

# create cycle: tail -> node with value 2 (index 1)
nodes[-1].next = nodes[1]

has = sol.hasCycle(head)
print(has)

    