# Problem: 523. Continuous Subarray Sum
# Link: https://leetcode.com/problems/continuous-subarray-sum/description/
# Difficulty: Medium
# Pattern: Prefix Sum + HashMap

# Approach:
# We keep adding numbers and make a running sum called prefix_sum.
# For every prefix_sum, we take remainder using prefix_sum % k.
# If the same remainder was seen before, it means the sum between that old index and current index is divisible by k.
# Then we only need to check if that subarray length is at least 2.
# We store the first index of each remainder because the oldest index gives the longest possible length.
# seen = {0: -1} is used because before the array starts, sum is 0 at fake index -1.
# This helps when the valid subarray starts from index 0.

# Intuition:
# If two prefix sums give the same remainder after dividing by k,
# then their difference is a multiple of k.
# That difference is the sum of the middle subarray.
# So same remainder again means we found a subarray whose sum is divisible by k.

# Time Complexity:
# O(n), because we go through the array only once.

# Space Complexity:
# O(k), because at most k different remainders can be stored in the hashmap.

from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = 0
        seen = {0: -1}

        for i in range(len(nums)):
            prefix_sum += nums[i]

            remainder = prefix_sum % k

            if remainder in seen:
                if (i - seen[remainder]) >= 2:
                    return True
            else:
                seen[remainder] = i
        
        return False
    
sol = Solution()
print(sol.checkSubarraySum([23, 2, 4, 6, 7], 6))