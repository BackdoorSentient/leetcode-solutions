# Problem: 19. Remove Nth Node From End of List
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Difficulty: Medium
# Pattern: Two Pointers (Fast & Slow)
# Topic: Linked List

# Approach / Intuition:
# We use two pointers (slow and fast) with a gap of n nodes between them.
# First, move fast n steps ahead.
# Then move both pointers together until fast reaches the end.
# Now slow will be just before the node we want to remove.
# We skip that node by changing the next pointer.
# A dummy node is used to handle edge cases like removing the first node.

# Time Complexity:
# O(n) → we traverse the list once

# Space Complexity:
# O(1) → no extra space used

from typing import Optional
from listnode import ListNode,print_linked_list,build_linked_list

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        slow=dummy
        fast=dummy

        for _ in range(n):
            fast=fast.next
        
        while fast.next:
            slow=slow.next
            fast=fast.next
        
        slow.next=slow.next.next

        return dummy.next


head = build_linked_list([1,2,3,4,5])

sol = Solution()

result = sol.removeNthFromEnd(head, 2)

print_linked_list(result)