# Problem: 121. Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Difficulty: Easy
# Pattern: Greedy

# Intuition:
# To maximize profit, we should buy at the lowest price and sell at a higher price later.
# We track the minimum price seen so far and calculate profit at each step.

# Approach:
# 1. Initialize min_price as infinity and max_profit as 0
# 2. Traverse the prices array
# 3. Update min_price if current price is smaller
# 4. Calculate profit = current price - min_price
# 5. Update max_profit if this profit is higher
# 6. Return max_profit

# Time Complexity:
# O(n) → Single pass through the array

# Space Complexity:
# O(1) → Constant space used
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price=float('inf')
        max_profit=0
        for price in prices:
            if price<min_price:
                min_price=price
            profit=price-min_price
            max_profit=max(max_profit,profit)
        
        return max_profit if max_profit else 0
    
sol=Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
# Note:
# This problem can also be seen as Dynamic Programming,
# but it is optimally solved using a Greedy approach.