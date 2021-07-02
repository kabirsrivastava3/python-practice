def inputFeet():							
	feet=int(input("enter number in feet "))
	return feet 

def inch(calculateinch):  						
	return calculateinch*12

def finalInch(inch):
    print(str(inch)+" inches")

output=inputFeet()
output2=inch(output)
finalInch(output2)