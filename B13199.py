import sys
input=sys.stdin.readline#입력 속도 증가
T=int(input())
for _ in range(T):
    p,m,f,c=map(int,input().split())
    ans_s=(m//p)#시작할 때 치킨을 먼저 시킨다.(s는 상언,d는 두영)
    ans_d=0
    coupons=c*(m//p)#시작할 때 먼저 시키며 받은 쿠폰 수
    if(coupons<f):
        pass
    else:
        ans_s+=(c*(m//p)-f)//(f-c)+1#쿠폰 수 계산
    ans_d=m//p+(((m//p)*c)//f)#쿠폰 수 계산2
    print(ans_s-ans_d)
