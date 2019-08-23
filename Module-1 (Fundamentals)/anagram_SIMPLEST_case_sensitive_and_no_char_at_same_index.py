def check_anagram(data1,data2):
    data1=data1.lower()
    data2=data2.lower()
    if(sorted(data1)==sorted(data2)):
        for let in data1:
            if(data1.index(let)==data2.index(let)):
                return False
        return True
    else:
        return False

print(check_anagram("listen","silent"))