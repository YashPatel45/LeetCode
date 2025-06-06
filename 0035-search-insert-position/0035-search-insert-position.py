class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:


        mid = len(nums)//2

        def getInd(n):
            # print("n",n)
            for ind, val in enumerate(n):
                print(ind, val)
                if val == target:
                    return ind
                elif val-1 == target:
                    return ind if ind != 0 else 0
                elif val+1 == target:
                    return ind+1 
            return 0
        
        if target == nums[mid]:
            return mid
        elif target > nums[-1]:
            return len(nums)
        elif target < nums[mid]:
            return getInd(nums[:mid])
        elif target > nums[mid]:
            return getInd(nums[mid:])+len(nums[:mid])