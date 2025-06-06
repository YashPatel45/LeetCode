class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_d = {}
        seen = set()

        result = -1
        for ind, i in enumerate(s):
            if i not in seen:
                s_d[i] = ind
                seen.add(i)
            elif i in s_d:
                del s_d[i]
        print(s_d)

        return min(s_d.values()) if s_d else -1
   
        