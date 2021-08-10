# A program that will create an object called filout for writing, associate it with the filename STRS.txt. 
# The code should keep on writing strings to it as long as the user wants.

filout = open("strs.txt","w")

while True :
      textInput = input("Enter text: ")
      filout.write(textInput)
      filout.write( "\n")
      user = input("For exiting: type quit: ")
      if user == "quit":
            break
print("Thankyou")

filout.close()
