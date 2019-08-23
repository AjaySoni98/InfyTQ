#PF-Assgn-55
ticket_list=['AI101:MUM:LON:001', 'AI101:MUM:LON:002', 'SI456:MUM:SIN:145', 'EM456:MUM:DUB:098', 'SI456:MUM:SIN:050', 'SI456:MUM:SIN:051']
def find_passengers_flight(airline_name="AI"):
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[0].startswith(airline_name)):
            count+=1
    return count
def find_passengers_destination(destination):
    des=0
    for i in ticket_list:
        lst=i.split(":")
        if(lst[2]==destination):
            des+=1
    return des
def find_passengers_per_flight():
    alines=[]
    final=[]
    done=[]
    for i in ticket_list:
        lst=i.split(":")
        alines.append(lst[0])
    for fno in alines:
        if fno not in done:
            done.append(fno)
            unit=fno+":"+str(alines.count(fno))
            final.append(unit)
    return final
def sort_passenger_list():
    prev_list=find_passengers_per_flight()
    order=[]
    new=[]
    for fpair in prev_list:
        order.append(fpair[6])
        order.sort(reverse=True)
    for x in order:
        for fpair in prev_list:
            if(fpair[6]==x):
                new.append(fpair)
    return new
print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
print(sort_passenger_list())
