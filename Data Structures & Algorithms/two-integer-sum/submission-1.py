class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for index in range(len(nums) - 1, -1, -1):
            remaining = target - nums[index]

            if remaining in nums:
                return [nums.index(remaining), index]