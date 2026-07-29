class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums = sorted(nums)

        output = 1

        for num in nums:
            if output == num:
                output = num + 1
        
        return output




        # nextNum = {0: 1}
        # largestNum, output = 0, 0

        # for num in nums:
        #     if num >= 0: nextNum[num] = num + 1
        #     if largestNum < num: largestNum = num
        
        # output = largestNum + 1
        
        # for key, value in nextNum.items():
        #     if nextNum.get(value, 0) == 0:
        #         if output > value:
        #             output = value
        
        # return output