class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:    
        s_d = {}
        p_d = {}

        if len(s) >= len(p):
            for i in range(len(p)):
                if p[i] in p_d:
                    p_d[p[i]] += 1
                else:
                    p_d[p[i]] = 1
                if s[i] in s_d:
                    s_d[s[i]] += 1
                else:
                    s_d[s[i]] = 1
        if len(p) > len(s):
            return []

        ans = []
        n = len(p)
        if s_d == p_d:
            ans.append(0)

        for i in range(0,len(s) - n):
            print('----', i, s[i+n])
            print(s_d)

            s_d[s[i]] -= 1
            if s_d[s[i]] == 0:
                del s_d[s[i]]

            if s[i+n] in s_d:
                s_d[s[i+n]] += 1
            else:
                s_d[s[i+n]] = 1

            if s_d == p_d:
                ans.append(i+1)

        return ans