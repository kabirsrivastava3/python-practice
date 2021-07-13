#calculation of power using iterative code


def exponentUsingIteration(base,power):
    result = 1
    if power == 0:
        return 1
    else:
        for index in range(power):
            result = result * base 
    return result

print("Enter only positive numbers below: ")
print("Enter a base: ")
number = int(input())

print("Enter a power: ")
exponent = int(input())

output = exponentUsingIteration(number,exponent)

print(number,"raised to the power of",exponent,"is",output)



