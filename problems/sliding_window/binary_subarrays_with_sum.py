# Problem: Binary Subarrays With Sum
# Link: https://leetcode.com/problems/binary-subarrays-with-sum
# Difficulty: Medium
# Pattern: Prefix Sum + HashMap

# Intuition:
# We want to count subarrays whose sum = goal.
# Instead of checking all subarrays (which is slow),
# we keep track of running sum (prefix sum).
#
# At any point, if current_sum = prefixsum,
# we check if there was a previous sum such that:
# previous_sum = prefixsum - goal
#
# If yes, then the subarray between them has sum = goal.
# So we count how many times (prefixsum - goal) has appeared before.

# Approach:
# - Use a variable 'prefixsum' to store running sum.
# - Use a hashmap to store frequency of prefix sums.
# - Initialize hashmap with {0:1} (to handle subarrays starting from index 0).
# - Traverse the array:
#     1. Add current number to prefixsum.
#     2. Check if (prefixsum - goal) exists in hashmap:
#        → If yes, add its frequency to count.
#     3. Store/update current prefixsum in hashmap.
# - Return the total count.

# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixsum = 0
        count = 0
        hashmap = {0: 1}

        for num in nums:
            prefixsum += num

            if (prefixsum - goal) in hashmap:
                count += hashmap[prefixsum - goal]

            if prefixsum in hashmap:
                hashmap[prefixsum] += 1
            else:
                hashmap[prefixsum] = 1

        return count
    
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixsum = 0
        count = 0
        hashmap = {0: 1}

        for num in nums:
            prefixsum += num

            count += hashmap.get(prefixsum - goal, 0)
            hashmap[prefixsum] = hashmap.get(prefixsum, 0) + 1

        return count