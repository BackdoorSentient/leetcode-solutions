# Problem: 53. Maximum Subarray
# Link: https://leetcode.com/problems/maximum-subarray/
# Difficulty: Medium
# Pattern: Kadane’s Algorithm
#
# Approach:
# We keep track of two things while moving through the array:
# curr_sum stores the best subarray sum ending at the current index.
# max_sum stores the best subarray sum found so far.
#
# At every number, we decide whether it is better to continue the previous subarray
# or start a new subarray from the current number.
#
# Intuition:
# If the previous sum is helping us increase the total, we continue with it.
# If the previous sum is hurting us, we drop it and start fresh from the current number.
#
# Example:
# For nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# The best subarray is [4, -1, 2, 1]
# Its sum is 6.
#
# Time Complexity:
# O(n), because we visit each element only once.
#
# Space Complexity:
# O(1), because we only use two extra variables.


from typing import List

class Solution:
    def maxSum(self, nums: List[int]):
        max_sum = nums[0]
        curr_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(curr_sum, max_sum)
        
        return max_sum

sol = Solution()
print(sol.maxSum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))