# Problem: 16. 3Sum Closest
# Link: https://leetcode.com/problems/3sum-closest/
# Difficulty: Medium
# Pattern: Two Pointers

# Approach / Intuition:
# first we sort the array so that we can use two pointer trick easily
# then we fix one number and try to find the best pair for it
# we use left and right pointer to check all possible pairs with that fixed number
# if current sum is closer to target than previous best, we update it
# if sum is small, we move left forward to increase sum
# if sum is big, we move right backward to decrease sum
# if we ever hit exact target, we just return it because nothing can be better than that

# Time Complexity:
# sorting takes O(n log n)
# loop + two pointer takes O(n^2)
# overall time complexity is O(n^2)

# Space Complexity:
# no extra space is used apart from variables
# so space complexity is O(1)

from typing import List

class Solution:
    def threeSumClosest(self,nums:List[int], target: int):
        nums.sort()
        closest=float('inf')

        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1

            while left<right:
                curr=nums[i]+nums[left]+nums[right]

                if abs(curr-target)<abs(closest-target):
                    closest=curr
                
                if curr<target:
                    left+=1
                elif curr>target:
                    right-=1
                else:
                    return curr
        return closest

sol=Solution()
print(sol.threeSumClosest([-1,2,1,-4],1))