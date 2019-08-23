#PF-Assgn-28


def find_max(num1, num2):
    max_num=-1
    digit=0
    summ=0
    listt=[]
    
    if(num1<num2):
        for number in range(num1,num2+1):
            strnum=str(number)
            if(len(strnum)==2 and number%5==0):
                summ=0
                temp=number
                while(number!=0):
                    digit=number%10
                    summ=summ+digit
                    number=number//10
                if(summ%3==0):
                    listt.append(temp)
    elif(num2<num1):
        return max_num
    if(len(listt)!=0):
        max_num=max(listt)
        return max_num
    else:
        return max_num

max_num=find_max(10,15)
print(max_num)