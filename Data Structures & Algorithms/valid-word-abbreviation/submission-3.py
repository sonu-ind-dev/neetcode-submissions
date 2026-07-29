class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, l = 0, 0

        # apple => a3e, 3le, ap4

        for c in abbr:
            if c == "0" and l == 0:
                return False

            if "0" <= c <= "9":
                l = (l * 10) + int(c)
                continue

            # Now there is a char
            i += l

            if i >= len(word) or c != word[i]:
                return False

            i, l = i + 1, 0

        return (i + l) == len(word)
