class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount, output = Counter(nums), []

        for i in range(k):
            largestNum = None

            for num, count in numCount.items():
                if numCount[largestNum] < count:
                    largestNum = num
            
            output.append(largestNum)
            numCount.pop(largestNum, None)
        
        return output