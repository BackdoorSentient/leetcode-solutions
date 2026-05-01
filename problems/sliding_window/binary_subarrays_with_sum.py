# Problem: 930. Binary Subarrays With Sum
# Link: https://leetcode.com/problems/binary-subarrays-with-sum/description/
# Difficulty: Medium
# Pattern: Prefix Sum + HashMap

# Intuition:
# We want to count subarrays whose sum is goal.
# Instead of checking all subarrays, we keep a running prefix sum.
# If current prefix sum is prefixsum, then we need an older prefix sum
# equal to prefixsum - goal.
# Every time that older prefix sum appeared, it gives one valid subarray.

# Approach:
# Keep prefixsum for the running sum.
# Keep hashmap where key is prefix sum and value is how many times it appeared.
# Start hashmap with {0: 1} to handle subarrays starting from index 0.
# For every num, update prefixsum.
# Add hashmap[prefixsum - goal] to count if it exists.
# Then store current prefixsum in hashmap.

# Time Complexity:
# O(n), because we walk through nums once.

# Space Complexity:
# O(n), because hashmap can store prefix sums.

from typing import List

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
