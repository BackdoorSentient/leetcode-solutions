# Problem: 88. Merge Sorted Array
# Link: https://leetcode.com/problems/merge-sorted-array/description/
# Difficulty: Easy
# Pattern: Two Pointer

# Intuition:
# Since nums1 has extra space at the end, we can merge from the back to avoid overwriting elements.
# Compare the largest elements from both arrays and place the larger one at the end.

# Approach:
# 1. Initialize three pointers:
#    - i = m - 1 (last valid element in nums1)
#    - j = n - 1 (last element in nums2)
#    - k = m + n - 1 (last position in nums1)
# 2. Compare nums1[i] and nums2[j]:
#    - Place the larger value at nums1[k]
#    - Move corresponding pointer backward
# 3. Repeat until one array is exhausted
# 4. If nums2 still has elements, copy them into nums1
# 5. nums1 will contain the merged sorted array

# Time Complexity:
# O(m + n) → Each element is processed once

# Space Complexity:
# O(1) → In-place merge, no extra space used


from typing import List

class Solution:
    def mergeSol(self,nums1:List[int],m:int,nums2:List[int],n:int):
        i=m-1
        j=n-1
        k=m+n-1

        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1

        while j>=0:
            nums1[k]=nums2[j]
            j-=1
            k-=1
        # return nums1


sol=Solution()
print(sol.mergeSol([1,2,3,0,0,0],3,[2,5,6],3))