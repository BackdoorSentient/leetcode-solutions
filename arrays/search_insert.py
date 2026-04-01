# Problem: 35. Search Insert Position
# Link: https://leetcode.com/problems/search-insert-position/description/
# Difficulty: Easy
# Pattern: Binary Search

# Intuition:
# Since the array is sorted, we can use binary search to efficiently locate
# the target. If the target exists, return its index.
# If it does not exist, we need to return the index where it would be inserted
# to maintain sorted order. Binary search naturally helps us find this position.

# Approach:
# 1. Initialize two pointers:
#    left = 0, right = len(nums) - 1
# 2. While left <= right:
#    - Compute mid = left + (right - left) // 2
#    - If nums[mid] == target → return mid
#    - If nums[mid] < target → move left to mid + 1
#    - Else → move right to mid - 1
# 3. If target is not found, left will point to the correct insertion index
#    → return left

# Time Complexity:
# O(log n) → Binary search reduces the search space by half each step

# Space Complexity:
# O(1) → No extra space is used

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left


sol = Solution()
print(sol.searchInsert([1,3,5,6], 5))