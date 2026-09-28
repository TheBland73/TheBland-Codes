from typing import List
#使用并查集方法 
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        parent = list(range(size))  #记录树的头节点 初始时为自己
        rank = [0] * size           #记录树的高度 起始为0
        def find(x):           #递归 一定需要一个出口   
            if x != parent[x]:      #x为城市索引，parent[x]为所属x城市索引
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            rx,ry = find(x),find(y)
            if rx == ry:
                return
            if rank[rx] > rank[ry]:
                parent[ry] = rx  #连接两颗树
            elif rank[rx] < rank[ry]:   #这样连接树高度没变 不用更新rank  因为是把矮的树接到高的树上
                parent[rx] = ry
            else: # rank[x] == rank[y] 两棵树高度相同
                parent[rx] = ry
                rank[rx] += 1
        #开始遍历上三角
        for i in range(size):
            for j in range(i+1,size):
                if isConnected[i][j] == 1:
                    union(i,j)
        provinces = len({find(i) for i in range(size)})
        return provinces

solution = Solution()
# solution.findCircleNum(isConnected=[[1,1,0],[1,1,0],[0,0,1]])
# solution.findCircleNum(isConnected=[[1,1,1],[1,1,1],[0,0,1]])
solution.findCircleNum(isConnected=[[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])



# 深度优先 dfs
# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         def dfs(i: int):
#             for j in range(cities):
#                 if isConnected[i][j] == 1 and j not in visited:
#                     visited.add(j)
#                     dfs(j)
#         cities = len(isConnected)
#         visited = set()
#         provinces = 0
#         for i in range(cities):
#             if i not in visited:
#                 dfs(i)
#                 provinces += 1
#         return provinces
