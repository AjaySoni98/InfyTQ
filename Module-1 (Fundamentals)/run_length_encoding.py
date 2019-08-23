#PF-Assgn-30
dicx=[]
def encode(message):
    cnt=1
    enmsg=""
    for i in range(len(message)-1):
        if(message[i]==message[i+1]):
            cnt+=1
        else:
            dicx.append(str(cnt)+message[i])
            cnt=1
    if(message[len(message)-1]!=message[len(message)-2]):
        dicx.append(str(1)+message[len(message)-1])
    for j in range(len(dicx)):
        enmsg+=dicx[j]
    return enmsg
    
encoded_message=encode("AABCCA")
print(encoded_message)