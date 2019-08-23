#PF-Assgn-52
def sum_of_numbers(list_of_num,filter_func=None):
    summ=0
    if(filter_func==None):
        for number in list_of_num:
            summ+=number
    else:
        list_of_num=filter_func(list_of_num)
        for number in list_of_num:
            summ+=number
    return summ
            

def even(data):
    even_lst=[]
    for number in data:
        if(number%2==0):
            even_lst.append(number)
    return even_lst

def odd(data):
    odd_lst=[]
    for number in data:
        if(number%2!=0):
            odd_lst.append(number)
    return odd_lst

sample_data = range(1,11)

print(sum_of_numbers(sample_data,even))