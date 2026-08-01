class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        i = 0
        min_r = 0
        for house in houses:
            while i < len(heaters) - 1 and abs(heaters[i + 1] - house) <= abs(heaters[i] - house):
                i += 1
            dist = abs(heaters[i] - house)
            min_r = max(min_r, dist)
        return min_r  