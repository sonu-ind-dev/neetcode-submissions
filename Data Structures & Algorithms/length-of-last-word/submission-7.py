class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = ''
        
        for index in range(len(s) - 1, -1, -1):
            if s[index] == ' ' and len(result) > 0:
                break
            elif s[index] != ' ':
                result = s[index] + result
        
        return len(result)