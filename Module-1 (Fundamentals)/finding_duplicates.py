#PF-Assgn-44
def find_duplicates(list_of_numbers):
    done=[]
    lst=[]
    for x in list_of_numbers:
        if(list_of_numbers.count(x)>1 and x not in done):
            lst.append(x)
            done.append(x)
    return lst

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)