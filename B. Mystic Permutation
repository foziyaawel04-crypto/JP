import sys
def solve():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        n = int(sys.stdin.readline().strip())
        pi = list(map(int, sys.stdin.readline().split()))
        pj = sorted(pi)
        if n == 1:
            print(-1)
            continue
        for j in range(n - 1):
            if pi[j] == pj[j]:
                pj[j], pj[j + 1] = pj[j + 1], pj[j]
        if pi[n - 1] == pj[n - 1]:
               pj[n - 1], pj[n - 2] = pj[n - 2], pj[n - 1]
        print(*(pj))
if __name__ == '__main__':
    solve()
