class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        # Check max length for incrementing & decrement

        maxInc, maxDec, IncFrom, DecFrom = 1, 1, 0, 0

        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                maxInc += 0 if maxInc >= (i - IncFrom + 2) else 1
                DecFrom = i + 1
            elif nums[i] > nums[i+1]:
                maxDec += 0 if maxDec >= (i - DecFrom + 2) else 1
                IncFrom = i + 1
            else:
                DecFrom = i + 1
                IncFrom = i + 1
        
        return maxInc if maxInc > maxDec else maxDec
