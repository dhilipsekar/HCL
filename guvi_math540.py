n=input()
l=list(n)
m=0
j=1
for i in range(len(l)):
    m+=int(l[i])
    j*=int(l[i])
if(m+j==int(n)):
    print("Great")
else:
    print("no")
