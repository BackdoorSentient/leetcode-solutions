# Problem: 27. Remove Element
# Link: https://leetcode.com/problems/remove-element/description/
# Difficulty: Easy
# Pattern: Two Pointer

# Intuition:
# We need to remove all occurrences of a given value in-place.
# Instead of actually deleting elements (which is costly),
# we overwrite unwanted elements by shifting valid elements forward.

# Approach:
# 1. Initialize k = 0 → position to place next valid element
# 2. Traverse the array using pointer i
# 3. If nums[i] != val:
#    - Place nums[i] at index k
#    - Increment k
# 4. Ignore elements equal to val
# 5. Return k (length of array after removal)

# Time Complexity:
# O(n) → Single pass through the array

# Space Complexity:
# O(1) → In-place operation, no extra space used


from typing import List

class Solution:
    def removeElements(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

sol = Solution()
print(sol.removeElements([3,2,2,3], 3))