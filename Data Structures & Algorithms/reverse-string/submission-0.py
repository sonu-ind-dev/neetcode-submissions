class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s)-1
        
        for i in range(len(s) // 2):
            ls, rs = s[l], s[r]

            s[l] = rs
            s[r] = ls

            l += 1
            r -= 1
        
        return s