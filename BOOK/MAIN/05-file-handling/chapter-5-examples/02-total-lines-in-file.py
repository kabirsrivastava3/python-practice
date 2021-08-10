#display the number of lines in the file

fileObj = open('poem.txt',"r")
str = fileObj.readlines()
lineCount = len(str)
print("Number of lines in file poem.txt is",lineCount)
fileObj.close()


#Output:

#Number of lines in file poem.txt is 33