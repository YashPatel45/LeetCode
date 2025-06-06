class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n_d = {}

        for i in nums:
            if i in n_d and n_d[i] >= 1:
                return True
            n_d[i] = n_d.get(i, 0) + 1
        return False