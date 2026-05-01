# Problem: 1248. Count Number of Nice Subarrays
# Link: https://leetcode.com/problems/count-number-of-nice-subarrays/
# Difficulty: Medium
# Pattern: Prefix Sum + HashMap

# Intuition:
# We are asked to count subarrays that contain exactly k odd numbers.
#
# Instead of dealing with actual values, we simplify the problem:
#   - Treat every odd number as 1
#   - Treat every even number as 0
#
# Now the problem becomes:
#   → "Count number of subarrays with sum = k"
#
# Why this works:
#   Because sum of this transformed array represents the count of odd numbers.
#
# We use Prefix Sum:
#   prefixsum = number of odd numbers from index 0 → current index
#
# If at any index:
#   prefixsum = current_sum
#
# We want a previous prefix such that:
#   current_sum - previous_sum = k
#   → previous_sum = current_sum - k
#
# So for every index:
#   - Check how many times (prefixsum - k) has appeared before
#   - Add that frequency to count
#
# We use a hashmap to store:
#   prefixsum → frequency (how many times it has occurred)
#
# Initialize hashmap with {0:1}:
#   This handles subarrays starting from index 0

# Approach:
# 1. Initialize:
#    - prefixsum = 0 → counts odd numbers so far
#    - count = 0 → result
#    - hashmap = {0:1} → prefix sum frequency
#
# 2. Traverse the array:
#    For each element:
#
#    a) If number is odd:
#          prefixsum += 1
#
#    b) Check if (prefixsum - k) exists in hashmap:
#          → If yes, add its frequency to count
#
#    c) Update hashmap:
#          Increase frequency of current prefixsum
#
# 3. Return count

# Approach:
# 1. Initialize:
#    - prefixsum = 0 → counts odd numbers so far
#    - count = 0 → result
#    - hashmap = {0:1} → prefix sum frequency
#
# 2. Traverse the array:
#    For each element:
#
#    a) If number is odd:
#          prefixsum += 1
#
#    b) Check if (prefixsum - k) exists in hashmap:
#          → If yes, add its frequency to count
#
#    c) Update hashmap:
#          Increase frequency of current prefixsum
#
# 3. Return count

# It means:
#   prefixsum = 0 has occurred once before starting
#
# This allows us to count subarrays that start from index 0
from typing import List

class Solution:
    def numberOfSubarrays(self,nums:List[int],k:int)->int:
        prefixsum=0
        count=0
        hashmap={0:1}

        for num in nums:
            if num%2==1:
                prefixsum += 1
            
            if (prefixsum -k) in hashmap:
                count += hashmap[prefixsum - k]

            if prefixsum in hashmap:
                hashmap[prefixsum] +=1
            else:
                hashmap[prefixsum] = 1
        
        return count
sol=Solution()
print(sol.numberOfSubarrays([1,1,2,1,1],3))