class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Solution 02
        numCount, pairCount = {}, 0

        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1
            if numCount[num] > 1: pairCount += numCount[num] - 1

        return pairCount
        
        
        # Solution 01
        # pairCount = 0

        # for i in range(0, len(nums) - 1):
        #     for j in range(i+1, len(nums)):

        #         if nums[i] == nums[j]:
        #             pairCount += 1
        
        # return pairCount
