# “SarojiniPoem.txt”
# Based on the above file, answer the following questions:

# (d) Change the script of part (c) that it append output to an existing file.

 
fileObj = open("sarojiniPoem.txt","r")
outputObj = open("output.txt","a")
text = fileObj.readlines()

for index in text:
    for reverse in range(-1,-len(index)-1,-1) :
        outputObj.write(index[reverse])
    outputObj.write("\n")

fileObj.close()
outputObj.close()


