class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0

        for value in details:
            if value[11] > '6' or (value[11] == '6' and value[12] != '0'):
                count += 1
        
        return count