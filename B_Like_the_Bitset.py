import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(input_data[idx])
        k = int(input_data[idx+1])
        s = input_data[idx+2]
        idx += 3
        
        # 1) ተከታታይ የ 1 ቁጥሮች ብዛት መፈተሽ (ከ k ጋር እኩል ወይም የሚበልጥ መሆኑን)
        cnt = 0
        ok = True
        for c in s:
            if c == '1':
                cnt += 1
                if cnt >= k:
                    ok = False
                    break
            else:
                cnt = 0
                
        if not ok:
            out.append("NO")
            continue
            
        out.append("YES")
        
        # 2) ፒርሙቴሽኑን በቅደም ተከተል 1, 2, ... n መጀመር
        ans = list(range(1, n + 1))
        
        # 3) የ '1' ቁጥሮችን ሰንሰለት ለይቶ ያንን ክፍል ብቻ መገልበጥ (Reverse)
        i = 0
        while i < n - 1:
            if s[i] == '1':
                j = i
                while j < n - 1 and s[j] == '1':
                    j += 1
                # ከ i እስከ j ያለውን ክፍል እንገለብጣለን
                ans[i : j + 1] = reversed(ans[i : j + 1])
                i = j
            else:
                i += 1
                
        out.append(" ".join(map(str, ans)))
        
    print("\n".join(out))

if __name__ == '__main__':
    solve()

    
       