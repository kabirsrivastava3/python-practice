#A function that receives a 4 digit number 
#The function calculates and prints the sum of squares of first 2 digits' number and last two digits' number.
#Eg: 1223 as 12^2 + 33^2



def sumofSquares(number):
    lastTwo = number % 100
    firstTwo = number // 100
    print("The number",number,"has",firstTwo,"as First Two digits and",lastTwo,"as Last Two digits")
    sumSquares = lastTwo ** 2 + firstTwo ** 2
    print("The sum of squares of First Two and Last Two Digits is: ",sumSquares)


inputNumber = int(input("Enter a number : "))
if inputNumber < 1000:
    print("Error! Values can't be less than 1000")
else:
    print(sumofSquares(inputNumber))


