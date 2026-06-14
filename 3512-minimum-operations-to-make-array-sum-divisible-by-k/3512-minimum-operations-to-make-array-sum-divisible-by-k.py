class Solution:
    def minOperations(self, nums: List[int], k: int):
       total_sum = sum(nums)
       remainder = total_sum % k
       return remainder



    
        