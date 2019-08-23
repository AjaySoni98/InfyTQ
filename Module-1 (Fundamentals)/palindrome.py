#PF-Assgn-31
def check_palindrome(word):
    
    ulta=""
    for i in range(len(word)-1, -1, -1):
        ulta+=word[i]
    if(word==ulta):
        return True
    else:
        return False
    
status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")