class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        wordHashMap = {}
        strHashMap = {}

        maxInstances = len(text)

        # Work Same Code => wordHashMap = Counter("balloon")
        for str in 'balloon':
            wordHashMap[str] = wordHashMap.get(str, 0) + 1

        # Work Same Code => strHashMap = Counter(text)
        for str in text:
            strHashMap[str] = strHashMap.get(str, 0) + 1
        
        for key, value in wordHashMap.items():
            totalKeyCount = strHashMap.get(key, 0)
            maxInstances = min(maxInstances, totalKeyCount // value)
        
        return maxInstances
            
            
