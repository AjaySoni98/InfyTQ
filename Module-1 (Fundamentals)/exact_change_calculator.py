#PF-Assgn-16
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    a=0
    
    if((5*no_of_five+no_of_one)<rupees_to_make):
        print("Cannot produce exact change!")
    else:
        five_needed=int(rupees_to_make/5)
        one_needed=rupees_to_make - (5*five_needed)
        if(no_of_five>=five_needed and no_of_one>=one_needed):
            if(rupees_to_make%5==0):
                one_needed=0
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", one_needed)
        elif(no_of_five<five_needed):
            a=(five_needed - no_of_five)*5
            if(no_of_one>=a):
                five_needed=no_of_five
                one_needed=rupees_to_make-(5*five_needed)
                print("No. of Five needed :", five_needed)
                print("No. of One needed  :", one_needed)
            else:
                print("Cannot produce exact change!")
        else:
            print("Cannot produce exact change!")

#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
amount=int(input("Enter amount of rupees to make : "))
fives=int(input("Enter number of five rupees coins : "))
ones=int(input("Enter number of one rupee coins : "))
make_amount(amount,fives,ones)