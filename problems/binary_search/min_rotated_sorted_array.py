# Problem: 153. Find Minimum in Rotated Sorted Array
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# Difficulty: Medium
# Pattern: Binary Search
#
# Intuition:
# The array was sorted, but after rotation, the smallest number is the point
# where the order breaks.
#
# Example:
# [3, 4, 5, 1, 2]
# Here 1 is the minimum because after 5, the array suddenly drops to 1.
#
# We do not need to check every number. Since the array is still partly sorted,
# we can use binary search and keep removing the side where the minimum cannot be.
#
# The main trick is to compare nums[mid] with nums[right].
#
# If nums[mid] > nums[right]:
# It means mid is in the bigger left part.
# So the minimum must be on the right side.
#
# Else:
# It means mid is already in the smaller sorted part.
# So the minimum can be nums[mid] itself or somewhere on the left side.
#
# Approach:
# Start with left at 0 and right at the last index.
# Find mid.
# If nums[mid] is greater than nums[right], move left to mid + 1.
# Otherwise, move right to mid.
# Keep doing this until left and right meet.
# When they meet, that index is the minimum element.
#
# Time Complexity:
# O(log n), because every step cuts the search space almost in half.
#
# Space Complexity:
# O(1), because we only use a few variables.

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


sol = Solution()
print(sol.findMin([3, 4, 5, 1, 2]))


from typing import List

class MyFirstSolution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        return nums[0]
    
# sort solution = O(n log n) above is this 
# binary search solution = O(log n) but this is expected