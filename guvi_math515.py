n=int(input())
l=input().split()
x=len(l)
d=[]
m=[]
y=[]
for i in range(0,x,3):
    d.append(l[i])
for j in range(1,x,3):
    m.append(l[j])
for k in range(2,x,3):
    y.append(l[k])
print(d)
print(m)
print(y)
