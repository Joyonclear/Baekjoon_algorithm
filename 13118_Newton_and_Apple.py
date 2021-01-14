#Baekjoon algorithm
#13118 - Newton and apple
#210113 Joyonclear

people = input().split(" ")
temp = input().split(" ")
try:
    print(people.index(temp[0])+1)
except:
    print(0)