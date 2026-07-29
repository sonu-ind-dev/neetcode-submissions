class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        # Solution 02

        numSet = set()

        for num in nums:
            if num in numSet:
                numSet.remove(num)
            else:
                numSet.add(num)
        
        return len(numSet) == 0

        # Solution 01
        # numCount = {}

        # for num in nums:
        #     numCount[num] = numCount.get(num, 0) + 1
        
        # for key, value in numCount.items():
        #     if value % 2 == 1:
        #         return False
        
        # return True