class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')
        n = len(nums) 
        for k in range(l, r + 1):
            cur_sum = sum(nums[:k])
            if cur_sum > 0:
                min_sum = min(min_sum,cur_sum)
            for i in range(k, n):
                cur_sum += nums[i] - nums[i - k]
                if cur_sum > 0: 
                    min_sum = min(min_sum,cur_sum)
        if min_sum != float('inf'):
            return min_sum
        else:
            return -1  
