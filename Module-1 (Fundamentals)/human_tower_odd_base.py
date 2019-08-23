#PF-Exer-32

def human_pyramid(no_of_people):
    weight=0
    while(no_of_people>0):
        weight+=no_of_people*50
        no_of_people-=2
    return weight

def find_maximum_people(max_weight):
    no_of_people=1
    cur_weight=human_pyramid(no_of_people)
    while(cur_weight<max_weight):
        no_of_people+=2
        cur_weight=human_pyramid(no_of_people)
    if(cur_weight==max_weight):
        return no_of_people
    else:
        return no_of_people-2

#Provide different values for max_weight and test your program
max_people=find_maximum_people(1000)
print(max_people)