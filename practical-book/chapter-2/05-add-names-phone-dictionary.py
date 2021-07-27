# Code to create a python dictionary 
# Add three name and their phone in the dictionary after getting input from user.


phoneDict = {}

for index in range(3):
    name  = input("Enter the Name: ")
    phone = input("Enter the Phone Number: ")
    phoneDict[name] = phone

while True :
    nameInput = input("Enter the name from the dictionary (For exit enter 'q'): ")
    if nameInput == "q" or nameInput == "Q":
        break
    else:
        print(phoneDict[nameInput])

