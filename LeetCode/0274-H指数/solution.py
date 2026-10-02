from typing import List
class Solution:
    def hIndex(self, citations: list[int]) -> int:
        res = 0
        citations.sort()
        citations.reverse()
        for val in citations:
            if val >= res+1:
                res += 1
        return res




solution = Solution()
print(solution.hIndex(citations = [3,0,6,1,5]))
print(solution.hIndex(citations = [1,3,1]))
