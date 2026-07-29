class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        uniqueNums = set(nums)
        result = []

        for i in range(1, len(nums) + 1):
            if i not in uniqueNums:
                result.append(i)
        
        return result