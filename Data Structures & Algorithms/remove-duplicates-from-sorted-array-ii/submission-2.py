class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r, count = 0, 0, 0
        num = nums[l]

        while r < len(nums):
            if num == nums[r]:
                count += 1
                if count <= 2:
                    nums[l] = nums[r]
                    l += 1
            else:
                num = nums[r]
                nums[l] = nums[r]
                l, count = l + 1, 1
            r += 1

        return l
