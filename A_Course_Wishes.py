import sys

def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().strip().split()))
        b = list(map(int, sys.stdin.readline().strip().split()))
        
        ans = []
        count = 0
        possible = True
        
        # በእያንዳንዱ ዙር የኮርሶቹን ብዛት በዲክሽነሪ በትክክል እንይዛለን
        counts = {}
        for level in b:
            counts[level] = counts.get(level, 0) + 1
            
        while min(b) < k:
            moved = False
            
            # 🎯 ከቀኝ ወደ ግራ (ከ n-1 ተነስተን ወደ 0) በሙሉ እንዞራለን
            for j in range(n - 1, -1, -1):
                level = b[j]
                
                # ኮርሱ ገና k ላይ ካልደረሰ እና ማሳደግ የሚቻል ከሆነ
                if level < k:
                    # ሕግ 1፡ የመጨረሻው ቁጥር ከሆነ ወይም በቀኝ ያለው ጎረቤቱ ከሱ የሚበልጥ ከሆነ
                    if j == n - 1 or b[j + 1] > level:
                        # ሕግ 2፡ ወደ ቀጣዩ ደረጃ (level + 1) ሲሄድ የ 'a' ገደብ የማይሞላ ከሆነ
                        # ⚠️ እዚህ ጋር 'level - 1 < len(a)' መሆኑን በማረጋገጥ IndexError ሙሉ በሙሉ ጠፋ!
                        next_count = counts.get(level + 1, 0)
                        if level - 1 < len(a) and next_count < a[level - 1]:
                            # ደረጃውን እናሳድጋለን
                            b[j] += 1
                            counts[level] -= 1
                            counts[level + 1] = counts.get(level + 1, 0) + 1
                            
                            count += 1
                            ans.append(j + 1) # 1-based index ለኮድፎርሰስ
                            moved = True
            
            # በአንድ ሙሉ ዙር አንድም ቁጥር ማሳደግ ካልተቻለ ሉፑ ይቆማል (መልሱ -1 ነው)
            if not moved:
                possible = False
                break
                
        if possible and min(b) == k:
            print(count)
            print(*(ans))
        else:
            print("-1")

if __name__ == "__main__":
    solve()
          
             
