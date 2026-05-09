# Problem: 152. Maximum Product Subarray
# Link: https://leetcode.com/problems/maximum-product-subarray/
# Difficulty: Medium
# Pattern: Kadane’s Algorithm
#
# Approach:
# We keep track of three values while moving through the array:
# max_prod stores the maximum product ending at the current index.
# min_prod stores the minimum product ending at the current index.
# ans stores the best product found so far.
#
# We need both max_prod and min_prod because a negative number can flip the result.
# A small negative product can become a large positive product when multiplied
# by another negative number.
#
# Intuition:
# At every number, we decide whether to start a new subarray from that number
# or continue the previous product.
#
# If the current number is negative, the maximum and minimum products swap roles.
# The previous maximum can become minimum, and the previous minimum can become maximum.


# Time Complexity:
# O(n), because we visit each element only once.
#
# Space Complexity:
# O(1), because we only use a few extra variables.


from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)

            ans = max(ans, max_prod)
        
        return ans
    
sol=Solution()
print(sol.maxProduct([2,3,-2,4]))