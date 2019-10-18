l=input().split()
n=len(l)
l1=[]
for i in range(n):
    l1.append(l[-1])
    del l[-1]
s=" ".join(l1)
print(s)
