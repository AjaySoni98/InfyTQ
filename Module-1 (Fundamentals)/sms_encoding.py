#PF-Assgn-50

def sms_encoding(data):
    new_sms=""
    lst=data.split(" ")
    for word in lst:
        vow=""
        con=""
        for x in word:
            if x in 'aeiou' or x in 'AEIOU':
                vow+=x
            else:
                con+=x
        if(len(con)>0):
            new_sms+=con+" "
        else:
            new_sms+=vow+" "
    return new_sms[:len(new_sms)-1]
        
data="I will not repeat mistakes"
print(sms_encoding(data))