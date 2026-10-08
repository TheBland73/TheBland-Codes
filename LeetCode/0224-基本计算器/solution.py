from typing import List
class Solution:
    #栈 递归 数学 字符串
    def calculate(self, s: str) -> int:
        stack = []
        res = 0  #当前已经算完的结果
        sign = 1 #处理+ - 
        num = 0 #当前正在处理的数字

        for val in s:
            if val.isdigit():
                num = num*10 + int(val) * sign
                # print(f"{sign},{val}")
            elif val == '+' or val == '-':
                #累计当前数字
                res += num
                num = 0
                sign = 1 if val == '+' else -1
            elif val == '(':
                #保护现场
                res += num
                stack.append(res) 
                stack.append(sign)
                #重置
                res = 0
                sign = 1
                num = 0
            elif val == ')':
                res += num
                num = 0
                #恢复现场
                pre_sign = stack.pop()
                pre_res = stack.pop()
                res = pre_sign * res + pre_res
            else:
                continue
        res += num
        return res
        

solution = Solution()
# # print(solution.calculate(s = "2-1+3"))
print(solution.calculate(s = "2-(1+2)+3"))  #2
# # print(solution.calculate(s = "(1+(4+5+2)-3)"))
print(solution.calculate(s = "(1+(4+5+2)-3)+(6+8)")) #9
print(solution.calculate(s = "2147483647"))
            
