import sys

def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        h, m = map(int, sys.stdin.readline().split())
        ans = 24 * 60 - h * 60 - m
        print(ans)
if __name__ == "__main__":
    solve()        