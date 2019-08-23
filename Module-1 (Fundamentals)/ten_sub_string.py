#PF-Assgn-41
lst=[]
j=1
def find_ten_substring(num_str):
    global lst
    global j
    global length
    summ=0
    strr=""
    while(length!=0):
        length-=1
        for i in range(len(num_str)):
            summ+=int(num_str[i])
            strr+=num_str[i]
            if(summ==10):
                lst.append(strr)
        find_ten_substring(num_str[j:])
        j+=1
    return lst

num_str="2825302"
length=len(num_str)
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)