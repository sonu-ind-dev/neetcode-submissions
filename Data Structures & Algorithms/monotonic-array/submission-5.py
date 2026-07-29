class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isInc, isDec = True, True

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                isDec = False
            elif nums[i-1] > nums[i]:
                isInc = False
        
        return isInc or isDec