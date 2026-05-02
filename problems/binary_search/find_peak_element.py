# Problem: 162. Find Peak Element
# Link: https://leetcode.com/problems/find-peak-element/description/
# Difficulty: Medium
# Pattern: Binary Search

# Approach:
# We use binary search to find any peak element.
# At each step, we check nums[mid] and nums[mid + 1].
# If nums[mid] is smaller, it means the slope is going upward,
# so there must be a peak on the right side.
# Otherwise, the slope is going downward,
# so the peak is either at mid or somewhere on the left side.
# We keep shrinking the search range until left and right meet.

# Intuition:
# Think of the array like a mountain path.
# If the path is going up, move right because a peak is ahead.
# If the path is going down, the peak is behind you or at your current spot.
# Since the outside values are treated as negative infinity,
# there will always be at least one peak.

# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def peakEle(self, nums: List[int]):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (right + left) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left


sol = Solution()
print(sol.peakEle([1, 2, 3, 1]))