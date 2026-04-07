# Problem: 76. Minimum Window Substring
# Link: https://leetcode.com/problems/minimum-window-substring/description/
# Difficulty: Hard
# Pattern: Dynamic Size Sliding Window

# ------------------------------------------------------------
# Intuition:
# The goal is to find the smallest substring in `s` that contains
# all characters of `t`, including duplicates.
#
# We use a sliding window approach:
# - Expand the window using the right pointer to include characters.
# - Once all required characters are present, shrink the window
#   from the left to remove unnecessary characters and minimize size.
#
# We track:
# - `need`: frequency of characters required from `t`
# - `window`: frequency of characters in current window
# - `have`: number of characters meeting required frequency
# - `need_count`: total unique characters required
#
# ------------------------------------------------------------
# Approach:
# 1. Build a frequency map `need` for string `t`.
# 2. Initialize two pointers `left` and `right` for the window.
# 3. Expand the window by moving `right`:
#    - Add current character to `window`.
#    - If its frequency matches the requirement in `need`, increment `have`.
#
# 4. When the window becomes valid (have == need_count):
#    - Try shrinking the window from the left.
#    - Update the result if the current window is smaller.
#    - If removing a character breaks the requirement, decrement `have`.
#
# 5. Continue until the entire string is processed.
#
# ------------------------------------------------------------
# Time Complexity:
# O(m + n)
# - m = length of string `s`
# - n = length of string `t`
# Each character is visited at most twice (once by right, once by left).
#
# ------------------------------------------------------------
# Space Complexity:
# O(k)
# - k = number of unique characters in `t`
# - In this problem, k is bounded by English letters, so effectively constant.
#
# ------------------------------------------------------------

class Solution:
    def minSubarray(self,s:str,t:str):
        if len(s)<len(t):
            return ""

        left=0
        have=0
        window={}
        need={}
        for ch in t:
            need[ch]=need.get(ch,0)+1
        
        need_count=len(need)
        res=[-1,-1]
        res_length=float('inf')
        
        for right in range(len(s)):
            ch=s[right]
            window[ch]=window.get(ch,0)+1

            if ch in need and window[ch]==need[ch]:
                have +=1

            while need_count==have:
                if (right-left+1)<res_length:
                    res=[left,right]
                    res_length=right-left+1

                left_ch=s[left]
                window[left_ch] -=1

                if left_ch in need and window[left_ch]<need[left_ch]:
                    have -=1

                left +=1

        l,r=res
        return s[l:r+1] if res_length != float('inf') else ""