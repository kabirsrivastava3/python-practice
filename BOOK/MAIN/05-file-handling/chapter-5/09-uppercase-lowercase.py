#A program that reads characters from the keyboard one by one. 
#All lower case characters get stored inside the file LOWER, all upper case characters get stored inside the file UPPER and all other characters get stored inside file OTHERS.


upperObj = open("upperFile.txt", "w")
lowerObj = open("lowerFile.txt", "w")
otherObj = open ("others.txt", "w")

while True :
    userInput = input("Enter a character (for exit enter quit ): ")
    if userInput == "quit" or userInput == "QUIT" :
        break
    elif userInput.isupper():
        upperObj.write(userInput + " ")
    elif userInput.islower():
        lowerObj.write(userInput + " ")
    else :
        otherObj.write(userInput + " ")

upperObj.close()
lowerObj.close()
otherObj.close()

print("Thankyou")
