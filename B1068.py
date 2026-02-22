n=int(input())
Tree={}
class Node:#트리에 쓸 노드 클래스 정의
    def __init__(self,childs):
        self.childs=childs
parent_li=list(map(int,input().split()))
for idx in range(len(parent_li)):
    Tree[idx]=Node(set())
for idx,p in enumerate(parent_li):
    if(p!=-1):
        Tree[p].childs.add(idx)#루트 노드의 부모 노드는 없으니까 루트 노드를 제외한 모든 노드의 자식 노드에 이 노드를 추가
d_idx=int(input())
def dfs(d):
    for c in list(Tree[d].childs):
        dfs(c)#d번 노드의 자식 노드 모두 샂게
    if(parent_li[d]!=-1):
        Tree[parent_li[d]].childs.remove(d)#부모 노드에서 이 노드 제거
    del Tree[d]#트리에서 이 노드 제거
dfs(d_idx)
ans=0
for key in Tree.keys():
    if(len(Tree[key].childs)==0):#리프 노드일때
        ans+=1#ans에 1 추가
print(ans)
