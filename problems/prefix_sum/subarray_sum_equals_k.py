# Problem: 560. Subarray Sum Equals K
# Link: https://leetcode.com/problems/subarray-sum-equals-k/description/
# Difficulty: Medium
# Pattern: Prefix Sum + HashMap

# Intuition:
# We need to count subarrays whose sum is exactly k.
# Instead of checking every subarray, we keep a running prefix sum.
# If current prefix sum is prefixsum, then we need an older prefix sum
# equal to prefixsum - k.
# That old prefix sum tells us the part between old and current has sum k.
#
# seen = {0: 1} helps count subarrays that start from index 0.

# Approach:
# Keep prefixsum for the running sum.
# Keep hashmap where key is prefix sum and value is how many times it appeared.
# For every num, update prefixsum.
# Add hashmap[prefixsum - k] to count if it exists.
# Then store current prefixsum in hashmap.

# Time Complexity:
# O(n), because we walk through nums once.

# Space Complexity:
# O(n), because hashmap can store many prefix sums.

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum = 0
        count = 0
        hashmap = {0: 1}

        for num in nums:
            prefixsum += num
            count += hashmap.get(prefixsum - k, 0)
            hashmap[prefixsum] = hashmap.get(prefixsum, 0) + 1

        return count
