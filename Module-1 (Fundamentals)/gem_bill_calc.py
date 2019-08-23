#PF-Assgn-23
def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    price=0
    quantity=0
    amount=0
    
    for gem in reqd_gems:
        if gem in gems_list:
            index_in_gems_list=gems_list.index(gem)
            price=price_list[index_in_gems_list]
            index_in_rqd_gem_list=reqd_gems.index(gem)
            quantity=reqd_quantity[index_in_rqd_gem_list]
            amount=price*quantity
            bill_amount=bill_amount+amount
        else:
            bill_amount=-1
            break
    
    return bill_amount

#List of gems available in the store
gems_list=['Amber', 'Aquamarine', 'Opal', 'Topaz']

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[4392, 1342, 8734, 6421]

#List of gems required by the customer
reqd_gems=['Amber', 'Opal', 'Topaz']

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[2, 1, 3]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)