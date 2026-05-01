# Problem: 81. Search in Rotated Sorted Array II
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
# Difficulty: Medium
# Pattern: Binary Search
#
# Intuition:
# This problem is almost like normal binary search, but the array is rotated.
# Because of rotation, the smaller values may come after bigger values.
#
# Example:
# [2, 5, 6, 0, 0, 1, 2]
#
# So we cannot directly say:
# if target is smaller, go left
# if target is bigger, go right
#
# Instead, we first try to find which side is sorted.
# If the left side is sorted, we check if target lies inside that left side.
# If yes, we search left.
# Otherwise, we search right.
#
# If the right side is sorted, we check if target lies inside that right side.
# If yes, we search right.
# Otherwise, we search left.
#
# The extra problem here is duplicates.
# Sometimes nums[left], nums[mid], and nums[right] are all same.
# In that case, we cannot clearly tell which side is sorted.
# So we safely shrink both sides by one step.
#
# Approach:
# Start left at 0 and right at the last index.
# Find mid.
# If nums[mid] is target, return True.
# If nums[left], nums[mid], and nums[right] are all equal,
# move left forward and right backward.
# Else if left side is sorted, check if target is inside that side.
# Else the right side is sorted, check if target is inside that side.
# If the loop ends, target is not present.
#
# Time Complexity:
# Average case: O(log n), because most of the time we cut the search area in half.
# Worst case: O(n), because duplicates can force us to shrink only one step at a time.
#
# Space Complexity:
# O(1), because we only use a few variables.
#
# My Previous Solution:
# My first solution was a simple linear search.
# It checks every number one by one and returns True if target is found.
# This is a valid solution and it gives the correct answer.
#
# But it does not use the rotated sorted array property.
# It also does not reduce the search steps like binary search.
#
# Time Complexity of My Previous Solution:
# O(n), because in the worst case it may check every element.
#
# Space Complexity of My Previous Solution:
# O(1), because it does not use extra space.

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True

            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


class PreviousSolution:
    def search(self, nums: List[int], target: int) -> bool:
        for num in nums:
            if num == target:
                return True

        return False


sol = Solution()
print(sol.search([2, 5, 6, 0, 0, 1, 2], 3))

prev_sol = PreviousSolution()
print(prev_sol.search([2, 5, 6, 0, 0, 1, 2], 3))