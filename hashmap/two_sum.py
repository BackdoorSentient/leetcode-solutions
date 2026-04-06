# Problem: 1. Two Sum
# Link: https://leetcode.com/problems/two-sum/description/
# Difficulty: Easy
# Pattern: Hash Map (Lookup)

# Intuition:
# We need to find two numbers such that their sum equals the target.
# Instead of checking every pair (which is slow), we store numbers we’ve already seen.
# For each element, we calculate its complement (target - current value).
# If that complement already exists in our hashmap, we’ve found the answer.

# Approach:
# 1. Initialize an empty hashmap (seen) to store value -> index.
# 2. Traverse the array using enumerate.
# 3. For each element:
#    - Compute remainder = target - current value.
#    - Check if remainder exists in hashmap:
#         - If yes → return indices.
#    - Otherwise, store current value with its index in hashmap.
# 4. This ensures we find the pair in a single pass.

# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for index,value in enumerate(nums):
            remainder=target-value
            if remainder in seen:
                return [seen[remainder],index]
            seen[value]=index

sol=Solution()
print(sol.twoSum([2,7,11,15],9))