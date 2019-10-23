n=int(input())
l=input().split()
l=list(map(int,l))
x=l[0]
s=1
for i in range(n):
    if(l[i]<x):
        x=l[i]
        s=i+1
        
print(s,end=" ")
b=1
y=l[0]
for j in range(n):
    if(l[j]>y):
        y=l[i]
        b=i+1
print(b)
