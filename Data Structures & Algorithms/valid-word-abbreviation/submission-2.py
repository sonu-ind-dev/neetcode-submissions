class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l, n = 0, 0

        # apple => a3e, 3le, ap4

        for i, c in enumerate(abbr):
            if c == "0" and l == 0:
                return False
            
            if "0" <= c <= "9":
                l = (l * 10) + int(c)
                continue
            
            # Now there is a char
            n += l

            if n >= len(word) or c != word[n]:
                return False
            
            l, n = 0, n+1
        
        if l > 0 and (n + l) != len(word):
            return False
        
        return True