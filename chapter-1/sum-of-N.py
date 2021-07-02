def sumofN():
    N = int(input("enter the number "))
    sum = 0
    if N > 0 :
        for i in range (N,N*2+1):
            sum += i
    else :
        for i in range (2*N, N+1):
            sum += i
        
print (sum)

sumofN()