class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        while n != 0:
            # Update last index of nums1
            if m == 0 or nums1[m-1] <= nums2[n-1]:
                nums1.insert(m, nums2[n-1])
                nums1.pop()
                n -= 1
            else:
                m -= 1

        # i, j = 0, 0

        # while j < n:
        #     if m == 0 or nums2[j] <= nums1[i]:
        #         nums1.insert(i, nums2[j])
        #         nums1.pop()
        #         j += 1
        #     else:
        #         m -= 1
        #     i += 1
