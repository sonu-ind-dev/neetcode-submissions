class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ln, i = len(nums), 0

        k = k % ln
        
        # Rotate whole array
        while i < ( ln // 2 ):
            nums[i], nums[ln-i-1] = nums[ln-i-1], nums[i]
            i = i+1

        # Ratate 0 to k-1 array
        i = 0
        while i < (k // 2):
            nums[i], nums[k-i-1] = nums[k-i-1], nums[i]
            i = i+1

        # Rotate k to len array
        i = 0
        while i < ((ln-k) // 2):
            nums[i+k], nums[ln-i-1] = nums[ln-i-1], nums[i+k]
            i = i+1
