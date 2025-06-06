class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        i = 0
        k = 1

        while k < len(nums):
            if nums[i] == nums[k]:
                nums.pop(k)
            else:
                i+=1
                k+=1