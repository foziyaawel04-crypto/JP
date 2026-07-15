import sys
def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        a = list(map(int,sys.stdin.readline().split()))
        max_a = max(a)
        results = []
        for i in range(m):
          parts = sys.stdin.readline().split()
          sign = parts[0]          
          l = int(parts[1])        
          r = int(parts[2])
          if l<= max_a <= r:
              if sign == "+":
                   max_a += 1 
              else:
                   max_a -= 1 
          results.append(str(max_a))
        print(" ".join(results))  
if __name__ == '__main__':
    solve()
