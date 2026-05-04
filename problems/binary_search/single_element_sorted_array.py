# Problem: 540. Single Element in a Sorted Array
# Link: https://leetcode.com/problems/single-element-in-a-sorted-array/
# Difficulty: Medium
# Pattern: Binary Search

# Approach:
# The array is sorted and every number appears twice except one number.
# Normally, pairs start from even indexes:
# index 0 and 1, index 2 and 3, index 4 and 5, and so on.
# But after the single element, this pair pattern gets disturbed.
#
# So we use binary search and always make mid an even index.
# Then we compare nums[mid] with nums[mid + 1].
#
# If both are equal, the pair is correct.
# That means the single element must be after this pair, so we move left to mid + 2.
#
# If both are not equal, the pair is broken.
# That means the single element is either at mid or somewhere before mid, so we move right to mid.
#
# Intuition:
# Before the single element, pairs are placed correctly.
# After the single element, pairs shift by one index.
# We use this shift to decide which side still contains the single element.
#
# Time Complexity:
# O(log n), because we cut the search space in half every time.
#
# Space Complexity:
# O(1), because we only use a few variables.

from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid

        return nums[left]


sol = Solution()
print(sol.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))