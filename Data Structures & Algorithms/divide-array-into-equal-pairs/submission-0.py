class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        result = True

        numCount = {}

        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1
        
        for key, value in numCount.items():
            if value % 2 == 1:
                return False
        
        return True