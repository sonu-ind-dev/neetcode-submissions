class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0 # i is index of 0 and j is index of non zero

        while j < len(nums):
            # Flip Nums[j] with nums[i]
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
            
            if nums[i] != 0 or nums[j] != 0:
                i = i+1

            j = j+1