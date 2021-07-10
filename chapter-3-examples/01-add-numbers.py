#sum of two numbers using a function


def addSum(number1,number2):
    sum = number1 + number2

    return sum

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


sum = addSum(num1,num2)

print("Sum of two numbers is: ",sum)

