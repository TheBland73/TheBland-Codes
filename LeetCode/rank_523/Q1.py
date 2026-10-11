class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        #即判断n/2是否存在于斐波那契额数列
        if n % 2 != 0: #为奇数
            return False
        if n == 2:
            return True
        target = n // 2
        cycle = [1,1]
        cur = 0
        while cur < target:  # 1 1 -> 1 2 -> 2 3 -> 3 5
            cur = cycle[0] + cycle[1]
            cycle[0] = cycle[1]
            cycle[1] = cur
        if cur == target:
            return True
        else:
            return False

solution = Solution()
print(solution.threeFibonacciSum(16))
print(solution.threeFibonacciSum(8))
print(solution.threeFibonacciSum(2))
print(solution.threeFibonacciSum(100000))
