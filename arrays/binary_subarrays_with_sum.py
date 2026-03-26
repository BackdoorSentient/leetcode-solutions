# Problem: Binary Subarrays With Sum
# Link: https://leetcode.com/problems/binary-subarrays-with-sum
# Difficulty: Medium
# Pattern: Prefix Sum + HashMap

# Approach:
# - We use prefix sum to convert subarray sum problem into a lookup problem
# - At any index, let current prefix sum = prefixsum
# - We want: prefixsum - previous_prefixsum = goal
#   ⇒ previous_prefixsum = prefixsum - goal
# - So for each index, check how many times (prefixsum - goal) has appeared before
# - Store frequency of prefix sums in hashmap
# - Add that frequency to count (number of valid subarrays ending at current index)
# - Update hashmap with current prefix sum
# - Initialize hashmap with {0:1} to handle subarrays starting from index 0

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