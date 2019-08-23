#PF-Assgn-46    
def nearest_palindrome(number):
    number+=1
    while(str(number)!=str(number)[::-1]):
        number+=1
    return number
number=0
print(nearest_palindrome(number))