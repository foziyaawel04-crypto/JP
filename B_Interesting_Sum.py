import sys
def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        a = list(map(int, sys.stdin.readline().split()))
        a.sort()
        ans = a[n - 1] - a[0] + a[n - 2] - a[1]
        print(ans)
if __name__ == "__main__":
    solve() 