class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        current_max = float('-inf')
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            current_max = max(current_max, nums[i][0])
        best_range = [float('-inf'), float('inf')]
        while min_heap:
            val, list_idx, elem_idx = heapq.heappop(min_heap)
            if current_max - val < best_range[1] - best_range[0]:
                best_range = [val, current_max]
            if elem_idx + 1 == len(nums[list_idx]):
                break
            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, elem_idx + 1))
            current_max = max(current_max, next_val)
        return best_range
        