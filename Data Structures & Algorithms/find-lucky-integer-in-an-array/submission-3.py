class Solution:
    def findLucky(self, arr: List[int]) -> int:
        luckyNum = -1
        numCount = {}

        for num in arr:
            numCount[num] = numCount.get(num, 0) + 1
        
        for num in numCount:
            if num == numCount[num] and luckyNum < num:
                luckyNum = num
        
        return luckyNum