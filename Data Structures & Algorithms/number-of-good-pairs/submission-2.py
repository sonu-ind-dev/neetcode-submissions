class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Solution 02
        numCount, pairCount = Counter(nums), 0

        for _, count in numCount.items():
            pairCount += count * (count - 1) // 2

        return pairCount
        
        
        # Solution 01
        # pairCount = 0

        # for i in range(0, len(nums) - 1):
        #     for j in range(i+1, len(nums)):

        #         if nums[i] == nums[j]:
        #             pairCount += 1
        
        # return pairCount
