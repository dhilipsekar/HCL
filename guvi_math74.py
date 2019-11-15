N,K=map(int,input().split())
l=input().split()
z=[]
x=K%N
if(x==0):
    s=" ".join(l)
    print(s)
else:
    d=N-x
    for i in range(d,N):
        z.append(l[i])
    for j in range(d):
        z.append(l[j])
s=" ".join(z)
print(s)
