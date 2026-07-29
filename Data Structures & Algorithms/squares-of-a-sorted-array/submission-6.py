class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sortedNums = []

        l, r = 0, len(nums) - 1

        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                sortedNums.insert(0, abs(nums[r]) ** 2)
                r = r-1
            else:
                sortedNums.insert(0, abs(nums[l]) ** 2)
                l = l+1

        return sortedNums