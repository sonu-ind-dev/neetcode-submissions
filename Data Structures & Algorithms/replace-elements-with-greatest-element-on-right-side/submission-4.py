class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largestNum = -1

        for i in range(len(arr)):
            index = len(arr) - i - 1
            value = arr[index]

            arr[index] = largestNum

            if largestNum < value:
                largestNum = value

        return arr
