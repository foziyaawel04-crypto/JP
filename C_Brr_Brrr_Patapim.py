import sys
def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        grid = []
        seen = set()
        for i in range(n):
            row = list(map(int, sys.stdin.readline().split()))
            grid.append(row)
            for num in row:
               seen.add(num)
        P1 = 0
        for num in range(1, 2 * n + 1):
            if num not in seen:
              P1 = num
              break
        P = [P1]
        for j in range(n):
            P.append(grid[0][j])
        for i in range(1, n):            
            P.append(grid[i][n - 1])    
        print(*P)
if __name__ == '__main__':
    solve()                  