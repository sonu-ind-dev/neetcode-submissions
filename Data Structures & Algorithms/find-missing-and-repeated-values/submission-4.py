class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        N = len(grid)
        numSet = set()
        duplicate, missing = 0, 0

        for arr in grid:
            for num in arr:
                if num in numSet:
                    duplicate = num
                else:
                    numSet.add(num)
        
        for i in range(1, (N * N) + 1):
            if i not in numSet:
                missing = i
                break
        
        return [duplicate, missing]