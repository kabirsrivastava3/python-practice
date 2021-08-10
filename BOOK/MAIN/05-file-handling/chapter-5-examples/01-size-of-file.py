#display the size of file in bytes

fileObj = open('poem.txt',"r")
str = fileObj.read()
size = len(str)
print("Size of the given file poem.txt is")
print(size,"bytes")


#Output:

#Size of the given file poem.txt is 596 bytes

##nano ~/Documents/python-practice/chapter-5-examples/marks.txt