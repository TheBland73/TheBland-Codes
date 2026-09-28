from typing import List
class Solution:
    #块交换的经典构造，叫“三反转 / 手摇算法”
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        step = k % l
        if k == 0:
            return
                
        # 块1 nums[0:l-step]
        l1 = (l-step) // 2
        for i in range(l1):   
            nums[i],nums[l-step-1-i] = nums[l-step-1-i],nums[i]
        
        # 块2 nums[l-step:l]
        start = l - step
        end = l - 1
        for i in range(step//2):
            nums[start+i],nums[end-i] = nums[end-i],nums[start+i]

        # 块1+2
        l3 = l // 2
        j = l-1
        for i in range(l3):   
            nums[i],nums[j] = nums[j],nums[i]
            j -= 1

solution = Solution()
# solution.rotate(nums = [1,2,3,4,5,6], k = 2)
solution.rotate(nums = [1,2], k = 3)

# 1 2 3 4 5 6 -> 6 5 4 3 2 1
# 1 2 3 4 5 -> 5 4 3 2 1

#手搓 1,2,3,4,5,6 -> 5,6,1,2,3,4

# 1,2,3,4,5,6 -> 4,3,2,1,5,6
# 4,3,2,1,5,6 -> 4,3,2,1,6,5
# 4,3,2,1,6,5 -> 5,6,1,2,3,4

# from typing import List
# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         # O(n) O(1)
#         l = len(nums)
#         step = k % l

#         if l % 2 == 0 and step % 2 == 0:
#             n1 = nums[0:l-step]
#             n2 = nums[l-step:]
#             n2.extend(n1)
#             print(n2)
#             nums = n2
#             return

#         t = None #保存被替换val
#         idx = 0
#         for i in range(l):
#             # 第一轮
#             if i == 0:
#                 t = nums[idx+step]
#                 nums[idx+step] = nums[idx]
                
#             # 其余轮
#             else:
#                 t1 = nums[(idx + step) % l]
#                 nums[(idx + step) % l] = t
#                 t = t1
#                 # print(f"i={i}{nums}")

#             idx = (idx + step) % l


# solution = Solution()
# # solution.rotate(nums = [1,2,3,4,5], k = 3)
# solution.rotate(nums = [-1,-100,3,99], k = 2)  #这种情况有问题
# # solution.rotate(nums = [1,2,3,4,5], k = 2)
# # solution.rotate(nums = [1,2,3,4], k = 3)