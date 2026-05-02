# Problem: 69. Sqrt(x)
# Link: https://leetcode.com/problems/sqrtx/description/
# Difficulty: Easy
# Pattern: Binary Search / Math
#
# Approach:
# We need to find the square root of x, but only the integer part.
# That means we need the biggest number whose square is less than or equal to x.
# Instead of checking every number one by one, we use binary search.
# For every middle number, we square it and compare it with x.
# If the square is too big, we search on the left side.
# If the square is small enough, we save it as a possible answer and search on the right side.
#
# Intuition:
# For x = 8, the answer is 2 because:
# 2 * 2 = 4, which is valid
# 3 * 3 = 9, which is too big
# So whenever mid * mid is smaller than x, mid can be the answer.
# But we still try bigger numbers because there might be a better answer.
# The variable ans keeps the last valid number we found.
#
# Time Complexity: O(log x)
# Binary search cuts the search range in half every time.
#
# Space Complexity: O(1)
# We only use a few variables.

class Solution:
    def mySqrt(self, x: int):
        left = 1
        right = x
        ans = 0

        if x < 2:
            return x

        while left <= right:
            mid = (right + left) // 2

            square = mid * mid

            if square == x:
                return mid

            elif square < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans



sol = Solution()
print(sol.mySqrt(8))