class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        s = sum(nums[:k])
        n_s = s

        for i in range(k, len(nums)):
            n_s = n_s - nums[i-k] + nums[i]
            s = max(s, n_s)
        
        return s/k
        
        
        
        
        
        
        
        
        # avg = {}
        # result = None
        # if len(nums) <= 1:
        #     return nums[0]
        # else: 
        #     for i in range(0, len(nums)-k+1): 
        #         val = tuple(nums[i:i+k])
        #         if val not in avg:
        #             avg[val] = 0
            
        #     for i in avg.keys():
        #         avg[i] = sum(i) / k
            
        #     return max(avg.values())
                