import sys

def solve():
    n, t = map(int, sys.stdin.readline().split())
    books = list(map(int, sys.stdin.readline().split()))
    
    max_books = 0
    left = 0
    current_time = 0
    
    for right in range(n):
        current_time += books[right] 
        while current_time > t:
            current_time -= books[left]
            left += 1
        max_books = max(max_books, right - left + 1)
        
    print(max_books)

if __name__ == '__main__':
    solve()