a1,a2=map(int,input().split())
b1,b2=map(int,input().split())
c1,c2=map(int,input().split())
d1,d2=map(int,input().split())
if(a2==b1 and b2==c1 and c2==d1 and d2==a1):
    print("yes")
else:
    print("no")
