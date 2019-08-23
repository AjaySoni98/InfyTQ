#PF-Assgn-54
def check_anagram(data1,data2):
    data1=data1.lower()
    data2=data2.lower()
    for let in data1:
        if(let in data2 and data1.find(let)!=data2.find(let) and data1.count(let)==data2.count(let)):
            data1=data1.replace(data1[data1.find(let)], " ",1)
            data2=data2.replace(data2[data2.find(let)], " ",1)
            pass
        else:
            return False
    return True

print(check_anagram("Schoolmaster","Theclassroom"))