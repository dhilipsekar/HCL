n=input()
l=list(map(int,str(n)))
x=sum(l)
if(x%3==0):
    print("Yes")
else:
    print("Not")
