n,k=map(int,input().split())
l=list(map(int,input().split()))
c=-1
for i in range(n):
    if(l[i]==k):
        c+=1
print(c)
