# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        max_profit = 0

        for i in range(len(prices)-1):

            if prices[i] < prices[i+1]:
                max_profit += prices[i+1] - prices[i]

        return max_profit

solution = Solution()

prices = [7,1,5,3,6,4]
print("pass") if solution.maxProfit(prices) == 7 else print("fail")

prices = []
print("pass") if solution.maxProfit(prices) == 0 else print("fail")


"""
Idea:
* iterate over prices
* buy if price[i] < price[i+1]

Time:
O(n)

Space:
O(1)

"""
