class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        result = list(range(1, len(nums) + 1))

        for num in nums:
            if num in result:
                result.remove(num)
        
        return result