#A program that appends the contents of one file to another. Have the program take the filenames from the user. 

file1 = input("Enter the name of file which you want to append: ")
file2 = input("Enter the name of original file: ")

oldFile =  open(file2, "r")
newFile = open(file1, "a")

data = oldFile.read()
newFile.write("\n" + data)

print("Files appended successfully ")

oldFile.close()
newFile.close()
