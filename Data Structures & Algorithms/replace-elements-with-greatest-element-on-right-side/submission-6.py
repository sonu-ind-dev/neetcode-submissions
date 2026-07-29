class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxNum = -1

        for index in range(len(arr)-1, -1, -1):
            newMaxNum = max(arr[index], maxNum)

            arr[index] = maxNum
            maxNum = newMaxNum

        return arr
