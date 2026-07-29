class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Solution 02

        # -ve value at index i means i+1 is presen in the array
        
        # Removing -ve values from array
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        # Making index = val - 1 to negetive because value is present
        for i in range(len(nums)):
            val = abs(nums[i])

            if 1 <= val <= len(nums):
                if nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)
                else:
                    nums[val - 1] = -1 * abs(nums[val - 1])
        
        # Checking which value is non negetive => that index is not present as value in the array
        for i in range(1, len(nums) + 1):
            if nums[i-1] >= 0:
                return i
        
        return len(nums) + 1


        # Solution 01
        # nums = set(nums)
        # for i in range(1, len(nums) + 1):
        #     if i not in nums:
        #         return i
        
        # return len(nums) + 1