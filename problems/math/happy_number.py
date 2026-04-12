# Problem: 202. Happy Number
# Link: https://leetcode.com/problems/happy-number/description/
# Difficulty: Easy
# Pattern: Math
# Topic: HashTable,Two pointer

# Intuition:
# A happy number is formed by repeatedly replacing the number with the sum of the
# squares of its digits. If the process eventually reaches 1, the number is happy.
# If it falls into a loop, it is not. We use a set to detect cycles by storing
# previously seen numbers.

# Approach:
# Initialize an empty set to track seen numbers.
# While the number is not equal to 1:
#   If the number is already in the set, a cycle is detected → return False.
#   Add the number to the set.
#   Compute the sum of the squares of its digits.
#   Update the number with this computed sum.
# If the number becomes 1, return True.

# Time Complexity:
# O(log n) — Each transformation processes digits of the number.

# Space Complexity:
# O(log n) — Set stores intermediate numbers (cycle detection).

class Solution:
    def isHappy(self,s:int):
        seen=set()

        while s!=1:
            if s in seen:
                return False
            seen.add(s)

            total=0

            while s>0:
                digit=s%10
                total += digit * digit
                s//= 10
            
            s=total
        return True
sol=Solution()
print(sol.isHappy(19))