class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0] * (l1+1) for _ in range(l2+1)]
        # dp[i][j]把 word1 的前 j 个字符，变成 word2 的前 i 个字符，最少需要几步？

        for a in range(l1+1):
            dp[0][a] = a
        for b in range(l2+1):
            dp[b][0] = b


        for i in range(1,l2+1):
            for j in range(1,l1+1):
                if word2[i-1] == word1[j-1]:
                    dp[i][j] = dp[i-1][j-1] 
                else: #有三种操作 替换 插入 删除
                    dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j]) + 1

        return dp[l2][l1]
