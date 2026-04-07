# Problem: 21. Merge Two Sorted Lists
# Link: https://leetcode.com/problems/merge-two-sorted-lists/description/
# Difficulty: Easy
# Pattern: Two Pointer (Merge Pattern)

# Intuition:
# We are given two sorted linked lists.
# To maintain sorted order, we always pick the smaller value
# from the heads of both lists and attach it to the result.
#
# Think of it like merging in merge sort:
# Compare → pick smaller → move forward → repeat
#
# A dummy node is used to simplify edge cases (like empty list
# or first insertion).

# Approach:
# 1. Create a dummy node to act as the start of merged list.
# 2. Use a pointer (current) to build the new list.
# 3. Traverse both lists:
#    - Compare list1.val and list2.val
#    - Attach the smaller node to current.next
#    - Move that list forward
#    - Move current forward
# 4. After loop, attach remaining nodes (if any)
# 5. Return dummy.next (actual head)

# Time Complexity: O(n + m)
# - We traverse both lists once

# Space Complexity: O(1)
# - No extra space used (in-place merge)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoPointers(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next

def build_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

sol = Solution()

l1 = build_linked_list([1, 2, 4])
l2 = build_linked_list([1, 3, 4])

merged = sol.mergeTwoPointers(l1, l2)

print_linked_list(merged)