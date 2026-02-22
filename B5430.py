import collections
T=int(input())
for _ in range(T):
    func=list(input().rstrip())
    n=int(input())
    s=input()
    if(s=='[]'):
        li=[]
    else:
        li=list(map(int,(s.replace('[','')).replace(']','').split(',')))
    queue=collections.deque()
    for i in li:
        queue.append(i)
    left=False
    error=False
    for f in func:
        if(f=='R'):
            left=not left#마지막에 수열을 뒤집을 지 말지 결정
        elif(f=='D'):
            if(queue):
                if(not left):
                    queue.popleft()#D명령 실행
                else:
                    queue.pop()#D명령 실행
            else:
                error=True#queue에 아무 원소도 없을 경우 에러 발생
                break
    if(error):
        print('error')
    else:
        if(left):
            queue.reverse()
        print('['+','.join(map(str,list(queue)))+']')
    
