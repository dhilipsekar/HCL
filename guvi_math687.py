n=int(input())
l=input().split()
rep=[]
x=1000
for i in range(n):
    c=0
    for j in range(n):
        if(l[i]==l[j] and i!=j):
            c+=1
    if(c<=x):
        x=c
        rep.append(l[i])
ans=list(set(rep))
ans=sorted(ans)
ans=ans[::-1]
s=" ".join(ans)
print(s)
