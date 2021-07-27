# A void function that receives a 4 digit number. 
# Calculate the sum of the square of first 2 digits number and last digits number.


def sumSquare(number):
    lastTwoDigits = number % 100
    firstTwoDigits = number // 100

    print("First 2 digits =",firstTwoDigits)
    print("Last 2 digits =",lastTwoDigits)

    sum = firstTwoDigits ** 2 + lastTwoDigits ** 2
    print("Total sum of squares of first 2 digits and last 2 digits is",sum)

sumSquare(1234)
