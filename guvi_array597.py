n=int(input())
a=input().split()
a=[int(i) for i in a]
s=0
for i in range(n):
    s+=a[i]

if(s%2==0 and s%3==0 and s%5==0):
    print("1")
else:
    print("0")
