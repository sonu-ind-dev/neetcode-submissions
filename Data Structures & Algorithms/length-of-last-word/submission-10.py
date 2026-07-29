class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        
        for index in range(len(s) - 1, -1, -1):
            if s[index] == ' ' and result > 0:
                break
            elif s[index] != ' ':
                result += 1
        
        return result