class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        result = ''

        for i in range(len(s)-1, -1, -1):
            if i != 0:
                result += s[i] + ' '
                continue
            result += s[i]
        return result

        # for i in range(len(s)-1, -1, -1):
        #     if s[i].isspace() or i == 0:
        #         if i == 0 and not s[i].isspace():
        #             result += s[i:prev_ind]
        #         elif i != 0:
        #             result += s[i+1:prev_ind] + ' '
        #         prev_ind = i

        # return result.strip()