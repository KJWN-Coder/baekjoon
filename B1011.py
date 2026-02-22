import sys
input=sys.stdin.readline
n=int(input())
li=[]
for i in range(n):
    m=list(map(int,input().split()))
    li.append(m[1]-m[0])
for x in li:
    i=1
    y=0
    if(x==0):
        print(0)
    else:
        while True:
            if(i==1):
                y=1
            elif(i==2):
                y=2
            elif(i%2==0):
                y=((i//2)*((i//2)+1))
            else:
                y=((i//2)*((i//2)+1))+(i+1)//2
            if(x<=y):
                break
            else:
                i+=1
        print(i)#얘도 옛날에 쓴 코드라서 어떻게 풀었는지 잘 기억이 안난다...
