class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index in range(0, len(nums)):
            num = nums[index]

            if num==target or num>target:
                return index
        
        return len(nums)