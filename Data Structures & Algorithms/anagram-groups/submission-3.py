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
                    else:
                        # check both are anagram or not
                        iWordChars, jWordChars = {}, {}

                        for index in range(len(iWord)):
                            iWordChars[iWord[index]] = iWordChars.get(iWord[index], 0) + 1
                            jWordChars[jWord[index]] = jWordChars.get(jWord[index], 0) + 1

                    if iWordChars == jWordChars:
                        included.append(jWord)
                        anagramArr.append(jWord)
                
                result.append(anagramArr)
        
        return result