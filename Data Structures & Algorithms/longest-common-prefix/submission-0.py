class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''

        for char in strs[0]:
            for word in strs:
                if len(word) == len(result):
                    return result
                elif word[ len(result) ] != char:
                    return result
            
            result = result + char

        
        return result