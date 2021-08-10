# A program chkOdd() that takes one argument and report if the argument is odd or not .

def chkOdd(number):
    if number % 2==0:
        return "Even"
    else :
        return "Odd"

output = int(input("Enter the positive number:  "))
print(chkOdd(output))

