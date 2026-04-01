# Problem: 704. Binary Search
# Link: https://leetcode.com/problems/binary-search/description/
# Difficulty: Easy
# Pattern: Binary Search

# Intuition:
# The array is sorted, so instead of checking every element (linear search),
# we can repeatedly divide the search space into half.
# At each step, compare the middle element with the target:
# - If equal → return index
# - If target is smaller → search left half
# - If target is larger → search right half

# Approach:
# 1. Initialize two pointers:
#    left = 0, right = len(nums) - 1
# 2. While left <= right:
#    - Find mid = (left + right) // 2
#    - If nums[mid] == target → return mid
#    - If nums[mid] < target → move left to mid + 1
#    - Else → move right to mid - 1
# 3. If not found, return -1

# Time Complexity:
# O(log n) → Each step halves the search space

# Space Complexity:
# O(1) → No extra space used

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1


sol = Solution()
print(sol.search([-1,0,3,5,9,12], 9))