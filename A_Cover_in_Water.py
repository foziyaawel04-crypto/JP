import sys
def solve():
    t = int(sys.stdin.readline().strip())
    
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        s = sys.stdin.readline().strip()
        count = 0
        if "..." in s:
            count = 2
        else:
             for i in range(n):   
                if s[i] == ".":
                    count += 1
        print(count)
if __name__ == "__main__":
    solve()