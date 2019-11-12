n=int(input())
l=input().split()
s1=0
s2=0
for i in range(3):
    s1=s1+int(l[i])
l.reverse()
for j in range(3):
    s2=s2+int(l[j])
if(s1==s2):
    print("1")
else:
    print("0")
