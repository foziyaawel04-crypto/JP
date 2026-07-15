import sys

def solve():
    t = int(sys.stdin.readline().strip())
    
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        s = list(sys.stdin.readline().strip())
        
        ans = 0
        for i in range(n - 2, -1, -1):
            if s[i] != s[i + 1]:
                ans += 1
                s[i] = s[i + 1]
                
        print(ans)

if __name__ == "__main__":
    solve()