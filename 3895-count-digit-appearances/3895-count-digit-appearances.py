class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
       count = 0
       d = str(digit)
       n = str(nums)
       for i in n:
         n = str(i)
         count += n.count(d)
       return(count)