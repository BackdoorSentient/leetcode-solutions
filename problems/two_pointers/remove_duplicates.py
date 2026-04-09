# Problem: 26. Remove Duplicates from Sorted Array
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# Difficulty: Easy
# Pattern: Two Pointer

# Intuition:
# Since the array is already sorted, duplicates will always be adjacent.
# We can use two pointers:
# - One pointer (i) to traverse the array
# - Another pointer (k) to track the position of the next unique element
# Whenever we find a new unique element, we place it at index k.

# Approach:
# 1. Initialize k = 1 (first element is always unique)
# 2. Traverse the array from index 1 to n-1
# 3. Compare current element with previous element
# 4. If different:
#    - Place it at index k
#    - Increment k
# 5. Return k (length of unique elements)

# Time Complexity:
# O(n) → We traverse the array once

# Space Complexity:
# O(1) → In-place modification, no extra space used


from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k

sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))