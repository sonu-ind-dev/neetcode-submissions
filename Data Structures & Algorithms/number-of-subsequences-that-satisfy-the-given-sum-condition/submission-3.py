class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = (10 ** 9) + 7
        l, r, result = 0, 0, 0

        for i in range(0, len(nums)):
            l = r = i
            while r < len(nums):
                min, max = nums[l], nums[r]

                if min + max <= target:
                    r += 1
                else:
                    if l==r:
                        return result % mod
                    
                    result += 2 ** (r - l - 1)
                    break
            
            result += 2 ** (r - l - 1) if r==len(nums) else 0

        return result % mod
