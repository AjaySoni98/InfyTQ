def repeatedString(s, n):
    length_of_string=len(s)
    number_of_a_in_the_string=s.count('a')
    mod=n%length_of_string
    if(mod==0):
        return int(number_of_a_in_the_string*(n/length_of_string))
    else:
        extra_string=s[:mod]
        extra_a=extra_string.count('a')
        return int((number_of_a_in_the_string*(n//length_of_string))+extra_a)
    
s=str(input("Enter a lower case string : "))
n=int(input("Enter the length upto which we have to count number of a's : "))
res=repeatedString(s, n)
print("Number of a's =",res)