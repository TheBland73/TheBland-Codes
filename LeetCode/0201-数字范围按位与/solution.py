class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left * 2 < right: #剪枝
            return 0 
        j = 31
        res = 0
        # 000101
        # 000110
        while j >= 0:
            n = pow(2,j)
            if right >= n:
                right -= n
                right_d = 1
            else:
                right_d = 0
            if left >= n:
                left -= n
                left_d = 1
            else:
                left_d = 0

            if right_d == left_d == 1:
                res += pow(2,j)
            elif right_d != left_d:
                break
            j -= 1
        return res
