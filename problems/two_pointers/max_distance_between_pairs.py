# Problem: 1855. Maximum Distance Between a Pair of Values
# Link: https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/description/?envType=daily-question&envId=2026-04-19
# Difficulty: Medium
# Pattern: Two Pointer (Sorted Arrays)

# Intuition:
# We have two arrays sorted in decreasing order.
# Instead of checking every pair (which is slow), we use two pointers.
# Start both pointers at 0.
# If nums1[i] <= nums2[j], it means this is a valid pair,
# so we try to increase distance by moving j forward.
# If nums1[i] > nums2[j], it means current i is too big,
# so we move i forward to get a smaller value.
# This way we explore maximum distance without rechecking everything.

# Approach:
# Use two pointers i and j.
# If condition is valid, update answer and move j.
# If not valid, move i.
# Keep going until one pointer reaches the end.

# Time Complexity:
# O(n + m) because each pointer moves at most once across the arrays.

# Space Complexity:
# O(1) because we are not using any extra space.

from typing import List
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max_count=0
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                max_count=max(max_count,j-i)
                j +=1
            else:
                i+=1
        return max_count

        ###brute force
        # max_value=0
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i]<=nums2[j]:
        #             max_value =max(max_value,j-i)
        # return max_value

sol=Solution()
print(sol.maxDistance([55,30,5,4,2],[100,20,10,10,5]))