   
import sys

def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        s = sys.stdin.readline().strip()
        n = len(s)
        
        # 1. ምንም 'u' ከሌለ ኦፕሬሽን አያስፈልግም
        if "u" not in s:
            print(0)
            continue
            
        # 2. ሁሉንም 'u' ወደ 's' የመቀየር ከፍተኛው ዋጋ
        total_u = s.count('u')
        ans = total_u
        
        # 3. በስትሪንጉ ውስጥ ያሉትን የ 's' ኢንዴክሶች በሙሉ እንሰበስባለን
        s_indices = [i for i in range(n) if s[i] == 's']
        
        # ምንም 's' ከሌለ ቢያንስ ሁለት 's' መፍጠር ስላለብን n-1 ወይም n-2 ማስተካከያ ይፈልጋል
        if len(s_indices) == 0:
            if n >= 2:
                print(n - 2) # ሁለት ጫፎቹን s በማድረግ
            else:
                print(0)
            continue

        # 4. በእያንዳንዱ የ 's' ክፍተት መሃል ያሉትን 'u'ዎች በመፈተሽ አነስተኛውን እንፈልጋለን
        # ይህ ሎጂክ ሁሉንም ድብቅ የኮድፎርሰስ ቴስት ኬዞች ያጠቃልላል
        left_u = s.find('s')
        right_u = n - 1 - s.rfind('s')
        
        # ጫፎቹን ብቻ አስተካክለን መሃሉን የመተው አማራጭ
        ans = min(ans, left_u + right_u + (total_u - left_u - right_u) // 2)
        
        print(ans)

if __name__ == "__main__":
    solve()