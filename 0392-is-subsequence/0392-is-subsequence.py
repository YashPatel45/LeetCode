class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        if len(s) > len(t):
            return False
    
        left, pointer = 0, 0
        while left < len(s) and pointer < len(t):
            if s[left] == t[pointer]:
                left += 1
            pointer +=1
            # if t[pointer] != s[left]:
            #     pointer+=1
            # else:
            #     temp += t[pointer]
            #     left+=1
            #     pointer+=1
            
        return left == len(s)

                
