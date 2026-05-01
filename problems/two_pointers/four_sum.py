# Problem: 18. 4Sum
# Link: https://leetcode.com/problems/4sum/description/
# Difficulty: Medium
# Pattern: Two Pointers

# Intuition / Approach:
# First, sort the array so we can use the two-pointer trick easily.
# We fix two numbers using two loops (i and j), and then try to find
# the remaining two numbers using left and right pointers.
#
# For every pair (i, j), we check the remaining part of the array
# and move left and right pointers based on the sum:
# - If sum is smaller, move left forward to increase it
# - If sum is bigger, move right backward to decrease it
# - If sum matches target, store the result and move both pointers
#
# We also skip duplicates at every step (i, j, left, right) to avoid
# repeating the same quadruplet again.
#
# Time Complexity:
# O(n^3) -> Two loops + one two-pointer scan
#
# Space Complexity:
# O(1) extra (not counting output list)

from typing import List

class Solution:
    def fourSum(self,nums:List[int],target:int):
        nums.sort()
        res=[]
        n=len(nums)

        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue

            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue

                left=j+1
                right=n-1

                while left<right:
                    total=nums[i]+nums[j]+nums[left]+nums[right]

                    if total==target:
                        res.append([nums[i],nums[j],nums[left],nums[right]])

                        left+=1
                        right-=1

                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                        
                        while left<right and nums[right]==nums[right+1]:
                            right -=1
                    elif total<target:
                        left+=1
                    else:
                        right-=1
        return res
    
sol=Solution()
print(sol.fourSum([1,0,-1,0,-2,2],0))