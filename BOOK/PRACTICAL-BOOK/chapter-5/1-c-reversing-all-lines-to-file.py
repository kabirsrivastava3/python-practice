# “SarojiniPoem.txt”
# Based on the above file, answer the following questions:

# (c) Modify the code so as to output to another file instead of the screen. 
# Let your script overwrite the output file.


fileObj = open ("sarojiniPoem.txt","r")
outputObj = open("output.txt","w")
text = fileObj.readlines()

for index in text:
    for reverse in range(-1,-len(index)-1,-1) :
        outputObj.write(index[reverse])
    outputObj.write("\n") 

fileObj.close()
outputObj.close()

 

