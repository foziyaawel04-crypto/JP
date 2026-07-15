import sys
def solve():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        n = int(sys.stdin.readline().strip())
        row_1 = sys.stdin.readline().strip()
        row_2 = sys.stdin.readline().strip()
        possible = True
        for i in range(n):
            if (row_1[i] == "R" and row_2[i] != "R") or (row_2[i] == "R" and row_1[i] != "R"):
                possible = False
                break     
        if possible:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()