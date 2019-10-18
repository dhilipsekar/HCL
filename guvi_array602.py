n=int(input())
l=input().split()
l=list(map(int,l))
p=l[0]
for i in range(n):
    if(l[i]>=p):
        p=l[i]
        x=i
for j in range(n):
    if(l[j]<=p):
        p=l[j]
        y=j
print(x-y)
    
