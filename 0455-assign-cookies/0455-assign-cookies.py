class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        s.sort()
        g.sort()
        greed = 0
        cookie = 0
        while greed < len(g) and cookie < len(s):
            if s[cookie] >= g[greed]:
                count += 1
                greed += 1
            cookie += 1
        return(count)

        