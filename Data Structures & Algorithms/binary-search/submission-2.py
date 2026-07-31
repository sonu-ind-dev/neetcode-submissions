class Solution:
    def search(self, nums: List[int], target: int) -> int:
        startIndex, endIndex = 0, len(nums)-1

        while startIndex <= endIndex:
            middleIndex = (startIndex + endIndex) // 2

            if nums[middleIndex]==target:
                return middleIndex
            elif nums[middleIndex]<target:
                startIndex = middleIndex+1
            else:
                endIndex = middleIndex-1
                
        return -1
        