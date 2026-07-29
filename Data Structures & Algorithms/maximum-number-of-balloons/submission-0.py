class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        minimumRequired = {}
        strHashMap = {}

        maxInstances = len(text)

        for str in 'balloon':
            minimumRequired[str] = minimumRequired.get(str, 0) + 1

        for str in text:
            strHashMap[str] = strHashMap.get(str, 0) + 1
        
        for key, value in minimumRequired.items():
            totalKeyCount = strHashMap.get(key, 0)
            maxInstances = min(maxInstances, totalKeyCount // value)
        
        return maxInstances
            
            
