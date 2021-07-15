#A BUZZ number is a number which either ends with 7 OR is divisible by 7.
#Eg: 277, 77, 27, 7


def checkBuzz(number):
    if number % 10 == 7 or number % 7 == 0:
        
        return True
    else:
        return False
    

inputNumber = int(input("Enter a number: "))

output = checkBuzz(inputNumber)

if output == True:
    print(inputNumber,"is a Buzz Number")
else:
    print(inputNumber,"is not a Buzz Number")



