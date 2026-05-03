# Problem: 34. Find First and Last Position of Element in Sorted Array
# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
# Difficulty: Medium
# Pattern: Binary Search

# Approach:
# Since the array is already sorted, we can use binary search instead of checking every index.
# But normal binary search only tells us whether the target exists or not.
# Here we need the first and last position of the target, so we run binary search two times.
#
# First binary search:
# When we find the target, we save its index in ans.
# Then we move to the left side because there may be another same target before it.
#
# Second binary search:
# When we find the target, we save its index in ans.
# Then we move to the right side because there may be another same target after it.
#
# Intuition:
# Think of ans as the best valid index found so far.
# For the first position, we keep trying to improve ans by going left.
# For the last position, we keep trying to improve ans by going right.
# If the target is never found, ans stays -1.
#
# Time Complexity:
# O(log n), because we use binary search two times.
# O(log n) + O(log n) is still O(log n).
#
# Space Complexity:
# O(1), because we only use a few variables.

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first():
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    ans = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        def last():
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    ans = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        left = first()
        right = last()

        return [left, right]


sol = Solution()
print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))