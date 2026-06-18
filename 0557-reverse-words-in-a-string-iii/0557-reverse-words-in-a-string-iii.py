class Solution:
    def reverseWords(self, s: str) -> str:
        word = list(s)
        left = 0
        for  right in range(len(word) + 1):
            if right ==len(word) or word[right] == " ":
                start = left
                end = right - 1
                while start < end:
                    word[start], word[end] = word[end], word[start]
                    start += 1
                    end -=1
                left = right + 1
        return "".join(word)