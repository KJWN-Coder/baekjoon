import sys
input=sys.stdin.readline#입력 속도 증가
a,b=map(int,input().split())
dp=[0]*(b+1)
for i in range(a):
    w,v=map(int,input().split())
    if(w<=b):
        for j in range(b,0,-1):
            if(j+w<=b and dp[j]!=0):
                dp[j+w]=max(dp[j+w], dp[j]+v)#dp 점화식(아무것도 안한 것과, 아이템을 넣기 전+아이템의 가치 중 더 큰 것을 정함)
        dp[w]=max(dp[w],v)
print(max(dp))
