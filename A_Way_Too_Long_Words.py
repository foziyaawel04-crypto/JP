n = int(input())
for i in range (n):
   long_word = input()
   if len(long_word) > 10:
    print (long_word[0] + str(len(long_word)-2) + long_word[-1])
   else:  
     print(long_word)=