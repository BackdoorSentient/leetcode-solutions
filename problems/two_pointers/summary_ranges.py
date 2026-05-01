# Problem: 228. Summary Ranges
# Link: https://leetcode.com/problems/summary-ranges/description/
# Difficulty: Easy
# Pattern: Two Pointer


# Intuition:
# The array is sorted, so consecutive numbers will appear next to each other.
# We group numbers into ranges by tracking the start of each range.
# If the current number is not consecutive to the previous one, the current range ends,
# and we add it to the result. Then we start a new range.

# Approach:
# Initialize a variable 'k' to store the start index of the current range.
# Iterate through the array starting from index 1.
# For each element, check if it is consecutive to the previous element.
# If not, finalize the range from nums[k] to nums[i-1]:
#   - If both are same, add it as a single number.
#   - Otherwise, add it as a range "start->end".
# Update 'k' to the current index to start a new range.
# After the loop, process the last range similarly.

# Time Complexity:
# O(n) — Single pass through the array.

# Space Complexity:
# O(1) — Only output list is used.

from typing import List

class Solution:
    def summaryRanges(self,nums:List[int]):

        k=0
        output=[]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                if k==i-1:
                    output.append(f"{nums[k]}")
                else:
                    output.append(f"{nums[k]}->{nums[i-1]}")
                k =i
        
        if k==len(nums)-1:
            output.append(f"{nums[k]}")
        else:
            output.append(f"{nums[k]}->{nums[-1]}")
        
        return output

sol=Solution()
print(sol.summaryRanges([0,1,2,4,5,7]))
# if not nums:
#             return []
#         result=[]
#         start=nums[0]
#         for i in range(1,len(nums)):
#             if nums[i]!=nums[i-1]+1:
#                 if start==nums[i-1]:
#                     result.append(str(start))
#                 else:
#                     result.append(f"{start}->{nums[i-1]}")
#                 start=nums[i]
        
#         if start==nums[-1]:
#             result.append(str(start))
#         else:
#             result.append(f"{start}->{nums[-1]}")
        
#         return result