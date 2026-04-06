# Problem: Contiguous Array
# Link: https://leetcode.com/problems/contiguous-array/
# Difficulty: Medium
# Pattern: Prefix Sum + HashMap

# Approach:
# - Since the array contains only 0s and 1s, we convert the problem:
#     0 → -1
#     1 → +1
#   This transforms the problem into:
#     "Find the longest subarray with sum = 0"
#
# - Use a prefix sum to track cumulative sum.
# - If the same prefix sum appears again, it means:
#     The subarray between those indices has sum = 0.
#
# - Use a hashmap to store:
#     prefix_sum → first occurrence index
#
# - For every index:
#     1. Update prefix sum
#     2. If prefix sum already exists in hashmap:
#           → subarray with sum 0 found
#           → calculate length = current_index - first_index
#           → update max_length
#     3. If prefix sum not seen before:
#           → store it in hashmap
#
# - Initialize hashmap with {0: -1}:
#     This handles cases where subarray starts from index 0.
#
# - Return the maximum length found.

# Intuition:
# Prefix sum represents sum from start to current index.
#
# If the same prefix sum occurs again:
#   → The elements in between cancel out to 0
#   → So we found a valid subarray
#
# To maximize length:
#   → Always store the FIRST occurrence of prefix sum

# Time Complexity: O(n)
# - We traverse the array once
# - Each hashmap operation is O(1)

# Space Complexity: O(n)
# - In worst case, all prefix sums are unique
# - Hashmap stores up to n entries


from typing import List

class Solution:
    def findMaxLength(self,nums:List[int]) -> int:
        prefixsum=0
        max_length=0
        hashmap={0:-1}

        for i in range(len(nums)):
            if nums[i]==0:
                prefixsum -=1
            else:
                prefixsum +=1
            
            if prefixsum in hashmap:
                length=i-hashmap[prefixsum]
                if length>max_length:
                    max_length=length
            else:
                hashmap[prefixsum]=i
        return max_length

sol=Solution()
print(sol.findMaxLength([0,1,0]))