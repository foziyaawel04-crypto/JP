       
import sys
def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        a = list(map(int, sys.stdin.readline().split()))
        a.sort()
        i = 0
        move = 0
        while i < n - 1 - move:
            if a[i] == a[i + 1]:
                a.append(a.pop(i + 1))
                move += 1
            else:
               i += 1
        print(*(a))
if __name__ == "__main__":
    solve()