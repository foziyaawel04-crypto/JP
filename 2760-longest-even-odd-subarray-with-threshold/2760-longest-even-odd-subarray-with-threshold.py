class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        max_length = 0
        left = 0
        right = len(nums)
        while left < right:
            if nums[left] % 2 == 0 and nums[left] <= threshold:
                r = left
                while r + 1 < right:
                    if nums[r + 1] <= threshold and nums[r + 1] % 2 != nums[r] % 2:
                        r += 1
                    else:
                        break
                max_length = max(max_length, r - left + 1)
                left = r + 1
            else:
                left += 1
        return max_length
    