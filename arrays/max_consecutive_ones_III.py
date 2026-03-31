# Problem:1004. Max Consecutive Ones III
# Link: https://leetcode.com/problems/max-consecutive-ones-iii/description/
# Difficulty: Medium
# Pattern: Silding Window

from typing import List
class Solution:
    def longestOne(self,nums:List[int],k:int):
        left=0
        max_length=0
        zero_count=0

        for right in range(len(nums)):
            if nums[right]==0:
                zero_count +=1
            
            while zero_count>k:
                if nums[left]==0:
                    zero_count -= 1
                left +=1
            
            max_length=max(max_length,right-left+1)
        
        return max_length

sol=Solution()
print(sol.longestOne([1,1,1,0,0,0,1,1,1,1,0],2))