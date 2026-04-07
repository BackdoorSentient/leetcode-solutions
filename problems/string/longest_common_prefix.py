# Problem: 14. Longest Common Prefix
# Link: https://leetcode.com/problems/longest-common-prefix/description/
# Difficulty: Easy
# Pattern: String

# Intuition:
# The common prefix of all strings must be a prefix of the first string.
# Start with the first string as the prefix and keep reducing it
# until it matches the prefix of every other string.

# Approach:
# 1. Initialize prefix as the first string.
# 2. Iterate over the remaining strings.
# 3. For each string, check if it starts with the current prefix.
# 4. If not, keep shortening the prefix from the end.
# 5. If prefix becomes empty, return "".
# 6. After checking all strings, return the prefix.

# Time Complexity: O(n * m)
# n = number of strings, m = length of prefix
# Space Complexity: O(1)

from typing import List
class Solution:
    def longestPrefix(self,strs:List[str]) -> str:
        prefix=strs[0]

        for value in strs[1:]:
            while not value.startswith(prefix):
                prefix=prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix

sol=Solution()
print(sol.longestPrefix(["flower","flow","flight"]))
# print(sol.longestPrefix(["dog","racecar","car"]))