class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''

        for char in strs[0]:
            for word in strs:
                # We have return second condition because in python if first condition is true then python don't even check condition after or
                if len(word) == len(result) or word[ len(result) ] != char:
                    return result
            
            result += char
        
        return result