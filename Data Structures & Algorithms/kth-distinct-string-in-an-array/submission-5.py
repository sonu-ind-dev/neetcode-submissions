class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        # Solution 01
        strCount = {}

        for string in arr:
            strCount[string] = strCount.get(string, 0) + 1
        
        for string, count in strCount.items():
            k -= 1 if count == 1 else 0
            
            if k == 0:
                return string
        
        return ''


        # Solution 02
        # uniqueStr, duplicateStr, nonDuplicateStr = [], [], []

        # for string in arr:
        #     if string not in uniqueStr:
        #         uniqueStr.append(string)
        #     else:
        #         duplicateStr.append(string)
        
        # for string in uniqueStr:
        #     if string not in duplicateStr:
        #         nonDuplicateStr.append(string)

        # return '' if k > len(nonDuplicateStr) else nonDuplicateStr[k - 1]