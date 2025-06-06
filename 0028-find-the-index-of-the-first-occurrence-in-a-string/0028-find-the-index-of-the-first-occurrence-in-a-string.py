class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        
        left = 0

        while left < len(haystack):
            if needle[0] == haystack[left]:
                if haystack[left:left+len(needle)] == needle:
                    return left
            elif len(haystack)-left < len(needle):
                return -1
            left+=1

        return -1
