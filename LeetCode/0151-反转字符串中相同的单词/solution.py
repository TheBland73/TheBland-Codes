# split
# sep=None：按任意空白分割
# 不传参数时，会按任意空白字符分割，包括空格、换行 \n、制表符 \t 等，并且会忽略开头、结尾和连续空白。
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        size = len(words)
        res = ''
        for idx,val in enumerate(reversed(words)):
            res += val 
            if idx != size-1:
                res += ' '
        return res

solution = Solution()
print(solution.reverseWords(s = "the sky is blue"))
print(solution.reverseWords(s = "  hello world  "))
