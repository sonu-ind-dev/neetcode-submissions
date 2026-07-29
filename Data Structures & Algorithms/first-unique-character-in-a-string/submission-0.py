class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniqueCharIndex = {}

        for i in range(len(s)):
            if s[i] not in uniqueCharIndex:
                uniqueCharIndex[s[i]] = i
            else:
                uniqueCharIndex[s[i]] = -1

        for _, index in uniqueCharIndex.items():
            if index != -1:
                return index
        
        return -1
