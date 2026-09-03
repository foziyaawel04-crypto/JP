class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        bad_idx = -1
        min_idx = -1
        max_idx = -1
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                bad_idx = i
            if nums[i] == minK:
                min_idx = i
            if nums[i] == maxK:
                max_idx = i
            valid_start = min(min_idx, max_idx)
            if valid_start > bad_idx:
                count += (valid_start - bad_idx)
        return count

