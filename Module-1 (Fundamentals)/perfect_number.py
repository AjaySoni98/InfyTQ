#PF-Assgn-59
def check_perfect_number(number):
    summ=0
    if(number<6):
        return False
    for i in range(1,number):
        if(number%i==0):
            summ+=i
    if(summ==number):
        return True
    else:
        return False

def check_perfectno_from_list(no_list):
    lst=[]
    for number in no_list:
        if(check_perfect_number(number)):
            lst.append(number)
    return lst

perfectno_list=check_perfectno_from_list([18,6,4,2,1,28])
print(perfectno_list)