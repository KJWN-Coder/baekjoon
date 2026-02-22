import math
G=int(input())
ans=[]
if(G%2==0):#When G is even:
    for i in range(2,2+int(math.sqrt(G))-int(math.sqrt(G))%2,2):
        if(G-i**2)%(2*i)==0 and (i+(G-i**2)//(2*i))**2!=G:
            ans.append(i+(G-i**2)//(2*i))#append available numbers in ans
else:#When G is odd
    for i in range(1,3+int(math.sqrt(G))-int(math.sqrt(G))%2,2):
        if(G-i**2)%(2*i)==0 and (i+(G-i**2)//(2*i))**2!=G:
            ans.append(i+(G-i**2)//(2*i)))#append available numbers in ans
ans=ans[::-1]#sort ans
if(ans):
    for a in ans:
        print(a)
else:
    print(-1)
