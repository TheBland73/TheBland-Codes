class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_s = {}
        s_lst = s.split(' ')
        
        if len(pattern) != len(s_lst):
            return False
        
        for i in range(0,len(pattern)):
            
            if pattern[i] not in pattern_s:
                if s_lst[i] in pattern_s.values():
                    return False
                else:
                    pattern_s[pattern[i]] = s_lst[i]
            else:
                if pattern_s[pattern[i]] == s_lst[i]:
                    continue
                else:
                    return False
        
        return True
