n=int(input())
l=input().split()
l=[int(x) for x in l]
k=[]
for i in range(n):
    c=0
    for j in range(n):
        if(l[i]==l[j]):
            c+=1
    if(c==2):
        k.append(l[i])
m=set(k)
str1 = ' '.join(str(e) for e in m)
print(str1)
        
