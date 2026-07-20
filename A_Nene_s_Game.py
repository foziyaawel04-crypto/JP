import sys

def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        k, q = map(int, sys.stdin.readline().split())
        a = list(map(int,sys.stdin.readline().split()))
        n = list(map(int,sys.stdin.readline().split()))
        ans = [min(x, a[0] - 1) for x in n]
        print(*ans) 


if __name__ == "__main__":
    solve() 