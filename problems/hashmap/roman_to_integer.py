# Problem: 13. Roman to Integer
# Link: https://leetcode.com/problems/roman-to-integer/description/
# Difficulty: Easy
# Pattern: HashMap

# Intuition:
# Roman numerals are usually added, but in some cases smaller value comes before larger (like IV = 4).
# So if current value is less than next value → subtract it, else add it.

# Approach:
# Use a hashmap to store values of Roman characters.
# Traverse the string:
# - If current < next → subtract
# - Else → add
# Keep updating the total sum.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def romanToInt(self,s:str):

        roman={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        count=0

        for i in range(len(s)):
            if i+1<len(s) and roman[s[i]]<roman[s[i+1]]:
                count -= roman[s[i]]
            else:
                count += roman[s[i]]
    
        return count
    
sol=Solution()
print(sol.romanToInt("III"))