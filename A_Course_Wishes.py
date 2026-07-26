import sys
def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        a = list(map(int,sys.stdin.readline().split()))
        b = list(map(int,sys.stdin.readline().split()))
        ans = []
        count = 0
        target = [k + 1] * n
        if b == target:
           print(count)
           print()
           continue
        level_counts = [0] * (k + 2)
        for lvl in b:
            level_counts[lvl] += 1
        while True:
            moved = False
            for lvl in range(k, 0, -1):
                if lvl == k or level_counts[lvl + 1] < a[lvl - 1]:
                    for i in range(n):
                        if b[i] == lvl:
                           b[i] += 1
                           level_counts[lvl] -= 1
                           level_counts[lvl + 1] += 1
                           ans.append(i + 1)
                           count += 1
                           moved = True
                           break
                if moved:
                     break
            if not moved:
               break   
        print(count)
        print(*(ans)) 
if __name__ == '__main__':
    solve()