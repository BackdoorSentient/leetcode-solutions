# Problem: 209. Minimum Size Subarray Sum
# Link: https://leetcode.com/problems/minimum-size-subarray-sum/
# Difficulty: Medium
# Pattern: Dynamic Size Sliding Window

# min_value = float('inf')
# max_value = float('-inf')

# why right - left + 1?
# This gives the length of the current subarray (window).
# Whenever working with:
# - Subarrays
# - Sliding window
# - Two pointers
# length = right - left + 1

# Intuition:
# - We need to find the SMALLEST subarray whose sum ≥ target.
#
# - Since all elements are positive:
#      Expanding window → increases sum
#     Shrinking window → decreases sum
#
# - This allows us to use a sliding window approach efficiently.
#
# - Strategy:
#     1. Expand the window by moving 'right'
#     2. When sum becomes ≥ target:
#           → we found a valid subarray
#     3. Then shrink from the left to make it as small as possible
#
# - We use a WHILE loop (not IF) because:
#     We want the minimum length
#     So we keep shrinking until condition breaks

# Approach:
# 1. Initialize:
#       left = 0
#       window_sum = 0
#       min_length = infinity (means no valid answer yet)
#
# 2. Iterate 'right' from 0 → n-1:
#       - Add nums[right] to window_sum (expand window)
#
# 3. When window_sum ≥ target:
#       - Update min_length using:
#             right - left + 1
#
#       - Shrink window:
#             subtract nums[left]
#             move left forward
#
#       - Repeat shrinking while condition holds
#
# 4. After loop:
#       - If min_length is still infinity → no valid subarray → return 0
#       - Else return min_length

# Time Complexity:
# - O(n)
#
# - Each element is:
#     added once (right pointer)
#     removed once (left pointer)
#
# - So total operations are linear

# Space Complexity:
# - O(1)
#
# - Only a few variables are used:
#     window_sum, left, min_length

from typing import List

class Solution:
    def minSubArrayLen(self, nums: List[int], target: int):
        window_sum = 0
        left = 0
        min_length = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                min_length = min(min_length, right - left + 1)

                window_sum -= nums[left]
                left += 1

        return 0 if min_length == float('inf') else min_length


sol = Solution()
print(sol.minSubArrayLen([2,3,1,2,4,3], 7))