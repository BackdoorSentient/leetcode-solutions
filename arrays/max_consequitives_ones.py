# Problem:485. Max Consecutive Ones
# Link: https://leetcode.com/problems/max-consecutive-ones/
# Difficulty: Easy
# Pattern: Simple Traversal (not really sliding window)

# Intuition:
# We need to find the longest streak of consecutive 1s.
# Every time we see a 1, we extend the current streak.
# When we see a 0, the streak breaks, so we reset the count.
# We keep track of the maximum streak seen so far.

# Approach:
# Initialize two variables:
# - count → to count current consecutive 1s
# - max_count → to store the maximum consecutive 1s
# Traverse the array:
# - If element is 1 → increment count and update max_count
# - If element is 0 → reset count to 0
# Return max_count at the end.

# Time Complexity:
# O(n) → we traverse the array once

# Space Complexity:
# O(1) → no extra space used


from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        max_count=0

        for i in nums:
            if i==1:
                count +=1
                max_count=max(max_count,count)
            else:
                count=0

        return max_count