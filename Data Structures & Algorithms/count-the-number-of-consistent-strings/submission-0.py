class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedChar, result = {}, 0

        for c in allowed:
            allowedChar[c] = True
        
        for word in words:
            isPresent = True
            for char in word:
                if not allowedChar.get(char, False):
                    isPresent = False
                    break
            result += 1 if isPresent else 0
        
        return result
                