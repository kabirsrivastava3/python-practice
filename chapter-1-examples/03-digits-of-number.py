#printing of numbers between ranges of 0-999 by using if, elif and else.

number = int(input("Enter a number between 0-999: "))
if number < 0:
    print("Invalid Number!!! Range is between 0-999")
elif number < 10:
    print("One digit Number "+str(number))
elif number < 100:
    print("Two digit Number "+str(number))
elif number <= 999:
    print("Three digit Number "+str(number))
else:
    print("Invalid Number!!! Range is between 0-999")  