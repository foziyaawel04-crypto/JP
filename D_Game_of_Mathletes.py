import sys
def solve():   
     itr = int(sys.stdin.readline().strip())
     for i in range(itr):
          n, m = map(int, sys.stdin.readline().strip().split())
          a = list(map(int, sys.stdin.readline().strip().split()))
          a.sort()
          
          sum = 0
          left = 0
          right = n - 1
          
          while left < right:
               current_sum = a[left] + a[right]
               if current_sum == m:
                    sum += 1      
                    left += 1     
                    right -= 1    
               elif current_sum < m:
                    left += 1     
               else:
                    right -= 1    
                    
          print(sum)

if __name__ == '__main__':
   solve()

