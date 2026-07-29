class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] *= nums[i]
        
        # Now nums = [16, 1, 0, 9, 100]

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