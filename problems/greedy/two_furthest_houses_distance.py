# Problem: 2078. Two Furthest Houses With Different Colors
# Link: https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/?envType=daily-question&envId=2026-04-20
# Difficulty: Easy
# Pattern: Array / Greedy (Ends comparison)

# Intuition:
# we want the biggest gap between two houses having different colors
# biggest gap will always involve either first house or last house
# so first we fix first house and try to go as far right as possible
# wherever color is different we check distance
# then we fix last house and go left to find different color
# again check distance
# finally take the maximum from both sides

# Approach:
# loop from left to right and compare with first color
# loop from right to left and compare with last color
# update max distance in both cases

# Time Complexity:
# O(n) because we go through array twice

# Space Complexity:
# O(1) because we are not using any extra space

from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n=len(colors)
        max_dist=0

        for i in range(n):
            if colors[i]!=colors[0]:
                max_dist=max(max_dist,i-0)
        
        for i in range(n-1,-1,-1):
            if colors[i]!=colors[n-1]:
                max_dist=max(max_dist,(n-1)-i)
        
        return max_dist
    
sol=Solution()
print(sol.maxDistance([1,1,1,6,1,1,1]))