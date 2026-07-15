class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        max_sum = 0
        while left < right:
          sum = nums[left] + nums[right]
          max_sum = max(max_sum, sum)
          left += 1
          right -= 1
        return max_sum
