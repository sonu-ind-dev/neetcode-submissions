class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j = 0, 0

        while j < n:
            if m == 0 or nums2[j] < nums1[i]:
                nums1.insert(i, nums2[j])
                nums1.pop()
                j += 1
            else:
                m -= 1
            i += 1
