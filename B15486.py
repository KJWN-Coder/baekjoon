import sys
input=sys.stdin.readline#입력 속도 증가
T,P=[0],[0]#time과 price는 나중에 선택할 때 첫번째를 선택하지 않는 경우의 수로 0을 각각 넣어둠
n=int(input())
for i in range(n):
    t,p=map(int,input().split())
    T.append(t)
    P.append(p)#입력 받아서 리스트에 추가
dp=[0]*(n+2)
for i in range(1,n+1):
    dp[i]=max(dp[i],dp[i-1])
    if(i+T[i]<=n+1):
        dp[i+T[i]]=max(dp[i+T[i]],dp[i]+P[i])#dp 점화식(할 수 있는 행동 상담을 받지 않기와 상담을 받고 가치를 더하기 중 가치의 최댓값으로 dp의 값을 갱신)
print(max(dp))
