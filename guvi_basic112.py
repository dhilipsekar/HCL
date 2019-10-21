n=int(input())
l=list(map(int,input().split()))
s=l[0]
for i in range(1,n):
    s=s|l[1]
print(s)
