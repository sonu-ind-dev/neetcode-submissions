class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        st0Count, st1Count = 0, 0

        for st in students:
            if st == 1:
                st1Count += 1
            else:
                st0Count += 1

        for sd in sandwiches:
            if (st0Count == 0 and sd == 0) or (st1Count == 0 and sd == 1):
                return st0Count + st1Count

            if sd == 1:
                st1Count -= 1
            else:
                st0Count -= 1

        return 0