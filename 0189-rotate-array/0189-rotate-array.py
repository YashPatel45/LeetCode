class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums) # get correct k index if k > len(nums)
        
        rotate = nums[-k:] + nums[:-k]
        for i in range(len(nums)):
            nums[i] = rotate[i]
            




        
   
        
        
