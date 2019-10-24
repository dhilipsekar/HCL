n,s=map(int,input().split())
l=list(map(int,input().split()))
for i in range(n):
    if(l[i]==s):
        print("yes")
        break
else:
    print("no")
