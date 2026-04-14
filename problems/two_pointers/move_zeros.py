# Problem: 283. Move Zeroes
# Link: https://leetcode.com/problems/move-zeroes/description/
# Difficulty: Easy
# Pattern: Two Pointer

# Intuition:
# We want to move all zeros to the end while maintaining the relative order
# of non-zero elements. So we shift all non-zero elements to the front and
# fill the remaining positions with zeros.

# Approach:
# Use a pointer 'k' to track the position where the next non-zero element should go.
# Traverse the array:
#   - If the current element is non-zero, swap it with the element at index 'k'
#     and increment 'k'.
# This ensures all non-zero elements are moved to the front in order,
# and zeros naturally move to the end.

# Time Complexity:
# O(n) — Single pass through the array.

# Space Complexity:
# O(1) — In-place modification, no extra space used.

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[k],nums[i]=nums[i],nums[k]
                k+=1
        
        return nums

sol=Solution()
print(sol.moveZeroes([0,1,0,3,12]))
        