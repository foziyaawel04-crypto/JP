class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = 0
        right = len(nums)
        less = []
        equal = []
        above = []
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                above.append(i)
            else:
                equal.append(i)
        return less + equal + above
