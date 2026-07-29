class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solution Without Division Operation
        value = 1
        output = [1] * len(nums)

        for i in range(1, len(nums)):
            value *= nums[i-1]
            output[i] *= value
        
        value = 1
        
        for i in range(len(nums) - 1, 0, -1):
            value *= nums[i]
            output[i-1] *= value

        return output

        
        # Solution With Division Operation
        # totalMultiple, countZero = 1, 0
        # output = []

        # for num in nums:
        #     if num != 0:
        #         totalMultiple *= num
        #     else:
        #         countZero += 1

        #     if countZero > 1:
        #         return [0] * len(nums)

        # for num in nums:
        #     if num == 0:
        #         output.append(totalMultiple)
        #     elif countZero > 0:
        #         output.append(0)
        #     else:
        #         output.append(totalMultiple // num)

        # return output
