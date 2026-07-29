class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0

        for value in details:
            if int(value[11] + value[12]) > 60:
                count += 1
        
        return count