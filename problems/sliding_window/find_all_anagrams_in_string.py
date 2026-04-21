# Problem: 438. Find All Anagrams in a String
# Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
# Difficulty: Medium
# Pattern: Fixed Size Sliding Window

# Approach / Intuition:
# We use a sliding window of size equal to length of p.
# Idea is simple: if two strings are anagrams, their character counts must match.
# So instead of sorting every substring, we keep track of frequency of characters.
#
# First, we store frequency of all characters in p.
# Then we start moving a window over s:
# - Add current character into window count
# - If window size exceeds m, remove the leftmost character
# - At every step, compare window count with p count
#   If they match, it means current window is an anagram
#
# This way we only scan the string once and keep updating counts.

# Time Complexity:
# O(n * 26) → roughly O(n)
# (we compare two arrays of size 26 at each step)

# Space Complexity:
# O(1)
# (since we only use two arrays of size 26, constant space)


class Solution:
    def findAnagrams(self,s:str,p:str):
        res=[]
        n=len(s)
        m=len(p)

        if m>n:
            return res

        s_count=[0]*26
        p_count=[0]*26
        
        for i in p:
            p_count[ord(i)-ord('a')]+=1
        
        for i in range(n):
            s_count[ord(s[i])-ord('a')] +=1

            if i>=m:
                s_count[ord(s[i-m])-ord('a')] -=1
            if s_count==p_count:
                res.append(i-m+1)
        
        return res
            
sol=Solution()
print(sol.findAnagrams("abab","ab"))
