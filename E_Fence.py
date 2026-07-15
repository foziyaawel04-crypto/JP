import sys
def solve():
    n, k = map(int, sys.stdin.readline().split())
    fences = list(map(int, sys.stdin.readline().split()))
    current_sum = sum(fences[:k])
    min_sum = current_sum
    best_index = 1
    for i in range(k, n):
        current_sum = current_sum - fences[i - k] + fences[i]
        if current_sum < min_sum:
            min_sum = current_sum
            best_index = i - k + 2
    print(best_index)
if __name__ == "__main__":
    solve()