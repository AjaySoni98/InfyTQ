#PF-Tryout
def find_armstrong(number):
    summ=0
    temp=number
    while(number!=0):
        digit=number%10
        number=number//10
        summ+=(digit*digit*digit)
    if(summ==temp):
        return True
    return False

number=371
if(find_armstrong(number)):
    print(number,"is an Armstrong number")
else:
    print(number,"is not an Armstrong number")