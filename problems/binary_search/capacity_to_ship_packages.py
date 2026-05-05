# Problem: 1011. Capacity To Ship Packages Within D Days
# Link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
# Difficulty: Medium
# Pattern: Binary Search
#
# Approach:
# The ship capacity can never be less than the heaviest package,
# because one package cannot be split.
# So the lowest possible capacity is max(weights).
#
# The highest possible capacity is sum(weights),
# because with that capacity we can ship all packages in one day.
#
# Now we binary search between max(weights) and sum(weights).
# For every middle capacity, we check how many days are needed.
# We keep adding packages to the current day until adding one more package
# crosses the capacity. When it crosses, we start a new day.
#
# If the required days are less than or equal to the given days,
# that capacity works, so we try to find a smaller valid capacity.
# If the required days are more than the given days,
# the capacity is too small, so we increase it.
#
# Intuition:
# Bigger ship capacity means fewer days are needed.
# Smaller ship capacity means more days are needed.
# So this is a good binary search problem because the answer has a clear
# possible / not possible pattern.
#
# Time Complexity:
# O(n * log(sum(weights)))
# For each guessed capacity, we scan all packages once.
#
# Space Complexity:
# O(1)
# We only use a few variables.

from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int):
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            current_weight = 0
            required_days = 1

            for weight in weights:
                if current_weight + weight > mid:
                    required_days += 1
                    current_weight = 0
                current_weight += weight

            if required_days <= days:
                right = mid
            else:
                left = mid + 1

        return left


sol = Solution()
print(sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))