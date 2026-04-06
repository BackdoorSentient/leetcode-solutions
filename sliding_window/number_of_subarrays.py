# Problem: 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# Link: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold
# Difficulty: Medium
# Pattern: Fixed Size Sliding Window

# Intuition:
# - We are given a fixed window size k and need to count how many
#   subarrays of size k have:
#
#           average ≥ threshold
#
# - Instead of calculating average every time:
#
#           average = sum / k
#
#   we transform the condition:
#
#           sum / k ≥ threshold
#      →    sum ≥ k * threshold
#
# - This avoids division and keeps everything in integers (faster).
#
# - So the problem becomes:
#
#   Count number of subarrays of size k whose SUM ≥ k * threshold
#
# - A brute force solution would:
#     - Generate all subarrays of size k
#     - Compute sum each time → O(n * k)
#
# - We optimize using Sliding Window:
#     - Reuse previous window sum in O(1)
#     - Only update by adding one element and removing one element

# Approach:
# 1. Compute the sum of the first k elements → initial window
#
# 2. Precompute target:
#        target = k * threshold
#
# 3. Check if the first window satisfies the condition:
#        if window_sum ≥ target → count++
#
# 4. Slide the window from index k → n-1:
#        For each step:
#            - Add nums[i] (new element entering window)
#            - Remove nums[i - k] (element leaving window)
#
#        window_sum += nums[i]
#        window_sum -= nums[i - k]
#
# 5. After updating, check:
#        if window_sum ≥ target → count++
#
# 6. Return count

# Time Complexity:
# - Computing initial sum → O(k)
# - Sliding window traversal → O(n - k)
#
# Total:
#        O(k + (n - k)) = O(n)
#
# - We traverse the array only once

# Space Complexity:
#        O(1)
#
# - We only use a few variables:
#     window_sum, count, target
# - No extra data structures used

from typing import List

class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        window_sum = sum(nums[:k])

        target = k * threshold

        count = 0

        if window_sum >= target:
            count += 1

        for i in range(k, len(nums)):
            window_sum += nums[i]

            window_sum -= nums[i - k]

            if window_sum >= target:
                count += 1

        return count


# Test
sol = Solution()
print(sol.numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4))