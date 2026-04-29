# Problem: 142. Linked List Cycle II
# Link: https://leetcode.com/problems/linked-list-cycle-ii/description/
# Difficulty: Medium
# Pattern: Fast & Slow Pointers
# Topic: Linked List

# Approach:
# We use two pointers: slow and fast.
# Slow moves one step at a time.
# Fast moves two steps at a time.
# If there is a cycle, both pointers will meet at some point.
# Once they meet, we place one more pointer at head.
# Then move both pointers one step at a time.
# The node where they meet again is the starting point of the cycle.

# Intuition:
# Think of it like two runners on a circular track.
# One runs slow and one runs fast.
# If there is a loop, the faster one will catch the slower one.
# After they meet, the distance from head to cycle start
# is equal to the distance from meeting point to cycle start.
# So moving both at same speed helps find the exact start.

# Time Complexity:
# O(n)
# In worst case we may traverse the list twice.

# Space Complexity:
# O(1)
# We only use pointers, no extra data structure.

from listnode import build_linked_list, ListNode, print_linked_list
from typing import Optional

class Solution:
    def linked_list(self, head: Optional[ListNode]):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                prt = head

                while slow != prt:
                    prt = prt.next
                    slow = slow.next
                
                return prt
        return 0
    

def build_linked_list_with_cycle(arr, pos):
    head = build_linked_list(arr)

    if pos == -1:
        return head

    cycle_start = None
    current = head
    index = 0

    while current.next:
        if index == pos:
            cycle_start = current
        current = current.next
        index += 1

    if index == pos:
        cycle_start = current

    current.next = cycle_start
    return head


head = build_linked_list_with_cycle([3, 2, 0, -4], 1)

sol = Solution()
ans = sol.linked_list(head)

if ans:
    print(ans.val)
else:
    print(None)