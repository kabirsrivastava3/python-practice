#HCF using recursion

def recursiveHCF(number1,number2):
    if number2 == 0:
        return number1
    else:
        return recursiveHCF(number2,number1%number2)


print("Enter first number: ")
number1 = int(input())

print("Enter second number: ")
number2 = int(input())

if number1 < number2:
    print("Error! First number can't be smaller!!Enter Again")
else:
    print("The H.C.F of",number1,"and",number2,"is:",recursiveHCF(number1,number2))