import sys
def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        for i in range(n):
            row = []
            for j in range(m):
                if (i % 4 in (0, 3) and j % 4 in (0, 3)) or (i % 4 in (1, 2) and j % 4 in (1, 2)):
                    row.append("1")
                else:
                    row.append("0")
            print(" ".join(row))
if __name__ == '__main__':
    solve()          

