def fibb(n):
    lst=[0,1]
    t_ele=ele(n)
    a,b=0,1
    while(t_ele!=1):
        c=a+b
        lst.append(c)
        a,b=b,c
        t_ele-=1
    return lst

def ele(n):
    summ=0
    for i in range(1,n+1):
        summ+=i
    return summ

def prow(i):
    global fib_ele, k
    if(i==1 or i==2):
        new_ele=fib_ele[i:]
        for j in range(i):
            if(j>0):
                print(" ", new_ele[j], end=" ")
            else:
                print(new_ele[j], end=" ")
    else:
        for l in range(i-2,i-1):
            k+=l
        m=i
        i=i+k
        new_ele=fib_ele[i:]
        for j in range(m):
            if(j>0):
                print(" ", new_ele[j], end=" ")
            else:
                print(new_ele[j], end=" ")
        
n,k=int(input("Enter number of rows: ")),0
print()
fib_ele=fibb(n)
for i in range(1,n+1):
    prow(i)
    print()
