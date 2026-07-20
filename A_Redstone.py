import sys
def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        a = list(map(int, sys.stdin.readline().split()))
        if len(a) != len(set(a)):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve() 