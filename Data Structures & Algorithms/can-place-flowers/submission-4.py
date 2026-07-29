class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        i = 0

        while i < len(flowerbed):
            # Is Available => (Current Area, Previous Area AND Next Area)
            if (flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0) ):
                flowerbed[i] = 1
                n = n - 1
                i += 1
            
            i += 1
            
            if n < 1:
                return True

        return False
