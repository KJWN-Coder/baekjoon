import sys#한줄씩 띄어있는 이유는 이 코드를 짤 때 모바일 앱에서 코드를 짜고 복붙해서 그런겁니다

input=sys.stdin.readline#입력 속도 증가

sys.setrecursionlimit(10**5)#재귀 최대 깊이가 이 문제에서는 최대 10000까지 늘어나므로 미리 설

s=int(input())

painting=[list(input().rstrip()) for _ in range(s)]

visited=[[0]*s for _ in range(s)]

ans=[0,0]

def dfs_special(x,y):#적록색맹 있는 상태로 판별

    visited[y][x]=1

    dx=[1,-1,0,0]

    dy=[0,0,1,-1]

    for i in range(4):

        nx,ny=x+dx[i],y+dy[i]

        if(painting[y][x]=='R' or painting[y][x]=='G'):#R과 G 동일시

            if(nx<0 or nx>=s or ny<0 or ny>=s or  painting[ny][nx]=='B' or visited[ny][nx]):#

                pass

            else:

                dfs_special(nx,ny)

        else:

            if(nx<0 or nx>=s or ny<0 or ny>=s or  painting[ny][nx]!='B' or visited[ny][nx]):

                pass

            else:

                dfs_special(nx,ny)

def dfs(x,y):#적록색맹 없는 상태로 판별

    visited[y][x]=1

    dx=[1,-1,0,0]

    dy=[0,0,1,-1]

    for i in range(4):

        nx,ny=x+dx[i],y+dy[i]

        if(nx<0 or nx>=s or ny<0 or ny>=s or  painting[ny][nx]!= painting[y][x]or visited[ny][nx]):

            pass

        else:

            dfs(nx,ny)

for y in range(s):

    for x in range(s):

        if(not visited[y][x]):

            dfs(x,y)#지금까지 방문한 적이 없다면 함수 실행

            ans[0]+=1

visited=[[0]*s for _ in range(s)]

for y in range(s):

    for x in range(s):

        if(not visited[y][x]):

            dfs_special(x,y)#지금까지 방문한 적이 없다면 함수 실행

            ans[1]+=1

print(' '.join(map(str,ans)))
