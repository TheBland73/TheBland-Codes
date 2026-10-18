class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        #列
        col = {0:[],1:[],2:[],
               3:[],4:[],5:[],
               6:[],7:[],8:[]}
        #行
        row = {0:[],1:[],2:[],
               3:[],4:[],5:[],
               6:[],7:[],8:[]}
        #3x3宫内
        block = {0:[],1:[],2:[],
                 3:[],4:[],5:[],
                 6:[],7:[],8:[]}

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':  #i 为行 j 为列
                    continue
                else:
                    if val in row[i]:
                        return False
                    else:
                        row[i].append(val)

                    if val in col[j]:
                        return False
                    else:
                        col[j].append(val)

                    block_x = i // 3
                    block_y = j // 3
                    block_idx = block_x * 3 + block_y
                    if val in block[block_idx]:
                        return False
                    else:
                        block[block_idx].append(val)
        return True
