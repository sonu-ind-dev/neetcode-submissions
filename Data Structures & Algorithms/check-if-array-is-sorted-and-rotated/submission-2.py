class Solution:
    def check(self, nums: List[int]) -> bool:
        x = 0 # Number of elements has been rotated

        for i in range(1, len(nums)):
            # The time we will get dec order x = len(nums) - i

            if nums[i-1] > nums[i]:
                x = len(nums) - i
                break
        
        for i in range( -1 * x, len(nums) - x - 1 ):
            if nums[i] > nums[i+1]:
                return False
        
        return True
        
        