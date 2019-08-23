#PF-Exer-26

def factorial(number):
    
    fact=1
    if(number==0):
        return 1
    else:
        while(number!=0):
            fact=fact*number
            number-=1
        return fact

def find_strong_numbers(num_list):
    
    strong_nos=[]
    for i in range(len(num_list)):
        digit=0
        summ=0
        factt=0
        numb=num_list[i]
        temp=numb
        while(numb!=0):
            digit=numb%10
            factt=factorial(digit)
            summ+=factt
            numb=numb//10
        if(summ==temp and temp!=0):
            strong_nos.append(temp)
    return strong_nos

num_list=[1, 2, 3, 4, 145, 230, 40585, 0]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)