class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for r in image:
            left = 0
            right = len(r) - 1
            while left <= right:
                r[left], r[right] = 1 - r[right], 1 - r[left]
                left += 1
                right -= 1
        return image