
import sys

def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        a = list(map(int, sys.stdin.readline().split()))
        a.sort()
        blue_sum = a[0] + a[1]
        red_sum = a[-1]
        left = 2
        right = n - 2
        possible = False
        while left < right:
            if red_sum > blue_sum:
                possible = True
                break
            blue_sum += a[left]
            left += 1
            red_sum += a[right]
            right -= 1
        
        if red_sum > blue_sum:
            possible = True
            
        if possible:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()