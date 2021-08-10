# A program to append more details to file "phonebook.det"



fileObj = open("phonebook.det ","a")
while True :
    name = input("Enter name: ")
    phone = input("Enter Phone: ")
    fileObj.write(name +"\t")
    fileObj.write(phone + "\t")
    fileObj.write("\n")
    user = input("Enter 'Q' or 'q' to quit (Q/q) OR any button to continue: ")
    if user == "Q" or user == "q":
        break
    else:
        continue
fileObj.close()
print("Thankyou")
