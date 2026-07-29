class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        uniqueStr, duplicateStr, nonDuplicateStr = [], [], []

        for string in arr:
            if string not in uniqueStr:
                uniqueStr.append(string)
            else:
                duplicateStr.append(string)
        
        for string in uniqueStr:
            if string not in duplicateStr:
                nonDuplicateStr.append(string)

        return '' if k > len(nonDuplicateStr) else nonDuplicateStr[k - 1]