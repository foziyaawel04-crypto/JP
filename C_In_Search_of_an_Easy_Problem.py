import sys
def solve():
   n = int(sys.stdin.readline().strip())
   n_ans = list(map(int, sys.stdin.readline().strip().split()))
   if 1 in n_ans:
      print("HARD")
   else:
      print("EASY")
if __name__ == '__main__':
   solve()