class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        

        for i in range(1, len(nums)):
            num1 = nums[i - 1]
            num2 = nums[i]

            haveOdd = num1 % 2 == 1 or num2 % 2 == 1
            haveEven = num1 % 2 == 0 or num2 % 2 == 0

            if haveEven and haveOdd:
                continue
            else:
                return False
        
        return True