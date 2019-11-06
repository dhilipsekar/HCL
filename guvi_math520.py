n=int(input())
c=0
for i in range(1,n+1):
    x=i
    Reverse = 0    
    while(i > 0):    
        Reminder =  i%10    
        Reverse = (Reverse *10) + Reminder    
        i = i //10
    if(x==Reverse):
        c+=1
print(c)
