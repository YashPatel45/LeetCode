class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n_d = {}

        for i in nums:
            if i in n_d:
                n_d[i] += 1
            else:
                n_d[i] = 1

        print(n_d)
        result = []
        for k, v in n_d.items():
            if v >= 2:
                result.append(k)
        
        return result

        # return [max(n_d, key=n_d.get)]