class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largestNum = -1

        for index in range(len(arr)-1, -1, -1):
            newLargestNum = max(arr[index], largestNum)

            arr[index] = largestNum
            largestNum = newLargestNum

        return arr
