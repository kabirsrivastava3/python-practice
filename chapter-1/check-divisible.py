def checkDivisible():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    if number1 % number2 == 0:                               #divisible
        print(str(number1)+" is divisible by "+str(number2))
    else:
        print(str(number1)+" is not divisible by "+str(number2))

checkDivisible()
