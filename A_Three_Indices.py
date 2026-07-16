import sys
def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        p = list(map(int, sys.stdin.readline().split()))
        possible = False
        ans = []
        
        for l in range(1,n - 1):
           i = p[l - 1]
           j = p[l]
           k = p[l + 1]
           if i < j and j > k:
              possible = True
              ans = [l, l + 1, l + 2]
              break
        if possible:
          print("YES")
          print(*(ans)) 
        else:
           print("NO")
if __name__ == "__main__":
    solve()           
           
            
        
