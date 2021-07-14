# Total digits a positive integer has by repeatedly dividing by 10 (without keeping the remainder) until the number is less than 10, consisting of only 1 digit. 
# Add 1 to this value for each time it is divided by 10.
# Test it with the values 15, 105, and 15105.


def countDigits(number):
    if number < 10 :
        return 1
    else:
        return 1 + countDigits(number // 10)


inputNumber = float(input("Enter a number: "))
print("Number of digits in number",inputNumber,"is/are",countDigits(inputNumber))

#test values
#countDigits(15), output = 2
#countDigits(105), output = 3
#countDigits(15105), output = 5