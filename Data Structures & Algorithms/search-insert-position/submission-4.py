class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # for index in range(0, len(nums)):
        #     num = nums[index]

        #     if num==target or num>target:
        #         return index
        
        # return len(nums)

        l, r = 0, len(nums)-1

        while l<=r:
            mid = (l+r) // 2

            if nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
            else:
                return mid

        return l