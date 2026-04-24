# Problem: 15. 3Sum
# Link: https://leetcode.com/problems/3sum/description/
# Difficulty: Easy
# Pattern: Two Pointers

# Approach / Intuition:
# First, sort the array so numbers are in order.
# Then pick one number at a time (fix it), and try to find two other numbers
# that make the total sum = 0.
# For the remaining part of the array, use two pointers:
# one from the left side and one from the right side.
# If the sum is too small, move left pointer forward.
# If the sum is too big, move right pointer backward.
# If sum becomes 0, store the triplet.
# To avoid duplicate answers, skip repeated values for i, left, and right.

# Time Complexity:
# O(n^2) → one loop + two pointer scan

# Space Complexity:
# O(1) extra space (ignoring output list)

from typing import List

class Solution:
    def threeSum(self,nums:List[int]):
        nums.sort()
        arr=[]

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            left=i+1
            right=len(nums)-1

            while left<right:
                total=nums[i]+nums[left]+nums[right]

                if total==0:
                    arr.append([nums[i],nums[left],nums[right]])

                    left+=1
                    right-=1

                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                    
                elif total<0:
                    left+=1
                else:
                    right-=1
        return arr

sol=Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))