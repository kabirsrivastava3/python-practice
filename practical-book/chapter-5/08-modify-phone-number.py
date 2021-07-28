# A program to edit the phone number of “Arvind” in file “phonebook.det”. 
# If there is no record for “Arvind”, report error.


fileObj = open("phonebook.det","r")
text = fileObj.readlines()
names = []
phones = []
newText = []

for line in text:
    newList = line.split(" ")
    names.append(newList[0])
    phones.append(newList[0])
findName = input("Enter the Name which you want to search: ")    
if findName not in names:
    print("Name not found")
else:
    for index,read,line in zip(names,phones,text):
        if (index == findName):
            oldPhoneNumber = read
            newPhoneNumber = input("Enter the new Phone-Number: ")
            line = line.replace(oldPhoneNumber, newPhoneNumber+"\n")
            newText.append(line)
        else:
            newText.append(line)
            fileObj1 = open("phonebook.det","w")
            fileObj1.writelines(newText)
            fileObj1.close()








