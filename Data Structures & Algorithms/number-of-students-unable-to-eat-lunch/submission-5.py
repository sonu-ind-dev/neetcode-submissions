class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stCount = Counter(students)

        for sd in sandwiches:
            if stCount.get(sd, 0) > 0:
                stCount[sd] -= 1
            else:
                break

        return stCount.get(0, 0) + stCount.get(1, 0)
