class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        TotalSum = 0

        for num in nums:
            TotalSum += num
        
        leftSum, rightSum = 0, TotalSum
        
        for index, num in enumerate(nums):
            leftSum += 0 if index == 0 else nums[index - 1]
            rightSum = TotalSum - ( leftSum + num )

            if leftSum == rightSum:
                return index
        
        return -1