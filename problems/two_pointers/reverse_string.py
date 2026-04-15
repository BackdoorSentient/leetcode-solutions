
# Problem: 344. Reverse String
# Link: https://leetcode.com/problems/reverse-string/description/
# Difficulty: Easy
# Pattern: Two Pointer
# Topic: Array / String

# Intuition:
# To reverse the string in-place, we swap characters from both ends
# moving towards the center.

# Approach:
# Initialize two pointers: left at the start and right at the end.
# Swap the characters at these positions.
# Move left forward and right backward.
# Continue until the pointers meet.

# Time Complexity:
# O(n) — Each element is visited once.

# Space Complexity:
# O(1) — In-place operation, no extra space used.

from typing import List

class Solution:
    def reverseString(self, s: List[str]):
        left = 0
        right = len(s) - 1

        while left < right:   # ✅ better condition
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s


sol = Solution()
print(sol.reverseString(["h","e","l","l","o"]))