
import sys

def solve():
    num = int(sys.stdin.readline().strip())
    for i in range(1, num + 1):
        if i % 2 == 0:
          sum = num // 2
        else:
          sum = -(num + 1) // 2
    print(sum)
if __name__ == '__main__':
    solve()

