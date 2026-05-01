# Problem: 2515. Shortest Distance to Target String in a Circular Array
# Link: https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/description/
# Difficulty: Easy
# Pattern: Array Traversal (Circular)
# Topic: Array, String

# Intuition:
# The array is circular, so the shortest path to a target can be direct
# or it can wrap around the end of the array.
# For every place where target appears, we check both distances and keep the smaller one.

# Approach:
# Walk through all words.
# Whenever words[i] is target, find the direct distance using abs(i - startIndex).
# The circular distance is n - direct distance.
# Keep the smallest distance.
# If target never appears, return -1.

# Time Complexity:
# O(n), because we check every word once.

# Space Complexity:
# O(1), because we only use a few variables.

from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        min_value = float('inf')
        n = len(words)

        for i in range(n):
            if words[i] == target:
                dist = abs(i - startIndex)
                min_value = min(min_value, dist, n - dist)

        return min_value if min_value != float('inf') else -1


sol = Solution()
print(sol.closestTarget(["hello", "i", "am", "leetcode", "hello"], "hello", 1))
