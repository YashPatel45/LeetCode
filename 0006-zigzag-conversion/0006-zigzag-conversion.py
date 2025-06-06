class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        l = ['' for _ in s]
        
        i = 0
        step = 1

        for c in s:
            l[i] += c
            i += step

            if i == numRows-1:
                step = -1
            elif i == 0:
                step = 1
            
        return ''.join(l)