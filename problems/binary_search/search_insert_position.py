# Problem: 35. Search Insert Position
# Link: https://leetcode.com/problems/search-insert-position/description/
# Difficulty: Easy
# Pattern: Binary Search

# Intuition:
# Since the array is sorted, we can use binary search to efficiently find the target.
# If the target exists, return its index.
# If not, the correct position to insert it is where it would fit while maintaining order.

# Approach:
# 1. Initialize left = 0 and right = len(nums) - 1
# 2. Perform binary search while left <= right
# 3. Find mid index
# 4. If nums[mid] == target → return mid
# 5. If nums[mid] < target → move left to mid + 1
# 6. Else → move right to mid - 1
# 7. When loop ends, left will be the correct insert position
# 8. Return left

# Time Complexity:
# O(log n) → Binary search halves the search space each time

# Space Complexity:
# O(1) → No extra space used


from typing import List

class Solution:
    def searchInsert(self,nums:List[int],target:int):
        left=0
        right=len(nums)-1

        while left<=right:
            mid=left+(right-left)//2

            if nums[mid]==target:
                return mid

            if nums[mid]<target:
                left=mid+1
            else:
                right=mid-1

        return left
    

sol=Solution()
print(sol.searchInsert([1,3,5,6],2))