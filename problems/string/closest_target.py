# Problem: 2515. Shortest Distance to Target String in a Circular Array
# Link: https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/description/
# Difficulty: Easy
# Pattern: Array Traversal (Circular)
# Topic: Array, String

# Intuition:
# Since the array is circular, the shortest path between two indices can be
# either moving forward or wrapping around backward. For every occurrence
# of the target, we calculate the direct distance and the circular distance,
# and take the minimum.

# Approach:
# Traverse the array and check for indices where words[i] == target.
# For each such index:
#   - Compute direct distance: abs(i - startIndex)
#   - Compute circular distance: n - direct distance
#   - Take the minimum of both distances
# Keep track of the smallest distance across all occurrences.
# If target is not found, return -1.

# Time Complexity:
# O(n) — Single pass through the array.

# Space Complexity:
# O(1) — No extra space used.

from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        min_value=float('inf')
        n=len(words)
        for i in range(n):
            if words[i]==target:

                if i>startIndex:
                    dist=i-startIndex
                else:
                    dist=startIndex-i
                
                min_value=min(min_value,dist,n-dist)
        
        return min_value if min_value != float('inf') else -1

sol=Solution()
print(sol.closestTarget(["hello","i","am","leetcode","hello"],"hello",1))


# Intuition:
# Since the array is circular, the shortest path between two indices can be
# either moving forward or wrapping around. For each occurrence of the target,
# we compute the direct distance and the circular distance, and take the minimum.

# Approach:
# Traverse the array and find indices where words[i] == target.
# For each such index:
#   - Compute direct distance using abs(i - startIndex)
#   - Compute circular distance as n - direct distance
#   - Take the minimum of both distances
# Track the smallest distance among all occurrences.
# If target is not found, return -1.

# Time Complexity:
# O(n) — Single pass through the array.

# Space Complexity:
# O(1) — No extra space used.

from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        min_value = float('inf')
        n = len(words)

        for i in range(n):
            if words[i] == target:
                dist = abs(i - startIndex)          # direct distance
                min_value = min(min_value, dist, n - dist)  # circular distance

        return min_value if min_value != float('inf') else -1


sol = Solution()
print(sol.closestTarget(["hello","i","am","leetcode","hello"], "hello", 1))