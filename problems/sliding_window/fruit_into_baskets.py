# Problem: 904. Fruit Into Baskets
# Link: https://leetcode.com/problems/fruit-into-baskets/description/
# Difficulty: Medium
# Pattern: Sliding Window (Variable Size)
# Topic: Array, HashMap

from typing import List

# Intuition:
# We need the longest subarray containing at most 2 distinct fruit types.
# This is a classic sliding window problem where we expand the window to include fruits,
# and shrink it when we have more than 2 types. The valid window always contains
# at most 2 distinct elements, and we track the maximum length of such a window.

# Approach:
# Use two pointers (left and right) to represent the window.
# Use a hashmap (dictionary) to store the count of fruits in the current window.
# Expand the window by moving right and adding fruits[right] to the map.
# If the number of distinct fruits exceeds 2, shrink the window from the left
# until only 2 types remain, updating the hashmap accordingly.
# At each step, calculate the window size (right - left + 1) and update max_len.
# Return the maximum length found.

# Time Complexity:
# O(n) — Each element is added and removed from the window at most once.

# Space Complexity:
# O(1) — The hashmap stores at most 2 fruit types.

from typing import List

class Solution:
    def totalFruit(self,fruits:List[int]):
        left=0
        max_len=0
        count={}

        for right in range(len(fruits)):
            count[fruits[right]]=count.get(fruits[right],0)+1

            while len(count)>2:
                count[fruits[left]]-=1
                if count[fruits[left]]==0:
                    del count[fruits[left]]
                
                left +=1
            
            max_len=max(max_len,right-left+1)
        
        return max_len

sol=Solution()
# print(sol.totalFruit([1,2,1]))
print(sol.totalFruit([1,2,3,2,2]))