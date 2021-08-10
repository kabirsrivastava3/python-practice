#simple interest using function
#default value: r = 0.10, t = 2 years

def simpleInterest(principal,time = 2,rate=0.10):
    return principal * rate * time


#__main__
print("Enter the principal amount: ")
principalAmount = float(input())

#principal for default value
si1 = simpleInterest(principalAmount)
print("Rs. ",si1)

print("Enter the rate value: ")
rate = float(input())

print("Enter the time in years")
time = int(input())

print("Simple Interest for the values :")
si2 = simpleInterest(principalAmount,rate,time)

print("Rs. ",si2)
