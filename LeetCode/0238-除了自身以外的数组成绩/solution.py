# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         size = len(nums)
#         prefix_dot = [1] * size
#         suffix_dot = [1] * size
#         res = [1] * size

#         prefix_dot[0] = nums[0]
#         suffix_dot[-1] = nums[-1]

#         for idx in range(1,size):
#             prefix_dot[idx] = prefix_dot[idx-1] * nums[idx]

#         for idx in range(size-2,-1,-1):
#             suffix_dot[idx] = suffix_dot[idx+1] * nums[idx]

#         print(prefix_dot)
#         print(suffix_dot)

#         res[0] = suffix_dot[1]
#         res[-1] = prefix_dot[-2]
#         for idx in range(1,size-1):
#             res[idx] = prefix_dot[idx-1] * suffix_dot[idx+1]

#         return res

# solution = Solution()
# print(solution.productExceptSelf(nums=[1,2,3,4]))
# # print(solution.productExceptSelf(nums = [-1,1,0,-3,3]))



class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        size = len(nums)
        res = [1] * size
        
        # 边界处理
        if size == 1:
            return res

        # 1. 从左往右遍历：res[i] 存储 nums[0] 到 nums[i-1] 的乘积（即前缀积）
        # res[0] 默认是 1，不需要改
        for i in range(1, size):
            res[i] = res[i-1] * nums[i-1]

        print(res)

        # 2. 从右往左遍历：用一个变量 suffix 维护后缀积
        suffix = 1
        for i in range(size - 1, -1, -1):
            res[i] = res[i] * suffix  # 前缀积 * 后缀积
            suffix *= nums[i]         # 更新后缀积，供下一个（左侧）元素使用

        return res

solution = Solution()
print(solution.productExceptSelf(nums=[4,3,2,1]))


