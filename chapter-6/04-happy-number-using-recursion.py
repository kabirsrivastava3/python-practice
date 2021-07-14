#A happy number is a number in which the eventual sum of the square of the digits of the number is equal to 1.
#Example 100 = (1)2 + ( 0 )2 + ( 0 )2 = 1+ 0 + 0 = 1. Hence , 100 is a happy number. 
#Using following two functions in it:
#(1)sum_sq_digits :returns the sum of the square of the digits of the number x, using the recursive technique
#(2)ishappy() : checks if the given number is a happy number by calling the function sum_sq_digits and displays an appropriate message


def sum_sq_digits(number):
    totalSum = 0
    while number > 0:
        remainder = number%10
        totalSum = totalSum + remainder * remainder
        number = number // 10
    
    if totalSum>10:
        return sum_sq_digits(totalSum)
    else:
        return totalSum

def isHappy(number):
    totalSum = sum_sq_digits(number)
    if totalSum == 1:
        return True
    elif totalSum <10:
        return False

inputNumber = int(input("Enter a number: "))
output = isHappy(inputNumber)
if output:
    print(inputNumber,"is a Happy Number")
else:
    print(inputNumber,"is not a Happy Number")

