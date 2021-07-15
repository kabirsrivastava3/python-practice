#automorphic number is an integer whose square ends with the given integer, as (25)2 = 625, and (76)2 = 5776.



def automorphicFunction(number):
    square = 0
    if number < 10:
        remainder = number % 10
    else:
        remainder = number % 100
    
    square = remainder * remainder
    return square == number



inputNumber = int(input("Enter a number: "))

output = automorphicFunction(inputNumber)

if output == True:
    print(inputNumber,"is an Automorphic Number")
else:
    print(inputNumber,"is not an Automorphic Number")



