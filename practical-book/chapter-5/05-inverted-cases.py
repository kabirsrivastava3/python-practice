# A program that reads a text file and then create a new file where each character‘s case is inverted.
 


fileObj1 = open("newFile1.txt","r")
fileObj2 = open("newFile2.txt","w")

data = fileObj1.readlines()

for index in data:
    for read in index:
        if read.isupper():
            fileObj2.write(read.lower())
        elif read.islower() :
            fileObj2.write(read.upper())
        else:
            fileObj2.write(read)

fileObj1.close()
fileObj2.close()
