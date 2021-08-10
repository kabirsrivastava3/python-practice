#Write a function that takes a number and tests if it is a prime number using recursion technique.


count = 0
def PrimeUsingRecursion(number,index=2):
    if index == number:
        return number
    else:
        global count
        if number % index == 0:
            count+=1
        PrimeUsingRecursion(number,index+1)
        

print("Enter number")
inputNumber = int(input())
PrimeUsingRecursion(inputNumber)

if count>0:
    print(inputNumber,"is not a Prime Number")
else:
    print(inputNumber,"is a Prime Number")


