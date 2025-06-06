class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = 0

        for val in range(len(nums)):
            if nums[val] != 0:
                nums[flag], nums[val] = nums[val], nums[flag]
                flag += 1
