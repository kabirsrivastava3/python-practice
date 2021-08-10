# Multipy two integer numbers without using * operator, use repeated addition

#Time Complexity = O(N)

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
count = number1
product = 0
while count != 0:              #same as count>0
    count -= 1
    product += number2
    
    print("The product of "+str(number1)+ " and "+str(number2)+" is: "+str(product))
