class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = sorted(strs)

        left = s[0]
        right = s[-1]

        result = ''

        for i in range(min(len(left), len(right))):
            if left[i] != right[i]:
                return result
            result += left[i]
        
        return result