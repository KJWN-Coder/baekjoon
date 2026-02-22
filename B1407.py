import sys,math
a,b=map(int,input().split())
answer=b-a
for i in range(1,int(math.log2(b))+3):
    answer+=(2**(i-1))*(b//(2**i)-a//(2**i))
    if(a%(2**i)==0):
        answer+=2**(i-1)
print(answer+1)#이건 옛날에 작성한 코드라 전에 어떻게 했는지 기억이 안난다...
