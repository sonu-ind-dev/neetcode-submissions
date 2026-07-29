class Solution:
    def maxDifference(self, s: str) -> int:

        # abb
        
        elementCounts = {}

        largestCount = 0
        secondLargestCount = len(s)
        
        for value in s:
            elementCounts[value] = elementCounts.get(value, 0) + 1

        for key, value in elementCounts.items():
            if largestCount < value and value % 2 == 1:
                largestCount = value
            
            if secondLargestCount > value and value % 2 == 0:
                secondLargestCount = value
            
        return largestCount - secondLargestCount

        
