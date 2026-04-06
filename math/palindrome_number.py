# Problem: 9. Palindrome Number
# Link: https://leetcode.com/problems/palindrome-number/description/
# Difficulty: Easy
# Pattern: Math

# Intuition:
# A palindrome number reads the same forward and backward.
# We can reverse the digits of the number and compare it with the original.

# Approach:
# 1. If the number is negative, return False.
# 2. Store the original value.
# 3. Reverse the number using modulo and division.
# 4. Compare reversed number with original value.

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def paliNum(self,x:int)->bool:
        if x<0:
            return False
        reverse=0
        actual_val=x
        while x>0:
            digit=x%10
            reverse=reverse*10+digit
            x=x//10
        return actual_val==reverse

sol=Solution()
print(sol.paliNum(-121))