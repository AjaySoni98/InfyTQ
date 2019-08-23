#PF-Assgn-61
import re
def validate_name(name):
    if(len(name)==0 or len(name)>15 or name.isalpha()!=True):
        return False
    else:
        return True

def validate_phone_no(phno):
    if(len(str(phno))!=10 or str(phno).isdigit()!=True or str(phno).count(str(phno)[0])==10):
        return False
    else:
        return True

def validate_email_id(email_id):
    if(re.search(r"^\w+@+gmail|yahoo|hotmail+.com$",email_id)):
        return True
    else:
        return False

def validate_all(name,phone_no,email_id):
    if(validate_name(name)==False):
        print("Invalid Name")
    elif(validate_phone_no(phone_no)==False):
        print("Invalid phone number")
    elif(validate_email_id(email_id)==False):
        print("Invalid email id")
    else:
        print("All the details are valid")


#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9994599998", "tina@hotmail.com")