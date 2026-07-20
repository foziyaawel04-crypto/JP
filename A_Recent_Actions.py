import sys
def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        p = list(map(int, sys.stdin.readline().split()))
        seen = set()
        ans = [-1] * n
        pointer = n - 1
        for i in range(m):
            if p[i] not in seen:
                seen.add(p[i])
                ans[pointer] = i + 1
                pointer -= 1
                if pointer < 0:
                    break
        print(*ans)


if __name__ == "__main__":
    solve()            
