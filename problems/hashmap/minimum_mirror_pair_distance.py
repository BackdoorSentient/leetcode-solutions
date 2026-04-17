# Problem: 3761. Minimum Absolute Distance Between Mirror Pairs
# Link: https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/description/?envType=daily-question&envId=2026-04-17
# Difficulty: Medium
# Pattern: HashMap

# Intuition:
# We need to find pairs (i, j) such that reverse(nums[i]) == nums[j] and minimize (j - i).
# Instead of checking all pairs (O(n^2)), we use a hashmap for O(1) lookups.
# For each number, we compute its reverse.
# We store reversed values in the hashmap as keys and their indices as values.
# When processing a number, if it already exists in the hashmap, it means
# some previous number's reverse equals the current number → mirror pair found.
# We update the minimum distance using index difference.

# Approach:
# 1. Iterate through the array.
# 2. Reverse the current number using digit manipulation.
# 3. Check if current value exists in hashmap.
# 4. If yes, compute distance and update minimum.
# 5. Store reversed number with current index in hashmap.

# Time Complexity: O(n * d), where d is number of digits (≈ O(n))
# Space Complexity: O(n)


from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        seen={}
        min_dist=float('inf')

        for index,value in enumerate(nums):
            x=value
            rev=0
            while x>0:
                digit=x%10
                rev=rev*10
                rev=rev+digit
                x//=10
            if value in seen:
                min_dist=min(min_dist,index-seen[value])
            seen[rev]=index
        return min_dist if min_dist!=float('inf') else -1



sol=Solution()
print(sol.minMirrorPairDistance([120,21]))
