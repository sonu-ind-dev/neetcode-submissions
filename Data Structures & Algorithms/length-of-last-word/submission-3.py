class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result, hadSpace = '', True

        for value in s:
            if value == ' ':
                hadSpace = True
            else:
                if hadSpace:
                    result = value
                    hadSpace = False
                else:
                    result += value
        
        return len(result)