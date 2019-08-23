def rotLeft(a, d):
    lst=[]
    for i in range(d,n):
        lst.append(a[i])
    for j in range(d):
        lst.append(a[j])
    return(lst)

n=int(input("Enter length of array : "))
a=[]
for k in range(n):
    a.append(int(input("Enter number : ")))
d=int(input("Enter number of rotations such that 0<=d<=n : "))
res=rotLeft(a, d)
print(res)
