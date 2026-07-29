class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r, count = 1, 1, 1
        num = nums[l]

        while r < len(nums):
            if nums[l-1] == nums[r]:
                count += 1
                if count <= 2:
                    nums[l] = nums[r]
                    l += 1
            else:
                # num = nums[r]
                nums[l] = nums[r]
                l, count = l + 1, 1
            r += 1

        return l
