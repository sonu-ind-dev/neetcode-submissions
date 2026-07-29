class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        totalMultiple = 1
        countZero = 0

        for num in nums:
            if num != 0:
                totalMultiple *= num
            else:
                countZero += 1

            if countZero > 1:
                return [0] * len(nums)

        for num in nums:
            if num == 0:
                output.append(totalMultiple)
            elif countZero > 0:
                output.append(0)
            else:
                output.append(totalMultiple // num)

        return output
