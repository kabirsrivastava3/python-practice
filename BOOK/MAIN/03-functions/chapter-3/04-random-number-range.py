#function-receives two numbers and generates a random number.
#Using this function,the main program should be able to print three numbers randomly.


import random

def generateRandom(number1,number2):

    print(random.randint(number1,number2))


generateRandom(1,10)
generateRandom(100,1000)
generateRandom(1000,9999)