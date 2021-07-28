# “SarojiniPoem.txt”
# Based on the above file, answer the following questions:

# (b) Modify the program so that the lines are printed in reverse order.


fileObj = open("sarojiniPoem.txt","r")

text = fileObj.readlines()

for index in text:
    for reverse in range(-1,-len(index)-1,-1) :
        print (index[reverse], end = "")
    print()

fileObj.close()







