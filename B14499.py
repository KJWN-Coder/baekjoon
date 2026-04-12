import sys
input=sys.stdin.readline#입력 줄이 유동적이니 입력 속도 증가
h,w,y,x,k=map(int,input().split())
map_=[list(map(int,input().split())) for _ in range(h)]
dice_idx=[1,6,3,4,2,5]#각각 윗면,아랫면,오른쪽면,왼쪽면,앞면,뒷면의 인덱스
dice=[0,0,0,0,0,0]
def move_N():
    global x,y,dice,dice_idx
    if(y==0):
        return
    dice_idx=[dice_idx[-1],dice_idx[-2],dice_idx[2],dice_idx[3],dice_idx[0],dice_idx[1]]#굴러간 것 표현
    x,y=x,y-1
    if(map_[y][x]):#굴러간 데에 0이 아닌 숫자가 있다면:
        dice[dice_idx[1]-1]=map_[y][x]#주사위의 아랫면에 그 수를 복사하고
        map_[y][x]=0#굴러간 데의 숫자는 0으로 만든다.
    else:
        map_[y][x]=dice[dice_idx[1]-1]
    print(dice[dice_idx[0]-1])
def move_S():
    global x,y,dice,dice_idx
    if(y==h-1):
        return
    dice_idx=[dice_idx[-2],dice_idx[-1],dice_idx[2],dice_idx[3],dice_idx[1],dice_idx[0]]#굴러간 것 표현
    x,y=x,y+1
    if(map_[y][x]):
        dice[dice_idx[1]-1]=map_[y][x]
        map_[y][x]=0
    else:
        map_[y][x]=dice[dice_idx[1]-1]
    print(dice[dice_idx[0]-1])
def move_E():
    global x,y,dice,dice_idx
    if(x==w-1):
        return
    dice_idx=[dice_idx[3],dice_idx[2],dice_idx[0],dice_idx[1],dice_idx[-2],dice_idx[-1]]#굴러간 것 표현
    x,y=x+1,y
    if(map_[y][x]):
        dice[dice_idx[1]-1]=map_[y][x]
        map_[y][x]=0
    else:
        map_[y][x]=dice[dice_idx[1]-1]
    print(dice[dice_idx[0]-1])
def move_W():
    global x,y,dice,dice_idx
    if(x==0):
        return
    dice_idx=[dice_idx[2],dice_idx[3],dice_idx[1],dice_idx[0],dice_idx[-2],dice_idx[-1]]#굴러간 것 표현
    x,y=x-1,y
    if(map_[y][x]):
        dice[dice_idx[1]-1]=map_[y][x]
        map_[y][x]=0
    else:
        map_[y][x]=dice[dice_idx[1]-1]
    print(dice[dice_idx[0]-1])
moves=list(map(int,input().split()))
for move in moves:#동쪽은 1,서쪽은 2,북쪽은 3,남쪽은 4로
    if(move==1):
        move_E()#함수 실행
    elif(move==2):
        move_W()
    elif(move==3):
        move_N()
    else:
        move_S()
