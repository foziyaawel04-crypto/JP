import sys
def solve():
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    R_status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(n):
           if "L" == s[i]:
             for left in range(10): 
               if R_status[left] == 0:
                 R_status[left] = 1
                 break
           elif "R" == s[i]:
               for right in range(9, -1, -1):
                 if R_status[right] == 0:
                   R_status[right] = 1
                   break
           else:
              room_idx = int(s[i])
              R_status[room_idx] = 0
    print("".join(map(str, R_status)))
if __name__ == "__main__":
    solve()