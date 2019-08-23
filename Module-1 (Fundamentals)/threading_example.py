#PF-Tryout
from threading import Thread
def func1():
    result_sum=0
    for i in range(1,10000001):
        result_sum+=i
    print("Sum from func1:",result_sum)

def func2():
    result_sum=0
    i=0
    while(i<5):
        a = int(input("Enter a number: "))
        result_sum+=a
        i+=1
    print("Sum from func2:",result_sum)

t1=Thread(target=func1())
t1.start()
t2=Thread(target=func2())
t2.start()
t1.join()
t2.join()