import sys
def solve():
    n, q = map(int, sys.stdin.readline().split())
    p = list(map(int,sys.stdin.readline().split()))
    grid = []
    for i in range(q):
        row = list(map(int, sys.stdin.readline().split()))
        grid.append(row)
    p.sort()
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + p[i]
    for row in grid:
        x = row[0]
        y = row[1]
        ans = pref[n - x + y] - pref[n - x]
        print(ans)
if __name__ == '__main__':
    solve()