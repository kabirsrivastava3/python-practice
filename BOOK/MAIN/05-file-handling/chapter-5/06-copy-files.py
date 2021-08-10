#A program that copies one file to another. Have the program read the file names from user?

fileObj = input("Enter the name of file with its format : ")

oldFile = open(fileObj,"r")
newFile = open("newFile.txt", "w")

data = oldFile.read()
newFile.write(data)

print("Files copied successfully")

oldFile.close()
newFile.close()
