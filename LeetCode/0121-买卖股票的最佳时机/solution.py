from typing import List

# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         if not prices:
#             return 0
#         min_price = prices[0]
#         max_profit = 0
#         for price in prices[1:]:
#             max_profit = max(max_profit, price - min_price)
#             min_price = min(min_price, price)
#         return max_profit

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        size = len(prices)
        if size < 2:
            return profit
        profit = max(0,prices[1]-prices[0])
        dp = [0] * (size + 1)  #dp[i] 表示第i天卖出时获得的最大利润
        bottom = prices[0] #表示第i天前股票的最低价格,不包括第i天
        dp[2] = max(0,prices[1]-prices[0])
        j = 1
        for i in range(2,size):
            bottom = min(bottom,prices[j])
            dp[i+1] = max(dp[i],prices[i]-bottom)
            
            j += 1 
            profit = max(profit,dp[i+1])


        return profit

solution = Solution()
# print(solution.maxProfit([7,1,5,3,6,4]))
# print(solution.maxProfit([7,6,4,3,1]))
print(solution.maxProfit([2,1,4]))        
