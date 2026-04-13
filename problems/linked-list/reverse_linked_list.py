# Problem: 206. Reverse Linked List
# Link: https://leetcode.com/problems/reverse-linked-list/description/
# Difficulty: Easy
# Pattern: Recursion

# Intuition:
# A linked list can be reversed by changing the direction of its pointers.
# Instead of each node pointing to the next node, we make it point to the previous one.
# We traverse the list once while keeping track of three pointers:
# current (node we are at), prev (previous node), and next (to not lose the rest of the list).

# Approach:
# Initialize prev as None and current as head.
# Traverse the list:
#   - Store next node (nxt = current.next)
#   - Reverse the link (current.next = prev)
#   - Move prev to current
#   - Move current to nxt
# At the end, prev will be the new head of the reversed list.
# Return prev.

# Time Complexity:
# O(n) — We traverse the linked list once.

# Space Complexity:
# O(1) — No extra space is used, reversal is done in-place.

from listnode import ListNode, build_linked_list, print_linked_list
from typing import Optional

class Solution:
    def reverseLinkedList(self, head: Optional[ListNode]):
        current = head
        prev = None

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev

sol = Solution()
l = build_linked_list([1, 2, 3, 4, 5])
reversed_head = sol.reverseLinkedList(l)
print_linked_list(reversed_head)