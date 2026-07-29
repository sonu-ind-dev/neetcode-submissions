class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        
        for index in range(len(s) - 1, -1, -1):
            if s[index] != ' ':
                result += 1
            elif s[index] == ' ' and result > 0:
                break
        
        return result