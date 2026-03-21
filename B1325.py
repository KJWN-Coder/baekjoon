import sys
from collections import deque
input=sys.stdin.readline#입력 속도 증가
n,m=map(int,input().split())
graphs=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graphs[b].append(a)#신뢰 여부 저장
ans=[]
ans_n=0
ans_dic={}
for i in range(1,n+1):#BFS
    num=1
    queue=deque()
    queue.append(i)
    visited=[0]*(n+1)
    visited[i]=1
    while(queue):
        for _ in range(len(queue)):
            v=queue.popleft()
            for j in graphs[v]:
                if(not visited[j]):
                    visited[j]=1
                    num+=1
                    queue.append(j)
    if num not in ans_dic:
        ans_dic[num]=[]
    ans_dic[num].append(i)
    if(ans_n<=num):
        ans_n=num
print(*ans_dic[ans_n])
