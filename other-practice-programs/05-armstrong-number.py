#armstrong-number
#Armstrong number is a number that is equal to the sum of cubes of its digits. 
#For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.



def checkArmstrong(number):
    onesDigit = number % 10
    twosDigit = (number // 10) % 10
    threesDigit = number // 100

    product = onesDigit*onesDigit*onesDigit +twosDigit*twosDigit*twosDigit +threesDigit*threesDigit*threesDigit

    return product == number


print("The Armstrong Numbers between 100 and 999 are: ")
for numbers in range(100,999):
    if checkArmstrong(numbers) == True:
        print(numbers,end =" ")


#153 = (1*1*1)+(5*5*5)+(3*3*3)  where:  
#(1*1*1)=1  
#(5*5*5)=125  
#(3*3*3)=27  
#So:  
#1+125+27=153 