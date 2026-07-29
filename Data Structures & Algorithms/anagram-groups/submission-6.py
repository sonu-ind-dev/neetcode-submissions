class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        included = []

        for i, iWord in enumerate(strs):
            if iWord in included:
                continue
            else:
                anagramArr = [iWord]

                for j, jWord in enumerate(strs):

                    if i == j or len(iWord) != len(jWord):
                        continue
                    elif sorted(iWord) == sorted(jWord):
                        included.append(jWord)
                        anagramArr.append(jWord)
                
                result.append(anagramArr)
        
        return result