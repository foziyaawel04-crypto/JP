import sys

def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        a = list(map(int, sys.stdin.readline().split()))
        
        i = 0

        while i < n - 1 and a[i] <= a[i + 1]:
            i += 1
            
        
        while i < n - 1 and a[i] >= a[i + 1]:
            i += 1
            
        
        if i == n - 1:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()