#Any number can be a Perfect Number if the sum of its positive divisors excluding the number itself is equal to that number. 
#For example, 28 is a perfect number because 28 is divisible by 1, 2, 4, 7, 14 and 28 and the sum of these values is 1 + 2 + 4 + 7 + 14 = 28.



def checkPerfect(number):
    sum = 0
    mid = number // 2

    for integers in range(1,mid+1):
        if number % integers == 0:
            sum = sum + integers
    
    if sum == number:
        return True
    else:
        return False

def generatePerfect(low,high):
    for numbers in range(low,high):
        if checkPerfect(numbers) == True:
            print(numbers)


lowerRange = int(input("Enter lower range: "))
higherRange = int(input("Enter higher range: "))

print("The Perfect Number between",lowerRange,"and",higherRange,"are: ")
generatePerfect(lowerRange,higherRange)




