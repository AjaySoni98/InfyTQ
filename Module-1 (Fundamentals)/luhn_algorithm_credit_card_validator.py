#PF-Assgn-58
def validate_credit_card_number(card_number):
    summ=0
    str_num=str(card_number)[::-1]
    if(len(str_num)<16):
        return False
    for i in range(len(str_num)):
        if(i%2==0):
            summ+=int(str_num[i])
        elif(i%2!=0):
            sumd=0
            for digit in str(int(str_num[i])*2):
                sumd+=int(digit)
            summ+=sumd
    if(summ%10==0):
        return True
    else:
        return False

card_number= 1456734512345698 #4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")