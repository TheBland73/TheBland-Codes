from typing import List
class Solution:
    def totalNQueens(self, n: int) -> int:
        # 回溯法
        # 由于是把n个皇后 放在 nxn的棋盘上
        # 每一行 + 每一列不能够有重复
        # queens = [1, 3, 0, 2] 用这样的形式表示一个解 0 1 2 3行 + 1 3 0 2列
        
        ans = []
        cnt = 0
        # queens[row] = col，表示第 row 行的皇后放在第 col 列
        queens = [-1] * n
        used_col = set()   #列
        used_diag1 = set() #主对角线
        used_diag2 = set() #副对角线

        def backtrack(row: int):  #row 变化状态，暴力是for循环的东西
            nonlocal cnt
            # 已经成功放完 n 行，说明找到一个解
            if row == n:  #成功放完n行，说明一个解已经找到
                board = []
                for r in range(n):
                    c = queens[r]
                    #添加每一列情况
                    board.append("." * c + "Q" + "." * (n - c - 1)) 
                ans.append(board)
                cnt += 1
                return

            #当前尝试第 row 行，逐一尝试每一列
            for col in range(n):
                if col in used_col: #该列被占用，跳过
                    continue
                if (row - col) in used_diag1:
                    continue
                if (row + col) in used_diag2:
                    continue

                queens[row] = col #把皇后进行放置
                #更新范围限制
                used_col.add(col)
                used_diag1.add(row - col)
                used_diag2.add(row + col)

                backtrack(row + 1) #递归处理

                #回溯
                used_col.remove(col)
                used_diag1.remove(row - col)
                used_diag2.remove(row + col)
                queens[row] = -1

        backtrack(0)
        return cnt  
        
solution = Solution()
print(solution.totalNQueens(n=4))

