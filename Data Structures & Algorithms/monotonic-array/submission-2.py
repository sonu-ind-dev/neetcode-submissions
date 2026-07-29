class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isInc, isDec = False, False

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                isInc = True
                if isDec == True: return False
            elif nums[i-1] > nums[i]:
                isDec = True
                if isInc == True: return False
        
        return True