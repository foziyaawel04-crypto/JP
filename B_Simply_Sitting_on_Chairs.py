import sys
def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        pi = list(map(int,sys.stdin.readline().split()))
        mark = "*"
        no_of_sit = 0
        for i in range(n):
            if i + 1 < pi[i]:
                continue
            else :
                mark
                no_of_sit += 1
        print(no_of_sit)
if __name__ == '__main__':
    solve()        
            

