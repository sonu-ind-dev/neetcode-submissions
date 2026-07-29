class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # i,j = 0,0

        # while i<len(s) and j<len(t):
        #     if s[i] == t[j]:
        #         j += 1
        #     i += 1
        
        # return len(t) - j
        
        matched = 0

        for index, value in enumerate(s):
            if matched == len(t):
                break
            if t[matched] == value:
                matched += 1
        
        return len(t) - matched
