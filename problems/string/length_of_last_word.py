# Problem: 58. Length of Last Word
# Link: https://leetcode.com/problems/length-of-last-word/
# Difficulty: Easy
# Pattern: String

# Intuition:
# The last word is the sequence of non-space characters at the end of the string.
# We traverse from the end, skip trailing spaces, then count characters until a space is found.

# Approach:
# 1. Start from the end of the string
# 2. Skip all trailing spaces
# 3. Count characters until a space or start of string is reached
# 4. Return the count

# Time Complexity:
# O(n) → In worst case, we traverse the entire string

# Space Complexity:
# O(1) → No extra space used


class Solution:
    def lengthOfLastWord(self,s:str):
        i=len(s)-1
        length=0

        while i>=0 and s[i]==" ":
            i -=1
        
        while i>=0 and s[i]!=" ":
            i -= 1
            length +=1

        return length
    

sol=Solution()
print(sol.lengthOfLastWord("Hello World"))