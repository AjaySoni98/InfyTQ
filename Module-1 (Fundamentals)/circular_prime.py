#PF-Assgn-57
def check_prime(number):
    for i in range(2,number):
        if(number%i==0):
            return False
    return True

def rotations(num):
    lst=[]
    j=len(str(num))
    while(j!=0):
        num=str(num)[-1]+str(num)[:len(str(num))-1]
        lst.append(int(num))
        j-=1
    return lst[::-1]

def get_circular_prime_count(limit):
    count=0
    for number in range(2,limit):
        if(check_prime(number)):
            for rot in rotations(number):
                if(check_prime(rot)!=True):
                    count-=1
                    break
            count+=1
    return count

#Provide different values for limit and test your program
print(get_circular_prime_count(7))