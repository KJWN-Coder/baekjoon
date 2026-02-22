import sys
input=sys.stdin.readline#입력 속도 증가
n,k=map(int,input().split())
coins=[int(input()) for _ in range(n)]
dp=[float('inf')]*(k+1)
dp[0]=0
for coin in coins:
    try:
        dp[coin]=1#coin원은 1개의 동전만으로 계산 가능
    except:
        pass
for i in range(min(coins)+1,k+1):
    for coin in coins:
        if(i-coin>=0 and dp[i-coin]!=float('inf')):
            dp[i]=min(dp[i],dp[i-coin]+1)#dp의 점화식
if(dp[k]!=float('inf')):
    print(dp[k])
else:
    print(-1)
