n=int(input())
Tree={}
class Node:
    def __init__(self,childs):
        self.childs=childs
parent_li=list(map(int,input().split()))
for idx in range(len(parent_li)):
    Tree[idx]=Node(set())
for idx,p in enumerate(parent_li):
    if(p!=-1):
        Tree[p].childs.add(idx)
d_idx=int(input())
def dfs(d):
    for c in list(Tree[d].childs):
        dfs(c)
    if(parent_li[d]!=-1):
        Tree[parent_li[d]].childs.remove(d)
    del Tree[d]
dfs(d_idx)
ans=0
for key in Tree.keys():
    if(len(Tree[key].childs)==0):
        ans+=1
print(ans)