from itertools import combinations as c
import sys
input = sys.stdin.readline#입력 속도 증가
b,a=map(int,input().split())
l=list(input().split())
answers=[]
for i in c(l,b):
    i=list(i)
    i.sort()
    if('a' in i or 'e' in i or 'i' in i or 'o' in i or 'u' in i):#모음 있는지 검사
        if(len(i)-sum([1 for j in i if j in 'aeiou'])>=2):#그리고 모음이 2개 이상 있는지 검사
            answers.append(''.join(i))
answers.sort()
for answer in answers:
    print(answer)
