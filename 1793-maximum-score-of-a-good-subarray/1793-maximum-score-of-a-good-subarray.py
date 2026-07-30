class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left = k
        right = k
        min_val = nums[k]
        max_val = []
        score = min_val * (right - left + 1) 
        max_val = [min_val * (right - left + 1)]
        n = len(nums)
        while  left > 0 or right < n - 1:
            left_val = nums[left - 1] if left > 0 else -1
            right_val = nums[right + 1] if right < n - 1 else -1 
            if right_val > left_val:
                right += 1
                min_val = min(min_val, nums[right])
            else:
                left -= 1
                min_val = min(min_val, nums[left])
            score = min_val * (right - left + 1)
            max_val.append(score)
    
        return(max(max_val))