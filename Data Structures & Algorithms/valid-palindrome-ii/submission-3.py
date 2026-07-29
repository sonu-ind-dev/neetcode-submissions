class Solution:
    def validPalindrome(self, s: str) -> bool:
        # abd dbba, abd bbba
        # Match => [0, 6], [1, 5]
        # Un-Match => [2, 4]

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                
                l, r = l+1, r-1
            
            return True


        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return isPalindrome(l+1, r) or isPalindrome(l, r-1)

            l, r = l + 1, r - 1

        return True
