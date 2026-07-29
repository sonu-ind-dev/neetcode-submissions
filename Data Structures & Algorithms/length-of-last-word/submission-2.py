class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result, hadSpace = '', True

        for value in s:
            if hadSpace:
                if value != ' ':
                    result = value
                    hadSpace = False
            elif value != ' ':
                result += value
            else:
                hadSpace = True
        
        return len(result)