n=input()
l=list(n)
l1=[]
for i in range(len(l)):
    if(int(l[i])%2!=0):
        l1.append(l[i])
if(len(l1)==0):
    print("-1")
else:
    s=" ".join(l1)
    print(s)
