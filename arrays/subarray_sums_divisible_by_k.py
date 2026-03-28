# Problem: Subarray Sums Divisible by K
# Link: https://leetcode.com/problems/subarray-sums-divisible-by-k/
# Difficulty: Medium
# Pattern: Prefix Sum + HashMap
# Approach:
# - Use prefix sum and store remainder frequency
# - If same remainder appears again, subarray between them is divisible by k
# - Handle negative remainders properly
# Time Complexity: O(n)
# Space Complexity: O(k)

from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixsum=0
        count=0
        hashmap={0:1}

        # for num in nums:
        #     prefixsum += num

        #     mod=prefixsum % k

        #     if mod<0:
        #         mod += k

        #     if mod in hashmap:
        #         count += hashmap[mod]
        #         hashmap[mod] += 1
        #     else:
        #         hashmap[mod] = 1
        
        # return count


        for num in nums:
            prefixsum += num

            mod= prefixsum % k

            count +=hashmap.get(mod,0)
            hashmap[mod]=hashmap.get(mod,0)+1
        return count