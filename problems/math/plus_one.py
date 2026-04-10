# Problem: 66. Plus One
# Link: https://leetcode.com/problems/plus-one/description/
# Difficulty: Easy
# Pattern: Math

# Intuition:
# We simulate how addition works digit by digit from right to left.
# If a digit is less than 9, we can simply increment it and stop.
# If it's 9, it becomes 0 and we carry over to the next digit.

# Approach:
# 1. Traverse the array from right to left
# 2. If current digit < 9:
#    - Increment it and return the array
# 3. If digit == 9:
#    - Set it to 0 and continue (carry over)
# 4. If all digits were 9:
#    - Add 1 at the beginning

# Time Complexity:
# O(n) → In worst case, we traverse all digits (e.g., [9,9,9])

# Space Complexity:
# O(1) → In-place modification (ignoring output array in worst case)


from typing import List
class Solution:
    def plusOne(self,digits:List[int]):
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        return [1]+digits


sol=Solution()
print(sol.plusOne([1,2,3]))