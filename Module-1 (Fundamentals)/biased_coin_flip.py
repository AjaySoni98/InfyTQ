import random
i=1
h,t=0,0
n=1000
while(i<=n):
    if((random.randint(1,(n+1)))<=7*(n/10)):
        h+=1
    else:
        t+=1
    i+=1
print((h/n)*100)