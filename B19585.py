import sys
input=sys.stdin.readline#입력 속도 증가
n,m=map(int,input().split())
min_col=sys.maxsize#색깔 텍스트의 최소 길이 변수
min_name=sys.maxsize#닉네임 텍스트의 최소 길이 변수
colors={}#dict자료형에서는 get() 함수가 O(1)에 실행되므로 dict로 표현
for _ in range(n):
    color=input().rstrip()
    colors[color]=1
    min_col=min(min_col,len(color))#색깔 텍스트의 최소 길이
names={}#colors={}와 동일
for _ in range(m):
    name=input().rstrip()
    names[name]=1
    min_name=min(min_name,len(name))#닉네임 텍스트의 최소 길이 변수
t=int(input())
for _ in range(t):
    nickname=input().rstrip()
    found=False
    for i in range(min_col-1,len(nickname)-min_name+1):#색깔과 닉네임의 분리되는 인덱스의 범위
        color=nickname[:i]
        name=nickname[i:]
        if(colors.get(color,0) and names.get(name,0)):#colors.get(color,0)과 names.get(name,0)으로 존재하는지 O(1)에 확인
            print('Yes')
            found=True
            break
    if(not found):
        print('No')
#첫 플래티넘 3문제
