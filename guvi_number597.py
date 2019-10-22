n=int(input())
l=list(map(int,input().split()))
x=sum(l)
if(x%2==0 and x%3==0 and x%5==0):
    print("1")
else:
    print("0")
