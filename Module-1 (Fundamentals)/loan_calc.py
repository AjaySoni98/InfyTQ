#PF-Assgn-20

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    accstr=str(account_number)
    
    if(accstr[0]!="1"):
        print("Invalid account number")
    elif(account_balance<100000):
        print("Insufficient account balance")
    elif(salary<25000 or (loan_type!="Car" and loan_type!="House" and loan_type!="Business")):
        print("Invalid loan type or salary")
    else:
        if(salary>25000):
            if(loan_type=="Car"):
                eligible_loan_amount=500000
                bank_emi_expected=36
            elif(loan_type=="House" and salary>50000):
                eligible_loan_amount=6000000
                bank_emi_expected=60
            elif(loan_type=="Business" and salary>75000):
                eligible_loan_amount=7500000
                bank_emi_expected=84
        else:
            print("The customer is not eligible for the loan")
        print("Account number:", account_number)
        print("The customer can avail the amount of Rs.", eligible_loan_amount)
        print("Eligible EMIs :", bank_emi_expected)
        print("Requested loan amount:", loan_amount_expected)
        print("Requested EMI's:",customer_emi_expected)
    
calculate_loan(1005,90000,255000,"Business",7600000,80)