#G.P using Recursion
#A GP with a first term a and a common ratio r with n terms, can be stated as:
#a, ar, ar2, ar³, ar4.....arn-1

def gpUsingRecursion(a,r,n):
    if n == term:
        return 0
    else :
        print(a*(r**n),end=",")
        return a*r**n + gpUsingRecursion(a,r,n+1)
    
    
a = int(input("Enter first term: "))
r = int(input("Enter common ratio: "))
term = int(input("Enter no. of terms: "))

print("Sum =",gpUsingRecursion(a,r,0))