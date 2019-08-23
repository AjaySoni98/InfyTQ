#PF-Assgn-39
#This verification is based on string match.     

#Global variables
menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,250,3]

'''This method accepts the item followed by the quantity required 
by a customer in the format item1, quantity_required, item2, quantity_required etc.'''
def place_order(*item_tuple):
    
    global menu
    for i in range(0, len(item_tuple), 2):
        item=item_tuple[i]
        quantity=item_tuple[i+1]
        if item not in menu:
            print(item,"is not available")
        else:
            index=menu.index(item)
            check_quantity_available(index, quantity)
    
'''This method accepts the index position of the item requested by 
the customer in the quantity_available list, and the requested quantity of the item.'''
def check_quantity_available(index,quantity_requested):
    
    global quantity_available
    global menu
    q_available=quantity_available[index]
    if(q_available<quantity_requested):
        print(menu[index],"stock is over")
    else:
        quantity_available[index]=quantity_available[index]-quantity_requested
        print(menu[index],"is available")
    
place_order("Veg Roll",2,"Noodles",250,"Chai", 2,"Soup",4)

    #print("<item name>is not available")
    #print("<item name>stock is over")
    #print ("<item name>is available")