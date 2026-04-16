# Problem: 643 Maximum Average Subarray I
# Link: https://leetcode.com/problems/maximum-average-subarray-i/
# Difficulty: Easy
# Pattern: Sliding Window (Fixed Size)

# What is “contiguous subarray of size k”?
# - Elements must be next to each other
# - Length must be exactly k

# Intuition:
# - Instead of calculating the average for every subarray,
#   we focus on finding the maximum SUM of any subarray of size k.
# - Why? Because:
#       average = sum / k
#   Since k is constant, maximizing sum automatically maximizes average.
#
# - A brute force approach would calculate sum for every subarray of size k,
#   which takes O(n * k) time.
#
# - We optimize this using a sliding window:
#   1. Compute sum of first k elements (initial window)
#   2. Slide the window by:
#        - Adding the next element
#        - Removing the previous element
#   3. Keep track of the maximum sum seen so far

# Approach:
# 1. Initialize window_sum with sum of first k elements
# 2. Set max_sum = window_sum
# 3. Loop from index k to end of array:
#       - Add nums[i] (new element entering window)
#       - Subtract nums[i - k] (element leaving window)
#       - Update max_sum
# 4. Return max_sum / k

# Time Complexity:
# - O(n), where n = length of nums
# - We traverse the array only once

# Space Complexity:
# - O(1), constant extra space (no additional data structures used)

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum=sum(nums[:k])
        max_sum=window_sum

        for i in range(k,len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i-k]

            max_sum=max(max_sum,window_sum)

        return max_sum/k

sol = Solution()
print(sol.findMaxAverage([1,12,-5,-6,50,3],4))