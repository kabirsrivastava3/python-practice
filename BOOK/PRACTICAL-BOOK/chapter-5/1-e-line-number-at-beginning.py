# “SarojiniPoem.txt”
# Based on the above file, answer the following questions:

#(e) Modify the program so that each line is printed with a line number at beginning.


fileObj = open("sarojiniPoem.txt","r")
text = fileObj.readlines()


for index in range(len(text)):
    print (index + 1, " = ", text[index])

fileObj.close() 