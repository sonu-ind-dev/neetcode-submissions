class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sDict, tDict = {}, {}

        for i in range(len(s)):
            sDict[s[i]] = False
            tDict[t[i]] = False
        
        for i in range(len(s)):

            if sDict[s[i]] == False:
                sDict[s[i]] = t[i]
            elif sDict[s[i]] != t[i]:
                return False
            
            if tDict[t[i]] == False:
                tDict[t[i]] = s[i]
            elif tDict[t[i]] != s[i]:
                return False
        
        return True