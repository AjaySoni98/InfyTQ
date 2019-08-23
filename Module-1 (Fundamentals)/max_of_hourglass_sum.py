def hourglassSum(arr):
    allsums=[]
    summ=0
    for i in range(4):
        for j in range(4):
            summ=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            allsums.append(summ)
    return(max(allsums))

print("You'll be entering 36 numbers in a 6x6 array.")
arr=[]
inar=[]
m=1
for k in range(6):
    for l in range(6):
        num=int(input("Enter number "+str(m)+" : "))
        m+=1
        inar.append(num)
    arr.append(inar)
    inar=[]
res=hourglassSum(arr)
print("The Highest Hourglass-sum is :",res)