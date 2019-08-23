#PF-Assgn-48

def find_correct(word_dict):
    cor,acor,wro=0,0,0
    lst=[]
    for key,value in word_dict.items():
        if(key==value):
            cor+=1
        elif(len(key)!=len(value)):
            wro+=1
        else:
            c=0
            for i in range(len(key)):
                if(key[i]!=value[i]):
                    c+=1
            if(c>2):
                wro+=1
            else:
                acor+=1
    lst.extend((cor,acor,wro))
    return lst

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))