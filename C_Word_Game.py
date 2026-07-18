import sys
def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        guy1 = sys.stdin.readline().split()
        guy2 = sys.stdin.readline().split()
        guy3 = sys.stdin.readline().split()
        guy1_count = 0
        guy2_count = 0
        guy3_count = 0
        set1 = set(guy1)
        set2 = set(guy2)
        set3 = set(guy3)
        for i in range(n):
           if guy1[i] in set2 and guy1[i] in set3:
                pass 
           elif guy1[i] in set2 or guy1[i] in set3:
                guy1_count += 1 
           else:
                guy1_count += 3
           if guy2[i] in set1 and guy2[i] in set3:
                pass
           elif guy2[i] in set1 or guy2[i] in set3:
                guy2_count += 1
           else:
                guy2_count += 3
           if guy3[i] in set1 and guy3[i] in set2:
                pass
           elif guy3[i] in set1 or guy3[i] in set2:
                guy3_count += 1
           else:
                guy3_count += 3 
        print(guy1_count, guy2_count, guy3_count)
if __name__ == "__main__":
    solve()       

