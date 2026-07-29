class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        completedChar = 0

        for index, char in enumerate(t):
            if char == s[completedChar]:
                completedChar = completedChar + 1
            if completedChar == len(s):
                return True

        return False