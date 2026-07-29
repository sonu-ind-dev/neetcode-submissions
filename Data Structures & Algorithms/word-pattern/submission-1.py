class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternHashMap, wordHashMap, wordsArr = {}, {}, s.split(' ')

        if len(pattern) != len(wordsArr):
            return False

        for i in range(len(pattern)):
            letter = pattern[i]
            word = wordsArr[i]

            if letter in patternHashMap and patternHashMap[letter] != word:
                return False
            
            if word in wordHashMap and wordHashMap[word] != letter:
                return False
            
            wordHashMap[word] = letter
            patternHashMap[letter] = word
        
        return True