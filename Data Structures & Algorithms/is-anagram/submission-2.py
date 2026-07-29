class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        sHashmap = {}
        tHashmap = {}

        for i in range(len(s)):
            sHashmap[s[i]] = sHashmap.get(s[i], 0) + 1
            tHashmap[t[i]] = tHashmap.get(t[i], 0) + 1

        for char in sHashmap:
            if sHashmap.get(char, 0) != tHashmap.get(char, 0):
                return False

        return True
