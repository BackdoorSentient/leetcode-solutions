# Problem: 11. Container With Most Water
# Link: https://leetcode.com/problems/container-with-most-water/description/
# Difficulty: Medium
# Pattern: Two Pointer

# Approach / Intuition:
# We place two pointers at the ends of the array (left and right).
# These two lines form a container, and we calculate how much water it can hold.
# The water level is always limited by the shorter line, so we take min(height[left], height[right]).
# Then we calculate width (distance between pointers) and get the area.
# We keep track of the maximum area seen so far.
# After that, we move the pointer which has the smaller height,
# because moving the taller one won’t help increase the height (it’s already limited by the shorter one).
# By doing this, we try to find a better (taller) boundary while the width shrinks.

# Time Complexity:
# O(n) → we go through the array once using two pointers

# Space Complexity:
# O(1) → no extra space used, only variables

from typing import List

class Solution:
    def maxArea(self,height:List[int]):
        max_area=0
        left=0
        right=len(height)-1

        while left<right:
            h=min(height[left],height[right])
            width=right-left

            area=h*width
            max_area=max(max_area,area)

            if height[left]<height[right]:
                left +=1
            else:
                right -=1
        
        return max_area

sol=Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))