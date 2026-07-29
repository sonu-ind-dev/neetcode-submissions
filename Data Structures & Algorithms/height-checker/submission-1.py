class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedArr = sorted(heights)
        output = 0

        for i, height in enumerate(heights):
            if height != sortedArr[i]:
                output += 1
        
        return output