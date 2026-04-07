# Problem: Subarray Sums Equals K
# Link: https://leetcode.com/problems/subarray-sum-equals-k/description/
# Difficulty: Medium
# Pattern: Prefix Sum + HashMap
# Approach:
# - Use prefix sum to keep track of cumulative sum
# - Use a hashmap to store frequency of prefix sums
# - For each element, check if (prefixsum - k) exists in hashmap
#   → If yes, it means a subarray with sum = k exists
# - Add the frequency of (prefixsum - k) to count
# - Update hashmap with current prefix sum
# - Initialize hashmap with {0:1} to handle subarrays starting from index 0
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum=0
        count=0
        hashmap={0:1}

        for num in nums:
            prefixsum += num

            count += hashmap.get(prefixsum-k,0)
            hashmap[prefixsum]=hashmap.get(prefixsum,0)+1
        return count

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum = 0
        count = 0
        hashmap = {0: 1}

        for num in nums:
            prefixsum += num

            if (prefixsum - k) in hashmap:
                count += hashmap[prefixsum - k]

            if prefixsum in hashmap:
                hashmap[prefixsum] += 1
            else:
                hashmap[prefixsum] = 1

        return count