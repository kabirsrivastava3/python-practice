#function for returning one's position digit of the integer 


def onesDigit(number):
    onesPlace = number%10
   
    return onesPlace


num1 = float(input("Enter an integer: "))

print(onesDigit(num1))
