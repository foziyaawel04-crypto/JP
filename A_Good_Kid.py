import sys
def solve():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        n = int(sys.stdin.readline().strip())
        a = list(map(int, sys.stdin.readline().split()))
        a.sort()
        a[0] += 1
        product = 1
        for num in a:
            product *= num  
        print(product)
if __name__ == '__main__':
    solve()