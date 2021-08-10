# A program that prompt the user for a file name and then read and prints the contents of the requested file in the upper case.


fileObj = open(input("Enter the file name :")+".txt","r+")
text = fileObj.readlines()
for index in text:
    for read in (index):
        print (read.upper(), end=" ")
fileObj.close()