# Problem: 125. Valid Palindrome
# Link: https://leetcode.com/problems/valid-palindrome/description/
# Difficulty: Easy
# Pattern: Two Pointers

# Intuition:
# A palindrome reads the same forward and backward. Since the string may contain
# non-alphanumeric characters and mixed cases, we skip invalid characters and
# compare only lowercase alphanumeric characters from both ends using two pointers.

# Approach:
# Initialize two pointers at the start and end of the string.
# Move the left pointer forward until it points to an alphanumeric character.
# Move the right pointer backward until it points to an alphanumeric character.
# Compare the characters at both pointers (in lowercase).
# If they differ, return False.
# Continue this process until the pointers meet or cross.
# If all valid character comparisons match, return True.

# Time Complexity:
# O(n) — Each character is processed at most once.

# Space Complexity:
# O(1) — No extra space is used apart from a few variables.

class Solution:
    def pali(self,s:str):
        left=0
        right=len(s)-1

        while left<right:
            while left<right and not s[left].isalnum():
                left+=1
            
            while left<right and not s[right].isalnum():
                right-=1

            if s[left].lower()!=s[right].lower():
                return False
            
            left +=1
            right-=1

        return True
    
sol=Solution()
# print(sol.pali("A man, a plan, a canal: Panama"))
print(sol.pali(".,"))