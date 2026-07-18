import sys
def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        a = list(map(int, sys.stdin.readline().split()))
        seen = set()
        count = 0
        for i in range(n - 1, -1, -1):
            if a[i] in seen:
                count = i + 1
                break
            seen.add(a[i])
        print(count)
if __name__ == "__main__":
    solve()
