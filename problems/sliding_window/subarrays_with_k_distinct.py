# Problem: 992. Subarrays with K Different Integers
# Link: https://leetcode.com/problems/subarrays-with-k-different-integers/description/
# Difficulty: Hard
# Pattern: Variable Size Sliding Window
# Trick: AtMost(K) - AtMost(K-1)

# Approach:
# We cannot directly count subarrays with exactly k different numbers easily.
# So we use a trick:
# count of subarrays with exactly k = (subarrays with at most k) - (subarrays with at most k-1)
#
# For "at most k":
# We use a sliding window.
# We expand the window by moving right.
# We keep track of how many different numbers are inside the window.
# If the count becomes more than k, we shrink from the left until it becomes valid again.
#
# At each step, we count how many subarrays end at the current position.
# That is: all subarrays starting from left to right are valid.
# So we add (right - left + 1) to the result.
#
# Finally:
# subtracting atMost(k-1) removes all smaller cases,
# leaving only subarrays with exactly k different numbers.


# Intuition:
# Instead of trying to hit exactly k (which is hard),
# we count everything up to k, then remove everything up to k-1.
# The remaining ones are exactly k.
#
# Sliding window helps us efficiently explore all subarrays
# without checking each one again and again.


# Time Complexity:
# O(n)
# Each element is added once and removed once from the window.
# So overall work is linear.


# Space Complexity:
# O(k)
# Because we only store up to k different numbers in the current window.

from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atmost(k):
            count={}
            result=0
            left=0

            for right,value in enumerate(nums):
                count[value]=count.get(value,0)+1

                while len(count)>k:
                    count[nums[left]]-=1
                    if count[nums[left]]==0:
                        del count[nums[left]]
                    
                    left +=1
                result += right -left +1
            
            return result

        return atmost(k)-atmost(k-1)

sol=Solution()
print(sol.subarraysWithKDistinct([1,2,1,2,3],2))