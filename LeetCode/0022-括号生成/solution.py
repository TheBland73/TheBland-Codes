from typing import List
# 回溯法
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def dfs(x,left_used,right_used):
            if len(x) == 2 * n:
                res.append(x)
                return

            if left_used < n:
                dfs(x+'(',left_used+1,right_used)

            if right_used < n and right_used < left_used:
                dfs(x+')',left_used,right_used+1)

        dfs('',0,0)
        return res

'''
def dfs(状态):
if 终止条件:
    收集结果
    return

for 每个可能的选择:
    if 这个选择合法:
        做出选择
        dfs(新状态)
        撤销选择

空	怎么填
状态是什么	我做判断时需要知道什么
终止条件	什么时候算一个完整答案
有哪些选择	每一步能做什么
选择合法吗	什么条件下这个选择允许
'''

