class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isInc, isDec = False, False

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                if isDec == True: return False
                isInc = True
            elif nums[i-1] > nums[i]:
                if isInc == True: return False
                isDec = True
        
        return True