#Baekjoon algorithm
#1978 - Prime Number
#210114 Joyonclear

a=int(input())
num_list=list(map(int,input().split()))
cnt=0
for i in num_list:
    if i==1:
        continue
    elif i==2:
        cnt+=1
    else:
        cnt+=1
        for j in range(2,i):
            if i%j==0:
                cnt-=1
                break
print(cnt)