#WAP:
#(i) = a function that takes a number as argument and calculates cube for it .The function does not return a value .
# If there is no value passed to the function in function call , the function should calculate cube of 2.
#(ii) = A function that takes two char arguments and returns True if both the arguments are equal otherwise False . 


def cubeNumber(number=2):
    cube = number* number * number
    print(cube)

def alphaEqual(one,two):
    return one == two


#provided value for a cube of a number
print(cubeNumber(5))

#default value for a cube of a number
print(cubeNumber())

#two characters are equal or not
print(alphaEqual("a","a"))
