class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        return sorted(nums)[len(nums) // 2]

        # elementCount = {}

        # for value in nums:
        #     elementCount[value] = elementCount.get(value, 0) + 1

        #     if elementCount[value] > len(nums)/2:
        #         return value