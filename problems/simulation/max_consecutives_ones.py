# Problem: 485. Max Consecutive Ones
# Link: https://leetcode.com/problems/max-consecutive-ones/description/
# Difficulty: Easy
# Pattern: Array Traversal
# Topic: Array

# Intuition:
# We need to find the longest sequence of consecutive 1s in the array.
# So we keep counting 1s as long as they appear continuously.
# When a 0 appears, the streak breaks and we reset the count.

# Approach:
# Initialize two variables: count (current streak) and max_count (maximum streak).
# Traverse the array:
#   - If the element is 1, increment count and update max_count.
#   - If the element is 0, reset count to 0.
# Return max_count after traversal.

# Time Complexity:
# O(n) — We traverse the array once.

# Space Complexity:
# O(1) — Only variables are used, no extra space.

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

sol=Solution()
print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))