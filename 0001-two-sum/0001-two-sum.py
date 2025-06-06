class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        n_d = defaultdict(list)

        for ind, n in enumerate(nums):
            if n in n_d:
                n_d[n].append(ind)
                return n_d[n]
            n_d[target-n].append(ind)