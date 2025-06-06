class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = len(nums)-1
        
        while j >= 0:
            if val == nums[j]:
                nums.pop(j)
            j-=1