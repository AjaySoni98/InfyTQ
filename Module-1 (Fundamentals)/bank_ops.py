#PF-Tryout
'''Here when we do a transaction rather than enquiry 
the results shown are correct, but the balance value doesn't 
change in the real balance_list. Hece, after doing a tranaction 
rather than enquiry if we check the balance using the given function, 
we see that the value is not being changed in the real balance_list.'''

def withdraw(account_number,account_list,balance_list):
    
    flag=None
    for index in range(0,len(account_list)):
        if(account_list[index]==account_number):
            flag=True
            value=index
    if(flag==True):
        balance=balance_list[value]
        new_balance=balance-amount
        if(new_balance >= 500):
            balance_list[value]=new_balance
            bal_change(value, new_balance)
            print("Transaction completed successfully")
            print("Balance Amount :", new_balance)
        else:
            print("Insufficient Balance")
    else:
        print("Invalid Account number")

def deposit(account_number,account_list,balance_list):
    
    flag=None
    for index in range(0,len(account_list)):
        if(account_list[index]==account_number):
            flag=True
            value=index
    if(flag==True):
        balance=balance_list[value]
        new_balance=balance+amount
        balance_list[value]=new_balance
        bal_change(value, new_balance)
        print("Transaction completed successfully")
        print("Balance Amount :", new_balance)
    else:
        print("Invalid Account number")
        
def bal_change(index, balance):
    global balance_list
    balance_list[index]=balance
        
def enq(account_number,account_list,balance_list):
    
    flag=None
    for index in range(0,len(account_list)):
        if(account_list[index]==account_number):
            flag=True
            value=index
    if(flag==True):
        balance=balance_list[value]
        print(balance)
    else:
        print("Invalid Account number")
        
account_list=[1001,1002,1003,1004,1005]
balance_list=[2500,10000,7000,1500,500]
amount=1000
account_number=1003
transaction_type="Balance Enquiry"

if(transaction_type=="Withdraw"):
    withdraw(account_number, account_list, balance_list)
elif(transaction_type=="Deposit"):
    deposit(account_number, account_list, balance_list)
elif(transaction_type=="Balance Enquiry"):
    enq(account_number, account_list, balance_list)
else:
    print("Invalid Transaction Type")