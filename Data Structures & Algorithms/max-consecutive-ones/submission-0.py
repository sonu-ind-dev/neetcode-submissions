class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, result = 0, 0

        for value in nums:
            count = (count + 1) if value == 1 else 0

            if count > result:
                result = count

        return result