class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] *= nums[i]
        
        # Array Element Sorting Algoritham
        i, j = 0, 0

        while i < len(nums):
            j = i+1
            while j < len(nums):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                
                j = j+1
            i = i+1
        
        return nums