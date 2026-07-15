import sys

def solve():
    n = int(sys.stdin.readline().strip())
    c_passengers = 0
    max_capacity = 0
    for _ in range(n):
        ai, bi = map(int, sys.stdin.readline().split())
        c_passengers += bi-ai
        max_capacity = max(max_capacity,c_passengers )
    print(max_capacity) 
if __name__ == '__main__':
    solve()