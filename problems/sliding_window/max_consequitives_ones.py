# Problem: 1004. Max Consecutive Ones III
# Link: https://leetcode.com/problems/max-consecutive-ones-iii/description/
# Difficulty: Medium
# Pattern: Sliding Window (Dynamic Size)

# Intuition:
# We need to find the longest contiguous subarray where we can flip at most k zeros.
# Instead of actually flipping, we allow at most k zeros in our window.
# So the problem becomes: find the longest subarray with at most k zeros.

# Approach:
# Use sliding window with two pointers (left and right).
# Expand the window by moving right pointer.
# Count the number of zeros in the current window.
# If zero_count exceeds k, shrink the window from the left
# until the window becomes valid again (zero_count <= k).
# At every step, update the maximum length of the valid window.

# Time Complexity:
# O(n) → Each element is visited at most twice (once by right, once by left)

# Space Complexity:
# O(1) → No extra space used apart from variables

from typing import List

class Solution:
    def longestOne(self, nums: List[int], k: int):
        left = 0
        max_length = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length


sol = Solution()
print(sol.longestOne([1,1,1,0,0,0,1,1,1,1,0], 2))