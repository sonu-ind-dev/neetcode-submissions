class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stCount = Counter(students)

        for sd in sandwiches:
            if stCount.get(sd, 0) > 0:
                stCount[sd] -= 1
            else:
                break
        
        return stCount.get(0, 0) + stCount.get(1, 0);

        for i in range(len(sandwiches)):
            taken = False
            # for j in range(i, len(students)):
            for j, _ in enumerate(students):
                if students[j] == sandwiches[i]:
                    taken = True
                    del students[j]
                    break

            if taken == True:
                continue
            else:
                return len(sandwiches) - i

        return 0
