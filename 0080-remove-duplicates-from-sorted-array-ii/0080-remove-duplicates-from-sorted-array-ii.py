class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 2
        
        write_index = 2

        for i in range(2, len(nums)):
            #[1,1,1,2,2,3]
            if nums[i] != nums[write_index-2]: # 1 != 2
                nums[write_index] = nums[i]
                write_index += 1
            
        return write_index

        