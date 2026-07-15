
import sys
def solve():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        n = int(sys.stdin.readline().strip())
        a = list(map(int, sys.stdin.readline().strip().split()))
        for j in range(n):
            a[j] = 100 //a[j]
        a.sort()
        possible = True
        sum = 0
        for k in range(n):
             w = a[k]
             if w <= sum + 1:
                sum += 100
             else:
                possible = False
                break
        if possible:
            print("Yes")
        else:
            print("No")
if __name__ == '__main__':
    solve()