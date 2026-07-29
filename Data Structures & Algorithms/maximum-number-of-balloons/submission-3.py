class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        textHashMap, wordHashMap, maxInstances = {}, {}, len(text)

        # Work Same Code => wordHashMap = Counter("balloon")
        for str in 'balloon':
            wordHashMap[str] = wordHashMap.get(str, 0) + 1

        # Work Same Code => textHashMap = Counter(text)
        for str in text:
            textHashMap[str] = textHashMap.get(str, 0) + 1
        
        for key, value in wordHashMap.items():
            totalKeyCount = textHashMap.get(key, 0)
            maxInstances = min(maxInstances, totalKeyCount // value)
        
        return maxInstances
            
            
