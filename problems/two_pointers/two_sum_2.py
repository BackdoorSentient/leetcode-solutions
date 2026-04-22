# Problem: 167. Two Sum II - Input Array Is Sorted
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# Difficulty: Medium
# Pattern: Two Pointers

# Approach / Intuition:
# Since the array is already sorted, we can use two pointers instead of checking all pairs.
# Start one pointer at the beginning (left) and one at the end (right).
# Add the numbers at both pointers and compare with target.
# If the sum is equal to target, we found our answer.
# If the sum is smaller than target, we move left forward to increase the sum.
# If the sum is greater than target, we move right backward to decrease the sum.
# This way we avoid unnecessary checks and reach the answer faster.

# Time Complexity:
# O(n) → we scan the array once using two pointers

# Space Complexity:
# O(1) → no extra space used

from typing import List

class Solution:
    def twoSum(self,numbers:List[int],target:int):

        left=0
        right=len(numbers)-1

        while left<right:
            curr=numbers[left]+numbers[right]

            if curr==target:
                return [left+1,right+1]

            if curr<target:
                left +=1
            else:
                right -=1

sol=Solution()
print(sol.twoSum([2,7,11,15],9))