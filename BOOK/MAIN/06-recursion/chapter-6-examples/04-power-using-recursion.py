#calculation of power using recursion


def exponentOfNumber(base,power):
    if power == 0:
        return 1
    else:
        return base * exponentOfNumber(base,power-1)


print("Enter only positive numbers below: ",)
print("Enter a base: ")
number = int(input())

print("Enter a power: ")
exponent = int(input())

result = exponentOfNumber(number,exponent)

print(number,"raised to the power of",exponent,"is",result)









