class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        ransomNoteChar, magazineChar = {}, {}

        for c in ransomNote:
            ransomNoteChar[c] = ransomNoteChar.get(c, 0) + 1

        for c in magazine:
            magazineChar[c] = magazineChar.get(c, 0) + 1

        for char, count in ransomNoteChar.items():
            if count > magazineChar.get(char, 0):
                return False

        return True
