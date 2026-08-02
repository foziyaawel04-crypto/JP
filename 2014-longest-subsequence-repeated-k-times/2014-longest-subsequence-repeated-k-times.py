from collections import Counter, deque
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        counts = Counter(s)
        valid_chars = sorted([char for char in counts if counts[char] >= k])
        def isSubsequence(sub: str) -> bool:
            target = sub * k
            it = iter(s)
            return all(char in it for char in target)
        queue = deque([""])
        ans = ""
        while queue:
            curr = queue.popleft()
            ans = curr
            for char in valid_chars:
                next_str = curr + char
                if isSubsequence(next_str):
                    queue.append(next_str)
        return ans