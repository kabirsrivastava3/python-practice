#function takes a number n and then returns a randomly generated number having exactly n digits (not starting with zero) 
# eg: if n is 2 then function can randomly return a number 10-99 but 07, 02 etc. are not valid two digit numbers.


import random

def randomBetween10To99(limit):

    range1 = 10 ** (limit-1)
    range2 = 10 ** limit -1

    result = random.randint(range1,range2)

    return result


print("Enter a number: ")
limit = int(input())

output = randomBetween10To99(limit)
print("Random generated number is: ")
print(output)
