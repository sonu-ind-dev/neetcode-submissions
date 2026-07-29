class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        num, count = None, 0

        for value in nums:
            if count == 0:
                num = value
                count = 1
            elif count:
                count += 1 if value == num else -1
        
        return num

        # Solution 01
        # return sorted(nums)[len(nums) // 2]

        # Solution 02
        # elementCount = {}

        # for value in nums:
        #     elementCount[value] = elementCount.get(value, 0) + 1

        #     if elementCount[value] > len(nums)/2:
        #         return value