#two numbers in a function and all arithematic operations


def operatorsCalc(number1,number2):
    return number1 + number2, number1 - number2, number1 * number2,  number1 / number2,  number1 % number2
 

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
add,subtract,multiply,division,modulo = operatorsCalc(num1,num2)

print("Addition: ",add)
print("Subtraction: ",subtract)
print("Multiplication: ",multiply)
print("Division: ",division)
print("Modulo: ",modulo)