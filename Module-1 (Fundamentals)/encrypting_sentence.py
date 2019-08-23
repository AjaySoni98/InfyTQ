#PF-Assgn-47
def encrypt_sentence(sentence):
    new_str=""
    lst=sentence.split(" ")
    for i in range(0,len(lst)):
        if(i%2==0):
            new_str+=lst[i][::-1]+" "
        else:
            vow=""
            for x in lst[i]:
                if x not in 'aeiou' or x not in 'AEIOU':
                    new_str+=x
                else:
                    vow+=x
            new_str+=vow+" "
    return  new_str[:len(new_str)-1]

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)