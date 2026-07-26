import sys
def solve():
      t = int(sys.stdin.readline().strip())
      for _ in range(t):
         n, k = map(int, sys.stdin.readline().split())
         s = sys.stdin.readline().strip()
         count = 0
         possible = True
         for c in s:
            if c == '1':
                count += 1
                if count >= k:
                    possible = False
                    break
            else:
                count = 0
         if not possible:
            print("NO")
            continue
         print("YES")
         ans = [0] * n
         cur = n
         for i in range(n):
            if s[i] == '0':
                ans[i] = cur
                cur -= 1
         for i in range(n):
            if s[i] == '1':
                ans[i] = cur
                cur -= 1
         print(*ans)
if __name__ == '__main__':
    solve()