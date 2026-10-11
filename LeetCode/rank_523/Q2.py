import math
class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        # 考虑所有<=n的 质数，从中选择一些质数，满足：
        # 质数总和 <= s
        # 质数数量最多
        # 每个质数只能选一次
        # 返回结果为一个数组，递增序列

        res = []
        if n < 2:
            return res
        
        def isprime(n):  # 质数判断
            for i in range(2, int(math.sqrt(n))+1 ):
                if n % i == 0:
                    return False
            return True

        for j in range(2,n+1):
            if isprime(j) and s >= j:
                res.append(j)
                s -= j
            if j > s:  #之前忘记剪枝了 很重要！
                break
        return res

solution = Solution()
print(solution.maxPrimes(n = 100000, s = 100000000))
print(solution.maxPrimes(n = 15, s = 15))
print(solution.maxPrimes(n = 2, s = 2))
print(solution.maxPrimes(n = 2, s = 1))
print(solution.maxPrimes(n = 2, s = 1))
