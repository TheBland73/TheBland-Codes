from typing import List
class Solution:
    #广度优先搜索/动态规划/背包问题/完全背包
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)  #dp[j] 装满j时，最少的硬币数量  无穷大表示无法实现
        dp[0] = 0
        #迭代更新，向前去找
        # amount = 6, coins= [1,5]
        # a = 1 ,[1]  +  5 -> a = 6,[1,5]
        # a = 2 ,[1,1]
        # a = 3 ,[1,1,1]
        # a = 4 ,[1,1,1,1]
        # a = 5 ,[5]
        # a = 6 ,[1,5]
        for c in coins:
            for i in range(c,amount+1):  #从c开始遍历，进行了部分剪枝
                dp[i] = min(dp[i],dp[i-c]+1)

        return dp[amount] if dp[amount] != float('inf') else -1

solution = Solution()
print(solution.coinChange(amount=6,coins=[5,1]))
print(solution.coinChange(amount=11,coins=[1,5,2]))
