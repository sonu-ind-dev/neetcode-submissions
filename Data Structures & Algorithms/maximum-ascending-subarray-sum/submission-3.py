class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        maxSum, currentSum = nums[0], nums[0]

        for i in range(len(nums) - 1):
            if not (nums[i] < nums[i+1]):
                currentSum = 0
            
            currentSum += nums[i+1]
            maxSum = max(maxSum, currentSum)
        
        return maxSum