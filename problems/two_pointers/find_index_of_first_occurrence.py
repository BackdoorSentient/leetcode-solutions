# Problem: 28. Find the Index of the First Occurrence in a String
# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
# Difficulty: Easy
# Pattern: Two Pointer

# Intuition:
# We need to find where the pattern (needle) first appears in the text (haystack).
# Since the substring must fully fit, we only check valid starting indices.
# At each index, we compare a substring of length n with the needle.

# Approach:
# 1. Let m = length of haystack, n = length of needle
# 2. Iterate i from 0 to m - n
# 3. At each i, check if haystack[i:i+n] == needle
# 4. If match found, return i
# 5. If no match found after loop, return -1

# Time Complexity:
# O(m * n) → In worst case, we compare n characters at each of m positions

# Space Complexity:
# O(1) → No extra space used (ignoring substring slicing cost)


class Solution:
    def strStr(self,haystack:str,needle:str):
        m=len(haystack)
        n=len(needle)

        for i in range(m-n+1):
            if haystack[i:i+n]==needle:
                return i
        
        return -1
    

sol=Solution()
print(sol.strStr("sadbutsad","sad"))