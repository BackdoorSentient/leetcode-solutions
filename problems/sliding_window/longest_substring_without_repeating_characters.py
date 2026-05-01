# Problem: 3. Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Difficulty: Medium
# Pattern: Dynamic Size Sliding Window

# Intuition:
# The goal is to find the longest substring that contains only unique characters.
# A brute-force approach would generate all substrings and check for duplicates,
# which would take O(n^2) time.
# Instead, we use a sliding window technique to maintain a valid substring
# (with no repeating characters) while traversing the string only once.
# We expand the window using the right pointer and shrink it using the left
# pointer whenever a duplicate character is found.

# Approach:
# 1. Use a set to store characters in the current window.
# 2. Initialize two pointers:
#    - left (start of window)
#    - right (end of window)
# 3. Traverse the string using the right pointer:
#    - If the character is not in the set → add it to the set
#    - If the character is already in the set → remove characters from the left
#      and move left forward until the duplicate is removed
# 4. At each step, calculate the window size (right - left + 1)
#    and update the maximum length.
# 5. Return the maximum length found.

# Time Complexity:
# O(n)
# Each character is processed at most twice (once by right pointer and once by left pointer),
# so the total operations are linear.

# Space Complexity:
# O(min(n, k))
# Where n is the length of the string and k is the size of the character set.
# In the worst case (all unique characters), the set stores n characters → O(n).


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))