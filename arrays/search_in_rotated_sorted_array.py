# Problem: 33. Search in Rotated Sorted Array
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# Difficulty: Medium
# Pattern: Binary Search

# Intuition:
# The array is rotated, so it is not fully sorted. However, at any given point,
# at least one half (left → mid OR mid → right) will always be sorted.
# We use this property to decide where the target can exist.
# First, we identify which half is sorted.
# Then, we check if the target lies within that sorted half.
# If yes, we search in that half; otherwise, we search in the other half.
# This way, we reduce the search space by half each time (like binary search).

# Approach:
# 1. Initialize two pointers: left = 0 and right = len(nums) - 1.
# 2. While left <= right:
#    a. Find mid index.
#    b. If nums[mid] == target → return mid.
#    c. Check if left half is sorted:
#         - If nums[left] <= nums[mid]:
#             • If target lies between nums[left] and nums[mid]:
#                 → move right = mid - 1
#             • Else:
#                 → move left = mid + 1
#    d. Else (right half is sorted):
#         • If target lies between nums[mid] and nums[right]:
#             → move left = mid + 1
#         • Else:
#             → move right = mid - 1
# 3. If not found, return -1.

# Time Complexity:
# O(log n) → Each iteration halves the search space (binary search behavior).

# Space Complexity:
# O(1) → No extra space used, only pointers.

from typing import List

class Solution:
    def search(self,nums:List[int],target:int):
        left=0
        right=len(nums)-1

        while left<=right:
            mid=left+(right-left)//2

            if nums[mid]==target:
                return mid
            
            if nums[left]<=nums[mid]:
                if nums[left]<=target<nums[mid]:
                    right = mid-1
                else:
                    left =mid +1

            else:
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return -1

sol=Solution()
print(sol.search([4,5,6,7,0,1,2],0))