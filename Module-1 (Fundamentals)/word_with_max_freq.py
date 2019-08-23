#PF-Assgn-56
def max_frequency_word_counter(data):
    dicx={}
    done=[]
    data=data.lower()
    data=data.replace(",", "")
    lst=data.split(" ")
    for wrd in lst:
        if wrd not in done:
            dicx[wrd]=lst.count(wrd)
            done.append(wrd)
    done=[]
    for value in dicx.values():
        done.append(value)
    m=max(done)
    if(done.count(m)>1):
        l=0
        for key,value in dicx.items():
            if(m==value and len(key)>l):
                l=len(key)
                word=key
        print(word,m)
    else:
        for key,value in dicx.items():
            if(m==value):
                word=key
        print(word,m)
data="like like like you you you"
max_frequency_word_counter(data)