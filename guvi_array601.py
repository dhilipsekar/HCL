n=int(input())
a=input().split()
a=list(map(int,a))
new_array=[]
for i in range(n):
    if(i%2==0):
        x=max(a)
        new_array.append(x)
        a.remove(x)
    else:
        y=min(a)
        new_array.append(y)
        a.remove(y)
print(new_array)
        
