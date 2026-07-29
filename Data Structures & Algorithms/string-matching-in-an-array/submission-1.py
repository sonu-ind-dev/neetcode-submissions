class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []

        # Pick every word one by one - loop on array
        # I will check is this word is a substring of any another word

        present = 0

        for subStr in words:
            for str in words:
                
                if subStr == str or len(str) < len(subStr):
                    continue
                
                present = 0
                for char in str:
                    if present == len(subStr):
                        break
                    elif ( present > 0 and char != subStr[present] ):
                        present = 0
                    elif char == subStr[present]:
                        present += 1
                
                if present == len(subStr):
                    result.append(subStr)
                    break
        
        return result
        
