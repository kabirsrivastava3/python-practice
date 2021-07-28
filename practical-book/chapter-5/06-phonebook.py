# Create a file phonebook.det that stores the details in following format:
 
# Name       Phone
# Jiving     8666000
# Kriti      1010101
 
# Obtain the details from the user.


fileObj = open("phonebook.det","w")
fileObj.write("Name \t")
fileObj.write("Phone \t")
fileObj.write("\n")
while True :
    name = input("Enter Name: ")
    fileObj.write(name +"\t")
    phone = input("Enter Phone: ")
    fileObj.write(phone + "\t")
    fileObj.write("\n")
    user = input("Enter 'Q' or 'q' to quit (Q/q) :-")
    if user == "Q" or user == "q":
        break
fileObj.close()
print("Thankyou")

# f1.close()
# f2.close()

 