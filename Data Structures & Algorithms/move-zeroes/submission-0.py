class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0 # i is index of 0 and j is index of non zero

        while j < len(nums):
            # When nums[i] is non zero but nums[j] is
            if nums[i] != 0:
                i = i+1
            elif nums[j] != 0:
                # Flip Non Zero Nums[j] with nums[i] 0
                nums[i], nums[j] = nums[j], nums[i]
                i = i+1

            j = j+1