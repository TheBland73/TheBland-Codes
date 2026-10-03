class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)

        dp = [[0] * (l1+1) for _ in range(l2+1)]

        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if text1[i-1] == text2[j-1]:
                    dp[j][i] = dp[j-1][i-1] + 1
                else:
                    dp[j][i] = max(dp[j-1][i],dp[j][i-1])

        # for t in dp:
        #     print(t)
        return dp[l2][l1]
