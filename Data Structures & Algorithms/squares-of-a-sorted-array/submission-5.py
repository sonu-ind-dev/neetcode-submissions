class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sortedNums = []

        l, r = 0, len(nums) - 1

        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                sortedNums.insert(0, abs(nums[r]) ** 2)
                r = r-1
            else:
                sortedNums.insert(0, abs(nums[l]) ** 2)
                l = l+1

        return sortedNums


        for n in range(len(nums)):
            nums[n] *= nums[n]
        
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