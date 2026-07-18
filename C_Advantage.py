import sys
def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        s = list(map(int, sys.stdin.readline().split()))
        ans = [0] * n
        sorted_s = sorted(s)
        max_val = sorted_s[-1]   # ያንቺ max(s)
        second_max = sorted_s[-2]
        for i in range(n):
            if max_val == s[i]:
                ans[i] = max_val - second_max
            else:
                ans[i] = s[i] - max_val
        print(*(ans))
if __name__ == "__main__":
    solve()
