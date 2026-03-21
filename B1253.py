n=int(input())#투포인터를 활용한 코드입니다.
li=list(map(int,input().split()))
li.sort()#투포인터를 쓰기 위해 수 정렬
ans=0
for idx,i in enumerate(li):
    left,right=0,n-1
    while left<right:
        if(left==idx):
            left+=1
        elif(right==idx):
            right-=1
        elif li[left]+li[right]==i:
            ans+=1
            break
        elif li[left]+li[right]>i:#합이 답보다 크면 오른쪽 포인터를 왼쪽으로 1칸 이동
            right-=1
        else:#합이 답보다 작으면 왼쪽 포인터를 오른쪽으로 1칸 이동
            left+=1
print(ans)
