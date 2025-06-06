class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        
        from collections import defaultdict
        m_d = defaultdict(int)

        for c in magazine:
            m_d[c] += 1

        for ch in ransomNote:
            if ch in m_d and m_d[ch] == 0:
                return False
            m_d[ch] -= 1
            
        return False if [v for v in m_d.values() if v < 0] else True
        
        