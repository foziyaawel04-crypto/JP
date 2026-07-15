class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
 
           print()
           if target > nums[-1]:
              return(len(nums)) 
           elif target not in nums:
              for i ,num in enumerate(nums):
                  if target < num:
                       return(i)
                    
    
           else:
               return(nums.index(target))