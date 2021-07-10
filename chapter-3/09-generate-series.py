#generates a series using a function which takes first and last values, 
# generates four terms = equidistant 
# e.g., if two numbers passed are 1 and 7 then function returns 1 3 5 7. 

#a**n = a + (n-1)d
#a = 1, n = 4 terms, a**n = 7 = last term
#d = 2


 
def generateSeries(number1, number2):
    if number1 == number2:
        print("Error! End limits' can't be equal")

    difference = int((number2 - number1)/3)    #d = a**n - a/(n-1)
    print("Series: = ",number1, number1 * difference, number1 + 2 * difference, number2)



print(generateSeries(1,7))
print(generateSeries(2,8))

            
