#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    cpp=0
    cof=0
    #write your logic here
    if(quantity_ordered!=0 and distance_in_kms!=0 and (food_type=="N" or food_type=="V")):
        if(food_type=="V"):
            cpp=120
        elif(food_type=="N"):
            cpp=150
        cof=cpp*quantity_ordered
        if(distance_in_kms<=3):
            cod=0
        elif(3<distance_in_kms<=6):
            cod=(distance_in_kms-3)*3
        elif(distance_in_kms>6):
            cod=9+((distance_in_kms-6)*6)
        bill_amount=cof+cod
        return bill_amount
    else:
        return "N/A"

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,10)
print(bill_amount)