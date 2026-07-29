class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []

        # Pick every word one by one - loop on array
        # I will check is this word is a substring of any another word

        for subStr in words:
            for str in words:

                if subStr == str or len(str) < len(subStr):
                    continue
                
                if subStr in str:
                    result.append(subStr)
                    break
        
        return result
        
