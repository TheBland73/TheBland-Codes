#Version 动态规划
class Solution:
    def jump(self, nums: list[int]) -> int:
        #返回跳到数组末尾需要的次数
        #dp - 动态规划
        size = len(nums)
        dp = list(range(size))
        for idx,val in enumerate(nums):
            for step in range(1,val+1):
                if idx + step < size:
                    dp[idx+step] = min(dp[idx]+1,dp[idx+step])
                else:
                    break
        print(f"the dp is {dp}")
        return dp[size-1]


solution = Solution()
print(solution.jump(nums=[2,3,1,1,4]))
print(solution.jump(nums=[2,3,0,1,4]))
print(solution.jump(nums=[1,2,1,1,1]))

#version 贪心算法-分层算法
class Solution:
    def jump(self, nums: list[int]) -> int:
        size = len(nums)
        current_end = 0 #当前步数能覆盖最远边界
        farthest = 0 #下一步能覆盖最远边界
        step = 0 #步数
        i = 0 #每一次起始位置
        while current_end < size - 1: #只要还没有覆盖当前边界，就继续判断
            for j in range(i,current_end + 1):
                farthest = max(farthest,j+nums[j]) #看看这个区间内，我下一次最远可以跳到哪

            step += 1
            i = current_end + 1
            current_end = farthest

        return step



class Solution:
    def jump(self, nums: list[int]) -> int:
        size = len(nums)
        i = 0  #遍历索引
        cur = 0  #当前能跳到最远的地方
        next = 0  #下一跳能挑到最远的地方
        step = 0  #总共跳跃次数
        while cur < size-1:
            for j in range(i,cur+1): #寻找下一跳能跳到的最远地方
                next = max(next,j+nums[j])

            i = cur + 1
            cur =next
            step += 1
        return step
