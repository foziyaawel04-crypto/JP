class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        sum_n = 0
        left = 0
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            sum_n = max(sum_n, i - left )
        return sum_n