class Solution:
    def maxDifference(self, s: str) -> int:

        elementCounts = {}

        largestElementOddCount = 0
        lowestElementEvenCount = len(s)
        
        for value in s:
            elementCounts[value] = elementCounts.get(value, 0) + 1

        for key, value in elementCounts.items():
            if largestElementOddCount < value and value % 2 == 1:
                largestElementOddCount = value
            
            if lowestElementEvenCount > value and value % 2 == 0:
                lowestElementEvenCount = value
            
        return largestElementOddCount - lowestElementEvenCount

        
