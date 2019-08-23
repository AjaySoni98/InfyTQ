#PF-Assgn-60
def remove_duplicates(value):
    done=""
    for x in value:
        if(x not in done):
            done+=x
    return done

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))