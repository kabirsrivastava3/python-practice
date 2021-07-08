##Finding the cube of a number using functions

def inputValue():
    number = int(input("Enter a number: "))
    return number

def cubeNumber(number):
    cube_number = number * number * number
    return cube_number

input = inputValue()
print(input)
output = cubeNumber(input)
print(output)
