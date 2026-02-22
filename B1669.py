a,b=map(int,input().split())
x=b-a
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
    print(i)#이거도 옛날에 풀어서 어떻게 풀었는지 기억이 안 난다...
