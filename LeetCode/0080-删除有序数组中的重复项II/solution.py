# 给定一个按 非递减顺序 排列的整数数组 nums，请你 原地 删除部分重复元素，
# 使得每个不同的元素 最多出现两次。元素的 相对顺序 应保持 不变。
# 很多时候不能循规蹈矩解体题目啊

# KEY!!!：比起原地删除什么，更值得你关心的是你原地保留了什么

# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         size = len(nums)
#         if size <= 2:
#             return size

#         slow = 2
#         fast = 2
#         while fast < size:
#             if nums[slow-2] != nums[fast]:  #核心的代码
#                 nums[slow] = nums[fast]
#                 slow += 1
#             fast += 1
        
#         return slow

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0 #记录更新覆盖的位置
        size = len(nums)
        if size <= 2:
            return size

        cnt = 0
        prev = None
        for n in nums:
            if n == prev:
                cnt += 1
            else:
                prev = n
                cnt = 1

            if cnt <= 2 :
                nums[i] = n
                i += 1

        return i 


solution = Solution()
# solution.removeDuplicates()
#                                           i j
solution.removeDuplicates(nums = [1,1,1,2,2,3])        #->[1,1,2,2,3]
solution.removeDuplicates(nums = [0,0,1,1,1,1,2,3,3])  #->[0,0,1,1,2,3,3]
