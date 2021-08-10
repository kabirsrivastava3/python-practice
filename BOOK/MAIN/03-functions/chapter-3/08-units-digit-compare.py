#a function that takes two numbers and returns the number that has minimum one's digit.


def compareUnitDigit(number1,number2):
    unitdigit1 = number1 % 10
    unitdigit2 = number2 % 10

    if unitdigit1 > unitdigit2:
        return number1
    else:
        return number2


#Example 1:
print(compareUnitDigit(491,278))
#Example 2:
print(compareUnitDigit(10,15))


