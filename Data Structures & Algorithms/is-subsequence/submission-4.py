class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # i, j = 0, 0

        # while i < len(s) and j < len(t):
        #     if s[i] == t[j]:
        #         i += 1
        #     j += 1
        
        # return i == len(s)

        matched = 0

        for index, value in enumerate(t):
            if matched == len(s):
                break
            if s[matched] == value:
                matched += 1
        
        return len(s) == matched