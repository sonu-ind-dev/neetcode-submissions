class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniqueCharIndex = {}

        for i in range(len(s)):
            uniqueCharIndex[s[i]] = -1 if s[i] in uniqueCharIndex else i

        for _, index in uniqueCharIndex.items():
            if index != -1:
                return index

        return -1
