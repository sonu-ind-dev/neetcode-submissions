class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        numHashMap = {}
        duplicate, missing = 0, 0

        for arr in grid:
            for num in arr:
                numHashMap[num] = numHashMap.get(num, 0) + 1

                if numHashMap[num] > 1:
                    duplicate = num
        
        for i in range(1, (len(grid) * len(grid)) + 1):
            if i not in numHashMap:
                missing = i
                break
        
        return [duplicate, missing]