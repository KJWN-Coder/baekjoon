import sys
input=sys.stdin.readline#입력 속도 증
n=int(input())
li=list(map(int,input().split()))
left=0
right=n-1
a,b=li[0],li[-1]
answer=li[0]+li[-1]
while left<right:#두 포인터
    summary=li[left]+li[right]
    if(abs(summary)<abs(answer)):#summary가 answer보다 0에 가까울 경우 answer 갱신
        answer=summary
        a=li[left]
        b=li[right]
    if(summary==0):#정확히 0이면 바로 정답 출력 후 프로그램 종료
        print(li[left],li[right])
        exit()
    if(summary>0):#0보다 크면 오른쪽을 1칸 왼쪽으로 보냄
        right-=1
    else:#0보다 작으면 왼쪽을 1칸 오른쪽으로 보냄
        left+=1
print(a,b)
