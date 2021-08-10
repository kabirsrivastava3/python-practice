#int(number) : returns only the integer part
#round(number, ndigits) : returns number rounded to ndigits after the decimal points. If ndigits is not given, it returns nearest integer to its input. 

def roundOffNumber(number):
    integerNumber = int(number)
    roundNumber = round(number)
    print("Number", number, "can be converted to integer in two ways as ",integerNumber,"and ",roundNumber)
    roundNumber = round(number,3)
    print("Number",number,"rounded off number after 3 digits is: ",roundNumber)

realNumber = float(input("Enter a real Number: "))

roundOffNumber(realNumber)