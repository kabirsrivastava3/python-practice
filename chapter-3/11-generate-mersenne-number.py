# A Mersenne Number is in the form: 2^n-1.
# A function that passes value and returns nth Mersenne number.

def generateMersenneNumber(n):
    return 2 ** n-1

testValue1 = generateMersenneNumber(3)
print("3rd Mersenne Number is: ",testValue1)
testValue2 = generateMersenneNumber(5)
print("5th Mersenne Number is: ",testValue2)
