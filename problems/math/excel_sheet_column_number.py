# Problem: 171. Excel Sheet Column Number
# Link: https://leetcode.com/problems/excel-sheet-column-number/description/
# Difficulty: Easy
# Pattern: Math (Base Conversion)
# Topic: String

# Intuition:
# Excel column titles follow a base-26 number system where each character
# represents a digit (A=1, B=2, ..., Z=26). Similar to how we build numbers
# in base-10, we process each character from left to right, shifting the
# current result and adding the value of the current character.

# Approach:
# Initialize result as 0.
# Iterate through each character in the string.
# For each character, convert it to its corresponding number using:
# (ord(char) - ord('A') + 1).
# Multiply the current result by 26 to shift it left in base-26.
# Add the current character's value to the result.
# Return the final result.

# Time Complexity:
# O(n) — We traverse the string once.

# Space Complexity:
# O(1) — No extra space is used apart from variables.

class Solution:
    def titleToNumber(self,s:str):
        result=0

        for i in s:
            result=result*26+(ord(i)-ord('A'))+1
        
        return result
    
sol=Solution()
print(sol.titleToNumber("ZY"))
