class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        if len(s) <= 1:
            return True
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]','',s)
        s_new = s[::-1]

        return s == s_new