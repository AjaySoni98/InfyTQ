#PF-Assgn-42
def find_factors(num):
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return find_largest_prime_factor(factors)

def is_prime(num, i):
    #Accepts the number num and num/2 --> i and returns True if the number is prime ,else returns False
    if(i==1):
        return True
    elif(num%i==0):
        return False;
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    for number in list_of_factors:
        global LAR_PRIME        
        i=number//2
        if(LAR_PRIME==0 and is_prime(number, i)):
            LAR_PRIME=number
        elif(LAR_PRIME!=0 and is_prime(number, i) and LAR_PRIME<number):
            LAR_PRIME=number
    return LAR_PRIME

def find_f(num):
    global LAR_PRIME
    LAR_PRIME=0
    largest_primeF=find_factors(num)
    return largest_primeF
    

def find_g(num):
    global summ
    last=num+8
    while(num<=last):
        summ+=find_f(num)
        num+=1
    return summ

#Note: Invoke function(s) from other function(s), wherever applicable.
LAR_PRIME=0
summ=0
print(find_g(42))