# Problem: 3783. Mirror Distance of an Integer
# Link: https://leetcode.com/problems/mirror-distance-of-an-integer/description/?envType=daily-question&envId=2026-04-18
# Difficulty: Easy
# Pattern: Math
# Topic: Number Manipulation

# Approach:
# The idea is to reverse the given number and then find the difference
# between the original number and the reversed number.
# To reverse the number, we take the last digit again and again,
# and build a new number by placing digits in reverse order.
#
# Once we get the reversed number, we simply subtract it from the original
# number and take the absolute value so the answer is always positive.


# Intuition:
# Think of looking at the number in a mirror.
# The digits appear in reverse order.
# So we recreate that mirrored version and measure how far it is
# from the original number.


# Time Complexity:
# O(d)
# where d is the number of digits in the number.
# We process each digit exactly once.


# Space Complexity:
# O(1)
# We only use a few variables and no extra space that grows with input size.


class Solution:
    def mirrorDistance(self, n: int) -> int:
        output=0
        def reverse(n):
            rev=0
            while n>0:
                digit=n%10
                rev=rev*10
                rev=rev+digit
                n//=10
            return rev

        output=abs(n-reverse(n))
        return output

sol=Solution()
print(sol.mirrorDistance(25))