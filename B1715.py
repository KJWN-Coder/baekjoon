import heapq
import sys
input=sys.stdin.readline#입력 속도 증가
que=[]
n=int(input())
for _ in range(n):
    heapq.heappush(que,int(input()))#큐에 카드 묶음 넣기
answer=0
while len(que)>1:
    ans=heapq.heappop(que)#최소와
    ans+=heapq.heappop(que)#두번째로 최소를 더해서
    answer+=ans#실제 정답에 더하고
    heapq.heappush(que,ans)#그걸 큐에 다시 넣기
print(answer)
