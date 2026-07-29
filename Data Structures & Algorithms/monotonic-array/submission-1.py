class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        # Solution 02

        count = 0

        for i in range(1, len(nums)):

            if (nums[i-1] < nums[i] and count < 0) or (nums[i-1] > nums[i] and count > 0):
                return False

            if nums[i-1] < nums[i]:
                count += 1
            elif nums[i-1] > nums[i]:
                count -= 1

        return True

        # Solution 01
        # isInc, isDec = False, False

        # for i in range(1, len(nums)):

        #     if nums[i-1] < nums[i]:
        #         isInc = True

        #         if isDec == True:
        #             return False
        #     elif nums[i-1] > nums[i]:
        #         isDec = True

        #         if isInc == True:
        #             return False
        
        # return True