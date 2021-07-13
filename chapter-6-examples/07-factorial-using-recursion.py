#Factorial using Recursion

def findFactorial(number):
    if number == 0:
        return 1
    elif number == 1:
        return 1
    else:
        return number * findFactorial(number-1)

print("Enter a number: ")
inputNumber = int(input())

if inputNumber < 0:
    print("Error! Can't be a negative number! Enter again!!!")

result = findFactorial(inputNumber)
print("Factorial of",inputNumber,"is",result)
