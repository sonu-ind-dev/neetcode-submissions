class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        for i in range(1, len(nums)):
            haveOdd = nums[i-1] % 2 == 1 or nums[i] % 2 == 1
            haveEven = nums[i-1] % 2 == 0 or nums[i] % 2 == 0

            if haveEven and haveOdd:
                continue
            else:
                return False
        
        return True