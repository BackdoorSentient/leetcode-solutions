# Problem: 876. Middle of the Linked List
# Link: https://leetcode.com/problems/middle-of-the-linked-list/description/
# Difficulty: Easy
# Pattern: Two Pointer (Slow & Fast)
# Topic: Linked List

# Approach:
# We use two pointers to find the middle of the linked list.
# One pointer moves one step at a time (slow),
# and the other moves two steps at a time (fast).
# As the fast pointer moves quicker, it reaches the end of the list first.
# By the time it reaches the end, the slow pointer will be at the middle.
#
# After finding the middle node, we use it as a starting point
# and print the remaining part of the list from that node.


# Intuition:
# Think of two people walking on a path.
# One walks normally, and the other runs twice as fast.
# When the faster one reaches the end, the slower one is exactly in the middle.


# Time Complexity:
# O(n)
# We go through the list only once.


# Space Complexity:
# O(1)
# We only use a few pointers and no extra space that grows with input size.


from listnode import ListNode,build_linked_list,print_linked_list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def middleList(self,head:Optional[ListNode]):
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        return slow
    
head = build_linked_list([1, 2, 3, 4, 5])

# Create solution object
sol = Solution()

# Get middle node
middle = sol.middleList(head)

print_linked_list(middle)