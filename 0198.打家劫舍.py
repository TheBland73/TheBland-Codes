from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        
        #特殊情况处理
        if length < 2:
            return nums[0]
        if length == 2:
            return max(nums[0],nums[1])

        dp = [0] * length # 到第i家时能偷的 最多东西      
        dp[0] = nums[0]
        dp[1] = nums[1]

        if dp[0] > dp[1]:
            dp[1] = dp[0]
        
        for i in range(2,length):
            dp[i] = max(dp[i-2] + nums[i],dp[i-1])
        
        # print(dp)
        return dp[-1]
    
solution = Solution()
print(solution.rob([1,2,3,1]))
print(solution.rob([2,7,9,3,1]))
print(solution.rob([0]))
print(solution.rob([3,1]))
print(solution.rob([2,1,1,2]))
# print(solution.rob())
