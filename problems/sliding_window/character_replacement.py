# Problem: 424. Longest Repeating Character Replacement
# Link: https://leetcode.com/problems/longest-repeating-character-replacement/description/
# Difficulty: Medium
# Pattern: Dynamic Size Sliding Window

# Intuition:
# We want the longest substring where we can make all characters the same
# by replacing at most k characters.
# Instead of trying all replacements, we keep track of the most frequent
# character in the current window.
# The remaining characters (window_size - max_freq) are the ones we must replace.
# If replacements needed <= k → window is valid.

# Approach:
# Use sliding window with two pointers (left, right).
# Expand window by moving right pointer and update frequency map.
# Track max_freq = highest frequency character in current window.
# If (window_size - max_freq) > k → window is invalid → shrink from left.
# Keep updating max_length with the maximum valid window size.
# Important: We only update max_freq when expanding (right pointer),
# and do NOT recompute it when shrinking to keep the solution O(n).

# Time Complexity:
# O(n) → each character is processed at most twice (once by right, once by left)

# Space Complexity:
# O(1) → at most 26 uppercase letters stored in freq map


class Solution:
    def characterReplacement(self,s:str,k:int):
        max_freq=0
        max_length=0
        freq={}
        left=0

        for right in range(len(s)):
            if s[right] in freq:
                freq[s[right]] +=1
            else:
                freq[s[right]] =1
            
            max_freq=max(max_freq,freq[s[right]])

            while (right-left+1)-max_freq>k:
                freq[s[left]] -=1
                left +=1

            max_length=max(max_length,right-left+1)
        
        return max_length
    

sol=Solution()
print(sol.characterReplacement("ABAB",2))