import sys

def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n, q = map(int, sys.stdin.readline().split())
        a = list(map(int,sys.stdin.readline().split()))
        total_sum = []
        initial_sum = sum(a)
        pref = [0] * (n + 1)
        for i in range(n):
                 pref[i+1] = pref[i] + a[i]
        for i in range(q):
            l, r, k_val = map(int, sys.stdin.readline().split())
            old_range_sum = pref[r] - pref[l-1]
            new_range_sum = (r - l + 1) * k_val
            total_sum = initial_sum - old_range_sum + new_range_sum
            if total_sum % 2 != 0:
                   print("YES")
            else:
                   print("NO")
if __name__ == '__main__':
    solve()

