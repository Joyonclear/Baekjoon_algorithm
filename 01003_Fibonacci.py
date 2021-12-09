#Baekjoon algorithm
#1003 - Fibonacci
#210113 Joyonclear

# cnt_zero,cnt_one = 0,0
# def fibo(x):
#     global cnt_zero, cnt_one
#     if x == 0:
#         cnt_zero += 1
#         return 0
#     elif x == 1:
#         cnt_one += 1
#         return 1
#     else:
#         return fibo(x-2) + fibo(x-1)

# case_num = int(input())
# for i in range(case_num):
#     N = int(input())
#     fibo(N)
#     print(cnt_zero,cnt_one)
#     cnt_zero,cnt_one = 0,0
    
    
case_num = int(input())
for i in range(case_num):
    N = int(input())
    fibo_list=[]
    if N == 0:
        print(1,0)
    elif N == 1:
        print(0,1)
    else:
        fibo_list = [0,1]
        for i in range(N-1):
            fibo_list.append(fibo_list[-1]+fibo_list[-2])
        print(fibo_list[-2],fibo_list[-1])