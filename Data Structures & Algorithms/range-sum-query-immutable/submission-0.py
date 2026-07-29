class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixArr = [0] * len(nums)

        for i, num in enumerate(nums):
            self.prefixArr[i] = self.prefixArr[i] + num if i == 0 else self.prefixArr[i-1] + num

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixArr[right] if left == 0 else self.prefixArr[right] - self.prefixArr[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)