import sys
def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        s = list(sys.stdin.readline().strip())
        count = 0
        s.sort()
        if n > 0:
            count += 2
        for i in range(n - 1):
            if s[i] != s[i + 1]:
                count += 2
            else:
                count += 1
        print(count)
if __name__ == "__main__":
    solve()
            