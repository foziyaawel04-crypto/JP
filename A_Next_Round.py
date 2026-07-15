import sys
def solve():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    no_p_adv = 0
    k_score = a[k - 1]
    for i in range(n):
        if a[i] >= k_score and a[i] > 0:
             no_p_adv += 1
        else:
            break
    print(no_p_adv)
if __name__ == "__main__":
    solve()
