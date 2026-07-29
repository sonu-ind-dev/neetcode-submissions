class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evenCount = 0

        for i, num in enumerate(nums):
            if num%2 == 0:
                nums[i], nums[evenCount] = nums[evenCount], nums[i]
                evenCount += 1
        
        return nums