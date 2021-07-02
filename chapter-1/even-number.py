def checkEven():
    number = int(input("Enter a number: "))
    if number%2 == 0:                               #even number
        return True
    else:
        return False

output = checkEven()
print(output)