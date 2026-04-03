# Problem: 875. Koko Eating Bananas
# Link: https://leetcode.com/problems/koko-eating-bananas/description/
# Difficulty: Medium
# Pattern: Binary Search

# Intuition:
# The faster Koko eats (higher k), the fewer hours she needs.
# The slower she eats (lower k), the more hours she needs.
# This creates a monotonic decreasing relationship:
# k ↑ → total_hours ↓
# So we can apply Binary Search on k (answer space).

# Approach:
# 1. Define search space:
#    - Minimum speed = 1 (cannot be 0)
#    - Maximum speed = max(piles)
#
# 2. Use Binary Search:
#    - For each mid (candidate speed k):
#        - Calculate total hours required:
#          total_hours += ceil(pile / k)
#
# 3. Decision:
#    - If total_hours <= h:
#        → valid speed, try smaller k (right = mid - 1)
#        → store answer
#    - Else:
#        → too slow, increase speed (left = mid + 1)
#
# 4. Return the minimum valid k

# Core Insight (Most Important)
# You are not searching in array.
# You are searching in:
# possible answers (k values)

# A monotonic decreasing function is a function where:
# As input increases → output never increases (it either decreases or stays same)

# Simple Definition
# If:
# x1 < x2
# Then:
# f(x1) ≥ f(x2)
# So output goes:
# Down ↓
# Or stays flat →
# But never goes up ↑

from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            total_hours = 0

            for pile in piles:
                total_hours += math.ceil(pile / mid)

            if total_hours <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


sol = Solution()
print(sol.minEatingSpeed([3,6,7,11], 8))