import sys

def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        no = []
        ans = 0
        a = 0
        b = 0
        for i in range(1, n + 1):
            no.append(2 ** i)
        left = 0
        right = n - 1
        a += no[right]
        right -= 1
        while left <= right:
            if left < (n // 2) - 1:
               a += no[left]
            else:
               b += no[left]
            left += 1
        ans = abs(a - b)
        print(ans)
if __name__ == "__main__":
    solve()