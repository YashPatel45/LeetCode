class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_d = {}

        s = s.split(' ')

        if len(pattern) != len(s):
            return False
        
        for ind, c in enumerate(pattern):
            if c in s_d and s_d[c] != s[ind]:
                return False
            elif c not in s_d and s[ind] in s_d.values():
                return False
            else:
                s_d[c] = s[ind]
 
        # print(s_d)
        return True

