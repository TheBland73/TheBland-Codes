from typing import List
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        pool = set(nums) #关键步骤！
        max_len = 0
        for n in pool:
            if n-1 not in pool: #关键步骤！
                cnt = 1
                t = n
                while t+1 in pool:
                    cnt += 1
                    t += 1
                max_len = max(max_len,cnt)
        return max_len
    
solution = Solution()
print(solution.longestConsecutive(nums=[100,4,200,1,3,2]))
