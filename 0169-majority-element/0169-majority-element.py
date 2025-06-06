class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        n_d = defaultdict(int)

        for i in nums:
            n_d[i] += 1
            
        return max(n_d, key=n_d.get)