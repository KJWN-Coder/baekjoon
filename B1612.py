import math
a=int(input())
b=a%10#a의 1의 자리수
if(b==2 or b==4 or b==5 or b==6 or b==8 or b==0):
    print(-1)#1의 자리수가 2,4,5,6,8,0인 경우 배수의 1의 자리수가 1이 될 수 없기 때문에 -1 출력 후 프로그램 종료
    exit()
i=int('1'*len(str(a)))#목표 숫자
l=len(str(a))
while True:
    if(i%a==0):
        print(l)#a의 배수 중 i가 있는 경우 출력 후 break
        break
    else:
        i=(i*10+1)%a
        l+=1#아닌 경우 i의 길이를 늘림
