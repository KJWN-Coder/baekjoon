px,py=[],[]#이 문제도 모바일로 풀어서 줄마다 줄바꿈이 되어있고 좀 더 간결하게 푸는 방법이 있을 것 같지만 일단은 이렇게 풀어봤습니다

for _ in range(3):

    x,y=map(int,input().split())

    px.append(x)

    py.append(y)

if(px[0]!=px[1] and px[1]!=px[2]):#모두다 x좌표가 다를떄

    dx1,dx2,dy1,dy2=px[1]-px[0],px[2]-px[1],py[1]-py[0],py[2]-py[1]

    if(dx1*dy2==dx2*dy1):#각도계산

        print(0)

        exit()

    if(dx1*dy2>dx2*dy1):#각도계산

        print(1)

        exit()

    if(dx1*dy2<dx2*dy1):#각도계산

        print(-1)

        exit()

elif(px[0]==px[1]==px[2]):#모두의 x좌표가 같다면 0 출력

    print(0)

elif(px[0]==px[1] and px[1]!=px[2]):#첫번째와 두번째 점의 x좌표가 같다면

    if(px[2]-px[1]>0):#각도 계산

        print(-1)

        exit()

    else:#각도 계산

        print(1)

        exit()

else:#두번째 점과 세번째 점의 x좌표가 같다면

    if(px[1]-px[0]>0):#각도 계산

        print(1)

        exit()

    else:#각도 계산

        print(-1)

        exit()
