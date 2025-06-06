class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_to_t = {}
        t_to_s = {}

        for i in range(len(t)):
            if s[i] not in s_to_t:
                s_to_t[s[i]] = t[i]
            
            if t[i] not in t_to_s:
                t_to_s[t[i]] = s[i]

        for a, b in s_to_t.items():
            if a not in t_to_s.values() or b not in t_to_s.keys():
                return False

        new_s = list(s)

        from collections import defaultdict
        final = defaultdict(str)

        for i, v in enumerate(new_s):
            if v in s_to_t:
                final[i] = s_to_t.get(v)
        
        s_final = ''
        for key, val in final.items():
            s_final += val

        return t == s_final