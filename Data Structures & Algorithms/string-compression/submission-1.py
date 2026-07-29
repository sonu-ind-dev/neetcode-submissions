class Solution:
    def compress(self, chars: List[str]) -> int:
        s = [chars[0], 1]

        for i in range(1, len(chars)):
            if chars[i - 1] == chars[i]:
                s[-1] += 1
            else:
                if s[-1] == 1:
                    del s[-1]
                s.append(chars[i])
                s.append(1)

        if s[-1] == 1:
            del s[-1]

        cIndex = 0

        for i in range(len(s)):
            if len(str(s[i])) == 1:
                chars[cIndex] = s[i]
                cIndex += 1
            else:
                for c in str(s[i]):
                    chars[cIndex] = c
                    cIndex += 1

        return cIndex
