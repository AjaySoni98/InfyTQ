def jumpingOnClouds(c):
    i=0
    jump=0
    while(i<=len(c)-3):
        if(c[i+2]==0):
            jump+=1
            i+=2
        else:
            jump+=1
            i+=1
    if(i==len(c)-1):
        return(jump)
    else:
        return(jump+1)
    
n=int(input("Enter the Number of Clouds : "))
c=[]
for j in range(n):
    m=int(input("0/ 1 ? : "))
    c.append(m)
res=jumpingOnClouds(c)
print("Number of jumps required are :",res)