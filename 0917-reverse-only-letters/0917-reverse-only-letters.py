class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        word = list(s)
        left = 0
        right = len(word) - 1
        while left < right:
            if not word[left].isalpha():
                left += 1
            elif not word[right].isalpha():
                right -= 1
            else:
                word[left], word[right] = word[right], word[left]
                left += 1
                right -=1
            
        return "".join(word)
        