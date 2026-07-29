class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # Solution 01
        for num in nums:
            i = abs(num) - 1
            nums[i] = -1 * abs(nums[i])
    
        res = []

        for i, num in enumerate(nums):
            if num > 0:
                res.append(i+1)
        
        return res


        # Solution 02
        # result = list(range(1, len(nums) + 1))

        # for num in nums:
        #     if num in result:
        #         result.remove(num)
        
        # return result



