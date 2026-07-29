class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        stCount = {0: 0, 1: 0}

        for st in students:
            stCount[st] += 1

        for sd in sandwiches:
            if stCount[sd] == 0:
                break
            
            stCount[sd] -= 1

        return stCount[0] + stCount[1]
