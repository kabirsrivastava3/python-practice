#A function product() to multiply 2 numbers recursively using + and - operators only. 


def productUsingRecursion(number1,number2):
    if number2 == 0:
        return 0
    else:
        return number1 + productUsingRecursion(number1,number2-1)


print("Enter First Number: ")
number1 = int(input())
print("Enter Second Number: ")
number2 = int(input())
print("Product of",number1,"and",number2,"is",productUsingRecursion(number1,number2))