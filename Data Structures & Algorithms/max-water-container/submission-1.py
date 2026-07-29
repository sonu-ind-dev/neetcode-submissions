class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        # Brut Force Solution O(N**2)
        # for i in range(len(heights)-1):
        #     for j in range(i+1, len(heights)):
        #         l, h = j-i, min(heights[i], heights[j])
        #         res = max(res, l*h)

        # Optimized Solution O(N)
        l, r = 0, len(heights) - 1

        while l < r:
            res = max(res, (r - l) * min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res
