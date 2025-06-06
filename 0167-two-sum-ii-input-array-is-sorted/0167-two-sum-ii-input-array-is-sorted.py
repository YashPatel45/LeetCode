class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        from collections import defaultdict

        n_d = defaultdict(list)

        for ind, n in enumerate(numbers):
            if n in n_d:
                n_d[n].append(ind+1)
                return n_d[n]
            n_d[target-n].append(ind+1)