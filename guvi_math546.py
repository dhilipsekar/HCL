n=input()
l=list(n)
c=0
m=0
f=0
for i in range(len(l)):
    if(l[i]=='1'):
        c+=1
        f=1
    else:
        c=0
    if(c>m):
        m=c
if(f==0):
    print("-1")
else:
    print(m)
