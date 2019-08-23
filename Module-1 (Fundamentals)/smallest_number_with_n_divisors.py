def num_divisor(n):
    for value in range(1,1000):
        listt=[]
        for num in range(1,value+1):
            if value%num ==0:
                listt.append(num)
            
        if len(listt) == n:
            print('The smallest number with',n,'divisors is',value)
            break

num_divisor(16)