class Solution:
    def romanToInt(self, s: str) -> int:
        collection = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s_len = len(s)

        left = 0
        result = 0

        while left < s_len:
            if left+1 < len(s) and collection[s[left]] < collection[s[left+1]]:
                result += collection[s[left+1]] - collection[s[left]]
                left+=2
            else:
                result += collection[s[left]]
                left+=1
        
        return result


        # pairs = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        # result = 0

        # left = 0
        # right = len(s)-1

        # while left < right:
        #     if s[left]+s[left+1] in pairs:
        #         result += collection[s[left+1]] - collection[s[left]]
        #         left+=2
        #         continue
        #     if s[left] in collection:
        #         result += collection[s[left]]
        #     left +=1

        # if left < len(s):
        #     result += collection[s[len(s)-1]]
            
        # return result