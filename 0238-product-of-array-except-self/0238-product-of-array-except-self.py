class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n == 1:
            return [1]
        
        left = [1]*n
        right = [1]*n
        arr = [1]*n

        for i in range(1, n):
            left[i] = nums[i-1] * left[i-1]

        for j in range(n-2, -1, -1):
            right[j] = nums[j+1] * right[j+1]

        for k in range(n):
            arr[k] = left[k] * right[k]
        
        return arr