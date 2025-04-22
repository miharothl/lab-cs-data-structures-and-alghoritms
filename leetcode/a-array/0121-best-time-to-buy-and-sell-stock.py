# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# topics: array, dynamic programming

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit

solution = Solution()

"""
Idea:
* iterate
** check min price
** check max profit

Time Complexity:
O(n) - linear pass

Space Complexity:
O(1) - only variables for min and max
"""

prices = [7,1,5,3,6,4]
r = solution.maxProfit(prices)
print(r)
