import sys
def solve():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        n = int(sys.stdin.readline().strip())
        a = list(map(int, sys.stdin.readline().split()))
        a.sort()
        
        possible1 = True
        for s in range(len(a) - 1):
            if  s % 2 == 0 :
              
                if a[s] != a[s + 1]:
                     possible1 = False
                     break
        possible2 = True
        for s in range(len(a) - 1):
            if s % 2 == 1:
                if a[s] != a[s + 1]:
                    possible2 = False
                    break
        
        if possible1 or possible2:
                print("YES")
                    

        else:
                print("NO")
              
        
                 
if __name__ == '__main__':
    solve()                           