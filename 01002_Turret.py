#Baekjoon algorithm
#1002 - Turret
#210113 Joyonclear
             
test_cases_number = int(input())
for i in range(test_cases_number):
    x1,y1,r1,x2,y2,r2 = map(int,input().split(" "))
    dis = ((x1-x2)**2 + (y1-y2)**2)**0.5
    
    if x1==x2 and y1==y2 and r1==r2:
        print(-1)
    elif dis>r1+r2:
        print(0)
    elif dis==r1+r2:
        print(1)
    else:
        if dis<abs(r1-r2):
            print(0)
        elif dis==abs(r1-r2):
            print(1)
        else:
            print(2)