class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        for i, num in enumerate(nums1):
            nums2Index = nums2.index(num)

            nums1[i] = -1
            for j in range(nums2Index + 1, len(nums2)):
                if nums2[j] > num:
                    nums1[i] = nums2[j]
                    break
        
        return nums1