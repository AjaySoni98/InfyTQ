def minimumBribes(q):
    moves = 0 
    q = [P-1 for P in q]
    for i,P in enumerate(q):
        if P - i > 2:
            print("Too chaotic")
            return
        for j in range(max(P-1,0),i):
            if q[j] > P:
                moves += 1
    print("Total number of bribes =",moves)

t=int(input("How many test cases ? : "))
for k in range(t):
    n=int(input("What is the size of queue ? : "))
    q=[]
    for l in range(n):
        q.append(int(input("Enter number : ")))
    minimumBribes(q)
