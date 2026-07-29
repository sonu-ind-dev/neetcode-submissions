class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        numHashMap = {}
        res = [0, 0]

        for arr in grid:
            for num in arr:
                numHashMap[num] = numHashMap.get(num, 0) + 1

                if numHashMap[num] > 1:
                    res[0] = num
        
        for i in range(1, (len(grid) * len(grid)) + 1):
            if numHashMap.get(i, 0) == 0:
                res[1] = i
                break
        
        return res